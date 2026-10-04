#!/usr/bin/env node
/**
 * Render original LaTeX equations as standalone SVG and transparent PNG.
 * Install once: npm --prefix tools-visuals install
 * Run: node scripts/build_formulas.mjs --help
 * This script never accesses .build/node_modules or a user-specific runtime path.
 */
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const defaults = {
  source: 'course/slides.json', out: 'assets/formulas', runtime: 'tools-visuals',
  'max-width': 1115, 'max-height': 110, 'font-size': 44, scale: 3, color: '#282A59',
};

function help() {
  console.log(`Render course equations with MathJax 3.2.2 and Sharp 0.34.3.

Usage: node scripts/build_formulas.mjs [options]
  --source PATH       Slides JSON, default course/slides.json
  --out PATH          Asset directory, default assets/formulas
  --runtime PATH      Package directory, default tools-visuals
  --max-width NUMBER  Maximum display width in pixels, default 1115
  --max-height NUMBER Maximum display height in pixels, default 110
  --font-size NUMBER  Preferred TeX em size in pixels, default 44
  --scale NUMBER      PNG pixels per display pixel, default 3 (integer)
  --color '#RRGGBB'   Formula color, default '#282A59'
  --help              Show this help

Paths are resolved relative to the course root, not the shell working directory.
Install: npm --prefix tools-visuals ci (or install before a lockfile exists).
No network access or dependency installation is performed by this renderer.`);
}

function parseArgs(argv) {
  const options = { ...defaults };
  for (let i = 0; i < argv.length; i++) {
    const flag = argv[i];
    if (flag === '--help' || flag === '-h') { help(); return null; }
    if (!flag.startsWith('--') || !(flag.slice(2) in defaults)) throw new Error(`Unknown option: ${flag}`);
    const key = flag.slice(2);
    const value = argv[++i];
    if (value === undefined || value.startsWith('--')) throw new Error(`Missing value for ${flag}`);
    options[key] = typeof defaults[key] === 'number' ? Number(value) : value;
  }
  for (const key of ['max-width', 'max-height', 'font-size', 'scale']) {
    if (!Number.isFinite(options[key]) || options[key] <= 0) throw new Error(`${key} must be positive.`);
  }
  if (!Number.isInteger(options.scale) || options.scale > 8) throw new Error('scale must be an integer between 1 and 8.');
  if (options['max-width'] < 40 || options['max-height'] < 30) throw new Error('Display bounds are too small.');
  if (!/^#[\da-f]{6}$/i.test(options.color)) throw new Error('color must use #RRGGBB notation.');
  return options;
}

const xml = value => String(value).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const relative = value => path.relative(ROOT, value).split(path.sep).join('/');
const sha256 = value => crypto.createHash('sha256').update(value).digest('hex');

async function main(options) {
  const sourcePath = path.resolve(ROOT, options.source);
  const outputDir = path.resolve(ROOT, options.out);
  const runtimeDir = path.resolve(ROOT, options.runtime);
  const sourceText = await fs.readFile(sourcePath, 'utf8');
  const source = JSON.parse(sourceText);
  const slides = Array.isArray(source) ? source : source.slides;
  if (!Array.isArray(slides) || !slides.length) throw new Error('Slides JSON must contain a nonempty array.');
  const formulas = slides.flatMap((slide, index) => {
    if (slide.formula_latex === undefined || slide.formula_latex === null) return [];
    if (typeof slide.formula_latex !== 'string' || !slide.formula_latex.trim()) {
      throw new Error(`Slide ${index + 1}: formula_latex must be a nonempty string.`);
    }
    return [{ ...slide, number: index + 1, latex: slide.formula_latex.trim() }];
  });
  if (!formulas.length) throw new Error('No formula_latex fields found. Wait for the course LaTeX sources before rendering.');

  const require = createRequire(path.join(runtimeDir, 'package.json'));
  let mathjax, TeX, SVG, liteAdaptor, RegisterHTMLHandler, AllPackages, sharp;
  try {
    ({ mathjax } = require('mathjax-full/js/mathjax.js'));
    ({ TeX } = require('mathjax-full/js/input/tex.js'));
    ({ SVG } = require('mathjax-full/js/output/svg.js'));
    ({ liteAdaptor } = require('mathjax-full/js/adaptors/liteAdaptor.js'));
    ({ RegisterHTMLHandler } = require('mathjax-full/js/handlers/html.js'));
    ({ AllPackages } = require('mathjax-full/js/input/tex/AllPackages.js'));
    sharp = require('sharp');
  } catch (error) {
    throw new Error(`Formula runtime unavailable. Run npm --prefix ${relative(runtimeDir)} ci or install. ${error.message}`);
  }
  const actualMathJax = require('mathjax-full/package.json').version;
  const actualSharp = require('sharp/package.json').version;
  if (actualMathJax !== '3.2.2' || actualSharp !== '0.34.3') {
    throw new Error(`Unexpected runtime versions: MathJax ${actualMathJax}, Sharp ${actualSharp}. Restore the lockfile versions.`);
  }

  const adaptor = liteAdaptor();
  RegisterHTMLHandler(adaptor);
  const input = new TeX({
    packages: AllPackages.filter(name => !['noerrors', 'noundefined'].includes(name)),
    formatError: (_jax, error) => { throw new Error(`LaTeX parse error: ${error.message}`); },
  });
  const output = new SVG({ fontCache: 'none' });
  const document = mathjax.document('', { InputJax: input, OutputJax: output });
  const manifest = {};
  const entries = [];
  const rendered = [];

  for (const formula of formulas) {
    if (/^\s*\$/.test(formula.latex)) throw new Error(`Slide ${formula.number}: omit dollar delimiters.`);
    const node = document.convert(formula.latex, { display: true, em: options['font-size'], ex: options['font-size'] / 2,
      containerWidth: options['max-width'] });
    const result = adaptor.outerHTML(node);
    if (/data-mml-node="merror"|<merror\b|data-mjx-error=/i.test(result)) {
      throw new Error(`Slide ${formula.number}: MathJax produced an error node.`);
    }
    const match = result.match(/<svg\b[\s\S]*?<\/svg>/);
    if (!match) throw new Error(`Slide ${formula.number}: missing rendered SVG.`);
    const svg = match[0];
    const box = svg.match(/viewBox="([^"]+)"/);
    if (!box) throw new Error(`Slide ${formula.number}: missing SVG viewBox.`);
    const [vx, vy, vw, vh] = box[1].trim().split(/\s+/).map(Number);
    if (![vx, vy, vw, vh].every(Number.isFinite) || vw <= 0 || vh <= 0) {
      throw new Error(`Slide ${formula.number}: invalid viewBox.`);
    }
    // MathJax TeX glyph coordinates use 1000 units per em. Add transparent gutters.
    const padding = 8;
    const preferred = options['font-size'] / 1000;
    const fit = Math.min(1, (options['max-width'] - 2 * padding) / (vw * preferred),
      (options['max-height'] - 2 * padding) / (vh * preferred));
    const unitScale = preferred * fit;
    const displayWidth = Math.ceil(vw * unitScale + 2 * padding - 1e-9);
    const displayHeight = Math.ceil(vh * unitScale + 2 * padding - 1e-9);
    const paddedViewBox = [vx - padding / unitScale, vy - padding / unitScale,
      displayWidth / unitScale, displayHeight / unitScale].map(v => Number(v.toFixed(5))).join(' ');
    const alt = formula.formula_alt || formula.formula || formula.formula_caption || formula.title || formula.latex;
    const body = svg.replace(/^<svg\b[^>]*>/, '').replace(/<\/svg>$/, '').replace(/currentColor/g, options.color);
    const standalone = `<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="${displayWidth}px" height="${displayHeight}px" viewBox="${paddedViewBox}" role="img" aria-labelledby="formula-title formula-description" color="${options.color}"><title id="formula-title">${xml(formula.title || `Formule ${formula.number}`)}</title><desc id="formula-description">${xml(alt)}</desc>${body}</svg>\n`;
    const png = await sharp(Buffer.from(standalone), { density: 72 * options.scale })
      .resize(displayWidth * options.scale, displayHeight * options.scale)
      .png({ compressionLevel: 9 }).toBuffer();
    const info = await sharp(png).metadata();
    const stats = await sharp(png).stats();
    if (!info.hasAlpha || info.channels !== 4 || stats.channels[3].min !== 0 || stats.channels[3].max === 0) {
      throw new Error(`Slide ${formula.number}: expected a nonempty transparent RGBA image.`);
    }
    if (displayWidth > options['max-width'] || displayHeight > options['max-height']) {
      throw new Error(`Slide ${formula.number}: image exceeds requested bounds.`);
    }
    const base = `slide-${formula.number}`;
    const effectiveEm = options['font-size'] * fit;
    manifest[String(formula.number)] = {
      svg: relative(path.join(outputDir, `${base}.svg`)), png: relative(path.join(outputDir, `${base}.png`)),
      latex: formula.latex, alt, caption: formula.formula_caption || '', symbols: formula.formula_symbols || [],
      width: info.width, height: info.height, display_width: displayWidth, display_height: displayHeight,
      scale: options.scale, color: options.color, effective_em_px: Number(effectiveEm.toFixed(2)),
      sha256_svg: sha256(standalone), sha256_png: sha256(png),
    };
    entries.push({ slide: formula.number, status: 'rendered', latex_error_nodes: 0,
      transparent: true, png_width: info.width, png_height: info.height,
      display_width: displayWidth, display_height: displayHeight,
      effective_em_px: Number(effectiveEm.toFixed(2)),
      warning: effectiveEm < 25 ? 'Small equation: review the LaTeX line breaks before publishing.' : null });
    rendered.push({ base, svg: standalone, png });
    console.log(`Slide ${formula.number}: ${displayWidth} × ${displayHeight} display px; ${info.width} × ${info.height} PNG px; TeX em ${effectiveEm.toFixed(1)} px.`);
  }

  // Do not publish a manifest that points to partially validated formulas.
  await fs.mkdir(outputDir, { recursive: true });
  for (const item of rendered) {
    await fs.writeFile(path.join(outputDir, `${item.base}.svg`), item.svg);
    await fs.writeFile(path.join(outputDir, `${item.base}.png`), item.png);
  }
  const report = { generated_at: new Date().toISOString(), source: relative(sourcePath), source_sha256: sha256(sourceText),
    renderer: { mathjax: actualMathJax, sharp: actualSharp, font: 'MathJax TeX, vector paths', node: process.version },
    options: { max_width: options['max-width'], max_height: options['max-height'], font_size: options['font-size'],
      scale: options.scale, color: options.color }, count: rendered.length,
    validation: 'LaTeX parsed; SVG paths rendered; transparent PNG pixels and dimensions checked.', entries };
  await fs.writeFile(path.join(outputDir, 'manifest.json'), JSON.stringify(manifest, null, 2) + '\n');
  await fs.writeFile(path.join(outputDir, 'render-report.json'), JSON.stringify(report, null, 2) + '\n');
  console.log(`Rendered ${rendered.length} equations. Manifest: ${relative(path.join(outputDir, 'manifest.json'))}`);
}

try {
  const options = parseArgs(process.argv.slice(2));
  if (options) await main(options);
} catch (error) {
  console.error(error.stack || error.message || String(error));
  process.exitCode = 1;
}
