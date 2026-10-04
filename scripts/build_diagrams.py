"""Generate original, editable SVG teaching diagrams and large PNG previews.

SVG construction uses only the Python standard library. PNG conversion uses
rsvg-convert when available, otherwise ImageMagick. No model or network call.
"""
from pathlib import Path
from html import escape
import argparse
import json
import shutil
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'diagrams'
BLUE = '#282A59'
ORANGE = '#BF2E00'
INK = '#171923'
MUTED = '#565968'
LIGHT = '#F0F1F7'
WARM = '#FFF0E8'
GREY = '#ECEEF1'
WHITE = '#FFFFFF'


class SVG:
    def __init__(self, title, alt, height=375):
        self.height = height
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc">',
            f'<title id="title">{escape(title)}</title><desc id="desc">{escape(alt)}</desc>',
            '<defs>',
            f'<marker id="blue-arrow" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,4 L0,8 Z" fill="{BLUE}"/></marker>',
            f'<marker id="orange-arrow" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,4 L0,8 Z" fill="{ORANGE}"/></marker>',
            f'<marker id="grey-arrow" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,4 L0,8 Z" fill="{MUTED}"/></marker>',
            '</defs>',
            f'<rect width="1200" height="{height}" fill="white"/>',
        ]

    def rect(self, x, y, w, h, fill=LIGHT, stroke=BLUE, radius=14, width=2, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"{d}/>')

    def text(self, x, y, value, size=28, fill=INK, weight=500, anchor='start', gap=None, mono=False):
        lines = value if isinstance(value, (list, tuple)) else str(value).split('\n')
        font = 'Roboto Mono, monospace' if mono else 'DM Sans, Arial, sans-serif'
        gap = gap or round(size * 1.25)
        self.parts.append(f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">')
        for i, line in enumerate(lines):
            self.parts.append(f'<tspan x="{x}" dy="{0 if i == 0 else gap}">{escape(str(line))}</tspan>')
        self.parts.append('</text>')

    def box(self, x, y, w, h, value, size=28, accent=False, fill=None, stroke=None, radius=14, weight=600):
        color = stroke or (ORANGE if accent else BLUE)
        self.rect(x, y, w, h, fill or (WARM if accent else LIGHT), color, radius)
        lines = value if isinstance(value, (list, tuple)) else str(value).split('\n')
        gap = round(size * 1.25)
        baseline = y + h / 2 - (len(lines) - 1) * gap / 2 + size * .35
        self.text(x + w / 2, baseline, lines, size=size, fill=color, weight=weight, anchor='middle', gap=gap)

    def arrow(self, points, color=BLUE, width=3, dash=None, end=True):
        coords = ' '.join(f'{x},{y}' for x, y in points)
        marker = 'orange-arrow' if color == ORANGE else 'grey-arrow' if color == MUTED else 'blue-arrow'
        extra = f' marker-end="url(#{marker})"' if end else ''
        if dash:
            extra += f' stroke-dasharray="{dash}"'
        self.parts.append(f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"{extra}/>')

    def circle(self, x, y, r, value=None, fill=WHITE, stroke=BLUE):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="3"/>')
        if value is not None:
            self.text(x, y + 11, value, size=34, fill=stroke, weight=600, anchor='middle')

    def finish(self):
        return '\n'.join(self.parts + ['</svg>']) + '\n'


SPECS = {
    17: ('embeddings', 'Les positions 2D sont illustratives ; la proximité ne prouve pas un sens identique.', 'Deux vecteurs illustratifs colis et livraison pointent dans des directions voisines ; facture pointe ailleurs. Deux phrases proches évoquent un colis non reçu.'),
    29: ('qkv', 'En self-attention, Q, K et V proviennent de trois projections apprises du même X.', 'La séquence X alimente trois projections apprises WQ, WK et WV, produisant respectivement queries, keys et values avec leurs rôles distincts.'),
    34: ('masque_causal', 'Le masque s’ajoute aux scores avant softmax : le futur reçoit une probabilité nulle.', 'Matrice de masque causal quatre par quatre : zéro sur et sous la diagonale, moins l’infini au-dessus. La troisième position ne lit que les trois premières positions.'),
    35: ('multi_tetes', 'Chaque tête apprend ses projections ; leurs sorties sont concaténées puis reprojetées.', 'Deux branches d’attention parallèles reçoivent X, utilisent des projections différentes, puis rejoignent une concaténation et une projection de sortie WO.'),
    36: ('bloc_transformer', 'Exemple Post-LN de type BERT ; d’autres Transformers placent la normalisation autrement.', 'Un bloc Post-LN relie entrée, attention, addition du premier résidu, LayerNorm, réseau positionnel FFN, addition du second résidu, LayerNorm et sortie.'),
    38: ('architectures', 'BERT encode ; GPT génère causalement ; T5 relie encodeur et décodeur par cross-attention.', 'Trois colonnes comparent BERT encodeur bidirectionnel, GPT décodeur causal, et T5 avec encodeur, décodeur causal et liaison de cross-attention depuis le texte source.'),
    40: ('pipeline', 'pipeline() assemble ces étapes ; inspecter chacune aide à localiser une erreur.', 'Un message est tokenisé en identifiants et masque, traité par le modèle qui produit des logits, puis post-traité pour obtenir une catégorie.'),
    49: ('tetes_taches', 'Une tête globale prédit une classe ; une tête NER prédit des labels par token.', 'Un encodeur transforme quatre tokens en quatre vecteurs. Une branche agrège une représentation globale vers cinq classes ; une autre conserve les quatre positions vers des logits NER.'),
    58: ('alignement_ner', 'Convention du TP : superviser le premier sous-token ; −100 ignore les autres dans la loss.', 'Marie, Dupont et Lyon sont alignés avec CLS, Marie, Du, double dièse pont, Lyon et SEP. Les labels sont moins cent, B-PER, I-PER, moins cent, B-LOC, moins cent.'),
    75: ('chat_template', 'Exemple de marqueurs Qwen ; utiliser le template associé au checkpoint.', 'Les messages system, user et assistant deviennent un texte avec marqueurs im_start et im_end, puis le tokenizer produit les identifiants des marqueurs et du contenu.'),
    76: ('masques_attention_loss', 'Le prompt reste visible ; la loss porte ici sur la réponse et sa fin de séquence.', 'Une table distingue tokens, masque d’attention et labels. Les trois tokens de contexte ont attention un et label moins cent ; réponse et EOS sont supervisés ; PAD est masqué et ignoré.'),
    77: ('decalage_causal', 'Chaque logit à la position t vise le token t+1 ; appliquer ce décalage une seule fois.', 'Les entrées le, colis, arrive, demain, EOS sont alignées avec les cibles colis, arrive, demain, EOS, aucune. Les quatre premières sorties prédisent le token suivant.'),
    80: ('qlora', 'Base stockée en NF4 ; calcul en FP16 ici ; seuls les adaptateurs sont entraînables.', 'L’entrée se sépare entre une base W0 gelée en quatre bits et une branche LoRA A puis B et facteur alpha sur r. Les deux contributions sont additionnées en sortie. Le calcul des couches quantifiées utilise FP16 dans cet exemple.'),
    84: ('resume_fidele', 'Chaque affirmation du résumé doit être étayée par un fait de la source.', 'Trois faits de la source, référence AB123 reçue mardi, article manquant et vérification demandée, sont reliés à leurs formulations dans un résumé. Un remboursement effectué est signalé comme non étayé.'),
    200: ('word2vec', 'Mikolov et al. · Google, 2013 · Des vecteurs appris par prédiction locale.', 'Deux objectifs d’apprentissage Word2Vec sur le colis arrive. À gauche, CBOW combine les vecteurs des mots de contexte le et arrive par une moyenne pour prédire colis. À droite, Skip-gram utilise le vecteur de colis pour prédire séparément ses voisins le et arrive. Les vecteurs sont ajustés par les erreurs de prédiction.'),
}

# These keys identify drawing routines, not current slide positions.
SLIDE_TITLES = {
    17: 'Un embedding rapproche des usages similaires',
    29: 'Q, K, V : demander, comparer, récupérer',
    34: 'Le masque causal empêche de lire la réponse future',
    35: 'Plusieurs têtes : plusieurs comparaisons apprises',
    36: "Un bloc ne se limite pas à l'attention",
    38: 'Encodeur, décodeur, encodeur-décodeur',
    40: 'Décomposer pipeline() pour savoir ce qui se passe',
    49: 'Un encodeur et une tête répondent à notre question',
    58: 'Un mot annoté peut devenir plusieurs sous-tokens',
    75: 'Le chat template transforme les rôles en tokens',
    76: 'Superviser la réponse, garder la question dans le contexte',
    77: "Le décalage causal ne doit se produire qu'une fois",
    80: 'QLoRA : quantifier la base, entraîner les adaptateurs',
    84: 'Résumer : conserver les faits utiles sous une contrainte',
    200: 'Word2Vec : apprendre en prédisant les voisins',
}


def resolve_slide_numbers(slides):
    """Resolve every drawing by its unique title before writing any output."""
    if set(SPECS) != set(SLIDE_TITLES):
        raise ValueError('Every drawing must have exactly one stable slide title.')
    positions = {}
    for number, slide in enumerate(slides, 1):
        positions.setdefault(slide.get('title'), []).append(number)
    resolved = {}
    for internal_id, title in SLIDE_TITLES.items():
        matches = positions.get(title, [])
        if len(matches) != 1:
            raise ValueError(f'Expected exactly one slide titled {title!r}; found {len(matches)}.')
        resolved[internal_id] = matches[0]
    if len(set(resolved.values())) != len(resolved):
        raise ValueError('Two drawings resolve to the same slide.')
    return resolved


def build(number):
    name, caption, alt = SPECS[number]
    s = SVG(name.replace('_', ' '), alt)
    if number == 17:
        s.text(30, 32, 'Espace 2D construit pour expliquer', size=25, fill=MUTED)
        s.arrow([(75, 303), (620, 303)], color=MUTED, width=2)
        s.arrow([(75, 303), (75, 58)], color=MUTED, width=2)
        s.text(575, 342, 'Axe 1', size=25, fill=MUTED)
        s.text(84, 67, 'Axe 2', size=25, fill=MUTED)
        for x, y, label, col, dx, dy in [(322, 122, 'colis', BLUE, -7, -22), (373, 161, 'livraison', ORANGE, 14, 9), (555, 269, 'facture', BLUE, -50, -22)]:
            s.arrow([(75, 303), (x, y)], color=col, width=4)
            s.circle(x, y, 6, fill=col, stroke=col)
            s.text(x + dx, y + dy, label, size=29, fill=col, weight=700)
        s.box(695, 62, 475, 88, '« Où est mon colis ? »', size=29)
        s.arrow([(933, 159), (933, 195)], color=ORANGE)
        s.box(695, 205, 475, 88, '« Je n’ai rien reçu. »', size=29, accent=True)
        s.text(932, 339, 'Usages voisins à vérifier', size=27, anchor='middle', fill=MUTED)
    elif number == 29:
        s.box(22, 142, 195, 94, ['X', 'séquence'], size=30)
        for y, letter, role in [(18, 'Q', 'Ce que je recherche'), (143, 'K', 'Ce qui me rend repérable'), (268, 'V', 'Ce que je transmets')]:
            cy = y + 43
            s.arrow([(217, 189), (262, 189), (262, cy), (308, cy)])
            s.box(308, cy-55, 205, 110, [f'W{letter}', 'projection', 'apprise'], size=25)
            s.arrow([(514, cy), (570, cy)])
            s.box(571, y, 150, 86, letter, size=38, accent=letter == 'V')
            s.arrow([(722, cy), (774, cy)], color=ORANGE if letter == 'V' else BLUE)
            s.box(775, y, 405, 86, role, size=27, fill=WHITE)
    elif number == 34:
        cols = ['le', 'colis', 'arrive', 'demain']
        s.text(520, 29, 'Clés : positions lues', size=27, anchor='middle', fill=BLUE, weight=600)
        s.text(25, 65, 'Query', size=27, fill=BLUE, weight=600)
        for c, token in enumerate(cols):
            s.text(355 + 110*c, 68, token, size=26, anchor='middle')
        for r, token in enumerate(cols):
            y = 83 + r*63
            s.text(240, y+40, f'{r+1} · {token}', size=26, anchor='end')
            for c in range(4):
                s.box(300+c*110, y, 108, 61, '0' if c <= r else '−∞', size=30, accent=c > r, radius=5)
        s.rect(296, 205, 448, 70, fill='none', stroke=ORANGE, width=3, radius=7)
        s.box(815, 90, 360, 62, '0 : accès autorisé', size=26)
        s.box(815, 170, 360, 62, '−∞ : accès interdit', size=26, accent=True)
        s.text(995, 282, ['La ligne 3 lit', 'les positions 1, 2 et 3.'], size=27, anchor='middle')
    elif number == 35:
        s.box(22, 140, 185, 98, ['X', 'séquence'], size=29)
        for y, n in [(40, 1), (225, 2)]:
            s.arrow([(207, 189), (250, 189), (250, y+55), (292, y+55)])
            s.box(292, y, 235, 110, [f'Tête {n}', f'Q{n}, K{n}, V{n}', '→ attention'], size=25, accent=n == 2)
            s.arrow([(528, y+55), (574, y+55), (574, 189), (620, 189)], color=ORANGE if n == 2 else BLUE)
        s.box(620, 132, 235, 114, ['Concaténation', '[ tête 1 | tête 2 ]'], size=27)
        s.arrow([(855, 189), (903, 189)])
        s.box(904, 140, 275, 98, ['Projection WO', 'sortie : d_model'], size=28)
        s.text(600, 359, 'Deux têtes illustrées ; leurs rôles ne sont pas fixés à l’avance.', size=25, anchor='middle', fill=MUTED)
    elif number == 36:
        s.text(25, 32, 'Exemple Post-LN · type BERT', size=26, fill=MUTED)
        s.box(20, 154, 90, 64, 'x', size=32)
        s.box(156, 132, 160, 108, 'Attention', size=27)
        s.circle(368, 186, 27, '+')
        s.box(421, 145, 138, 82, ['Layer', 'Norm'], size=27)
        s.box(611, 132, 145, 108, 'FFN', size=29)
        s.circle(810, 186, 27, '+')
        s.box(858, 145, 138, 82, ['Layer', 'Norm'], size=27)
        s.box(1043, 154, 135, 64, 'sortie', size=27)
        for a, b in [(110,156),(316,341),(395,421),(559,611),(756,783),(837,858),(996,1043)]:
            s.arrow([(a,186),(b,186)])
        s.arrow([(129,186),(129,76),(368,76),(368,156)], color=ORANGE)
        s.text(251, 66, 'résidu', size=25, fill=ORANGE, anchor='middle')
        s.arrow([(584,186),(584,308),(810,308),(810,216)], color=ORANGE)
        s.text(686, 345, 'résidu', size=25, fill=ORANGE, anchor='middle')
        s.text(231, 282, ['entre', 'positions'], size=25, anchor='middle', fill=MUTED)
        s.text(685, 275, 'par position', size=25, anchor='middle', fill=MUTED)
    elif number == 38:
        for x, title in [(15,'BERT · encodeur'),(415,'GPT · décodeur'),(815,'T5 · encodeur-décodeur')]:
            s.rect(x, 12, 370, 352, fill=WHITE, stroke='#D5D8E4', radius=18)
            s.text(x+185, 50, title, size=27, fill=BLUE, weight=700, anchor='middle')
        s.text(200, 105, 'Représentations', size=27, anchor='middle')
        s.box(44, 146, 312, 89, ['Self-attention', 'bidirectionnelle'], size=28)
        s.arrow([(200,146),(200,117)])
        s.box(69, 281, 262, 58, 'Texte complet', size=27)
        s.arrow([(200,280),(200,240)])
        s.text(600, 105, 'Token suivant', size=27, anchor='middle')
        s.box(444, 146, 312, 89, ['Self-attention', 'causale'], size=28, accent=True)
        s.arrow([(600,146),(600,117)], color=ORANGE)
        s.box(457, 281, 286, 58, 'Tokens déjà produits', size=25, accent=True)
        s.arrow([(600,280),(600,240)], color=ORANGE)
        s.text(1090, 112, 'Token suivant', size=25, anchor='middle')
        s.box(833, 184, 146, 75, 'Encodeur', size=25)
        s.box(1012, 184, 156, 75, ['Décodeur', 'causal'], size=25, accent=True)
        s.arrow([(979,221),(1008,221)])
        s.text(834, 152, 'Cross-attention', size=25, fill=BLUE)
        s.box(833, 285, 146, 70, ['Texte', 'source'], size=25)
        s.box(1012, 285, 156, 70, ['Tokens déjà', 'produits'], size=25, accent=True)
        s.arrow([(906,284),(906,263)], width=2)
        s.arrow([(1090,284),(1090,263)], color=ORANGE, width=2)
        s.arrow([(1090,184),(1090,125)], color=ORANGE)
    elif number == 40:
        s.text(27, 51, 'Exemple : classification d’un message', size=27, fill=MUTED)
        for x, w, value, accent in [(23,180,['« colis','perdu »'],False),(262,200,['Tokenizer','IDs + masque'],False),(521,183,['Modèle','logits'],False),(763,200,['Post-traiter','argmax'],True),(1022,156,['Catégorie','livraison'],True)]:
            s.box(x, 135, w, 111, value, size=26, accent=accent)
        for a,b in [(203,256),(462,515),(704,757),(963,1016)]:
            s.arrow([(a,190),(b,190)])
        s.text(362, 291, 'IDs illustratifs', size=25, anchor='middle', fill=MUTED)
        s.text(612, 291, 'scores de classes', size=25, anchor='middle', fill=MUTED)
        s.text(861, 291, 'règle de décision', size=25, anchor='middle', fill=MUTED)
    elif number == 49:
        s.box(20, 140, 182, 95, ['Texte', '4 tokens'], size=28)
        s.arrow([(202,187),(252,187)])
        s.box(253, 108, 235, 158, ['Encodeur', 'H : 4 × d'], size=31)
        for y, rep, head, out in [(28,['Représentation','globale'],['Tête globale','5 logits'],'1 classe / message'),(230,['Représentation','de chaque token'],['Tête NER','4 × C logits'],'1 label / token')]:
            s.arrow([(488,187),(548,187),(548,y+48),(610,y+48)])
            s.box(611,y,245,96,rep,size=27)
            s.arrow([(856,y+48),(921,y+48)])
            s.box(922,y,258,96,head,size=28,accent=True)
            s.text(1051,y+128,out,size=25,anchor='middle',fill=ORANGE)
    elif number == 58:
        s.text(28, 98, 'Mot', size=29, weight=600)
        s.text(28, 193, 'Token', size=29, weight=600)
        s.text(28, 291, 'Label', size=29, weight=600)
        xs = [198+i*160 for i in range(6)]
        for col, word, w in [(0,'—',154),(1,'Marie',154),(2,'Dupont',314),(4,'Lyon',154),(5,'—',154)]:
            s.box(xs[col],55,w,62,word,size=28,fill=WHITE)
        for i,(token,label) in enumerate(zip(['[CLS]','Marie','Du','##pont','Lyon','[SEP]'],['−100','B-PER','I-PER','−100','B-LOC','−100'])):
            s.box(xs[i],150,154,62,token,size=27)
            s.box(xs[i],249,154,62,label,size=29,accent=label!='−100',fill=GREY if label=='−100' else None,stroke=MUTED if label=='−100' else None)
            s.arrow([(xs[i]+77,216),(xs[i]+77,244)],color=MUTED)
        for i in [0,1,4,5]:
            s.arrow([(xs[i]+77,121),(xs[i]+77,146)],color=MUTED)
        s.arrow([(xs[2]+157,118),(xs[2]+157,131),(xs[2]+77,131),(xs[2]+77,146)])
        s.arrow([(xs[2]+157,131),(xs[3]+77,131),(xs[3]+77,146)])
        s.text(680,355,'−100 : pas de contribution à la loss',size=26,fill=MUTED,anchor='middle')
    elif number == 75:
        s.text(164,30,'Messages',size=27,fill=BLUE,weight=600,anchor='middle')
        for y, role, content in [(48,'system','Style concis.'),(150,'user','Où est AB123 ?'),(252,'assistant','Je vérifie.')]:
            s.box(20,y,284,78,[role,content],size=26,accent=role=='assistant')
        s.arrow([(306,190),(375,190)])
        s.text(610,30,'Texte rendu',size=27,fill=BLUE,weight=600,anchor='middle')
        s.rect(388,46,445,304,fill=LIGHT)
        s.text(405,75,['<|im_start|>system','Style concis.<|im_end|>','<|im_start|>user','Où est AB123 ?<|im_end|>','<|im_start|>assistant','Je vérifie.<|im_end|>'],size=25,mono=True,gap=48)
        s.arrow([(836,190),(894,190)])
        s.text(1036,81,'Tokenizer',size=28,fill=BLUE,weight=600,anchor='middle')
        s.box(907,108,264,62,'IDs des marqueurs',size=25)
        s.box(907,188,264,62,'IDs du texte',size=25,accent=True)
        s.text(1039,302,'IDs illustratifs',size=25,fill=MUTED,anchor='middle')
    elif number == 76:
        xs=[205+i*160 for i in range(6)]
        s.text(436,31,'Contexte fourni',size=27,fill=BLUE,anchor='middle',weight=600)
        s.text(838,31,'Réponse cible',size=27,fill=ORANGE,anchor='middle',weight=600)
        s.text(1081,31,'Padding',size=26,fill=MUTED,anchor='middle')
        for y, title in [(110,'Tokens'),(205,'Attention'),(300,'Labels')]:
            s.text(20,y,title,size=27,weight=600)
        for i, token in enumerate(['[SYS]','[USR]','[AST]','livraison','EOS','PAD']):
            s.box(xs[i],73,152,60,token,size=26,accent=i in [3,4],fill=GREY if i==5 else None,stroke=MUTED if i==5 else None)
            s.box(xs[i],168,152,60,'0' if i==5 else '1',size=31,fill=GREY if i==5 else WHITE,stroke=MUTED if i==5 else BLUE)
            supervised=i in [3,4]
            s.box(xs[i],263,152,60,('ID' if i==3 else 'ID_EOS') if supervised else '−100',size=27,accent=supervised,fill=None if supervised else GREY,stroke=None if supervised else MUTED)
        s.text(600,362,'Visibilité du contexte ≠ supervision de la loss',size=26,fill=MUTED,anchor='middle')
    elif number == 77:
        s.text(25,120,['Entrée','à la position t'],size=27,weight=600)
        s.text(25,272,['Cible','token t+1'],size=27,weight=600)
        for i,(token,target) in enumerate(zip(['le','colis','arrive','demain','EOS'],['colis','arrive','demain','EOS','—'])):
            x=235+i*187
            s.text(x+83,43,str(i+1),size=27,fill=MUTED,anchor='middle')
            s.box(x,70,165,70,token,size=29)
            s.box(x,241,165,70,target,size=29,accent=i<4,fill=GREY if i==4 else None,stroke=MUTED if i==4 else None)
            if i<4:
                s.arrow([(x+83,145),(x+83,231)],color=ORANGE)
                s.text(x+102,193,f'logit {i+1}',size=25,fill=ORANGE)
            else:
                s.text(x+83,193,'ignoré',size=25,anchor='middle',fill=MUTED)
    elif number == 80:
        s.box(18,144,101,82,'x',size=33)
        s.box(283,26,478,92,['W₀ : base figée','poids stockés en NF4 · 4 bits'],size=28)
        s.arrow([(119,185),(184,185),(184,72),(279,72)])
        s.text(522,157,'Calcul de ces couches : FP16',size=26,fill=BLUE,anchor='middle')
        s.arrow([(761,72),(931,72),(931,149)])
        s.box(262,234,159,83,['A','rang r'],size=29,accent=True)
        s.box(480,234,159,83,['B','projection'],size=28,accent=True)
        s.box(697,240,123,71,'α / r',size=31,accent=True)
        s.arrow([(184,185),(184,275),(257,275)],color=ORANGE)
        s.arrow([(422,275),(475,275)],color=ORANGE)
        s.arrow([(640,275),(692,275)],color=ORANGE)
        s.arrow([(821,275),(931,275),(931,221)],color=ORANGE)
        s.circle(931,185,33,'+')
        s.arrow([(966,185),(1026,185)])
        s.box(1029,144,151,82,'y',size=33)
        s.text(546,358,'A et B : paramètres entraînables',size=27,fill=ORANGE,weight=600,anchor='middle')
    elif number == 84:
        s.text(243,34,'Faits de la source',size=28,fill=BLUE,weight=600,anchor='middle')
        facts=['AB123 reçu mardi.','Un article manque.','Vérification demandée.']
        for i,fact in enumerate(facts):
            y=60+i*92
            s.box(20,y,450,69,fact,size=28)
            s.arrow([(474,y+34),(594,y+34),(594,94+i*38),(690,94+i*38)])
        s.text(943,34,'Résumé fidèle',size=28,fill=BLUE,weight=600,anchor='middle')
        s.box(695,59,487,151,['AB123 reçu mardi ;','un article manque.','Vérification demandée.'],size=28,fill=WHITE)
        s.box(695,272,487,60,'« Remboursement effectué »',size=26,accent=True)
        s.text(941,255,'Non étayé par la source',size=26,fill=ORANGE,weight=600,anchor='middle')
    elif number == 200:
        s.rect(12,10,575,350,fill=WHITE,stroke=BLUE,radius=18)
        s.rect(612,10,575,350,fill=WHITE,stroke=ORANGE,radius=18)
        s.text(299,49,'CBOW',size=32,fill=BLUE,weight=700,anchor='middle')
        s.text(899,49,'Skip-gram',size=32,fill=ORANGE,weight=700,anchor='middle')
        s.text(299,89,'Contexte → mot central',size=26,anchor='middle')
        s.text(899,89,'Mot central → contexte',size=26,anchor='middle')
        s.box(27,140,110,64,'le',size=29)
        s.box(27,237,110,64,'arrive',size=29)
        s.box(202,166,189,100,['Moyenne','des vecteurs'],size=26)
        s.arrow([(139,172),(169,172),(169,202),(195,202)])
        s.arrow([(139,269),(169,269),(169,232),(195,232)])
        s.text(515,155,'Prédire',size=25,fill=ORANGE,anchor='middle')
        s.arrow([(394,216),(454,216)],color=ORANGE)
        s.box(460,184,110,64,'colis',size=29,accent=True)
        s.box(637,184,110,64,'colis',size=29)
        s.arrow([(750,216),(780,216)])
        s.box(786,166,169,100,['Vecteur','de « colis »'],size=25)
        s.text(1099,126,'Prédire',size=25,fill=ORANGE,anchor='middle')
        s.arrow([(958,202),(990,202),(990,172),(1037,172)],color=ORANGE)
        s.arrow([(958,232),(990,232),(990,269),(1037,269)],color=ORANGE)
        s.box(1044,140,110,64,'le',size=29,accent=True)
        s.box(1044,237,110,64,'arrive',size=29,accent=True)
        s.text(299,336,'« le colis arrive » · fenêtre de 1',size=24,fill=MUTED,anchor='middle')
        s.text(899,336,'Deux voisins : deux cibles à prédire',size=24,fill=MUTED,anchor='middle')
    else:
        raise ValueError(number)
    return s.finish(), caption, alt


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--svg-only',action='store_true',help='Write vector diagrams without rendering PNGs')
    parser.add_argument('--png-width',type=int,default=2400)
    args=parser.parse_args()
    if args.png_width < 1600:
        parser.error('Use a PNG width of at least 1600 pixels for legible slide assets.')
    source=json.loads((ROOT/'course/slides.json').read_text(encoding='utf-8'))
    slides=source if isinstance(source,list) else source['slides']
    resolved=resolve_slide_numbers(slides)
    renderer=shutil.which('rsvg-convert') or shutil.which('magick')
    if not args.svg_only and not renderer:
        parser.error('Install librsvg (rsvg-convert) or ImageMagick, or pass --svg-only.')
    manifest_path=OUT/'manifest.json'
    previous=json.loads(manifest_path.read_text(encoding='utf-8')) if manifest_path.is_file() else {}
    OUT.mkdir(parents=True,exist_ok=True)
    manifest={}
    for internal_id,(slug,_,_) in SPECS.items():
        number=resolved[internal_id]
        svg,caption,alt=build(internal_id)
        ET.fromstring(svg)
        vector=OUT/f'{number:02}_{slug}.svg'
        raster=vector.with_suffix('.png')
        vector.write_text(svg,encoding='utf-8')
        if not args.svg_only:
            if Path(renderer).name=='rsvg-convert':
                subprocess.run([renderer,'--width',str(args.png_width),'--output',str(raster),str(vector)],check=True)
            else:
                subprocess.run([renderer,'-background','white','-density','192',str(vector),'-resize',str(args.png_width),str(raster)],check=True)
            header=raster.read_bytes()[:24]
            if header[:8] != b'\x89PNG\r\n\x1a\n' or int.from_bytes(header[16:20],'big') != args.png_width or int.from_bytes(header[20:24],'big') <= 0:
                raise ValueError(f'Invalid rendered PNG dimensions: {raster}')
        manifest[str(number)]={'svg':str(vector.relative_to(ROOT)),'png':str(raster.relative_to(ROOT)),'caption':caption,'alt':alt,'slide_title':SLIDE_TITLES[internal_id]}
    manifest=dict(sorted(manifest.items(),key=lambda item:int(item[0])))
    manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    retired=[]
    if not args.svg_only:
        old_paths={str(asset[key]) for asset in previous.values() for key in ('svg','png') if asset.get(key)}
        new_paths={asset[key] for asset in manifest.values() for key in ('svg','png')}
        # Retire only files explicitly owned by the previous manifest, after all renders validate.
        for name in sorted(old_paths-new_paths):
            file=(ROOT/name).resolve()
            if file.parent != OUT.resolve() or file.suffix not in {'.svg','.png'} or not file.is_file():
                continue
            backup=ROOT/'.build/diagrams-retired'
            backup.mkdir(parents=True,exist_ok=True)
            (backup/'manifest-before-refresh.json').write_text(json.dumps(previous,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
            shutil.copy2(file,backup/file.name)
            file.unlink()
            retired.append(name)
    print(json.dumps({'diagrams':len(manifest),'format':'SVG + PNG' if not args.svg_only else 'SVG','png_width':args.png_width if not args.svg_only else None,'manifest':str(manifest_path.relative_to(ROOT)),'retired_files':retired},ensure_ascii=False))


if __name__=='__main__':
    main()
