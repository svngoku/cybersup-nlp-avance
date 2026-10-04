# Quiz — 25 questions de raisonnement

**Cinq questions par jour.** Répondre en quelques lignes, avec le calcul demandé lorsqu'il y en a un. Le quiz peut servir de diagnostic collectif ou de contrôle individuel. Pour une note : 1 point par question, puis conversion sur 20. Les réponses ne figurent pas dans le pack étudiant.

## Jour 1 — Représenter le texte

1. Deux demandes sont des paraphrases du même incident. L'une va dans le train et l'autre dans le test. Pourquoi ce découpage peut-il surestimer la qualité ? Proposer une correction.
2. Un mot apparaît dans tous les documents, un autre dans un seul. Que cherche à faire l'IDF avec ces deux mots ? Où apprendre l'IDF dans un exercice de classification train/validation/test ?
3. Calculer le cosinus entre `u = (1, 1)` et `v = (1, 0)`. Le résultat change-t-il si l'on remplace `u` par `(10, 10)` ?
4. Les IDs de deux tokens sont 17 et 18. Sont-ils sémantiquement proches pour cette raison ? Pourquoi ne peut-on pas brancher sans précaution un nouveau tokenizer sur un modèle préentraîné ?
5. « Mon paiement a été accepté » et « Mon paiement n'a pas été accepté » peuvent être proches dans un espace de représentation. Quel risque cela crée-t-il pour une recherche de réponses ? Proposer un test.

## Jour 2 — Attention et génération

6. Pour une attention, Q a la forme `4 × 2`, K la forme `5 × 2` et V la forme `5 × 3`. Quelles sont les formes de QK transposé, des poids après softmax et de la sortie ?
7. Dans une séquence de quatre tokens, quelles positions peut consulter la troisième position sous un masque causal ? Quelle différence avec un masque de padding ?
8. Deux scores d'attention valent `0` et `ln(3)`. Calculer leurs poids softmax, puis la sortie si les valeurs scalaires sont `2` et `10`.
9. Avec un décodage strictement greedy et une température positive, augmenter la température doit-il changer le token choisi ? Pourquoi la réponse diffère-t-elle pour l'échantillonnage ?
10. Pour la séquence « le colis arrive demain », écrire le décalage entrée/cible utilisé pour apprendre la prédiction du token suivant. Pourquoi une représentation bidirectionnelle du même texte pose-t-elle problème pour cet objectif ?

## Jour 3 — Classification et NER

11. Une classe compte TP = 6, FP = 2 et FN = 4. Calculer précision, rappel et F1.
12. Un mot annoté est découpé en trois sous-tokens. Dans une stratégie supervisant seulement le premier sous-token, que deviennent les deux autres labels ? Cela signifie-t-il que les sous-tokens sont supprimés de l'entrée ?
13. La loss d'entraînement baisse mais la métrique de validation se dégrade. Que peut-on suspecter ? Quel jeu ne faut-il pas utiliser pour choisir le nombre d'epochs ?
14. Le chargement d'un encodeur en classifieur signale une tête nouvellement initialisée. Est-ce forcément une erreur ? Que faut-il vérifier avant d'entraîner ?
15. La référence NER contient l'entité LOC « Paris Gare de Lyon ». Le modèle prédit uniquement LOC « Paris ». En évaluation stricte par entité, est-ce un vrai positif ? Quel piège pose l'accuracy par token ?

## Jour 4 — SFT et LoRA

16. Une matrice de poids a la taille `1024 × 1024`. Une mise à jour LoRA de rang 8 utilise deux matrices. Combien de paramètres sont ajoutés, hors biais ? Comparer avec la matrice complète.
17. Dans le parcours QLoRA, qu'est-ce qui est quantifié et qu'est-ce qui est entraîné ? Peut-on conclure que toute la mémoire GPU est divisée par quatre ?
18. Un corpus SFT contient plusieurs reformulations du même scénario, avec la même réponse cible. Pourquoi les répartir aléatoirement ligne par ligne peut-il fausser l'évaluation ?
19. Après SFT, la loss baisse et les réponses sont mieux formatées, mais une date est inventée dans plusieurs résumés. Peut-on conclure que le système résume mieux ? Quelles preuves manquent ?
20. Une source dit « aucun remboursement confirmé » ; le résumé dit « remboursement confirmé ». Pourquoi une métrique de recouvrement lexical peut-elle manquer la gravité de cette erreur ? Quelle vérification complémentaire proposer ?

## Jour 5 — Comparer et présenter

21. Comment définir une baseline zero-shot générative comparable au classifieur de demandes ? Préciser entrées, labels, prompt et évaluation.
22. Le LLM produit une catégorie inconnue sur trois demandes test. Peut-on retirer ces demandes du calcul du score ? Quelle règle publier ?
23. Deux modèles obtiennent 8/10 et 9/10 bonnes réponses. Peut-on annoncer que le second est globalement meilleur ? Donner deux raisons de prudence et une expérience supplémentaire utile.
24. Une interface Gradio fonctionne dans un notebook. Qu'est-ce que cela démontre ? Citer deux éléments supplémentaires nécessaires avant de parler d'un service exploitable.
25. Un modèle obtient un excellent score sur les textes fictifs du TP. Quelle conclusion est défendable, quelle conclusion ne l'est pas, et quelle prochaine validation proposer ?
