# Schémas pédagogiques originaux

Le générateur contient actuellement quinze dessins vectoriels, dont le comparatif Word2Vec CBOW/Skip-gram. Le nombre produit est calculé depuis les spécifications, sans dépendre du nombre ni de l'ordre des diapositives. Les SVG restent éditables ; les PNG de 2 400 pixels de large servent à une insertion fiable dans le PowerPoint. Le manifeste relie chaque numéro de diapositive à ses fichiers, son titre source (`slide_title`), sa légende courte et sa description accessible.

Les couleurs reprennent le template Cybersup : bleu `#282A59`, orange `#BF2E00` et fonds clairs. Les libellés, formes et symboles portent l'information indépendamment de la couleur. Police demandée : DM Sans, avec Arial/sans-serif en repli. Aucun schéma de publication ni capture de cours tiers n'est reproduit.

## Régénération

Depuis la racine du cours : `python3 scripts/build_diagrams.py`.

Le script construit les SVG avec la bibliothèque standard Python puis rend les PNG avec `rsvg-convert` (librsvg) ou, en repli, `magick` (ImageMagick). Pour produire uniquement les sources vectorielles : `python3 scripts/build_diagrams.py --svg-only`. `--png-width 2400` permet d'expliciter la résolution de sortie. Une largeur inférieure à 1 600 pixels est refusée. Le rendu des polices dépend des polices disponibles sur la machine ; vérifier visuellement les PNG après changement d'environnement.

Les clés de `SPECS` sont des identifiants internes de dessin ; elles ne désignent pas la position actuelle d'une slide. `SLIDE_TITLES` les associe à des titres exacts et stables. Avant toute écriture, le script lit `course/slides.json` et exige exactement une occurrence de chaque titre. Après insertion ou déplacement de diapositives, régénérer : les positions dans le manifeste et les préfixes des fichiers sont recalculés. Lors d'un changement de titre, modifier aussi sa correspondance dans `SLIDE_TITLES`. Un titre absent ou dupliqué interrompt la génération.

Après un rendu complet, tous les SVG sont analysés et les dimensions des PNG vérifiées. Les anciens fichiers SVG/PNG référencés par le précédent manifeste et absents du nouveau sont sauvegardés dans `.build/diagrams-retired/`, puis retirés du seul dossier `assets/diagrams`. Les autres fichiers ne sont pas nettoyés. Le mode `--svg-only` ne retire rien et doit être suivi d'un rendu complet avant l'assemblage du support. Le manifeste produit contient les dessins de ce générateur ; ajouter les éventuelles illustrations externes après sa régénération, avec leur `slide_title` exact. Le validateur du cours refuse une association de titre ou de formule décalée.

## Simplifications explicites

- Word2Vec illustre deux objectifs d'apprentissage sur une fenêtre de taille un : CBOW moyenne les vecteurs du contexte pour prédire le mot central ; Skip-gram prédit séparément les voisins depuis le mot central. Les couches de sortie et l'échantillonnage négatif sont omis. Ce schéma ne décrit ni BERT ni un token de masquage.
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
