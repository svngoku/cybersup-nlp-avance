/** Build an editable course from the supplied Cybersup template. */
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath, pathToFileURL } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const deps = process.env.NLP_RUNTIME_MODULES || '/Users/svngoku/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
process.env.RUNTIME_NODE_MODULES ||= deps;
const skill = process.env.NLP_SLIDES_SKILL || '/Users/svngoku/.codex/plugins/cache/openai-primary-runtime/presentations/26.909.12148/skills/presentations';
const python = process.env.NLP_RUNTIME_PYTHON || '/Users/svngoku/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3';
const { FileBlob, PresentationFile } = await import(pathToFileURL(path.join(deps, '@oai/artifact-tool/dist/artifact_tool.mjs')));
const { finalizePresentation } = await import(pathToFileURL(path.join(skill, 'container_tools/artifact_tool_utils.mjs')));
const template = path.join(root, 'CYBERSUP - TEMPLATE DATA_IA.pptx');
const build = path.join(root, '.build');
const out = path.join(root, 'output');
await fs.mkdir(build, { recursive: true }); await fs.mkdir(out, { recursive: true });
const source = JSON.parse(await fs.readFile(path.join(root, 'course/slides.json'), 'utf8'));
const slides = Array.isArray(source) ? source : source.slides;
if (!slides?.length) throw new Error('Missing course slides');
const diagrams = JSON.parse(await fs.readFile(path.join(root,'assets/diagrams/manifest.json'),'utf8'));
const formulas = JSON.parse(await fs.readFile(path.join(root,'assets/formulas/manifest.json'),'utf8'));
const p = await PresentationFile.importPptx(await FileBlob.load(template));
const originals = [...p.slides.items];
const tableOwners = [];
const manifest = [];
const label = ['Programme', 'Fondations', 'Transformers', 'Fine-tuning', 'LLM et adaptation', 'Évaluation et projet'];
const COLORS = { ink:'#111111', accent:'#BF2E00', blue:'#282A59', muted:'#50505C' };

function text(slide, name, value, x, y, w, h, size=26, opts={}) {
  const shape = slide.shapes.add({name, geometry:'textbox', position:{left:x,top:y,width:w,height:h}, fill:'none', line:{fill:'none',width:0}});
  shape.text=String(value);
  shape.text.style={typeface:'DM Sans',fontSize:size,color:COLORS.ink,autoFit:'none',wrap:'square',verticalAlignment:'top',insets:{left:0,right:0,top:0,bottom:0},...opts};
  return shape;
}
function setText(shape, value, size, color) {
  shape.text=value;
  if(size) shape.text.style={fontSize:size, ...(color?{color}:{}),autoFit:'none'};
}
function common(slide, day, index) {
  for(const shape of slide.shapes.items){
    const raw=shape.text.toString();
    if(raw.includes('{{NOM_DU_COURS}}')) setText(shape, 'NLP avancé  ·  M2 IA', 17.333);
    else if(raw.includes('{{AN1-AN2}}')) setText(shape, '/2026–2027', 17.333);
    else if(raw.includes('{{NOM_DU_CHAPITRE}}') && shape.position.top < 100) setText(shape, `J${day} · ${label[day]}`, 16);
  }
  if(index>0) text(slide,'folio',String(index+1),1171,583,28,21,13,{alignment:'right',color:COLORS.muted});
}
function bodyLines(slide, bullets, top, height, width=1115, size=27) {
  const count=bullets.length;
  if(!count)return;
  const step=height/count;
  bullets.forEach((b,j)=>{
    text(slide,`body-${j+1}`,b,82,top+j*step,width,Math.min(step-5,90),size);
  });
}

async function insertAsset(slide, asset, position) {
  if(!asset?.png) throw new Error('Missing rendered image asset');
  return slide.images.add({blob:new Uint8Array(await fs.readFile(path.join(root,asset.png))),contentType:'image/png',alt:asset.alt||asset.caption||'Illustration pédagogique',fit:'contain',position});
}
function equationPosition(asset, frame) {
  const width=Number(asset.display_width),height=Number(asset.display_height);
  if(!Number.isFinite(width)||!Number.isFinite(height)||width<=0||height<=0)throw new Error('Missing formula display dimensions');
  const scale=Math.min(1,frame.width/width,frame.height/height);
  const finalWidth=width*scale,finalHeight=height*scale;
  return {left:frame.left+(frame.width-finalWidth)/2,top:frame.top+(frame.height-finalHeight)/2,width:finalWidth,height:finalHeight};
}
function nativeTable(slide,d,position,size=22) {
  const values=[d.table.headers,...d.table.rows].map(row=>row.map(String));
  const table=slide.tables.add({rows:values.length,columns:values[0].length,...position,values,columnTracks:values[0].map(()=>({mode:'fr',value:1}))});
  table.cells.block({row:0,column:0,rowCount:values.length,columnCount:values[0].length}).assign({textStyle:{typeface:'DM Sans',fontSize:size,color:COLORS.ink},margins:{left:10,right:10,top:8,bottom:8},anchor:'center'});
  table.borders.assign({fill:'#D5D5DD',width:.7});
  for(let r=0;r<values.length;r++)for(let c=0;c<values[0].length;c++){
    const cell=table.getCell(r,c);cell.fill=r===0?COLORS.blue:r%2?'#F4F3F2':'#FFFFFF';
    cell.text.style={typeface:'DM Sans',fontSize:size,color:r===0?'#FFFFFF':COLORS.ink,bold:r===0,verticalAlignment:'middle',autoFit:'none'};
  }
  return table;
}
function additionalNotes(d,i) {
  const visual=diagrams[String(i+1)],equation=formulas[String(i+1)];
  const notes=[];
  if(visual){
    notes.push(`Description accessible du schéma\n${visual.alt}\n${visual.caption}`);
    notes.push(`Repères associés à l'illustration\n${[d.lead,...(d.bullets||[]),...(d.table?[d.table.headers.join(' | '),...d.table.rows.map(r=>r.join(' | '))]:[])].filter(Boolean).join('\n')}`);
  }
  if(equation)notes.push(`Source de l'image de formule — LaTeX\n${d.formula_latex}\n\nLégende projetée\n${(d.formula_symbols||[]).join('\n')}\n\n${d.formula_example||''}`);
  return notes.join('\n\n');
}

for(let i=0;i<slides.length;i++){
  const d=slides[i];
  const isCover=d.kind==='cover'; const isSection=d.kind==='section';
  const slide=(isCover?originals[0]:isSection?originals[4]:originals[5]).duplicate();
  slide.moveTo(originals.length + i);
  common(slide,d.day||0,i);
  if(isCover){
    for(const shape of slide.shapes.items){
      const raw=shape.text.toString();
      if(shape.position.top<200 && raw==='NLP avancé  ·  M2 IA') {setText(shape,'NLP AVANCÉ',80,'#FFFFFF');}
      if(raw.includes('{{SOUS-TITRE}}')){setText(shape,'(BERT, GPT, Hugging Face)',46,'#FFFFFF');shape.position={...shape.position,height:140};}
      if(raw.includes('{{LOGO}}'))setText(shape,'35 H',22,COLORS.accent);
      if(raw==='SCAN ME')setText(shape,'COLAB T4',12,COLORS.ink);
      if(raw==='SYLLABUS')setText(shape,'5 JOURS',12,COLORS.ink);
    }
    text(slide,'presenter','Chrys NIONGOLO',96,432,860,40,28,{color:'#FFFFFF'});
    text(slide,'format','15 h de notions et d’exemples · 20 h de pratique',96,484,890,55,26,{color:'#FFFFFF'});
  } else if(isSection){
    for(const shape of [...slide.shapes.items]){
      if(shape.text.toString()==='01')setText(shape,String(d.day).padStart(2,'0'),72,'#FFFFFF');
      if(shape.text.toString().includes('{{NOM_DU_CHAPITRE}}')){
        const title=d.title.replace(/^Jour\s+\d+\s*[·—:–-]?\s*/i,'');
        shape.delete();
        text(slide,'section-title',title,272,205,885,170,48,{typeface:'Archivo Black',color:'#FFFFFF',verticalAlignment:'middle'});
      }
    }
    if(d.lead)text(slide,'day-goal',d.lead,100,444,1080,77,27,{color:'#FFFFFF'});
    if(d.bullets?.length)text(slide,'day-agenda',d.bullets.join('\n'),100,533,1080,74,20,{color:'#FFFFFF'});
  } else {
    const titleSize=d.title.length>67?36:d.title.length>51?40:43;
    text(slide,'course-title',d.title,80,84,1118,110,titleSize,{typeface:'Archivo Black'});
    const diagram=diagrams[String(i+1)],equation=formulas[String(i+1)];
    if(diagram){
      await insertAsset(slide,diagram,{left:82,top:183,width:1115,height:350});
      text(slide,'diagram-caption',diagram.caption,82,546,1115,44,23,{color:COLORS.accent});
    } else if(equation){
      if(!d.formula_latex || !d.formula_symbols?.length)throw new Error(`Missing LaTeX annotations on slide ${i+1}`);
      await insertAsset(slide,equation,equationPosition(equation,{left:82,top:195,width:1115,height:118}));
      text(slide,'formula-caption',d.formula_caption||'',82,325,1115,42,24,{color:COLORS.accent});
      if(d.table){
        nativeTable(slide,d,{left:82,top:375,width:650,height:185},20);
        tableOwners.push(i+1);
        d.formula_symbols.forEach((item,j)=>text(slide,`formula-symbol-${j}`,item,755,376+j*43,443,43,21));
      } else {
        d.formula_symbols.forEach((item,j)=>text(slide,`formula-symbol-${j}`,item,82+(j%2)*572,380+Math.floor(j/2)*49,543,47,22));
        if(d.formula_example)text(slide,'formula-example',d.formula_example,82,541,1115,46,22,{color:COLORS.blue,bold:true});
      }
    } else {
    if(d.formula)throw new Error(`Formula image missing on slide ${i+1}`);
    let top=205;
    if(d.lead){text(slide,'concrete-example',d.lead,82,199,1113,77,27,{color:COLORS.accent,bold:true});top=287;}
    if(d.table){
      const vals=[d.table.headers,...d.table.rows].map(r=>r.map(String));
      const formulaH=d.formula?65:0;
      const bullets=d.bullets||[];
      const remaining=579-top-formulaH;
      const tableHeight=Math.min(remaining-(bullets.length?76:0),Math.max(150,vals.length*51));
      const table=slide.tables.add({rows:vals.length,columns:vals[0].length,left:82,top,width:1115,height:tableHeight,values:vals,columnTracks:vals[0].map(()=>({mode:'fr',value:1}))});
      const fs=vals[0].length>=4?20:22;
      table.cells.block({row:0,column:0,rowCount:vals.length,columnCount:vals[0].length}).assign({textStyle:{typeface:'DM Sans',fontSize:fs,color:COLORS.ink},margins:{left:12,right:12,top:9,bottom:9},anchor:'center'});
      table.borders.assign({fill:'#D5D5DD',width:.7});
      for(let r=0;r<vals.length;r++)for(let c=0;c<vals[0].length;c++){
        const cell=table.getCell(r,c);cell.fill=r===0?COLORS.blue:r%2?'#F4F3F2':'#FFFFFF';
        cell.text.style={typeface:'DM Sans',fontSize:fs,color:r===0?'#FFFFFF':COLORS.ink,bold:r===0,verticalAlignment:'middle',autoFit:'none'};
      }
      tableOwners.push(i+1);top+=tableHeight+15;
      if(d.formula){text(slide,'formula',d.formula,82,top,1115,57,24,{typeface:'Roboto Mono',color:COLORS.blue});top+=65;}
      if(bullets.length)text(slide,'table-takeaway',bullets.join(' '),82,top,1115,70,22,{color:COLORS.muted});
    } else if(d.formula){
      text(slide,'formula',d.formula,82,top,1115,83,30,{typeface:'Roboto Mono',color:COLORS.blue});
      bodyLines(slide,d.bullets||[],top+103,575-top-103,1115,25);
    } else {
      bodyLines(slide,d.bullets||[],top,578-top,1115,27);
    }
    }
  }
  const notes=[`DIAPOSITIVE ${i+1} — ${d.title}`,`Jour ${d.day||0} · ${d.period||'repère'} · ${d.minutes||0} min`,d.notes||'',additionalNotes(d,i),d.sources?.length?`\nSources\n${d.sources.join('\n')}`:''].join('\n\n');
  slide.speakerNotes.textFrame.setText(notes);
  manifest.push({slide:i+1,id:slide.id,title:d.title,day:d.day,minutes:d.minutes,period:d.period,notesWords:notes.split(/\s+/).length,table:tableOwners.includes(i+1),diagram:!!diagrams[String(i+1)],formulaImage:!!formulas[String(i+1)]});
}
for(const s of originals)s.delete();
const candidate=path.join(build,'candidate.pptx');
await (await PresentationFile.exportPptx(p)).save(candidate);
const finalPath=path.join(out,process.env.NLP_DECK_NAME||'CYBERSUP-NLP-M2-35h-visuel.pptx');
const result=await finalizePresentation({workspaceDir:root,candidatePath:candidate,finalPath,pythonExecutable:python,
  integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
  layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
  layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit',...tableOwners.flatMap(n=>['--require-native-table-slide',String(n)])],
  explicitTotalSlideCount:slides.length,requiredNativeTableOwnerSlides:tableOwners,
  fontPolicy:{basis:'reference',families:['Archivo Black','DM Sans','Roboto Mono'],referencePath:template,referenceSha256:crypto.createHash('sha256').update(await fs.readFile(template)).digest('hex')},
  verifyArtifactToolImport:true,receiptPath:path.join(build,`${path.parse(finalPath).name}.validation.json`)});
await fs.writeFile(path.join(build,'slides-manifest.json'),JSON.stringify(manifest,null,2));
await fs.writeFile(path.join(out,'Notes-presentateur.md'),('# NLP Avancé (BERT, GPT, Hugging Face) — Notes du présentateur\n\nChrys NIONGOLO · Cybersup · M2 IA · 35 heures\n\n'+slides.map((d,i)=>`## ${i+1}. ${d.title}\n\nJour ${d.day||0} · ${d.period||'repère'} · ${d.minutes||0} min\n\n${d.notes||''}\n\n${additionalNotes(d,i)}\n\n${(d.sources||[]).map(s=>`- ${s}`).join('\n')}\n`).join('\n')).trimEnd()+'\n');
console.log(JSON.stringify({finalPath,slides:slides.length,tables:tableOwners.length,notesWords:manifest.reduce((s,x)=>s+x.notesWords,0),result},null,2));
