# Rendu des formules du cours

Ce runtime Node est distinct de celui du générateur de slides. Il ne modifie pas les dépendances intégrées à Codex ni le lien `.build/node_modules`.

Depuis la racine du cours :

```sh
npm --prefix tools-visuals install
node scripts/build_formulas.mjs
```

Après la première installation, conserver `package-lock.json`. Pour reconstruire les mêmes dépendances :

```sh
npm --prefix tools-visuals ci
node scripts/build_formulas.mjs
```

Node 18.17+ est requis. MathJax 3.2.2 convertit le LaTeX en chemins SVG indépendants des polices installées. Sharp 0.34.3 produit les PNG transparents à trois fois la résolution d’affichage. Les versions sont fixées pour éviter qu’un changement de moteur modifie silencieusement les équations.

## Entrée et sortie

Le script lit `course/slides.json`, liste de diapositives ou objet possédant une liste `slides`.

- `formula_latex` : chaîne LaTeX, sans délimiteurs dollar, obligatoire pour rendre une équation.
- `formula` : description textuelle de secours utilisée pour l’accessibilité.
- `formula_alt` : description accessible facultative, prioritaire sur `formula`.
- `formula_caption` et `formula_symbols` : métadonnées pédagogiques conservées dans le manifest.

Chaque formule reçoit son propre SVG et PNG : `assets/formulas/slide-N.svg` et `slide-N.png`, avec N égal au numéro de diapositive, à partir de 1. Le fichier `manifest.json` est indexé par N. Les chemins y sont relatifs à la racine du cours. `width` et `height` donnent la taille du PNG ; `display_width` et `display_height` donnent la taille de référence pour les slides. Les ratios sont identiques.

`render-report.json` enregistre les contrôles de syntaxe MathJax, les dimensions, la transparence et les éventuels avertissements de taille. LaTeX et description restent disponibles même si l’équation est insérée comme image dans PowerPoint.

```sh
node scripts/build_formulas.mjs --help
node scripts/build_formulas.mjs --max-width 1115 --max-height 110 --font-size 44 --scale 3 --color '#282A59'
```

Le script ajuste l’échelle de façon uniforme, sans déformer ni couper l’équation. Pour une longue équation, écrire explicitement deux lignes avec l’environnement `aligned` dans le JSON ; le renderer ne devine pas une coupure mathématique. Les fichiers sont validés avant publication du nouveau manifest. Une erreur de syntaxe provoque un code de sortie non nul.

Inclure dans le pack formateur ce dossier **sans node_modules**, le fichier de verrouillage, le générateur et `assets/formulas/`. Aucune connexion réseau n’est nécessaire pour le rendu une fois les dépendances installées.

Références : [MathJax 3.2 — sortie SVG et cache de polices](https://docs.mathjax.org/en/v3.2/options/output/svg.html), [Sharp — entrée SVG](https://sharp.pixelplumbing.com/api-constructor/).
