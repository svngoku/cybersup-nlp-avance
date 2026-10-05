# Glossaire — NLP Avancé

187 entrées. Chaque définition renvoie au cours et au lexique projetable. Les sigles sont développés, les exemples sont illustratifs.

## Accès rapide

- Jour 1 : lexique du PowerPoint à partir de la diapositive 124.
- Jour 2 : lexique du PowerPoint à partir de la diapositive 141.
- Jour 3 : lexique du PowerPoint à partir de la diapositive 152.
- Jour 4 : lexique du PowerPoint à partir de la diapositive 161.
- Jour 5 : lexique du PowerPoint à partir de la diapositive 168.

## Jour 1

### NLP / TAL

Le traitement automatique du langage naturel (TAL), ou Natural Language Processing (NLP), regroupe les méthodes qui transforment des textes en sorties utiles et vérifiables.

**Exemple.** À partir d’un ticket, classer l’intention, extraire une référence ou retrouver une FAQ sont trois tâches NLP différentes.

**À distinguer.** NLP ne signifie pas seulement chatbot ou génération de texte.

Cours : diapositive 5 · Lexique : diapositive 124.

### langage naturel

Langage utilisé par les personnes pour communiquer, à l’écrit ou à l’oral.

**Exemple.** Une demande client contient des sous-entendus et des ambiguïtés.

**À distinguer.** Un texte grammatical peut rester ambigu ou factuellement faux.

Cours : diapositive 5 · Lexique : diapositive 124.

### LLM

Large Language Model : modèle de langage doté de nombreux paramètres, entraîné à modéliser des séquences de tokens.

**Exemple.** Le petit Qwen du TP permet d’observer la génération sous budget.

**À distinguer.** La taille seule ne garantit ni les faits ni le respect des consignes.

Cours : diapositive 5 · Lexique : diapositive 124.

### document

Une unité de texte choisie pour une tâche, par exemple un ticket ou une fiche FAQ.

**Exemple.** La fiche « réinitialiser mon mot de passe » est un document de l’index.

**À distinguer.** Un document n’est pas nécessairement un fichier entier.

Cours : diapositive 6 · Lexique : diapositive 124.

### corpus

Un ensemble de documents rassemblés pour une analyse ou un apprentissage.

**Exemple.** Les 12 fiches FAQ et les requêtes annotées forment des collections distinctes du corpus de l’exercice.

**À distinguer.** Un corpus n’est pas automatiquement représentatif du domaine réel.

Cours : diapositive 6 · Lexique : diapositive 125.

### token

Une unité produite par un tokenizer : mot, morceau de mot, signe ou unité spéciale.

**Exemple.** « remboursement » peut être un token ou plusieurs sous-tokens selon le tokenizer.

**À distinguer.** Token ne veut pas toujours dire mot entier.

Cours : diapositive 6 · Lexique : diapositive 125.

### type lexical

Une forme distincte comptée dans un texte ou un corpus, quelle que soit sa fréquence.

**Exemple.** Dans « colis, colis, retard », les types sont colis et retard ; il y en a deux.

**À distinguer.** Un type n’est pas une occurrence : colis apparaît deux fois mais reste un seul type.

Cours : diapositive 6 · Lexique : diapositive 125.

### vocabulaire

L’inventaire des tokens qu’un tokenizer sait encoder, souvent associé à des identifiants entiers.

**Exemple.** Une entrée du vocabulaire peut associer le token « colis » à l’identifiant 1234.

**À distinguer.** Un identifiant n’est ni une mesure de sens ni un classement de proximité.

Cours : diapositive 6 · Lexique : diapositive 125.

### embedding

Une représentation apprise sous forme de vecteur dense, pour un token ou une séquence selon le modèle.

**Exemple.** Un encodeur peut représenter deux formulations proches par des vecteurs voisins.

**À distinguer.** Un embedding n’est pas une définition lisible ni une garantie de compréhension.

Cours : diapositive 6 · Lexique : diapositive 126.

### recherche d’information

Tâche qui classe des documents selon leur pertinence pour une requête.

**Exemple.** Pour « colis en retard », la fiche qui explique le suivi doit remonter avant une fiche de facturation.

**À distinguer.** Le meilleur score dépend de la représentation et de la pertinence définie pour l’exercice.

Cours : diapositive 7 · Lexique : diapositive 126.

### sac de mots

Représentation qui compte les termes d’un document sans conserver leur ordre.

**Exemple.** « colis facture colis » devient colis=2, facture=1.

**À distinguer.** Deux textes avec les mêmes comptes peuvent exprimer des intentions opposées.

Cours : diapositive 8 · Lexique : diapositive 126.

### TF-IDF

Pondération qui combine la fréquence d’un terme dans un document (TF) et sa rareté parmi les documents (IDF). TF-IDF signifie term frequency–inverse document frequency.

**Exemple.** « bloqué » présent dans une seule fiche distingue davantage que « compte » présent partout.

**À distinguer.** Un terme rare peut être une faute ou du bruit ; rareté ne signifie pas pertinence.

Cours : diapositive 8 · Lexique : diapositive 126.

### IDF

Inverse document frequency : facteur qui réduit le poids des termes présents dans beaucoup de documents.

**Exemple.** Avec N=4 et df=1, log(N/df)=log(4) ; si df=4, le poids non lissé vaut zéro.

**À distinguer.** Les bibliothèques ajoutent parfois un lissage ou une autre normalisation : préciser la variante avant de comparer des valeurs.

Cours : diapositive 8 · Lexique : diapositive 127.

### lexical / sémantique

Lexical concerne les formes des mots ; sémantique concerne leur sens dans un usage et un contexte.

**Exemple.** « colis » et « paquet » diffèrent lexicalement mais peuvent désigner le même objet.

**À distinguer.** Un score dit sémantique reste une mesure produite par un modèle, pas une preuve de compréhension.

Cours : diapositive 8 · Lexique : diapositive 127.

### Word2Vec

Famille de méthodes qui apprend des vecteurs de mots en prédisant des mots à partir de leur contexte, ou l’inverse.

**Exemple.** Dans « le colis arrive », une fenêtre autour de colis fournit des exemples d’apprentissage.

**À distinguer.** Word2Vec n’est ni le premier embedding ni un modèle complet de compréhension de phrases.

Cours : diapositive 9 · Lexique : diapositive 127.

### CBOW

Continuous Bag of Words : agrège les mots du contexte local pour prédire le mot central.

**Exemple.** Avec « le _ arrive », CBOW prédit « colis » à partir de le et arrive.

**À distinguer.** Le contexte est agrégé ; cette forme de base ne préserve pas directement son ordre.

Cours : diapositive 9 · Lexique : diapositive 127.

### Skip-gram

Variante de Word2Vec qui part du mot central pour prédire les mots voisins de son contexte.

**Exemple.** À partir de « colis », prédire « le » et « arrive » dans une fenêtre donnée.

**À distinguer.** Les mots prédits sont des cibles d’apprentissage, pas des ajouts automatiques au document.

Cours : diapositive 9 · Lexique : diapositive 128.

### auto-supervision

Apprentissage où une cible est construite à partir des données elles-mêmes, sans annotation humaine pour chaque exemple.

**Exemple.** Le texte fournit le mot central à prédire pour CBOW.

**À distinguer.** L’absence d’annotation manuelle ne rend pas les données ou la tâche sans biais.

Cours : diapositive 9 · Lexique : diapositive 128.

### GloVe

Global Vectors : méthode qui apprend des vecteurs à partir de statistiques globales de cooccurrence des mots.

**Exemple.** Elle exploite combien de fois colis et retard apparaissent dans des voisinages du corpus.

**À distinguer.** Cooccurrence indique une association dans les données, pas une synonymie.

Cours : diapositive 10 · Lexique : diapositive 128.

### fastText

Méthode qui représente un mot à partir de son vecteur et de vecteurs de n-grammes de caractères, afin de partager de l’information entre formes proches.

**Exemple.** « remboursement » et « remboursements » peuvent partager des fragments appris.

**À distinguer.** Les fragments ne sont pas nécessairement des morphèmes et ne garantissent pas la correction d’une faute.

Cours : diapositive 10 · Lexique : diapositive 128.

### n-gramme de caractères

Séquence de n caractères consécutifs extraite d’une forme écrite.

**Exemple.** Pour « chat », les trigrammes internes possibles incluent cha et hat.

**À distinguer.** Un n-gramme de caractères fastText n’est pas un sous-token BPE.

Cours : diapositive 10 · Lexique : diapositive 129.

### représentation statique

Vecteur fixe associé à une entrée lexicale dans un modèle donné, quel que soit son contexte d’emploi.

**Exemple.** Un vecteur Word2Vec pour « banque » reste le même dans « banque de données » et « banque prêteuse ».

**À distinguer.** La proximité avec un mot ne garantit pas que les deux soient interchangeables.

Cours : diapositive 11 · Lexique : diapositive 129.

### représentation contextuelle

Vecteur interne calculé à partir d’une occurrence et des tokens autour d’elle, selon l’architecture et le contexte autorisé.

**Exemple.** « banque de données » et « banque refuse le prêt » peuvent produire des représentations différentes de banque.

**À distinguer.** Le contexte rend la représentation variable, mais ne garantit ni raisonnement juste ni fidélité factuelle.

Cours : diapositive 11 · Lexique : diapositive 129.

### BERT

Bidirectional Encoder Representations from Transformers : famille de modèles à encodeur Transformer entraînés notamment avec un objectif de token masqué.

**Exemple.** DistilBERT multilingue reprend une partie de l’approche BERT dans une version distillée.

**À distinguer.** BERT désigne une famille et une architecture d’encodeur, pas un chatbot génératif par défaut.

Cours : diapositive 11 · Lexique : diapositive 129.

### GPT

Generative Pre-trained Transformer : famille de modèles Transformer à décodeur causal qui prédisent la suite à partir d’un préfixe.

**Exemple.** Un modèle de type GPT complète « Le colis est arrivé… » token après token.

**À distinguer.** Qwen est une autre famille de checkpoints à décodeur causal, pas un modèle GPT d’OpenAI.

Cours : diapositive 11 · Lexique : diapositive 130.

### distillation

Entraînement d’un modèle élève pour reproduire certaines sorties ou représentations d’un modèle enseignant.

**Exemple.** DistilBERT est une famille de modèles obtenus par distillation.

**À distinguer.** Le modèle élève ne conserve pas nécessairement toutes les capacités de l’enseignant.

Cours : diapositive 11 · Lexique : diapositive 130.

### NER

Named Entity Recognition, ou reconnaissance d’entités nommées : repérer dans un texte les segments correspondant à des catégories définies.

**Exemple.** Dans « Commande AB123 à Lyon », étiqueter AB123 comme référence et Lyon comme lieu.

**À distinguer.** Une entité détectée n’est pas nécessairement correcte ; les frontières et la catégorie s’évaluent séparément.

Cours : diapositive 14 · Lexique : diapositive 130.

### classification

Affectation d’une ou plusieurs catégories à une entrée selon une règle de tâche.

**Exemple.** Attribuer « facturation » à un ticket de double débit.

**À distinguer.** La classe attendue dépend du guide d’annotation, surtout pour les demandes multiples.

Cours : diapositive 14 · Lexique : diapositive 130.

### jeu de données

Exemples organisés avec les champs nécessaires à une tâche, parfois accompagnés de labels ou de références pertinentes.

**Exemple.** Une requête FAQ avec l’identifiant de sa fiche attendue constitue un exemple de recherche annoté.

**À distinguer.** Les données fictives servent à expliquer la méthode, pas à prouver une performance métier.

Cours : diapositive 15 · Lexique : diapositive 131.

### pertinence

Règle qui indique quels résultats comptent comme corrects pour une requête donnée.

**Exemple.** Une fiche indiquant comment suivre un colis peut être pertinente pour « où est ma commande ? ».

**À distinguer.** Une métrique de recherche n’a de sens qu’avec une pertinence définie avant l’évaluation.

Cours : diapositive 15 · Lexique : diapositive 131.

### annotation / label

L’annotation attribue une information de référence à un exemple ; un label est l’étiquette utilisée comme cible.

**Exemple.** Annoter un message « facturation » ou une ville comme lieu.

**À distinguer.** Un désaccord entre annotateurs peut signaler une règle ambiguë plutôt qu’une faute individuelle.

Cours : diapositive 15 · Lexique : diapositive 131.

### split

Partition d’un jeu de données en sous-ensembles réservés à des rôles différents, souvent train, validation et test.

**Exemple.** Des paraphrases d’un même scénario sont gardées ensemble dans une seule partition.

**À distinguer.** Un découpage aléatoire par ligne peut séparer des exemples quasi identiques.

Cours : diapositive 16 · Lexique : diapositive 131.

### fuite de données

Accès, pendant l’apprentissage ou le choix du système, à une information qui ne serait pas disponible dans l’usage ou l’évaluation finale.

**Exemple.** Une paraphrase d’un ticket de test présente dans train peut gonfler artificiellement le score.

**À distinguer.** Une excellente mesure ne démontre pas la généralisation si les partitions partagent leurs scénarios.

Cours : diapositive 16 · Lexique : diapositive 132.

### train / validation / test

Train sert à ajuster les paramètres ; validation à choisir les réglages ; test à mesurer le système retenu une fois.

**Exemple.** Choisir k sur validation, puis rapporter la mesure finale sur les requêtes test gardées à part.

**À distinguer.** Réutiliser le test pour régler le système transforme le test en validation.

Cours : diapositive 16 · Lexique : diapositive 132.

### paraphrase

Reformulation qui conserve le sens pertinent pour la tâche.

**Exemple.** « Où est mon colis ? » et « Je voudrais suivre ma commande ».

**À distinguer.** Une négation ou une date modifiée peut changer le sens et invalider la paraphrase.

Cours : diapositive 16 · Lexique : diapositive 132.

### vecteur creux

Vecteur dont la plupart des coordonnées sont nulles, souvent obtenu en comptant les termes d’un grand vocabulaire.

**Exemple.** Un document de trois mots n’active que quelques colonnes d’un vocabulaire de milliers de termes.

**À distinguer.** Creux décrit le nombre de valeurs nulles, pas la qualité ou l’importance sémantique.

Cours : diapositive 17 · Lexique : diapositive 132.

### n-gramme de tokens

Suite de n tokens consécutifs utilisée comme unité de représentation ou de comparaison.

**Exemple.** « colis reçu » est un bigramme si les tokens sont les mots.

**À distinguer.** Les frontières dépendent du tokenizer ; ne pas confondre avec les n-grammes de caractères.

Cours : diapositive 17 · Lexique : diapositive 133.

### TF

Term frequency : fréquence ou présence d’un terme à l’intérieur d’un document, selon la variante choisie.

**Exemple.** Dans le document « colis colis », le compte brut de colis vaut 2.

**À distinguer.** Le compte brut, la fréquence normalisée et la présence binaire donnent des valeurs différentes.

Cours : diapositive 18 · Lexique : diapositive 133.

### df

Document frequency : nombre de documents du corpus qui contiennent le terme au moins une fois.

**Exemple.** Si « bloqué » apparaît dans une seule des quatre fiches, df=1.

**À distinguer.** df compte les documents contenant le terme, pas toutes ses occurrences.

Cours : diapositive 18 · Lexique : diapositive 133.

### N

Nombre total de documents de la collection utilisée pour calculer IDF.

**Exemple.** Pour quatre fiches indexées, N=4.

**À distinguer.** N désigne ici les documents de l’index, pas les requêtes de validation.

Cours : diapositive 18 · Lexique : diapositive 133.

### baseline

Système de référence simple et reproductible, utilisé pour juger si une méthode plus complexe apporte un gain.

**Exemple.** Comparer un embedding de phrase à une recherche TF-IDF sur les mêmes requêtes et fiches.

**À distinguer.** Une baseline faible ou mal réglée rend la comparaison trompeuse.

Cours : diapositive 19 · Lexique : diapositive 134.

### Recall@k

Rappel à k : fraction des documents pertinents retrouvés parmi les k premiers résultats, calculée par requête puis moyennée.

**Exemple.** Si 6 requêtes sur 8 trouvent leur fiche dans les trois premiers résultats, Recall@3=6/8=0,75.

**À distinguer.** Avec plusieurs résultats pertinents attendus, le rappel classique à k compte les éléments pertinents retrouvés, pas seulement si un élément apparaît.

Cours : diapositive 19 · Lexique : diapositive 134.

### MRR

Mean Reciprocal Rank : moyenne, sur les requêtes, de l’inverse du rang du premier résultat pertinent ; une absence de résultat pertinent reçoit zéro.

**Exemple.** Premiers rangs pertinents 1, 2 et absent donnent MRR=(1+1/2+0)/3=0,5.

**À distinguer.** MRR ignore les autres résultats pertinents après le premier.

Cours : diapositive 19 · Lexique : diapositive 134.

### accuracy

Exactitude globale : proportion de prédictions exactement correctes parmi toutes les observations évaluées.

**Exemple.** 17 prédictions correctes sur 20 donnent 85 %.

**À distinguer.** Un score global peut masquer une classe rare mal reconnue.

Cours : diapositive 20 · Lexique : diapositive 134.

### matrice de confusion

Table qui croise classes attendues et prédites pour montrer les bonnes réponses et les confusions.

**Exemple.** Deux demandes livraison prédites facturation apparaissent hors diagonale.

**À distinguer.** Lire les axes et la convention de normalisation avant d’interpréter les cellules.

Cours : diapositive 20 · Lexique : diapositive 135.

### tokenizer

Composant qui découpe le texte selon un vocabulaire et convertit les unités en identifiants pour un modèle donné.

**Exemple.** Un tokenizer peut encoder un emoji comme plusieurs unités plutôt qu’un seul token.

**À distinguer.** Le découpage exact dépend du tokenizer ; les sous-mots ne sont pas des morphèmes garantis.

Cours : diapositive 21 · Lexique : diapositive 135.

### BPE

Byte Pair Encoding : méthode qui construit un vocabulaire en fusionnant progressivement les paires d’unités les plus fréquentes.

**Exemple.** Une fusion b+a → ba permet ensuite de compter de nouvelles paires avec ba.

**À distinguer.** Il faut recompter après chaque fusion ; le BPE réel peut ajouter des marqueurs et traiter les octets autrement.

Cours : diapositive 21 · Lexique : diapositive 135.

### WordPiece

Algorithme de sous-mots qui choisit des unités selon un vocabulaire appris et un critère de score de fusion, utilisé notamment dans BERT.

**Exemple.** Un mot rare peut être encodé comme une suite de morceaux connus.

**À distinguer.** WordPiece n’est pas identique au BPE même si les deux découpent en sous-mots.

Cours : diapositive 21 · Lexique : diapositive 135.

### tokenisation unigram

Méthode qui apprend un vocabulaire de sous-mots puis choisit un découpage de forte probabilité, plutôt que de construire uniquement une suite de fusions BPE.

**Exemple.** Un même mot peut avoir plusieurs segmentations candidates et le tokenizer retient une segmentation favorisée par son modèle.

**À distinguer.** Unigram ici désigne une méthode de tokenisation, pas un modèle de langue à un seul token de contexte.

Cours : diapositive 21 · Lexique : diapositive 136.

### UTF-8

Encodage de caractères Unicode en unités d’octets de longueur variable.

**Exemple.** Un caractère accentué peut occuper plusieurs octets en UTF-8.

**À distinguer.** Un octet n’est pas forcément un caractère, et un token n’est pas forcément un octet.

Cours : diapositive 21 · Lexique : diapositive 136.

### troncature

Suppression d’une partie des tokens pour respecter une longueur maximale d’entrée.

**Exemple.** Limiter une demande à 128 tokens peut retirer la référence située à la fin.

**À distinguer.** La troncature perd de l’information ; vérifier quelle partie du texte est conservée.

Cours : diapositive 21 · Lexique : diapositive 136.

### Unicode

Norme qui attribue des points de code aux caractères de nombreux systèmes d’écriture et symboles.

**Exemple.** é peut être stocké comme caractère précomposé ou comme e suivi d’un accent combinant.

**À distinguer.** Deux chaînes visuellement identiques peuvent avoir des suites de points de code différentes.

Cours : diapositive 22 · Lexique : diapositive 136.

### normalisation Unicode

Transformation définie qui rend certaines représentations Unicode équivalentes sous une forme canonique ou de compatibilité.

**Exemple.** NFC peut composer e et un accent combinant en une forme précomposée.

**À distinguer.** Normaliser ne signifie pas supprimer tous les accents ; ne pas confondre NFC et NFKC.

Cours : diapositive 22 · Lexique : diapositive 137.

### lemmatisation

Réduction d’une forme fléchie à son lemme, souvent une forme de dictionnaire, à l’aide d’analyses linguistiques.

**Exemple.** « payées » peut être ramené à « payer » selon l’outil et le contexte.

**À distinguer.** Une lemmatisation erronée peut supprimer une distinction utile ; les Transformers attendent souvent le texte brut.

Cours : diapositive 22 · Lexique : diapositive 137.

### racinisation

Réduction heuristique d’un mot à une racine approximative en retirant des suffixes, sans garantir un mot de dictionnaire.

**Exemple.** Un algorithme peut ramener plusieurs formes de remboursement à une même chaîne tronquée.

**À distinguer.** Une racine tronquée n’est pas un lemme et peut fusionner des mots différents.

Cours : diapositive 22 · Lexique : diapositive 137.

### fusion BPE

Étape d’apprentissage qui remplace une paire adjacente fréquente par une nouvelle unité, puis recalcule les fréquences.

**Exemple.** Après b+a → ba, « bas » devient ba+s avant la prochaine fusion.

**À distinguer.** Apprendre les fusions du vocabulaire et appliquer ces fusions à un texte sont deux étapes distinctes.

Cours : diapositive 23 · Lexique : diapositive 137.

### tenseur

Tableau numérique à une ou plusieurs dimensions manipulé par le modèle.

**Exemple.** input_ids pour trois phrases complétées à longueur cinq forme un tableau de taille 3×5.

**À distinguer.** La forme d’un tenseur indique ses dimensions, pas à elle seule la signification de chaque axe.

Cours : diapositive 24 · Lexique : diapositive 138.

### batch

Petit groupe d’exemples traités ensemble dans une même opération du modèle.

**Exemple.** Trois phrases peuvent constituer un batch de taille 3.

**À distinguer.** Les phrases d’un batch doivent être mises en forme compatible, souvent par padding et masque.

Cours : diapositive 24 · Lexique : diapositive 138.

### input_ids

Suite d’identifiants entiers qui représente les tokens après tokenisation.

**Exemple.** [101, 1234, 102] peut coder un début, un token et une fin selon le tokenizer.

**À distinguer.** Les nombres sont des indices arbitraires du vocabulaire, pas des vecteurs sémantiques.

Cours : diapositive 24 · Lexique : diapositive 138.

### attention_mask

Masque qui distingue les positions réelles des positions de padding dans une entrée batched.

**Exemple.** [1,1,1,0] indique trois positions conservées et une position de padding.

**À distinguer.** Ce masque de padding n’est pas le masque causal qui interdit l’accès au futur.

Cours : diapositive 24 · Lexique : diapositive 138.

### padding

Tokens ajoutés pour donner aux séquences d’un batch une longueur commune.

**Exemple.** Une phrase de trois tokens reçoit une position de remplissage pour rejoindre une séquence de quatre.

**À distinguer.** Le padding n’est pas du texte observé et doit être masqué selon l’usage.

Cours : diapositive 24 · Lexique : diapositive 139.

### représentation dense

Vecteur où la plupart des coordonnées sont non nulles, appris ou calculé pour résumer des caractéristiques.

**Exemple.** Un embedding de phrase peut relier « colis en retard » à « ma livraison n’arrive pas ».

**À distinguer.** Une proximité dense peut suivre le thème sans préserver une négation ou un détail critique.

Cours : diapositive 25 · Lexique : diapositive 139.

### embedding de phrase

Vecteur unique calculé pour représenter une séquence entière, avec une méthode propre au modèle.

**Exemple.** Encoder une requête et chaque FAQ permet de comparer leurs vecteurs.

**À distinguer.** Le résultat dépend de l’objectif d’entraînement et de la méthode d’agrégation ; un vecteur de token n’est pas automatiquement un embedding de phrase.

Cours : diapositive 25 · Lexique : diapositive 139.

### similarité cosinus

Produit scalaire de deux vecteurs normalisés par leurs longueurs ; elle compare leur direction.

**Exemple.** (1,0) et (2,0) ont un cosinus de 1 car ils pointent dans la même direction.

**À distinguer.** Un score élevé ne prouve pas que les textes ont la même intention, notamment en présence de négation.

Cours : diapositive 26 · Lexique : diapositive 139.

### produit scalaire

Somme des produits des coordonnées correspondantes de deux vecteurs de même dimension.

**Exemple.** (1, 2) · (3, 4) = 1×3 + 2×4 = 11.

**À distinguer.** Le produit scalaire dépend de la norme des vecteurs, contrairement au cosinus normalisé.

Cours : diapositive 26 · Lexique : diapositive 140.

### norme L2

Longueur d’un vecteur, calculée par la racine carrée de la somme des carrés de ses coordonnées.

**Exemple.** La norme L2 de (3, 4) vaut √(9+16) = 5.

**À distinguer.** Le cosinus avec un vecteur nul n’est pas défini ; annoncer la convention logicielle.

Cours : diapositive 26 · Lexique : diapositive 140.

### Recall@k et hit rate

Avec une seule FAQ pertinente par requête, Recall@k est égal au hit rate : la proportion de requêtes dont la FAQ attendue figure dans les k premiers résultats.

**Exemple.** Sur 8 requêtes, si la FAQ attendue figure dans les trois premiers pour 6, Recall@3 et hit rate@3 valent 0,75.

**À distinguer.** Avec plusieurs éléments pertinents par requête, le rappel classique mesure la fraction de tous ces éléments retrouvés parmi les k premiers ; ce n’est pas simplement un indicateur oui/non.

Cours : diapositive 28 · Lexique : diapositive 140.

### protocole de comparaison

Conditions fixées pour comparer équitablement plusieurs représentations : mêmes requêtes, corpus, pertinence et mesure.

**Exemple.** Comparer TF-IDF et embeddings sur les huit mêmes requêtes annotées.

**À distinguer.** Changer les requêtes ou la définition de pertinence entre systèmes invalide l’interprétation du gain.

Cours : diapositive 28 · Lexique : diapositive 140.


## Jour 2

### prédiction du prochain token

Objectif qui apprend à attribuer une distribution aux tokens pouvant suivre un préfixe.

**Exemple.** Après « Le colis », les continuations possibles peuvent inclure « arrive » ou « manque » selon le contexte.

**À distinguer.** Le texte d’entraînement fournit des cibles, mais les continuations ne sont pas toutes également vraies ou utiles.

Cours : diapositive 37 · Lexique : diapositive 141.

### décalage entrée-cible

Construction où les tokens précédents servent d’entrée et le token suivant de cible à chaque position.

**Exemple.** Entrée « Le colis » → cible « arrive ».

**À distinguer.** Le modèle ne doit pas voir la cible future au moment de calculer la prédiction.

Cours : diapositive 37 · Lexique : diapositive 141.

### RNN

Recurrent Neural Network, ou réseau neuronal récurrent : traite une séquence en propageant un état d’une position à la suivante.

**Exemple.** En lisant « le colis arrive », l’état après colis est transmis au traitement d’arrive.

**À distinguer.** Les RNN ne sont pas tous incapables de retenir les longues dépendances, mais l’information suit un chemin séquentiel.

Cours : diapositive 38 · Lexique : diapositive 141.

### attention

Calcul qui compare une représentation à plusieurs positions, puis combine leurs informations avec des poids calculés à partir de projections apprises.

**Exemple.** Pour interpréter « il », une position peut accorder du poids au nom « colis » mentionné plus tôt.

**À distinguer.** Les poids d’attention seuls n’expliquent pas intégralement la décision du modèle.

Cours : diapositive 38 · Lexique : diapositive 141.

### séquence

Suite ordonnée de tokens, généralement munie de positions et de masques.

**Exemple.** Les tokens de « le colis arrive » forment une séquence de longueur trois.

**À distinguer.** Un sac de mots conserve les éléments mais perd leur ordre.

Cours : diapositive 38 · Lexique : diapositive 142.

### query (Q), key (K), value (V)

Dans l’attention, Q exprime la position qui interroge, K sert à calculer la compatibilité de chaque position, et V porte le contenu pondéré dans la sortie.

**Exemple.** Une requête cherche une notice en comparant Q aux K, puis récupère les informations correspondantes depuis V.

**À distinguer.** K et V peuvent provenir du même token mais de projections apprises distinctes ; V ne sert pas à calculer les poids.

Cours : diapositive 39 · Lexique : diapositive 142.

### projection linéaire

Transformation d’un vecteur par une matrice de paramètres appris, éventuellement suivie d’un biais.

**Exemple.** À partir de X, les matrices WQ, WK et WV produisent les représentations Q, K et V.

**À distinguer.** Les projections ne correspondent pas à des champs nommés explicitement dans le texte.

Cours : diapositive 39 · Lexique : diapositive 142.

### produit matriciel

Opération qui combine les lignes d’une matrice avec les colonnes d’une autre ; les dimensions internes doivent être compatibles.

**Exemple.** Pour Q de forme 3×2 et Kᵀ de forme 2×3, QKᵀ a la forme 3×3.

**À distinguer.** Vérifier l’ordre des axes : les lignes correspondent ici aux requêtes et les colonnes aux clés.

Cours : diapositive 40 · Lexique : diapositive 142.

### dimension d_k

Nombre de coordonnées d’une clé et d’une requête dans une tête d’attention donnée.

**Exemple.** Une clé (1,0) a d_k=2.

**À distinguer.** d_k n’est pas nécessairement la dimension totale du modèle ni le nombre de tokens.

Cours : diapositive 40 · Lexique : diapositive 143.

### matrice / transposée

Une matrice est un tableau à deux dimensions ; sa transposée échange lignes et colonnes.

**Exemple.** K de forme 3×2 donne Kᵀ de forme 2×3.

**À distinguer.** Transposer ne signifie pas inverser une matrice.

Cours : diapositive 40 · Lexique : diapositive 143.

### score de compatibilité

Produit scalaire entre une query et une key ; un score plus élevé contribue à un poids d’attention plus élevé après normalisation.

**Exemple.** q=(1,0) et k=(1,1) donnent qᵀk=1.

**À distinguer.** Un score brut n’est pas une probabilité et peut être positif ou négatif.

Cours : diapositive 41 · Lexique : diapositive 143.

### softmax

Fonction qui transforme un vecteur de scores en poids positifs ou nuls dont la somme vaut un, sur les positions autorisées.

**Exemple.** Sans mise à l’échelle, softmax([1, 0, 1]) ≈ [0,422 ; 0,155 ; 0,422]. Après division par √2, on obtient [0,401 ; 0,198 ; 0,401].

**À distinguer.** La somme vaut un par requête et sur l’axe des clés ; les positions interdites doivent être masquées avant la normalisation.

Cours : diapositive 42 · Lexique : diapositive 143.

### mise à l’échelle par √d_k

Division des scores de produit scalaire par la racine de la dimension des clés avant softmax afin de contrôler leur amplitude.

**Exemple.** Pour d_k=2, le score 1 devient 1/√2≈0,707.

**À distinguer.** Cette division ne transforme pas le score en cosinus et ne change pas d_k en dimension totale du modèle.

Cours : diapositive 42 · Lexique : diapositive 144.

### somme pondérée

Somme des vecteurs V après multiplication de chacun par son poids d’attention.

**Exemple.** 0,401(2,0)+0,198(0,2)+0,401(2,2)≈(1,604;1,198).

**À distinguer.** La sortie est une représentation vectorielle, pas directement un mot ou une explication.

Cours : diapositive 43 · Lexique : diapositive 144.

### masque causal

Masque qui interdit à chaque position d’utiliser les clés correspondant aux positions futures, afin de prédire la suite sans la révéler.

**Exemple.** À la position de « colis », le modèle peut voir « Le », mais pas « arrive » dans « Le colis arrive ».

**À distinguer.** Masquer les futurs scores avant softmax ; un masque de padding répond à une autre question.

Cours : diapositive 44 · Lexique : diapositive 144.

### attention multi-tête

Calcul de plusieurs attentions en parallèle avec des projections distinctes, puis concaténation et projection de leurs sorties.

**Exemple.** Avec 256 dimensions et 8 têtes de même taille, chaque tête peut traiter 32 dimensions.

**À distinguer.** Les têtes ne sont pas des modèles indépendants et n’ont pas un rôle linguistique fixe garanti.

Cours : diapositive 45 · Lexique : diapositive 144.

### concaténation

Assemblage de vecteurs le long d’un axe, sans les moyenner.

**Exemple.** Huit sorties de 32 coordonnées donnent 256 coordonnées concaténées.

**À distinguer.** Concaténer conserve les blocs côte à côte ; une projection ultérieure peut ensuite les mélanger.

Cours : diapositive 45 · Lexique : diapositive 145.

### MLP / FFN

Multi-Layer Perceptron / Feed-Forward Network : réseau de couches appliqué aux caractéristiques de chaque position, généralement avec une transformation non linéaire.

**Exemple.** Après l’attention, le FFN transforme séparément la représentation de chaque token avec des paramètres partagés entre positions.

**À distinguer.** Le FFN mélange les caractéristiques d’une position ; l’attention réalise l’échange d’information entre positions.

Cours : diapositive 46 · Lexique : diapositive 145.

### connexion résiduelle

Chemin qui additionne l’entrée d’un sous-bloc à sa transformation, lorsque leurs formes sont compatibles.

**Exemple.** x=[1,2] et f(x)=[0,5,−0,5] donnent x+f(x)=[1,5,1,5].

**À distinguer.** C’est une addition, pas une concaténation ni une moyenne.

Cours : diapositive 46 · Lexique : diapositive 145.

### normalisation

Opération qui remet à l’échelle les caractéristiques d’une représentation selon une règle du modèle, comme LayerNorm.

**Exemple.** LayerNorm agit sur les caractéristiques d’un token selon l’axe prévu par l’architecture.

**À distinguer.** Elle n’est pas le softmax sur les clés ; son ordre dans le bloc varie selon l’architecture.

Cours : diapositive 46 · Lexique : diapositive 145.

### information positionnelle

Représentation ou transformation qui donne au modèle un signal sur la position des tokens ou leurs relations d’ordre.

**Exemple.** Elle permet de distinguer « le client rembourse le vendeur » de « le vendeur rembourse le client ».

**À distinguer.** Un identifiant de token n’encode pas son rang dans la séquence ; longueur maximale ne garantit pas la qualité sur tout document.

Cours : diapositive 47 · Lexique : diapositive 146.

### encodeur Transformer

Architecture qui construit des représentations d’une séquence d’entrée en exploitant le contexte autorisé de cette séquence.

**Exemple.** Un encodeur de type BERT fournit des représentations pour classifier un message ou étiqueter ses tokens.

**À distinguer.** Un encodeur seul n’est pas automatiquement un générateur causal.

Cours : diapositive 48 · Lexique : diapositive 146.

### décodeur causal

Architecture qui prédit des tokens de sortie à partir du préfixe disponible, avec accès empêché aux tokens futurs.

**Exemple.** Un modèle de famille GPT reçoit « Le colis » puis génère le token suivant.

**À distinguer.** Classification et résumé restent possibles avec un décodeur via une tâche adaptée ; les exemples du tableau ne sont pas des interdictions.

Cours : diapositive 48 · Lexique : diapositive 146.

### encodeur-décodeur

Architecture qui encode une séquence source puis génère une séquence cible en consultant la source et le préfixe de sortie.

**Exemple.** T5 peut encoder une demande et générer sa traduction ou son résumé.

**À distinguer.** La cross-attention relie le décodeur à la source, elle ne lui donne pas accès aux futures cibles.

Cours : diapositive 48 · Lexique : diapositive 146.

### T5

Text-to-Text Transfer Transformer : famille encodeur-décodeur qui formule de nombreuses tâches sous forme d’entrée texte vers sortie texte.

**Exemple.** Une entrée à résumer est encodée puis une sortie plus courte est générée.

**À distinguer.** T5 est un exemple d’architecture ; ses capacités dépendent du checkpoint et de son entraînement.

Cours : diapositive 48 · Lexique : diapositive 147.

### préentraînement masqué

Objectif où certains tokens d’entrée sont masqués et prédits en s’appuyant sur le contexte rendu disponible par le modèle.

**Exemple.** Pour « Le colis est [MASK] », proposer « arrivé » à partir des mots observés.

**À distinguer.** Un modèle masqué n’est pas nécessairement un modèle conversationnel ou un classifieur métier.

Cours : diapositive 49 · Lexique : diapositive 147.

### fine-tuning

Poursuite de l’apprentissage d’un checkpoint préentraîné sur une tâche ou un format ciblé.

**Exemple.** Adapter l’encodeur et une tête de classification aux intentions annotées du support.

**À distinguer.** Le checkpoint préentraîné seul ne connaît pas automatiquement les labels du projet.

Cours : diapositive 49 · Lexique : diapositive 147.

### tête de classification

Couche de sortie ajoutée à une représentation du modèle pour produire des scores de classes définies.

**Exemple.** Une tête à cinq sorties peut produire un logit pour chacune des cinq intentions.

**À distinguer.** Une nouvelle tête doit être entraînée et évaluée ; sa forme correcte ne garantit pas de prédictions fiables.

Cours : diapositive 49 · Lexique : diapositive 147.

### préentraînement

Apprentissage initial de représentations sur un corpus général avant une adaptation éventuelle à une tâche.

**Exemple.** Un modèle apprend à prédire des tokens sur de nombreux textes.

**À distinguer.** Le fine-tuning poursuit l’apprentissage à partir de poids déjà appris.

Cours : diapositive 49 · Lexique : diapositive 148.

### paramètre / hyperparamètre

Un paramètre est appris à partir des données ; un hyperparamètre règle l’architecture ou l’apprentissage.

**Exemple.** Une valeur de poids est un paramètre ; le taux d’apprentissage est un hyperparamètre.

**À distinguer.** Choisir les hyperparamètres sur le test biaise la mesure finale.

Cours : diapositive 49 · Lexique : diapositive 148.

### pipeline

Interface logicielle de haut niveau qui enchaîne préparation des entrées, exécution du modèle et post-traitement pour une tâche choisie.

**Exemple.** Un pipeline fill-mask tokenise la phrase, calcule des scores puis affiche des tokens candidats.

**À distinguer.** pipeline() ne désigne ni une architecture ni un entraînement automatique ; tâche et checkpoint doivent être compatibles.

Cours : diapositive 50 · Lexique : diapositive 148.

### checkpoint

État enregistré d’un modèle, comprenant ses paramètres et souvent sa configuration après une étape d’apprentissage.

**Exemple.** Charger un checkpoint DistilBERT multilingue avec le tokenizer correspondant.

**À distinguer.** Un checkpoint n’est pas nécessairement adapté à la tâche, à la langue ou à la version choisie.

Cours : diapositive 50 · Lexique : diapositive 148.

### logits

Scores réels non normalisés produits avant softmax pour des classes ou des tokens candidats.

**Exemple.** [2,0] devient environ [0,88,0,12] après softmax à température 1.

**À distinguer.** Les logits ne sont pas des probabilités et un score élevé ne valide pas un fait.

Cours : diapositive 50 · Lexique : diapositive 149.

### inférence

Utilisation d’un modèle pour calculer une sortie à partir d’une nouvelle entrée.

**Exemple.** Obtenir la classe d’un message avec les poids déjà appris.

**À distinguer.** L’inférence seule ne met pas à jour les poids du modèle.

Cours : diapositive 50 · Lexique : diapositive 149.

### API

Application Programming Interface : interface définie qui permet à un programme d’utiliser une bibliothèque ou un service.

**Exemple.** pipeline() est une entrée d’API Python ; une API distante peut recevoir une requête HTTP.

**À distinguer.** API ne signifie pas forcément service payant ou distant.

Cours : diapositive 50 · Lexique : diapositive 149.

### décodage glouton (greedy)

À chaque étape, sélectionne le token de probabilité la plus élevée sans tirer au hasard.

**Exemple.** Pour [0,50; 0,30; 0,20], greedy choisit le premier token.

**À distinguer.** La sortie est déterministe pour un calcul fixé mais peut être répétitive ou erronée.

Cours : diapositive 51 · Lexique : diapositive 149.

### échantillonnage

Choix aléatoire d’un token selon une distribution de probabilités, souvent après filtrage des candidats.

**Exemple.** Un token à probabilité 0,30 peut être tiré même si un autre vaut 0,50.

**À distinguer.** La diversité accrue ne garantit ni exactitude ni meilleure fidélité.

Cours : diapositive 51 · Lexique : diapositive 150.

### température

Paramètre qui divise les logits avant softmax ; une température basse concentre la distribution et une température haute l’aplatit.

**Exemple.** Pour les logits [2,0], T=1 donne environ [0,88;0,12] et T=2 environ [0,73;0,27].

**À distinguer.** La température change le choix des tokens, pas les connaissances ou les poids appris ; elle n’a pas d’effet de diversité en greedy.

Cours : diapositive 51 · Lexique : diapositive 150.

### top-k

Filtrage qui ne garde que les k tokens les plus probables avant échantillonnage.

**Exemple.** Avec top-k=3, seuls les trois candidats de plus forte probabilité restent disponibles.

**À distinguer.** k fixe le nombre de candidats, pas leur masse totale de probabilité.

Cours : diapositive 51 · Lexique : diapositive 150.

### top-p

Échantillonnage à noyau : conserve le plus petit ensemble des tokens les plus probables dont la probabilité cumulée atteint p, puis renormalise.

**Exemple.** Avec [0,50;0,30;0,15;0,05] et p=0,8, les deux premiers candidats sont retenus.

**À distinguer.** Le nombre de candidats varie avec la distribution ; top-p n’est pas équivalent à un k fixe.

Cours : diapositive 51 · Lexique : diapositive 150.

### prompt

Texte ou structure de messages fournie au modèle comme contexte et consigne de génération.

**Exemple.** « Résume en une phrase : le colis AB123 est arrivé mardi avec un article manquant. »

**À distinguer.** Un prompt clair ne garantit pas que le modèle respecte les faits ou la consigne.

Cours : diapositive 52 · Lexique : diapositive 151.

### chat template

Formatage propre à un modèle qui transforme les rôles et messages en tokens ou marqueurs attendus par son entraînement.

**Exemple.** Le template peut sérialiser un message utilisateur puis signaler qu’une réponse assistant doit commencer.

**À distinguer.** Le format brut d’un autre modèle peut provoquer une génération mal formée ou mal conditionnée.

Cours : diapositive 52 · Lexique : diapositive 151.

### max_new_tokens

Limite supérieure du nombre de tokens nouveaux générés, sans compter les tokens du prompt.

**Exemple.** max_new_tokens=40 autorise au plus 40 tokens de continuation.

**À distinguer.** Un token n’est pas un mot ; la limite ne fixe ni le nombre de caractères ni la fidélité.

Cours : diapositive 52 · Lexique : diapositive 151.


## Jour 3

### id2label / label2id

Correspondances sauvegardées entre l’indice numérique d’une classe et son nom, dans les deux sens.

**Exemple.** 0 ↔ livraison ; 1 ↔ facturation.

**À distinguer.** Un ordre incohérent affiche des noms erronés même si les calculs du modèle sont inchangés.

Cours : diapositive 59 · Lexique : diapositive 152.

### loss (fonction de perte)

Valeur calculée à partir des prédictions et des cibles, que l’entraînement cherche à réduire.

**Exemple.** Si la vraie classe reçoit 0,8, −ln(0,8) ≈ 0,223.

**À distinguer.** Une loss basse sur l’entraînement ne garantit pas de bonnes prédictions sur de nouveaux exemples.

Cours : diapositive 60 · Lexique : diapositive 152.

### entropie croisée (cross-entropy)

Loss de classification qui pénalise la faible probabilité attribuée à la classe correcte.

**Exemple.** PyTorch CrossEntropyLoss reçoit généralement des logits et les indices des classes vraies.

**À distinguer.** Ne pas appliquer softmax avant CrossEntropyLoss lorsque l’API attend des logits.

Cours : diapositive 60 · Lexique : diapositive 152.

### forward pass (passe avant)

Calcul qui fait traverser les entrées au modèle pour produire des prédictions.

**Exemple.** Un batch de messages donne cinq logits par message.

**À distinguer.** La passe avant calcule les sorties ; elle ne met pas à elle seule les poids à jour.

Cours : diapositive 61 · Lexique : diapositive 152.

### backpropagation (rétropropagation)

Calcul qui propage l’erreur de la loss vers les paramètres afin d’obtenir leurs gradients.

**Exemple.** La loss finale contribue aux gradients de la tête et, si elle est dégelée, de l’encodeur.

**À distinguer.** La rétropropagation calcule des gradients ; c’est l’optimiseur qui applique la mise à jour.

Cours : diapositive 61 · Lexique : diapositive 153.

### gradient

Dérivée qui indique comment la loss changerait si un paramètre changeait légèrement.

**Exemple.** Un gradient négatif peut conduire l’optimiseur à augmenter le paramètre pour réduire la loss.

**À distinguer.** Ce n’est pas une prédiction ni une garantie que chaque mise à jour améliore la validation.

Cours : diapositive 61 · Lexique : diapositive 153.

### optimiseur

Algorithme qui utilise les gradients et ses réglages pour mettre à jour les paramètres entraînables.

**Exemple.** AdamW adapte les mises à jour à l’historique des gradients et applique une décroissance des poids.

**À distinguer.** Changer d’optimiseur ou de réglages peut changer le résultat même avec les mêmes données.

Cours : diapositive 61 · Lexique : diapositive 153.

### AdamW

Optimiseur adaptatif qui estime des moyennes des gradients et sépare la décroissance des poids de l’adaptation du pas.

**Exemple.** Un fine-tuning utilise souvent AdamW avec un learning rate faible.

**À distinguer.** AdamW ne choisit ni les bonnes données ni la bonne métrique.

Cours : diapositive 61 · Lexique : diapositive 153.

### learning rate (taux d’apprentissage)

Réglage qui détermine l’ampleur des mises à jour des paramètres par l’optimiseur.

**Exemple.** Un taux trop élevé peut faire osciller ou diverger la loss.

**À distinguer.** Ce n’est ni la taille du batch ni le nombre de mises à jour.

Cours : diapositive 61 · Lexique : diapositive 154.

### Trainer

Classe Hugging Face Transformers qui orchestre l’entraînement et l’évaluation selon une configuration fournie.

**Exemple.** Trainer reçoit modèle, arguments, jeux de données, tokenizer ou collator et calcul de métriques.

**À distinguer.** Il automatise la boucle mais ne vérifie pas que les labels, partitions ou scores sont corrects.

Cours : diapositive 61 · Lexique : diapositive 154.

### collator

Fonction qui assemble des exemples en batch et complète au besoin leurs entrées et leurs labels.

**Exemple.** Un collator dynamique padde chaque batch jusqu’à sa séquence la plus longue.

**À distinguer.** Inspecter le batch produit : le dataset seul ne révèle ni les formes ni les masques finaux.

Cours : diapositive 62 · Lexique : diapositive 154.

### pas d’entraînement (step)

Dans ce support, une étape désigne une mise à jour de l’optimiseur ; vérifier la convention du compteur utilisé.

**Exemple.** Quatre micro-batchs accumulés peuvent contribuer à un pas d’optimiseur.

**À distinguer.** Certaines bibliothèques comptent aussi les micro-batchs comme steps ; ne pas comparer sans définir le compteur.

Cours : diapositive 63 · Lexique : diapositive 154.

### époque (epoch)

Un passage complet sur les exemples du jeu d’entraînement, selon l’ordre et les exclusions définis.

**Exemple.** 30 micro-batchs de 8 couvrent 240 exemples en une époque.

**À distinguer.** Une époque n’est pas une mise à jour unique ; elle peut contenir plusieurs pas d’optimiseur.

Cours : diapositive 63 · Lexique : diapositive 155.

### accumulation de gradients

Addition des gradients de plusieurs micro-batchs avant d’effectuer une mise à jour.

**Exemple.** Accumuler quatre micro-batchs de 8 donne un lot effectif de 32 exemples sur un GPU, hors dernier groupe partiel.

**À distinguer.** Cela réduit la mémoire des activations simultanées, mais ne reproduit pas tous les effets d’un batch physique de 32.

Cours : diapositive 63 · Lexique : diapositive 155.

### jeu de validation

Partie réservée au choix du modèle et de ses réglages pendant le développement.

**Exemple.** Choisir le checkpoint au meilleur macro-F1 de validation selon une règle annoncée.

**À distinguer.** Des choix répétés guidés par la validation peuvent finir par s’y suradapter.

Cours : diapositive 64 · Lexique : diapositive 155.

### jeu de test

Partie tenue à l’écart des choix de modèle, utilisée pour une estimation finale selon le protocole.

**Exemple.** Après sélection sur validation, calculer une fois les scores finaux sur le test réservé.

**À distinguer.** Si le score test guide un nouveau réglage, ce test n’est plus une mesure finale indépendante.

Cours : diapositive 64 · Lexique : diapositive 155.

### surapprentissage (overfitting)

Situation où un modèle s’ajuste trop aux exemples d’entraînement et généralise moins bien à des exemples nouveaux.

**Exemple.** La loss train baisse tandis que le score de validation se dégrade.

**À distinguer.** Une divergence train-validation est un signal à examiner, pas une preuve isolée de sa cause.

Cours : diapositive 64 · Lexique : diapositive 156.

### précision

Parmi les exemples prédits positifs pour une classe, part qui appartient réellement à cette classe.

**Exemple.** 4 vrais positifs et 1 faux positif donnent une précision de 4/5 = 0,8.

**À distinguer.** Une forte précision peut coexister avec un rappel faible si le modèle prédit rarement cette classe.

Cours : diapositive 65 · Lexique : diapositive 156.

### rappel

Parmi les exemples réellement d’une classe, part que le modèle retrouve.

**Exemple.** 4 vrais positifs et 4 faux négatifs donnent un rappel de 4/8 = 0,5.

**À distinguer.** Un rappel élevé peut venir de nombreuses prédictions positives erronées.

Cours : diapositive 65 · Lexique : diapositive 156.

### F1

Moyenne harmonique de la précision et du rappel, qui baisse lorsque l’un des deux est faible.

**Exemple.** Précision 0,8 et rappel 0,5 donnent F1 ≈ 0,615.

**À distinguer.** Le F1 ne précise pas quelle classe ou quelle règle d’agrégation a été utilisée.

Cours : diapositive 65 · Lexique : diapositive 156.

### macro-F1

Moyenne arithmétique des F1 calculés séparément pour chaque classe, avec le même poids pour chacune.

**Exemple.** Des F1 de 0,90 et 0,30 donnent un macro-F1 de 0,60.

**À distinguer.** Il ne pondère pas par le nombre d’exemples et ne prouve pas l’équité entre sous-groupes.

Cours : diapositive 65 · Lexique : diapositive 157.

### TP / FP / FN

True Positive : vrai positif ; False Positive : faux positif ; False Negative : faux négatif, pour une classe et une unité d’évaluation données.

**Exemple.** Pour « facturation » : TP = bien détecté, FP = prédit à tort, FN = manqué.

**À distinguer.** Définir la classe positive avant de compter ; les lettres TP désignent aussi un travail pratique dans le cours.

Cours : diapositive 65 · Lexique : diapositive 157.

### micro-F1 / F1 pondéré

Micro-F1 agrège les comptes avant le calcul ; F1 pondéré moyenne les F1 de classe selon leurs effectifs réels.

**Exemple.** Une classe fréquente pèse davantage dans le F1 pondéré que dans macro-F1.

**À distinguer.** La moyenne macro est encore une autre agrégation ; donner son nom exact.

Cours : diapositive 65 · Lexique : diapositive 157.

### CPU / GPU / VRAM / OOM

CPU : processeur généraliste ; GPU : processeur adapté aux calculs parallèles ; VRAM : sa mémoire ; OOM : mémoire insuffisante.

**Exemple.** Réduire le micro-batch peut résoudre un manque de mémoire GPU.

**À distinguer.** Libérer la mémoire GPU ne libère pas l’espace disque du poste.

Cours : diapositive 66 · Lexique : diapositive 157.

### BIO

Schéma d’étiquetage : B marque le début d’une entité, I sa continuation et O un token hors entité.

**Exemple.** B-PER I-PER étiquette « Marie Dupont » comme une personne complète.

**À distinguer.** Le type doit rester cohérent ; I-PER sans entité précédente peut former une séquence invalide selon la convention.

Cours : diapositive 67 · Lexique : diapositive 158.

### span (segment)

Portion de texte délimitée par un début et une fin, à laquelle on peut associer un type d’entité.

**Exemple.** « Marie Dupont » est un segment de deux mots de type personne.

**À distinguer.** Le bon type avec une mauvaise frontière reste une erreur en évaluation stricte.

Cours : diapositive 67 · Lexique : diapositive 158.

### sous-token

Morceau d’un mot produit par le tokenizer, qui peut découper un mot rare en plusieurs unités.

**Exemple.** Un tokenizer peut représenter « Dupont » par « Du » et « ##pont ».

**À distinguer.** Le découpage dépend du tokenizer ; ne pas le supposer à partir d’un exemple illustratif.

Cours : diapositive 68 · Lexique : diapositive 158.

### word_id

Indice reliant un sous-token au mot d’origine de la séquence, quand le tokenizer fournit cet alignement.

**Exemple.** Les sous-tokens « Du » et « ##pont » peuvent tous deux avoir word_id 1.

**À distinguer.** Les tokens spéciaux peuvent avoir word_id None ; leur absence d’indice ne les rend pas des mots annotés.

Cours : diapositive 68 · Lexique : diapositive 158.

### −100 / ignore_index

Valeur conventionnelle qui indique à certaines fonctions de loss d’ignorer cette position, et non une classe à prédire.

**Exemple.** La continuation « ##pont » reçoit −100 si seule la première partie du mot est supervisée.

**À distinguer.** La convention et l’API doivent correspondre ; −100 ne signifie pas que le sous-token est absent de l’entrée.

Cours : diapositive 68 · Lexique : diapositive 159.

### masque de labels

Indicateur des positions dont les cibles participent au calcul de la loss.

**Exemple.** Un sous-token peut avoir attention_mask = 1 et label = −100 : visible en entrée, ignoré comme cible.

**À distinguer.** Ne pas confondre les positions à lire avec les positions à superviser.

Cours : diapositive 69 · Lexique : diapositive 159.

### argmax

Opération qui renvoie l’indice de la valeur maximale d’un tableau de scores.

**Exemple.** Pour [0,2 ; 0,7 ; 0,1], argmax renvoie l’indice 1 avec des indices commençant à zéro.

**À distinguer.** Argmax retourne un indice, pas la valeur 0,7 ni le nom de la classe.

Cours : diapositive 70 · Lexique : diapositive 159.

### évaluation stricte d’entité

Règle qui compte une entité comme correcte seulement si son début, sa fin et son type concordent avec la référence.

**Exemple.** Prédire « Marie » pour « Marie Dupont : PER » est une erreur de frontière.

**À distinguer.** Préciser la règle et le schéma avant de comparer des scores issus de métriques différentes.

Cours : diapositive 71 · Lexique : diapositive 159.

### artefact de modèle

Ensemble de fichiers nécessaires pour identifier, recharger et utiliser un modèle ou son adaptation.

**Exemple.** Poids, configuration, tokenizer, mapping des labels et versions de l’expérience.

**À distinguer.** Des poids isolés peuvent être inutilisables si manquent tokenizer, configuration ou modèle de base requis.

Cours : diapositive 74 · Lexique : diapositive 160.

### graine aléatoire (seed)

Valeur initiale qui rend répétables certains tirages pseudo-aléatoires dans un protocole donné.

**Exemple.** Fixer la graine avant de mélanger les données et d’initialiser une tête neuve.

**À distinguer.** Une graine ne garantit pas une reproduction bit à bit sur tout matériel ou toute bibliothèque.

Cours : diapositive 74 · Lexique : diapositive 160.


## Jour 4

### RAG (Retrieval-Augmented Generation, génération augmentée par récupération)

Méthode qui recherche des passages pertinents et les ajoute au contexte avant la génération.

**Exemple.** Retrouver une procédure à jour puis demander au modèle de répondre à partir de ce texte.

**À distinguer.** Le RAG ne garantit pas que la recherche retrouve les bonnes sources ni que la réponse les respecte.

Cours : diapositive 81 · Lexique : diapositive 161.

### SFT (Supervised Fine-Tuning, ajustement fin supervisé)

Adaptation d’un modèle à partir d’exemples d’entrées et de réponses cibles préparés par des personnes ou une règle documentée.

**Exemple.** Montrer des demandes de support suivies de réponses utiles et prudentes.

**À distinguer.** SFT décrit le type de supervision, pas la méthode d’économie mémoire comme LoRA.

Cours : diapositive 81 · Lexique : diapositive 161.

### few-shot dans le prompt

Utilisation de quelques exemples de la tâche dans le contexte pour guider la réponse, sans mise à jour des poids.

**Exemple.** Montrer deux demandes étiquetées avant de classer une nouvelle demande.

**À distinguer.** Distinguer les exemples en contexte d’un entraînement sur ces exemples.

Cours : diapositive 81 · Lexique : diapositive 161.

### curation des données

Sélection, vérification et organisation d’exemples dont on documente l’origine et les transformations.

**Exemple.** Retirer un doublon, corriger une contradiction, consigner la décision.

**À distinguer.** Un corpus propre en apparence peut rester déséquilibré ou contenir une fuite de données.

Cours : diapositive 84 · Lexique : diapositive 161.

### masque de loss

Masque qui détermine quelles positions prédites contribuent à la loss d’entraînement.

**Exemple.** Le prompt reste visible au modèle tandis que les labels du prompt valent −100 et ceux de la réponse sont conservés.

**À distinguer.** Masquer une cible n’enlève pas automatiquement son texte du contexte d’entrée.

Cours : diapositive 86 · Lexique : diapositive 162.

### décalage causal (causal shift)

Alignement où les logits à une position prédisent le token suivant, sans donner accès à ce token futur.

**Exemple.** L’entrée « le colis » entraîne une cible « colis » à la position du token « le ».

**À distinguer.** Certaines pertes de modèles causaux effectuent déjà le décalage ; ne pas le refaire dans les données.

Cours : diapositive 87 · Lexique : diapositive 162.

### PEFT (Parameter-Efficient Fine-Tuning, ajustement fin économe en paramètres)

Famille de méthodes qui adapte un modèle en entraînant une petite partie des paramètres ou des paramètres ajoutés.

**Exemple.** LoRA ajoute de petites matrices entraînables à des poids de base gelés.

**À distinguer.** Moins de paramètres entraînables ne supprime pas les besoins de calcul, de mémoire d’activations ni d’évaluation.

Cours : diapositive 88 · Lexique : diapositive 162.

### LoRA (Low-Rank Adaptation, adaptation de faible rang)

Méthode PEFT qui représente une correction de poids par le produit de deux petites matrices entraînables, tandis que la matrice de base reste généralement gelée.

**Exemple.** Une matrice 1024×1024 reçoit une correction BA de rang 8, avec 8×(1024+1024) paramètres.

**À distinguer.** Le rang réduit la taille de la correction ; il ne signifie pas que le modèle entier a peu de paramètres.

Cours : diapositive 88 · Lexique : diapositive 162.

### rang (rank)

Dimension intermédiaire qui borne le nombre de directions indépendantes représentées par une correction matricielle LoRA.

**Exemple.** Avec r = 8, A et B passent par un espace intermédiaire de dimension 8.

**À distinguer.** Un rang plus élevé ajoute des paramètres et n’assure pas automatiquement de meilleures sorties.

Cours : diapositive 88 · Lexique : diapositive 163.

### quantification

Représentation des poids avec moins de bits, en acceptant une approximation contrôlée pour réduire leur stockage.

**Exemple.** Stocker les poids de base sur 4 bits au lieu de FP16 réduit leur taille théorique.

**À distinguer.** Le nombre de bits de stockage ne fixe pas à lui seul la précision de calcul de toutes les opérations.

Cours : diapositive 90 · Lexique : diapositive 163.

### QLoRA (Quantized Low-Rank Adaptation)

Méthode qui garde une base quantifiée et gelée tout en entraînant des adaptateurs LoRA en précision de calcul adaptée.

**Exemple.** Une base en NF4 et des adaptateurs LoRA entraînables avec calcul FP16.

**À distinguer.** QLoRA ne signifie pas que gradients, activations et toutes les opérations se font en 4 bits.

Cours : diapositive 90 · Lexique : diapositive 163.

### NF4 (4-bit NormalFloat)

Format de quantification sur quatre bits conçu pour représenter efficacement des poids dont les valeurs suivent une distribution approximativement normale.

**Exemple.** QLoRA peut stocker la base dans NF4, puis déquantifier par blocs pour le calcul.

**À distinguer.** NF4 est un format de stockage des poids, pas une précision universelle pour les calculs.

Cours : diapositive 90 · Lexique : diapositive 163.

### dtype (type de données)

Format numérique utilisé pour stocker ou calculer des valeurs, avec une précision et un coût mémoire donnés.

**Exemple.** FP16 est un format flottant 16 bits utilisé pour certaines opérations sur GPU.

**À distinguer.** Le dtype des poids, des activations et des calculs peut différer.

Cours : diapositive 90 · Lexique : diapositive 164.

### FP16 / BF16

Deux formats flottants de 16 bits : FP16 offre plus de précision sur la mantisse ; BF16 offre une plage d’exposants plus large.

**Exemple.** Le TP T4 utilise les réglages compatibles prévus, sans supposer le BF16 natif.

**À distinguer.** 16 bits ne signifie pas même plage numérique ni même prise en charge matérielle.

Cours : diapositive 90 · Lexique : diapositive 164.

### bitsandbytes

Bibliothèque qui fournit notamment des opérations et des couches quantifiées utilisées dans certains chargements de modèles.

**Exemple.** Un chargement QLoRA peut utiliser bitsandbytes pour la base 4 bits.

**À distinguer.** NF4 est un format ; bitsandbytes est une bibliothèque qui l’implémente.

Cours : diapositive 90 · Lexique : diapositive 164.

### activations

Valeurs intermédiaires produites par le réseau pendant la passe avant et parfois conservées pour calculer les gradients.

**Exemple.** La mémoire des activations augmente généralement avec la longueur des séquences et la taille du micro-batch.

**À distinguer.** Quantifier les poids ne quantifie pas automatiquement toutes les activations ni les états de l’optimiseur.

Cours : diapositive 91 · Lexique : diapositive 164.

### gradient checkpointing (recalcul des activations)

Technique qui conserve moins d’activations intermédiaires et en recalcule certaines pendant la rétropropagation.

**Exemple.** Activer le checkpointing peut réduire la mémoire au prix de calculs supplémentaires.

**À distinguer.** Ce réglage économise de la mémoire mais ralentit l’entraînement ; il n’est pas une sauvegarde de modèle.

Cours : diapositive 92 · Lexique : diapositive 165.

### ROUGE (Recall-Oriented Understudy for Gisting Evaluation)

Famille de mesures automatiques qui compare des unités lexicales ou des séquences communes entre un résumé et une référence.

**Exemple.** ROUGE-1 compare les recouvrements de mots après tokenisation.

**À distinguer.** Un recouvrement élevé ne prouve ni la fidélité factuelle ni l’utilité du résumé.

Cours : diapositive 95 · Lexique : diapositive 165.

### ROUGE-1

Mesure le recouvrement des unigrammes, c’est-à-dire des unités d’un token, entre candidat et référence.

**Exemple.** « colis reçu mardi » et « colis arrivé mardi » partagent plusieurs mots après tokenisation.

**À distinguer.** Le résultat dépend de la tokenisation et du choix précision, rappel ou F-mesure.

Cours : diapositive 95 · Lexique : diapositive 165.

### ROUGE-2

Mesure le recouvrement des suites de deux tokens consécutifs entre résumé produit et référence.

**Exemple.** « colis reçu mardi » et « paquet reçu mardi » partagent le bigramme « reçu mardi ».

**À distinguer.** Une paraphrase correcte peut avoir peu de bigrammes en commun.

Cours : diapositive 95 · Lexique : diapositive 165.

### ROUGE-L

Mesure fondée sur la plus longue sous-séquence commune, qui conserve l’ordre sans exiger que les tokens soient contigus.

**Exemple.** « colis … reçu mardi » partage une sous-séquence avec « colis reçu mardi ».

**À distinguer.** Une sous-séquence commune ne détecte pas à elle seule une négation ou une inversion de fait.

Cours : diapositive 95 · Lexique : diapositive 166.

### résumé extractif

Résumé composé en sélectionnant des phrases ou passages de la source, souvent sans les reformuler.

**Exemple.** Choisir la phrase mentionnant l’article manquant et la demande de vérification.

**À distinguer.** Les phrases sélectionnées peuvent être redondantes ou manquer de contexte.

Cours : diapositive 95 · Lexique : diapositive 166.

### résumé abstractif

Résumé qui reformule et combine les informations de la source en générant de nouveaux textes.

**Exemple.** Reformuler plusieurs détails en une phrase concise destinée au service client.

**À distinguer.** La reformulation peut introduire des détails absents de la source.

Cours : diapositive 95 · Lexique : diapositive 166.

### hallucination (affirmation non étayée)

Contenu généré présenté comme vrai alors qu’il est absent ou contredit par les éléments fournis.

**Exemple.** Dire qu’un remboursement a été effectué alors que la source dit seulement qu’une vérification est demandée.

**À distinguer.** Une formulation plausible ou un ROUGE élevé ne constitue pas une preuve.

Cours : diapositive 96 · Lexique : diapositive 166.

### fidélité factuelle

Mesure dans laquelle les affirmations du résumé sont soutenues par la source et n’en contredisent pas les faits.

**Exemple.** Vérifier séparément la référence, la date, le problème signalé et l’action demandée.

**À distinguer.** Un résumé fidèle peut omettre un fait important ; fidélité et couverture sont deux critères distincts.

Cours : diapositive 96 · Lexique : diapositive 167.


## Jour 5

### biais d’évaluation

Distorsion du résultat causée par un échantillon, une annotation, une métrique ou une procédure qui représente mal l’usage visé.

**Exemple.** Un test composé presque uniquement de messages courts masque les erreurs sur les longues demandes.

**À distinguer.** Une métrique définie correctement ne corrige pas à elle seule un échantillon non représentatif.

Cours : diapositive 103 · Lexique : diapositive 168.

### benchmark

Protocole défini de tâches, données, métriques et conditions d’exécution servant à comparer des systèmes.

**Exemple.** Comparer les mêmes modèles sur les mêmes messages test et la même règle macro-F1.

**À distinguer.** Le nom d’un jeu ou d’une métrique ne suffit pas à rendre deux résultats comparables.

Cours : diapositive 104 · Lexique : diapositive 168.

### robustesse

Capacité d’un système à conserver un comportement acceptable lorsque les entrées varient dans les conditions prévues.

**Exemple.** Tester paraphrases, négations, fautes ou messages hors domaine selon une règle fixe.

**À distinguer.** Réussir quelques variations ne prouve pas la robustesse à toutes les entrées possibles.

Cours : diapositive 104 · Lexique : diapositive 168.

### reproductibilité

Possibilité de refaire une expérience et d’obtenir des résultats comparables à partir de ses données, réglages et artefacts documentés.

**Exemple.** Conserver graine, versions, partitions, configuration et script de mesure.

**À distinguer.** Des résultats proches ne sont pas nécessairement bit à bit identiques entre matériels.

Cours : diapositive 104 · Lexique : diapositive 168.

### zéro-shot (zero-shot)

Utilisation d’un modèle pour une tâche sans exemple annoté de cette tâche dans son prompt ni adaptation dédiée sur ces exemples.

**Exemple.** Demander à un LLM de choisir une intention parmi cinq descriptions, sans fournir d’exemples étiquetés.

**À distinguer.** Il faut toujours définir la consigne, les classes, le décodage et le traitement des réponses invalides.

Cours : diapositive 105 · Lexique : diapositive 169.

### JSON / parsing

JSON est un format textuel structuré ; le parsing analyse ce texte pour vérifier sa structure et récupérer ses champs.

**Exemple.** Décoder {"label":"compte"}, puis vérifier que compte est une classe autorisée.

**À distinguer.** Un JSON valide peut contenir une réponse fausse ; compter aussi les sorties invalides.

Cours : diapositive 105 · Lexique : diapositive 169.

### bootstrap (rééchantillonnage bootstrap)

Méthode d’estimation de l’incertitude qui tire plusieurs échantillons avec remise à partir des observations disponibles et recalcule le score.

**Exemple.** Rééchantillonner les 20 cas test pour obtenir une distribution de macro-F1, si le protocole convient.

**À distinguer.** Les répétitions ne créent pas de nouvelles données indépendantes et ne réparent ni biais ni fuite.

Cours : diapositive 108 · Lexique : diapositive 169.

### ablation

Expérience qui retire ou modifie un composant à la fois pour estimer sa contribution, en gardant le reste du protocole comparable.

**Exemple.** Comparer RAG activé puis désactivé sur les mêmes requêtes réservées.

**À distinguer.** Si plusieurs facteurs changent à la fois, leur effet individuel devient difficile à attribuer.

Cours : diapositive 112 · Lexique : diapositive 169.

### latence

Temps écoulé entre une requête et la disponibilité de sa réponse, selon les bornes de mesure choisies.

**Exemple.** Mesurer séparément le chargement du modèle et le temps d’inférence par requête.

**À distinguer.** Sans préciser matériel, longueur, batch et inclusion du chargement, les chiffres ne sont pas comparables.

Cours : diapositive 113 · Lexique : diapositive 170.

### démarrage à froid (cold start)

Première exécution qui inclut des coûts d’initialisation tels que chargement du modèle ou allocation du GPU.

**Exemple.** La première prédiction peut prendre plusieurs secondes alors que les suivantes sont plus rapides.

**À distinguer.** Ne pas mélanger temps de démarrage et temps d’inférence à chaud dans une même statistique.

Cours : diapositive 113 · Lexique : diapositive 170.

### échauffement (warm-up)

Exécutions préalables destinées à laisser le système atteindre son régime stable avant les mesures chronométrées.

**Exemple.** Lancer quelques requêtes, puis chronométrer les suivantes dans les mêmes conditions.

**À distinguer.** Préciser que les essais d’échauffement sont exclus ; ils ne représentent pas le délai de la toute première requête.

Cours : diapositive 113 · Lexique : diapositive 170.

### p50 / p95

Percentiles de latence : p50 est la médiane ; p95 est le seuil sous lequel se trouvent 95 % des mesures observées.

**Exemple.** p50 = 0,4 s et p95 = 1,2 s indiquent que la queue lente dépasse la médiane.

**À distinguer.** Le percentile dépend du nombre et des conditions des mesures ; rapporter aussi ces conditions.

Cours : diapositive 113 · Lexique : diapositive 170.

### Gradio

Bibliothèque Python qui crée une interface web pour appeler une fonction et afficher ses résultats.

**Exemple.** Un champ texte envoie une demande au classifieur déjà chargé.

**À distinguer.** Une démo interactive ne garantit ni la qualité du modèle ni la robustesse d’un service de production.

Cours : diapositive 114 · Lexique : diapositive 171.

### model card (fiche de modèle)

Document qui décrit un modèle, son origine, son entraînement, ses évaluations, ses usages prévus et ses limites.

**Exemple.** Indiquer le checkpoint de base, les données d’adaptation, les métriques et les cas à éviter.

**À distinguer.** Une fiche ne remplace ni les fichiers nécessaires au rechargement ni les preuves d’évaluation.

Cours : diapositive 115 · Lexique : diapositive 171.

### data card (fiche de données)

Document qui précise l’origine, la construction, le contenu, les partitions, les limites et les droits associés à un jeu de données.

**Exemple.** Expliquer la provenance des messages et comment train, validation et test ont été séparés.

**À distinguer.** Ne pas présenter une licence ou une provenance inconnue comme vérifiée.

Cours : diapositive 115 · Lexique : diapositive 171.

### licence

Conditions juridiques qui précisent les droits et obligations de réutilisation d’un modèle ou d’un jeu de données.

**Exemple.** Vérifier séparément les conditions du checkpoint de base et des données d’adaptation.

**À distinguer.** Publier un adaptateur n’efface pas les conditions applicables au modèle de base ni aux données.

Cours : diapositive 116 · Lexique : diapositive 171.

### Hugging Face Hub / Space

Le Hub héberge des dépôts de modèles et de données ; un Space héberge une application de démonstration.

**Exemple.** Un dépôt conserve les poids ; un Space peut présenter une démo Gradio.

**À distinguer.** Publier des poids et déployer une application sont deux opérations distinctes.

Cours : diapositive 116 · Lexique : diapositive 172.
