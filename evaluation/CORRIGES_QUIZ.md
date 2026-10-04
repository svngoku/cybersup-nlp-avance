# Corrigé du quiz — réservé au formateur

Chaque question vaut 1 point : 0,5 pour l'idée centrale, 0,5 pour la justification, le calcul ou la proposition demandée. Une formulation différente est acceptée si le sens est correct. Le total sur 25 se convertit sur 20 en multipliant par 0,8. Ne pas pénaliser une approximation numérique correctement expliquée.

## Jour 1

1. Le test ressemble au train au niveau du scénario ; la reconnaissance d'une formulation voisine peut remplacer la généralisation attendue. Grouper toutes les paraphrases/variantes du même incident avant le split, puis vérifier les intersections de groupes. Une simple suppression des doublons exacts ne suffit pas.
2. L'IDF réduit le pouvoir discriminant des termes très répandus et donne davantage de poids aux termes rares, selon la formule/lissage utilisés. En classification, apprendre vocabulaire et IDF sur le train ; appliquer ensuite la transformation figée à validation/test. La rareté ne garantit pas qu'un terme soit utile.
3. Produit scalaire = 1 ; normes = `sqrt(2)` et 1 ; cosinus = `1/sqrt(2) ≈ 0,7071`. Avec `(10,10)`, le facteur dix se simplifie. Il s'agit de direction, pas d'une probabilité de même sens.
4. Les IDs sont des indices arbitraires. Les lignes d'embedding apprises correspondent au vocabulaire du tokenizer d'origine. Changer le découpage, les IDs ou les tokens spéciaux sans adapter les embeddings et le modèle rompt ce contrat.
5. Une réponse adaptée à un paiement accepté peut être proposée à un paiement refusé. Construire des paires minimales affirmative/négative, conserver les mêmes candidats, puis observer les voisins et leurs erreurs. La similarité seule ne garantit pas la prise en compte de la négation.

## Jour 2

6. `QKᵀ` : `4 × 5`. Les poids softmax : `4 × 5`, avec normalisation sur les cinq keys pour chaque query. Sortie : `(4 × 5)(5 × 3) = 4 × 3`. Les longueurs de Q et K peuvent différer dans une cross-attention.
7. La troisième position consulte 1, 2 et 3 ; elle ne consulte pas 4. Le masque de padding ignore des positions artificielles ajoutées pour former un batch. Il ne code pas, à lui seul, la contrainte temporelle.
8. Exponentielles : 1 et 3 ; somme : 4 ; poids : 0,25 et 0,75. Sortie : `0,25 × 2 + 0,75 × 10 = 8`. Ce résultat illustre un mélange pondéré, pas une sélection dure.
9. Diviser des logits par une température strictement positive préserve leur ordre, donc l'argmax greedy, hors détails numériques. En sampling, la température modifie les probabilités relatives et donc la distribution des tokens tirés. Cela ne garantit pas qu'un tirage individuel change.
10. Entrée : « le colis arrive » ; cibles : « colis arrive demain », ou équivalent avec tokens spéciaux explicités. Une représentation qui voit déjà le token cible à droite ferait fuiter la réponse dans ce calcul. L'apprentissage causal masque ces positions futures.

## Jour 3

11. Précision = `6/8 = 0,75` ; rappel = `6/10 = 0,60` ; F1 = `2TP/(2TP+FP+FN) = 12/18 ≈ 0,667`. Les dénominateurs décrivent des populations différentes. Accorder le point complet si formule et valeurs sont justes.
12. Les labels des deux sous-tokens suivants deviennent `-100` dans cette stratégie, comme les positions spéciales/padding selon la préparation. Ils restent dans l'entrée et peuvent contribuer aux représentations. Le masque de loss et le masque d'attention sont différents.
13. Suspecter notamment le surapprentissage, mais vérifier aussi données, métrique et stabilité de l'évaluation. Choisir epoch/checkpoint sur validation. Le test ne doit pas servir à cette sélection. Une seule courbe n'identifie pas forcément la cause précise.
14. Non, une nouvelle tête pour la tâche peut être attendue. Vérifier architecture, nombre de labels, correspondance ID/nom, données et couches entraînables. Une tête neuve n'est pas déjà adaptée à la classification visée.
15. Non en correspondance exacte : frontière différente, donc une entité prédite incorrecte et une entité de référence manquée. L'accuracy par token peut être dominée par `O` et sous-représenter les erreurs sur les entités rares ou multi-mots.

## Jour 4

16. `1024 × 8 + 8 × 1024 = 16 384` paramètres. La matrice complète en compte `1 048 576` ; le rapport est 64 et la mise à jour représente 1,5625 % de ce compte. Ce rapport ne mesure ni toute la mémoire ni la vitesse du modèle complet.
17. Dans le parcours, les poids de base sont stockés sous forme quantifiée et restent figés ; les adaptateurs LoRA sont entraînés. Calculs, activations et états d'optimiseur utilisent d'autres représentations. Aucune division universelle par quatre de la mémoire totale n'en découle.
18. Des exemples presque identiques peuvent apparaître de part et d'autre du split, ce qui mesure surtout leur proximité. Grouper par scénario avant le découpage, dédupliquer/auditer, puis vérifier qu'aucun groupe ne traverse train/validation/test.
19. Non. Il y a une observation de meilleure loss/forme, mais un défaut de factualité. Il faut une comparaison avant/après sur les mêmes sources réservées, une grille d'affirmations étayées, couverture et format, et un décompte des erreurs. Ne pas présenter le gain de loss comme un gain de qualité globale.
20. Les mots se recouvrent presque entièrement alors que la négation inverse le fait. Vérifier chaque affirmation par rapport à la source, avec une grille humaine, des cas de négation et des contrôles de dates/nombres. ROUGE ou une similarité ne remplace pas cette vérification.

## Jour 5

21. Utiliser les mêmes demandes et labels ; fixer un prompt décrivant la tâche et la liste des catégories sans exemples de démonstration. Choisir le prompt sur validation, conserver template/décodage, définir le parsing, puis mesurer sur le même test avec la même métrique. Le modèle Instruct reste préentraîné/adapté antérieurement.
22. Non : les retirer améliore artificiellement le résultat et change la population évaluée. Les compter incorrectes selon une règle annoncée ; rapporter le taux de sorties valides et conserver les exemples dans le dénominateur. On peut ajouter une métrique conditionnelle, clairement étiquetée, mais jamais la substituer silencieusement au résultat global.
23. Non avec une telle généralité : petit effectif, variabilité, difficulté des exemples, éventuels groupes communs ou biais de sélection. Examiner les erreurs appariées et évaluer sur davantage de scénarios indépendants, ou répéter selon un protocole défini avant le test. Une différence observée d'un exemple reste une observation locale.
24. Cela démontre qu'un parcours de démonstration donné a produit des sorties dans cet environnement. Il faut notamment vérifier rechargement/reproductibilité, entrées limites, contrôle d'accès, latence/charge, supervision des erreurs et données représentatives selon l'usage. Deux éléments justifiés suffisent ; aucun déploiement réel n'est exigé pour répondre.
25. Conclusion défendable : le pipeline réussit cette tâche sur ce corpus et ce protocole, avec les résultats observés. Conclusion non défendable : il est fiable pour tous les clients ou prêt pour production. Proposer une évaluation indépendante sur des données autorisées représentatives, avec annotation, cas difficiles, coûts d'erreur et analyse par sous-groupes.

## Exploiter les erreurs de quiz

Si les questions 1/13/18/22 échouent, revenir au protocole avant d'optimiser les modèles. Si 6/7/8 échouent, refaire l'attention à une query et deux keys. Si 12/15 échouent, afficher un alignement mot/sous-token/label. Si 16/17 échouent, dessiner la matrice figée et ses deux facteurs, puis séparer le compte de paramètres de la mémoire totale.
