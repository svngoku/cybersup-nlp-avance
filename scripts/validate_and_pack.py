"""Validate authored course files and package student/instructor materials.

This is a structural check, not a hosted Colab or GPU execution.
Run after build_slides.mjs and the PDF export. Standard library only.
"""
from pathlib import Path
from collections import Counter
import ast
import hashlib
import json
import re
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output'
NS = {'a':'http://schemas.openxmlformats.org/drawingml/2006/main'}

def main():
    source = json.loads((ROOT / 'course/slides.json').read_text())
    slides = source if isinstance(source, list) else source['slides']
    totals = Counter()
    for slide in slides:
        if slide.get('day', 0):
            totals[slide['day']] += slide.get('minutes', 0)
        assert slide.get('notes'), slide['title']
    assert len(slides) >= 90, 'Incomplete five-day course'
    assert all(totals[d] == 420 for d in range(1, 6)), totals
    nb_files = sorted((ROOT / 'notebooks').rglob('*.ipynb'))
    assert len(nb_files) >= 14, len(nb_files)
    for file in nb_files:
        nb = json.loads(file.read_text())
        assert nb['nbformat'] == 4
        for cell in nb['cells']:
            if cell['cell_type'] != 'code':
                continue
            assert not cell.get('outputs'), str(file)
            assert cell.get('execution_count') is None
            code = cell['source']
            code = ''.join(code) if isinstance(code, list) else code
            if code.lstrip().startswith('%%'):
                continue
            filtered = '\n'.join('pass' if line.lstrip().startswith(('!', '%')) else line for line in code.splitlines())
            ast.parse(filtered, filename=str(file))
    diagrams = json.loads((ROOT/'assets/diagrams/manifest.json').read_text())
    formulas = json.loads((ROOT/'assets/formulas/manifest.json').read_text())
    assert len(diagrams) >= 12
    assert len(formulas) == sum(bool(s.get('formula')) for s in slides)
    for collection in (diagrams, formulas):
        for num, asset in collection.items():
            assert (ROOT/asset['png']).is_file()
            assert (ROOT/asset['svg']).is_file()
            assert asset.get('alt'), num
    pptx = OUT / 'CYBERSUP-NLP-M2-35h-visuel.pptx'
    with zipfile.ZipFile(pptx) as z:
        slide_parts = [n for n in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+.xml', n)]
        note_parts = [n for n in z.namelist() if re.fullmatch(r'ppt/notesSlides/notesSlide\d+.xml', n)]
        assert len(slide_parts) == len(slides)
        assert len(note_parts) == len(slides)
        table_count = 0
        for name in slide_parts:
            xml = ET.fromstring(z.read(name))
            visible = ' '.join(n.text or '' for n in xml.findall('.//a:t', NS))
            assert '{{' not in visible and '}}' not in visible, name
            assert 'Fortune 500' not in visible and 'VECTEURS D\'ATTAQUE' not in visible
            table_count += len(xml.findall('.//a:tbl', NS))
        pns = {'p':'http://schemas.openxmlformats.org/presentationml/2006/main'}
        for num in set(diagrams) | set(formulas):
            xml = ET.fromstring(z.read(f'ppt/slides/slide{num}.xml'))
            assert len(xml.findall('.//p:pic',pns)) >= 1, f'Missing slide image {num}'
    pdf = OUT / 'CYBERSUP-NLP-M2-35h-visuel.pdf'
    assert pdf.exists() and pdf.stat().st_size > 10000, 'Export PDF first'
    assert (OUT / 'Notes-presentateur.md').exists()
    student_paths = [pdf, ROOT/'docs/ETUDIANTS.md', ROOT/'docs/COLAB.md', ROOT/'docs/PROGRAMME_35H.md', ROOT/'evaluation/PROJET.md', ROOT/'evaluation/QUIZ.md', ROOT/'evaluation/MODEL_CARD.md', ROOT/'ressources/RESSOURCES_VERIFIEES.md', ROOT/'ressources/PROVENANCE.md', ROOT/'requirements-colab.txt']
    student_paths += sorted((ROOT/'notebooks/etudiants').glob('*.ipynb'))
    if (ROOT/'docs/RUNPOD_OPTION.md').exists():
        student_paths.append(ROOT/'docs/RUNPOD_OPTION.md')
    assert len([x for x in student_paths if x.suffix=='.ipynb']) == 7
    for f in student_paths:
        assert f.is_file(), f
    validation_path = OUT/'VALIDATION.md'
    student_paths.append(validation_path)
    student_zip = OUT/'CYBERSUP-NLP-M2-Pack-etudiant.zip'
    template_path = ROOT/'CYBERSUP - TEMPLATE DATA_IA.pptx'
    teacher_paths = set(student_paths + [pptx, template_path, OUT/'Notes-presentateur.md', ROOT/'README.md', ROOT/'docs/GUIDE_FORMATEUR.md', ROOT/'evaluation/CORRIGES_QUIZ.md'])
    practical_guide_path = ROOT/'docs/FIL_CONDUCTEUR_PRATIQUE.md'
    if practical_guide_path.is_file():
        teacher_paths.add(practical_guide_path)
    cpu_checks_path = ROOT/'docs/VERIFICATIONS_CPU.md'
    if cpu_checks_path.is_file():
        teacher_paths.add(cpu_checks_path)
        cpu_checks_note = 'Les vérifications CPU partielles réellement exécutées sont détaillées dans docs/VERIFICATIONS_CPU.md, inclus dans le pack formateur. Leur portée est limitée aux opérations explicitement consignées.'
    else:
        cpu_checks_note = 'Aucun compte rendu complémentaire de vérifications CPU partielles n’était présent lors de cette génération des packs.'
    for folder in ['notebooks/formateur','scripts','course','assets']:
        teacher_paths.update(f for f in (ROOT/folder).rglob('*') if f.is_file() and '__pycache__' not in str(f))
    if (ROOT/'tools-visuals').exists():
        teacher_paths.update((ROOT/'tools-visuals').glob('package*.json'))
        for name in ['README.md', '.gitignore']:
            runtime_doc = ROOT/'tools-visuals'/name
            assert runtime_doc.is_file(), runtime_doc
            teacher_paths.add(runtime_doc)
    teacher_zip = OUT/'CYBERSUP-NLP-M2-Pack-formateur.zip'
    report = {'date':'2026-10-04','slides':len(slides),'slides_with_notes':len(note_parts),'native_tables':table_count,'diagrams':len(diagrams),'latex_formula_images':len(formulas),'notebooks':len(nb_files),'minutes_by_day':dict(totals),'colab_t4_executed':False,'student_pack_files':len(student_paths),'instructor_pack_files':len(teacher_paths),'template_sha256':hashlib.sha256((ROOT/'CYBERSUP - TEMPLATE DATA_IA.pptx').read_bytes()).hexdigest()}
    (ROOT/'.build/course-validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
    validation_path.write_text(f'''# Validation et préparation de la séance

État au 4 octobre 2026.

- {len(slides)} diapositives éditables et autant de notes du présentateur.
- {table_count} tableaux natifs dans le support.
- {len(diagrams)} illustrations et architectures originales, avec sources SVG et descriptions accessibles.
- {len(formulas)} formules rendues en images depuis LaTeX ; sources, légendes des symboles et explications détaillées conservées.
- 5 journées de 420 minutes, soit 35 heures hors pauses et déjeuner.
- {len(nb_files)} notebooks valides en JSON et syntaxe Python, sans sorties préremplies.
- Export PDF du support. Les notes détaillées se consultent dans PowerPoint ou Notes-presentateur.md.
- Pack étudiant contrôlé par liste autorisée, sans PowerPoint contenant les notes, corrigés ou guide formateur.
- Template original conservé. Empreinte SHA256 : `{report['template_sha256']}`.
- Template source inclus dans le pack formateur pour permettre sa régénération dans le runtime approprié.

## Vérifications CPU partielles

{cpu_checks_note}

## Limites de cette validation

Le chargement des poids des modèles, les entraînements GPU et l'enchaînement complet des notebooks sur Google Colab T4 ou Runpod L4 restent à exécuter avant la séance. Les scores et durées GPU ne sont pas préremplis. La syntaxe correcte ne garantit ni les téléchargements du Hub, ni la mémoire disponible, ni la compatibilité d'un runtime futur. Consulter docs/COLAB.md et docs/RUNPOD_OPTION.md pour la répétition et les solutions de repli. Les corpus fictifs servent à comprendre la mécanique et ne constituent pas un benchmark métier ; le transfert sur un sous-ensemble Allociné ne vaut pas évaluation complète du benchmark.
''')
    with zipfile.ZipFile(student_zip, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in student_paths:
            z.write(f, str(f.relative_to(ROOT)))
    with zipfile.ZipFile(student_zip) as z:
        names = z.namelist()
        assert len(names) == len(set(names)) == report['student_pack_files']
        assert 'output/VALIDATION.md' in names
        assert not any(any(v in n.lower() for v in ('corrige','formateur','presentateur','.pptx')) for n in names)
        assert 'docs/FIL_CONDUCTEUR_PRATIQUE.md' not in names
    with zipfile.ZipFile(teacher_zip, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in sorted(teacher_paths):
            z.write(f, str(f.relative_to(ROOT)))
    with zipfile.ZipFile(teacher_zip) as z:
        names = z.namelist()
        assert len(names) == len(set(names)) == report['instructor_pack_files']
        assert 'output/VALIDATION.md' in names
        assert template_path.name in names
        if cpu_checks_path.is_file():
            assert 'docs/VERIFICATIONS_CPU.md' in names
        if practical_guide_path.is_file():
            assert 'docs/FIL_CONDUCTEUR_PRATIQUE.md' in names
        if (ROOT/'tools-visuals').exists():
            assert 'tools-visuals/README.md' in names
            assert 'tools-visuals/.gitignore' in names
            assert 'tools-visuals/package.json' in names
        assert not any('node_modules' in Path(name).parts for name in names)
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
