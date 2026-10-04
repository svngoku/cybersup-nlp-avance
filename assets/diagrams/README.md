# Schémas pédagogiques originaux

Quatorze dessins vectoriels accompagnent les notions du cours. Les SVG restent éditables ; les PNG de 2 400 pixels de large servent à une insertion fiable dans le PowerPoint. Le manifeste relie chaque numéro de diapositive à ses fichiers, sa légende courte et sa description accessible.

Les couleurs reprennent le template Cybersup : bleu `#282A59`, orange `#BF2E00` et fonds clairs. Les libellés, formes et symboles portent l'information indépendamment de la couleur. Police demandée : DM Sans, avec Arial/sans-serif en repli. Aucun schéma de publication ni capture de cours tiers n'est reproduit.

## Régénération

Depuis la racine du cours : `python3 scripts/build_diagrams.py`.

Le script construit les SVG avec la bibliothèque standard Python puis rend les PNG avec `rsvg-convert` (librsvg) ou, en repli, `magick` (ImageMagick). Pour produire uniquement les sources vectorielles : `python3 scripts/build_diagrams.py --svg-only`. `--png-width 2400` permet d'expliciter la résolution de sortie. Une largeur inférieure à 1 600 pixels est refusée. Le rendu des polices dépend des polices disponibles sur la machine ; vérifier visuellement les PNG après changement d'environnement.

## Simplifications explicites

- Les coordonnées des embeddings sont illustratives, sans projection d'un modèle ni résultat expérimental.
- Le multi-head montre deux têtes ; leurs rôles linguistiques ne sont pas imposés.
- Le bloc Transformer représente une organisation **Post-LN de type BERT**, pas une organisation universelle.
- Le comparatif BERT/GPT/T5 présente les relations d'accès au contexte ; les détails de chaque bloc sont volontairement omis.
- L'alignement NER illustre la convention « premier sous-token supervisé » ; d'autres conventions existent.
- Les marqueurs de chat illustrent le format Qwen. Les IDs affichés dans les schémas sont conceptuels.
- Les masques d'attention et de loss ont des fonctions distinctes ; les marqueurs du contexte sont ici exclus de la supervision.
- Le décalage causal montre les cibles à la position suivante. Il n'ordonne pas un décalage manuel supplémentaire lorsque le modèle le fait déjà.
- QLoRA sépare stockage NF4, précision de calcul choisie et adaptateurs entraînables. Les opérations auxiliaires peuvent utiliser une autre précision.
- Le résumé est un exemple construit dont chaque affirmation doit être reliée à sa source.

Les concepts se rattachent aux références déjà citées dans `ressources/RESSOURCES_VERIFIEES.md` et aux explications des notes du présentateur. Les images sont des constructions originales du cours, pas des résultats mesurés.
