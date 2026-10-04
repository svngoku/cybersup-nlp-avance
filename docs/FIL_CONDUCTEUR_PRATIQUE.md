# Fil conducteur pratique — guide réservé au formateur

**Chrys NIONGOLO · NLP Avancé (BERT, GPT, Hugging Face) · M2 IA · 35 heures.**

Ce document permet d'animer la semaine avec les supports et les notebooks fournis. Il répond au besoin exprimé après le cours de **deep learning** jugé trop théorique : faire prévoir, manipuler et expliquer un comportement dès le matin, puis construire l'après-midi. Aucun livre supplémentaire n'est nécessaire pendant la séance. Les lectures externes restent des prolongements facultatifs.

**Diffusion : formateur uniquement.** Ce guide contient les observations attendues, réponses de vérification et remédiations. Projeter les diapositives et la version étudiante des notebooks ; garder ce document et les notebooks `_corrige` hors du pack étudiant. Une sortie préparée par le formateur doit être annoncée comme telle, avec sa configuration et sa date ; elle ne devient pas une exécution de l'étudiant.

## Préparer une manipulation, pas une séance de téléchargement

Les dix microdémonstrations ci-dessous pointent vers des **cellules réellement présentes** dans les sept notebooks étudiants. Une cellule de code n'a généralement pas de titre : le repère donné est le titre exact de la section Markdown qui la précède, suivi de son identifiant stable et d'un début de code reconnaissable. Les liens utilisent `#cell-id=…`. Si le lecteur de notebooks n'ouvre pas directement cette ancre, rechercher la section et le début de code ; l'identifiant est aussi consultable dans le JSON du notebook. Le document n'affirme pas que tous les lecteurs prennent en charge les ancres de cellules.

Avant le cours, installer les dépendances des notebooks, redémarrer les runtimes si demandé et exécuter leurs cellules d'initialisation. Les petites opérations NumPy, TF-IDF, BPE, audit de données et métriques utilisent le CPU. Le padding et le chat template nécessitent un **tokenizer préchargé**, mais aucun poids de Transformer ni GPU. Préparer à l'avance les tokenizers de `distilbert/distilbert-base-multilingual-cased` et `Qwen/Qwen2.5-0.5B-Instruct` dans la session qui servira à projeter.

Pour une cellule mêlant un calcul jouet et un entraînement, le guide précise le **sous-bloc exact** à utiliser. Préparer ce sous-bloc dans une cellule de travail de la copie du formateur, à partir du code existant, puis conserver le notebook source intact. Aucun nouveau notebook à distribuer n'est nécessaire. Ne pas lancer « Tout exécuter » pendant une microdémo : cela pourrait ouvrir le test final ou démarrer un entraînement placé plus bas.

Les poids et les éventuels artefacts d'entraînement destinés à l'après-midi se préchargent avant la séance ou pendant un travail autonome prévu. Leur téléchargement ne fait pas partie des cinq à huit minutes de manipulation du matin. Le T4, ou le L4 si fourni, intervient dans les entraînements et les démonstrations de modèles ; il n'est requis par **aucune des dix microdémos minimales**. Sans réseau, utiliser les tableaux réellement préparés pendant la répétition et faire refaire le calcul à la main ; annoncer précisément l'étape qui n'a pas été exécutée en direct.

## Insérer les dix microdémos sans ajouter une minute

Les temps sont des minutes pédagogiques cumulées depuis le début de la matinée, hors pauses. Ils s'insèrent dans les blocs de vingt minutes du [programme](PROGRAMME_35H.md), en remplaçant la fin de l'explication et l'exercice déjà prévus. Chaque matin reste à **180 minutes**, chaque après-midi à **240 minutes**. Une démo de sept minutes peut suivre : une minute de prédiction, trois de manipulation, deux d'explication, une de vérification. Une remédiation remplace la variante ; elle ne rallonge pas le bloc.

| Repère | Créneau existant | Temps de démo inclus | Action visible | Matériel minimal |
|---|---|---:|---|---|
| J1-A | TF-IDF, 60–80 | 73–80 : 7 min | Changer une requête, lire les voisins | CPU |
| J1-B | BPE, 100–120 | 113–120 : 7 min | Comparer deux vocabulaires sur les mêmes textes | CPU |
| J2-A | Scores et softmax, 60–80 | 72–80 : 8 min | Modifier V après avoir prédit l'effet | CPU |
| J2-B | Masques, 80–100 | 92–100 : 8 min | Perturber le futur, comparer avec/sans masque | CPU |
| J3-A | Collator, 40–60 | 53–60 : 7 min | Assembler deux phrases de longueurs différentes | CPU + tokenizer en cache |
| J3-B | F1 d'entités, 140–160 | 153–160 : 7 min | Tronquer une frontière BIO et mesurer l'effet | CPU |
| J4-A | Curation, 40–60 | 52–60 : 8 min | Écarter les exemples défectueux, relire le rendu chat | CPU + tokenizer en cache pour le rendu |
| J4-B | Métriques, 140–160 | 153–160 : 7 min | Inverser un fait tout en gardant presque les mêmes mots | CPU |
| J5-A | Comparaison, 20–40 | 33–40 : 7 min | Comparer une seule variante sur validation commune | CPU |
| J5-B | Contrat d'entrée, 100–120 | 113–120 : 7 min | Tester texte normal, vide et trop long | CPU ; serveur désactivé |

Ces manipulations occupent 73 minutes **à l'intérieur** des 900 minutes de matinée. Le reste des activités, calculs et corrections du programme est conservé. Si une sortie tarde, passer à la sortie de répétition attribuée au formateur et consacrer le temps restant à l'interprétation.

## J1 — Faire changer la représentation avant de nommer ses avantages

### J1-A · Une paraphrase est-elle retrouvée par les mots ?

**Cellule source :** [TP01 — TF-IDF, `455e827b2edc`](../notebooks/etudiants/01_j1_textes_recherche.ipynb#cell-id=455e827b2edc). Section réelle : **« 2. Une baseline que l’on comprend : TF-IDF »**. Début : `from sklearn.feature_extraction.text import TfidfVectorizer`.

- **Préparation :** exécuter les cellules d'installation et d'initialisation du TP01, puis les données `7827739c78bb`. On dispose de douze fiches FAQ, huit requêtes de validation et six requêtes finales. Garder les requêtes finales hors projection.
- **Question de prédiction :** « La demande “Il me faut une pièce pour ma comptabilité” retrouvera-t-elle la facture, même sans employer le mot facture ? Quel terme pourrait aider ? » Faire écrire une fiche attendue avant le clic.
- **Manipulation :** exécuter la cellule avec sa requête initiale. Lire le tableau des termes pondérés et les trois fiches classées. Remplacer uniquement `query` par une formulation contenant explicitement « facture », relancer le classement puis revenir à la formulation indirecte. Conserver l'index et `NGRAM_RANGE` inchangés dans cette microdémo.
- **Observation attendue :** le classement dépend des termes connus qui se recouvrent entre question et fiches. Il peut changer, ou rester identique pour une raison à expliquer. Aucun score de réussite n'est annoncé à l'avance. Un bon résultat lexical ne prouve pas une compréhension générale des paraphrases.
- **Retour au schéma :** montrer texte → vocabulaire TF-IDF → vecteur de requête → cosinus avec les fiches. Relier le terme partagé à une colonne de la matrice. Le score est une similarité, pas la probabilité que la fiche résolve le problème.
- **Vérification :** « Si aucun terme de la requête n'est dans le vocabulaire, que peuvent devenir les scores ? » Ils peuvent tous être nuls ; le départage ne constitue alors pas une preuve de pertinence.
- **Remédiation :** afficher deux termes et deux fiches seulement, puis calculer quel vecteur possède une coordonnée commune. Reporter la comparaison d'embeddings à l'après-midi.

### J1-B · Agrandir le vocabulaire supprime-t-il tous les inconnus ?

**Cellule source :** [TP01 — BPE, `c324f191cf80`](../notebooks/etudiants/01_j1_textes_recherche.ipynb#cell-id=c324f191cf80). Section réelle : **« 3. Construire un petit tokenizer BPE »**. Début : `from tokenizers import Tokenizer, models, trainers, pre_tokenizers`.

- **Préparation :** mêmes données `docs` que J1-A ; aucun tokenizer distant ni poids de modèle. La cellule entraîne deux petits BPE sur les fiches, avec tailles cibles 120 et 240.
- **Question de prédiction :** « Quel texte aura le plus de morceaux : “réinitialisation du mot de passe” ou “coliiiiis 😅” ? Doubler la taille cible suffit-il pour connaître l'emoji ? »
- **Manipulation :** exécuter la boucle existante sur les quatre phrases. Comparer, pour une même phrase, les colonnes `vocab`, `tokens`, `nombre` et `inconnus`. Faire choisir une variation orthographique et remplacer une entrée de `phrases`, sans changer les textes d'apprentissage.
- **Observation attendue :** certains découpages et nombres de morceaux peuvent changer. La taille réellement obtenue peut être inférieure à la taille demandée. Un caractère absent du corpus peut rester inconnu malgré un vocabulaire cible plus grand. Les sorties visibles tranchent la prédiction.
- **Retour au schéma :** distinguer l'apprentissage des fusions, la tokenisation d'un texte et les identifiants obtenus. Une pièce plus longue n'est pas une unité de sens garantie.
- **Vérification :** « Peut-on mettre ce nouveau tokenizer à la place de celui de DistilBERT ? » Non : les IDs ne correspondent plus nécessairement aux lignes de sa table d'embeddings.
- **Remédiation :** reprendre la fusion manuelle du support, puis suivre une seule ligne de `bpe_rows`. Ne pas introduire un troisième algorithme de tokenisation pour résoudre une confusion entre token et ID.

### J1 après-midi · Produire une décision de recherche

**Minimum à réussir :** expliquer le rôle des fiches et des requêtes, exécuter TF-IDF et le BPE, mesurer une recherche sur validation, choisir une configuration avant le test final, montrer deux erreurs et exporter `resultats/j1_resultats.json`. Le parcours complet compare aussi les embeddings multilingues ; s'ils ne sont pas exécutés, leur mesure reste absente et la limite est déclarée.

| Défi | Hypothèse et manipulation dans le code existant | Interprétation et production |
|---|---|---|
| 1 — Vérifier | Dans `455e827b2edc`, comparer `NGRAM_RANGE = (1,1)` et `(1,2)` ; relancer `0f6f18a254e0` sur les **mêmes** `dev_queries`. | Garder une ligne par configuration avant de relancer, car la cellule réinitialise `experiments`. Lire Recall@1, Recall@3, MRR et un classement, sans exiger que les bigrammes gagnent. |
| 2 — Expliquer | Dans `c324f191cf80`, conserver les deux tailles 120/240 et les mêmes phrases ; isoler l'effet d'une faute ou d'un caractère absent. | Montrer deux découpages, leurs inconnus et une explication. Une diminution de longueur n'est pas un score de compréhension. |
| 3 — Décider | Utiliser `USE_PRETRAINED` dans `3c564f73ae3e`, puis lire la comparaison `252dd3b90ec0`. Figer `CHOSEN_METHOD` dans `5c2fdc58482c` avant d'ouvrir le test. | Comparer lexical et dense sur les mêmes huit requêtes, puis évaluer les six requêtes finales. La PCA est illustrative. Retenir une méthode, un cas favorable à l'autre et une limite. |

**Points de passage de 30 minutes — preuve à montrer, pas nombre de cellules exécutées :**

| Minute | Production du binôme |
|---:|---|
| 30 | Trois associations requête → fiche, avec une ambiguïté discutée |
| 60 | Les trois voisins d'une requête et les termes qui expliquent le classement |
| 90 | Deux configurations lexicales consignées sur la même validation |
| 120 | Deux découpages BPE et une unité inconnue expliquée, si présente |
| 150 | Premiers vecteurs et contrôle de norme, ou étape dense explicitement non exécutée |
| 180 | Tableau lexical/dense sur validation, ou comparaison lexicale documentée |
| 210 | Choix écrit **avant** le test ; deux erreurs prêtes à commenter |
| 240 | Notebook, JSON et recommandation limitée au petit corpus |

## J2 — Faire vérifier une propriété du calcul

### J2-A · Modifier le contenu change-t-il les poids ?

**Cellule source :** [TP02 — QKV, `ec071352786e`](../notebooks/etudiants/02_j2_attention_transformers.ipynb#cell-id=ec071352786e). Section réelle : **« 1. Q, K, V sans mystère »**. Début : `def softmax(x, axis=-1):`.

- **Préparation :** initialisation du TP02 ; aucun checkpoint n'est requis. Q et K ont quatre lignes et deux colonnes ; V a quatre lignes et trois colonnes. Les nombres sont construits pour l'exercice.
- **Question de prédiction :** « Si je change seulement les valeurs V, les poids qui comparent Q à K vont-ils changer ? Quelle sera la forme de la sortie ? »
- **Manipulation :** exécuter le calcul initial et lire les formes imprimées. Dans la copie de travail, changer une seule valeur de la matrice `V`, en conservant Q et K ; relancer. Comparer `weights` et `output` avant/après. La cellule calcule déjà les deux objets ; les afficher côte à côte si nécessaire.
- **Observation attendue :** les poids restent identiques puisque Q et K sont inchangés ; la sortie peut changer parce que le contenu pondéré change. Les assertions vérifient une sortie `(4,3)` et des sommes de lignes égales à un.
- **Retour au schéma :** suivre Q/K vers les scores et V vers la somme pondérée. Les quatre lignes correspondent aux quatre positions qui interrogent ; les trois colonnes de sortie proviennent de la dimension des valeurs.
- **Vérification :** « Pourquoi la sortie ne possède-t-elle pas deux colonnes comme Q ? » La combinaison transmet des valeurs de dimension trois ; les scores ne sont pas le contenu transmis.
- **Remédiation :** ne garder oralement qu'une requête et deux valeurs. Refaire une somme pondérée à la main, sans changer le code du modèle complet.

### J2-B · Le futur peut-il modifier le passé ?

**Cellule source :** [TP02 — causalité, `c983f20204b7`](../notebooks/etudiants/02_j2_attention_transformers.ipynb#cell-id=c983f20204b7). Section réelle : **« 2. Le test qui révèle la causalité »**. Début : `causal_output, causal_weights = attention(Q, K, V, causal=True)`.

- **Préparation :** restaurer et exécuter la cellule QKV initiale `ec071352786e`. Aucun GPU ni téléchargement n'est nécessaire.
- **Question de prédiction :** « On ajoute 100 à la dernière valeur, celle de demain. La première position doit-elle changer avec le masque ? Et sans masque ? »
- **Manipulation :** lire `V_changed[-1] += 100`, puis exécuter les comparaisons `changed_masked` et `changed_unmasked`. Montrer les deux matrices colorées et les assertions existantes. Faire pointer une case interdite avant de regarder la couleur.
- **Observation attendue :** les sorties des positions antérieures restent inchangées dans le cas causal ; la première sortie sans masque est modifiée. Les poids au-dessus de la diagonale sont nuls. Ce résultat teste une propriété du calcul jouet, pas la robustesse générale d'un LLM.
- **Retour au schéma :** lire ligne = position qui interroge, colonne = position lue. La diagonale est autorisée ; la sortie de la position courante sert à prédire le token suivant.
- **Vérification :** « Le masque de padding sert-il aussi à interdire le futur ? » Non : il écarte les positions artificielles de remplissage. La causalité concerne de vrais tokens futurs.
- **Remédiation :** dessiner une matrice 2 × 2 et cacher physiquement la case future. Refaire le même raisonnement avant de revenir aux quatre tokens.

### J2 après-midi · Construire une preuve, puis observer les modèles

**Minimum à réussir :** expliquer les formes et la somme des poids, faire passer le test causal, produire un contre-exemple sans masque, puis distinguer une complétion masquée d'une génération. Le parcours complet exécute DistilBERT et Qwen ; si ces chargements échouent, le calcul NumPy et ses conclusions restent exécutables et l'observation des modèles est marquée non réalisée.

| Défi | Hypothèse et manipulation dans le code existant | Interprétation et production |
|---|---|---|
| 1 — Vérifier | Modifier séparément une entrée de Q, K ou V dans `ec071352786e`, en restaurant l'état initial entre essais. | Trois prédictions écrites, matrices obtenues et explication de ce qui peut changer dans les poids ou la sortie. |
| 2 — Expliquer | Dans `05623b106886`, comparer `scaled=False/True` pour les dimensions 4, 64 et 256 déjà prévues. | Lire `entropie_moyenne` et relier la concentration des poids à la division par √dₖ. Ne pas transformer une expérience aléatoire courte en loi numérique exacte. |
| 3 — Décider | Dans `6d4bcf2839fb`, comparer les deux contextes du token masqué. Dans `f75cbe413776`, conserver les messages et comparer `temperature=None`, `0.3`, `1.0` ; utiliser ensuite `c0b574f9a82f`. | Tableau des sorties, format, invention éventuelle et réglages. `None` désigne ici greedy ; une température numérique active le sampling. Aucun réglage n'est déclaré plus vrai sans contrôle des faits. |

| Minute | Production du binôme |
|---:|---|
| 30 | Dimensions de Q, K, V et sortie prédites sur papier |
| 60 | Matrice de poids et contrôle de la somme de ses lignes |
| 90 | Test causal et explication d'un changement sans masque |
| 120 | Comparaison mise à l'échelle/sans mise à l'échelle, avec interprétation |
| 150 | Candidats du modèle masqué dans deux contextes, ou statut non exécuté |
| 180 | Prompt réellement rendu et première génération documentée |
| 210 | Variantes de décodage et au moins une limite précise |
| 240 | JSON exporté et explication orale encodeur/décodeur par les deux membres |

## J3 — Montrer ce que le batch et la métrique décident

### J3-A · La forme du batch dépend-elle du plus long texte ?

**Cellule source :** [TP03 — collator, `6cccc0122d87`](../notebooks/etudiants/03_j3_classification.ipynb#cell-id=6cccc0122d87). Section réelle : **« 2. Brancher les quatre pièces »**. Début : `collator = DataCollatorWithPadding(tokenizer)`.

- **Préparation :** initialisation et données `fb9a463ea005`, baseline `4a9ea3077938`, puis préparation du tokenizer/datasets `f6e398687c25` avec le tokenizer déjà en cache. **Sauter** la cellule d'entraînement `4c8fef34d3b9` ; `trainer` et `trained_model` sont initialisés à `None` dans la préparation. Aucun poids de modèle n'est chargé.
- **Question de prédiction :** « Deux messages de longueurs différentes entrent dans le collator : combien de lignes, combien de colonnes, combien de labels obtient-on ? »
- **Manipulation :** lire les longueurs de `train_ds[0]` et `train_ds[1]`, puis exécuter la cellule. Dans une copie de travail, remplacer seulement les deux indices par ceux de deux exemples de longueurs plus contrastées. Inspecter `example_batch['input_ids']` et `example_batch['attention_mask']` en plus de leurs formes.
- **Observation attendue :** deux lignes, une largeur fixée par le plus long exemple du batch et un label par message. Les positions de remplissage portent le masque approprié. Si les deux textes choisis ont finalement la même longueur, l'absence de padding est un résultat cohérent.
- **Retour au schéma :** suivre tokenizer → listes de longueurs variables → collator → tenseur rectangulaire → modèle. Distinguer ajout de padding et troncature déjà effectuée lors de la tokenisation.
- **Vérification :** « La classification doit-elle produire un label par case du tenseur ? » Non : ici `labels.shape == (2,)`. La NER utilise une cible par position supervisée.
- **Remédiation :** écrire deux listes de trois et cinq tokens sur papier ; ajouter seulement les places nécessaires pour obtenir deux lignes de cinq.

### J3-B · Un nom partiellement retrouvé est-il une entité exacte ?

**Cellule source :** [TP04 — F1 strict, `1d5ac67cbaa8`](../notebooks/etudiants/04_j3_ner.ipynb#cell-id=1d5ac67cbaa8). Section réelle : **« 3. Entraîner puis mesurer des entités entières »**. Début : `from seqeval.metrics import f1_score as entity_f1…`.

- **Préparation minimale :** prélever les imports `seqeval` et `IOB2`, puis le sous-bloc de `example_true = …` jusqu'aux deux premiers `print(...)`. Ne pas exécuter ici le bloc `true_test`, ni le chargement du modèle, ni `trainer.train()`. Ce calcul ne requiert ni données NER test, ni tokenizer, ni GPU.
- **Question de prédiction :** « La référence contient `B-PER, I-PER, O, B-LOC`. Si le deuxième label devient O, a-t-on encore retrouvé toute la personne ? »
- **Manipulation :** comparer `example_true` à lui-même, puis à `example_partial`. Modifier uniquement le type de la dernière entité dans une copie du tableau de prédiction et refaire le calcul strict. Ne pas changer la référence pour améliorer le score.
- **Observation attendue :** la prédiction identique reçoit le résultat parfait ; une frontière tronquée perd une entité exacte, et un type incorrect ne devient pas juste parce que les frontières correspondent. Lire les résultats réellement imprimés plutôt qu'annoncer une performance de modèle.
- **Retour au schéma :** relier mot → sous-tokens → cibles au schéma d'alignement, puis montrer que la métrique juge des segments reconstruits. La politique premier sous-token / `-100` s'inspecte dans `182416e4c78b` à l'après-midi.
- **Vérification :** « Pourquoi une accuracy par token pourrait-elle sembler bonne avec tout O ? » Beaucoup de positions ne portent aucune entité, tandis que le F1 d'entités exige de retrouver les segments.
- **Remédiation :** remplacer les labels par des surligneurs sur « Marie Dupont » et « Lyon », puis recompter entités exactes, manquées et prédites à tort.

### J3 après-midi · Garder l'alignement et les tâches séparés

**Minimum à réussir :** comparer une baseline et l'encodeur adapté sur le support lorsque le GPU est disponible ; inspecter un batch ; sauvegarder puis recharger `modele_classification.zip` ; réussir un alignement NER et expliquer la métrique stricte. L'extension Allociné change de tâche et produit un export séparé. Si un entraînement n'a pas été réalisé, le distinguer des calculs CPU réussis et conserver le protocole reproductible.

Le budget est **140 minutes classification = 100 minutes support + 40 minutes Allociné**, puis **100 minutes NER**. Les défis s'insèrent dans ces blocs ; ils ne demandent pas une seconde journée d'entraînement.

| Défi | Hypothèse et manipulation dans le code existant | Interprétation et production |
|---|---|---|
| 1 — Vérifier les données | Exécuter le contre-exemple de séparation naïve `0c2946f8e4d0`, puis comparer aux groupes de `fb9a463ea005`. Le split naïf reste une démonstration, jamais le protocole retenu. | Montrer l'intersection des scénarios et expliquer quel type de nouveauté chaque séparation mesure. Ne pas attribuer un score à une expérience qui n'a pas été entraînée. |
| 2 — Expliquer les cibles | Dans TP04 `182416e4c78b`, lire `word_id` et `label_loss` ; remplacer l'exemple affiché par un autre `ner_rows[i]`. Puis relier à la métrique jouet `1d5ac67cbaa8`. | Tableau mot/sous-token/cible ; expliquer chaque `IGNORÉ`. Conserver la règle premier sous-token. Une modification exploratoire qui casse l'assertion doit être diagnostiquée avant tout entraînement. |
| 3 — Transférer et décider | Dans TP03 `37a2978849dc`, inspecter Allociné 1 000/200/200 ; dans `86ab1e2a61e3`, lire la proportion tronquée à 128, la baseline et l'adaptation de sentiment. | Comparer des méthodes sur la même tâche Allociné, sans comparer ce score au routage comme s'il s'agissait d'un benchmark commun. Préserver `modele_allocine.zip` séparément. Une variante de longueur demande une nouvelle expérience explicitement bornée, pas un réglage changé pendant le test. |

Pour une investigation supplémentaire sur le support, `EPOCHS` et `LEARNING_RATE` se trouvent dans `f6e398687c25` et `variant_log` dans `1e7c63e5a7f3`. Choisir un seul facteur, repartir du checkpoint initial et rester dans le budget des 100 minutes ; retirer cette variante si elle empêche l'analyse, l'export ou l'extension réelle.

| Minute | Production du binôme |
|---:|---|
| 30 | Labels, groupes disjoints et formes d'un batch |
| 60 | Configuration réelle, état de l'entraînement et métriques disponibles — pas une mesure inventée si le calcul continue |
| 90 | Comparaison support sur validation et prédictions de contrôle pour le rechargement |
| 120 | Changement de tâche Allociné expliqué ; tailles, labels et premiers exemples réels lus |
| 150 | Exports support/sentiment distingués ; première phrase NER annotée à la main |
| 180 | Alignement sous-tokens et `-100` validé par un autre binôme |
| 210 | Entraînement NER ou limitation explicitée ; frontière/type évalués sur le cas jouet |
| 240 | Archives disponibles, JSON de classification/NER et trois erreurs ou limites commentées |

## J4 — Rendre le signal d'apprentissage et la fidélité visibles

### J4-A · Une donnée mal formée devient-elle un mauvais apprentissage ?

**Cellule source principale :** [TP05 — audit, `40d2cd66a265`](../notebooks/etudiants/05_j4_sft_lora.ipynb#cell-id=40d2cd66a265). Section réelle : **« 1. Le contrat avant le GPU »**. Début : `import re, copy`.

- **Préparation :** exécuter l'initialisation et les données support/réponses `2ec691c1ae19`. Préparer aussi le tokenizer Qwen en cache si le rendu chat est montré. Aucun poids n'est requis.
- **Question de prédiction :** montrer les exemples ajoutés à `raw_examples` et demander lesquels seront rejetés : doublon, texte blanc, réponse vide, adresse électronique. Faire justifier la règle, pas seulement deviner le nombre de lignes restantes.
- **Manipulation :** exécuter `audit_and_clean` puis lire `audit`. Dans la copie de travail, ajouter une variante du doublon qui change seulement espaces et casse ; vérifier ce que fait `normalized`. Montrer ensuite le rendu déjà préparé de `ca56aab1f5c4`, section **« 2. Le prompt est une entrée ; la réponse est la cible »** : `as_conversation` sépare prompt et completion, puis `apply_chat_template` affiche les rôles.
- **Observation attendue :** les rejets portent des raisons distinctes ; une variation d'espaces/casse reste un doublon après normalisation. Le rendu chat expose les marqueurs réellement attendus. Ni la regex ni la déduplication exacte ne garantissent une curation complète ; des paraphrases et des informations sensibles non reconnues peuvent rester.
- **Retour au schéma :** relier exemples → audit → groupes/partitions → template → tokens. Repérer consigne/question dans le prompt et réponse dans la completion ; il n'y a encore aucun apprentissage.
- **Vérification :** « Retirer le prompt de la loss signifie-t-il le retirer de l'entrée ? » Non. Le modèle doit le lire pour produire la réponse ; la supervision est une autre décision.
- **Remédiation :** afficher une seule paire et colorier les trois rôles. Réserver l'inspection réelle des labels de `0fbe86886db7` à l'après-midi ou à une sortie formateur attribuée ; cette cellule complète démarre ensuite l'entraînement.

### J4-B · Peut-on avoir des mots proches et un fait contraire ?

**Cellule source :** [TP06 — ROUGE-L, `30e4dc922ff5`](../notebooks/etudiants/06_j4_resume_evaluation.ipynb#cell-id=30e4dc922ff5). Section réelle : **« 4. ROUGE-L ne juge pas la vérité »**. Début : `from rouge_score import rouge_scorer`.

- **Préparation minimale :** importer `re` et `pandas` dans la session. Prélever le début de la cellule, de l'import ROUGE jusqu'à la création de `scorer`, puis le sous-bloc `reference = …`, `candidates = …` et le tableau qui les compare. **Ne pas** exécuter les boucles sur `test_cases`, `human_grid` ou l'export pendant cette microdémo ; aucun texte test n'est ouvert et aucun poids n'est chargé.
- **Question de prédiction :** « La phrase “Le remboursement de la commande est confirmé” est-elle un bon résumé de “Le remboursement de la commande n'est pas confirmé” ? Leurs mots resteront-ils proches ? »
- **Manipulation :** exécuter les deux candidats déjà présents. Faire surligner les mots communs, puis le fragment qui inverse le statut. Garder la référence constante.
- **Observation attendue :** le candidat contradictoire peut conserver un recouvrement lexical important malgré un fait inversé. Le score affiché est celui de ces deux phrases construites, pas celui du modèle entraîné. La tokenisation française du notebook conserve les caractères Unicode et désactive le stemming anglais.
- **Retour au schéma :** relier résumé à deux voies d'évaluation : recouvrement lexical d'un côté, preuves dans la source de l'autre. Le joli texte et le score ne remplacent pas la vérification du remboursement.
- **Vérification :** « Une paraphrase fidèle mais avec d'autres mots peut-elle recevoir un score plus faible ? » Oui ; une référence unique ne représente pas toutes les formulations correctes.
- **Remédiation :** faire remplir seulement deux cases : affirmation du résumé / passage source qui la soutient. L'absence de preuve se discute avant tout agrégat de métriques.

### J4 après-midi · Deux adaptations, deux comparaisons réelles

**Minimum à réussir :** auditer les exemples et le template ; inspecter les cibles du batch réel avant l'entraînement ; comparer modèle initial et LoRA sur les mêmes demandes réservées ; pour le résumé, distinguer extractif, initial et adaptateur spécifique. Les deux expériences GPU prévues restent dans les **160 minutes SFT support + 80 minutes résumé**. En cas d'indisponibilité, les audits et métriques jouets sont exécutables sur CPU, mais aucune sortie adaptée ni compétence d'exécution GPU n'est déclarée acquise sans exécution.

| Défi | Hypothèse et manipulation dans le code existant | Interprétation et production |
|---|---|---|
| 1 — Améliorer le matériau | Dans `40d2cd66a265`, ajouter un défaut contrôlé aux exemples d'audit, sans modifier le test métier ; lire la décision et ses limites. Dans `ca56aab1f5c4`, inspecter les rôles et les longueurs. | Une fiche « défaut → règle → exemple conservé/rejeté → limite ». Vérifier qu'une réponse utile ne promet pas une action non effectuée. |
| 2 — Vérifier ce qui apprend | Dans `e98deaaa20de`, lire `RANK`, `MAX_STEPS`, `USE_QLORA` et les paramètres entraînables. Dans `0fbe86886db7`, lire `PROMPT IGNORÉ`, `CIBLE APPRISE` et le tableau `appris` **avant** la ligne `trainer.train()`. | Relier les positions `-100` au masque de loss et le nombre de paramètres à LoRA. L'inspection du batch requiert ici le modèle préparé ; elle n'est pas présentée comme une microdémo CPU autonome. |
| 3 — Mesurer l'effet de l'adaptation | Support : `answer_question(..., disable_adapter=True)` dans `bb510004415a` contre adaptateur actif dans `0f66ac37a688`. Résumé : `summarize(..., initial=True)` contre adaptation dédiée, dans TP06 `de9ec3b597e9`, puis `265988e82617` après gel du choix. | Ablation « même base avec/sans adaptateur », prompt/décodage constants. Montrer gain, régression ou résultat indécidable avec preuves. TP06 : 16 train, 2 validation, 4 test et 12 pas prévus ; ne pas réutiliser l'adaptateur support comme s'il avait appris à résumer. |

Ne pas relancer `0f66ac37a688` pendant une recherche de réglages : cette cellule contient aussi la première lecture du test support. Pour une investigation sur validation, isoler son premier bloc avant `final_test = []`, conserver les essais et n'ouvrir le bloc final qu'une fois le choix figé. Même discipline pour les quatre tests du TP06. Un changement de rang ou de quantification est une extension qui remplace une autre investigation si le budget le permet, pas une obligation supplémentaire.

| Minute | Production du binôme |
|---:|---|
| 30 | Tableau de rejets de curation et une limite de la règle |
| 60 | Rendu chat, longueurs et calcul des paramètres LoRA |
| 90 | Exemple de cible réellement supervisée ; matériel et budget réels |
| 120 | Trace d'entraînement disponible et lecture des sorties de validation |
| 150 | Comparaison support, limites et archive `adaptateur_lora.zip` en préparation |
| 180 | Jeu de résumé 16/2/4 identifié, faits à conserver et baseline extractive |
| 210 | État des 12 pas de résumé et observations sur les deux cas de validation |
| 240 | Comparaison finale des méthodes exécutées, grille factuelle et `adaptateur_resume.zip` si entraîné |

## J5 — Faire défendre une comparaison et un contrat d'usage

### J5-A · Un seul facteur change, les exemples restent les mêmes

**Cellule source :** [TP07 — baseline commune, `3ee680618067`](../notebooks/etudiants/07_j5_projet.ipynb#cell-id=3ee680618067). Section réelle : **« 1. Contrat du mini-projet »**. Début : `from sklearn.pipeline import make_pipeline`.

- **Préparation :** initialisation, données `e14f0b7c5ada` et contrat `700239142b32`. Ne pas ouvrir `CHALLENGE` dans `6e58371ddca3` : les vingt nouveaux scénarios du test J5 restent réservés à l'après-midi après sélection.
- **Question de prédiction :** « Ajouter des bigrammes peut-il aider certaines expressions et en rendre d'autres plus rares ? Si le score ne bouge pas, peut-on néanmoins observer des erreurs différentes ? »
- **Manipulation :** noter l'hypothèse dans `project_contract`. Dans la cellule de baseline, comparer `ngram_range=(1,1)` à `(1,2)` en conservant `C=2.0`, `SEED`, train et `val_df` identiques. Consigner chaque valeur de validation avant relance ; inspecter `val_pred_baseline` face aux labels et textes de `val_df` pour expliquer un cas.
- **Observation attendue :** le résultat peut progresser, régresser ou rester identique. Seule la comparaison observée autorise une conclusion. Un score inchangé peut cacher des cas différents, ou réellement les mêmes décisions.
- **Retour au schéma :** les deux branches reçoivent les mêmes données et rejoignent la même métrique. La différence porte sur la représentation, pas sur la tâche ni le test. Les choix se font sur validation.
- **Vérification :** « Peut-on choisir le réglage qui marche le mieux sur le défi J5 après l'avoir regardé ? » Il deviendrait un jeu de développement ; on perdrait l'évaluation indépendante annoncée.
- **Remédiation :** afficher deux lignes de validation, leurs labels et les deux prédictions ; raisonner sur ces cas avant de revenir au macro-F1.

### J5-B · La fonction fait-elle ce que l'interface promet ?

**Cellule source :** [TP07 — contrat d'entrée, `e7f6543e18ee`](../notebooks/etudiants/07_j5_projet.ipynb#cell-id=e7f6543e18ee). Section réelle : **« 5. Démontrer un comportement utile »**. Début : `import gradio as gr`.

- **Préparation minimale :** baseline de J5-A disponible, `id2label` défini et `trained_model = None` pour ce parcours CPU. Garder `LAUNCH_DEMO = False`. La fonction utilise `choices[0]`, donc la baseline ; elle ne charge ni modèle adapté ni LLM. Installer Gradio avant la séance. Aucun serveur ni lien public n'est nécessaire.
- **Question de prédiction :** « Une entrée contenant seulement des espaces est-elle un message valide ? Où doit s'arrêter le traitement d'un texte de 2 001 caractères ? »
- **Manipulation :** appeler la fonction existante sur son message normal, sur `" "` et sur `"a" * 2001`, avec la même méthode. Lire les assertions déjà présentes et rendre visibles les chaînes retournées. Tester ensuite une demande ambiguë et lire l'avertissement de validation humaine.
- **Observation attendue :** l'entrée blanche produit une invitation à saisir ; l'entrée trop longue un message de limite ; une entrée acceptée retourne une catégorie et le statut de prototype. La baseline n'effectue aucune action sur une commande réelle.
- **Retour au schéma :** texte → contrôles d'entrée → inférence → post-traitement → affichage. Les rejets d'entrée doivent arriver avant la prédiction, et le modèle est réutilisé plutôt que rechargé à chaque clic.
- **Vérification :** « Une entrée hors domaine courte sera-t-elle automatiquement rejetée ? » Non : le classifieur à cinq classes peut encore choisir une catégorie. Le texte d'interface ne constitue pas un détecteur hors domaine.
- **Remédiation :** faire nommer trois sorties distinctes — erreur d'entrée, prédiction, limite d'usage — puis rejouer un seul exemple de chaque catégorie.

### J5 après-midi · Livrer une décision vérifiable

**Minimum à réussir :** protocole écrit, baseline exécutée, modèle support du J3 rechargé si disponible, comparaison commune, cinq erreurs ou cas limites analysés, démo contrôlée, documentation et exports. Le zéro-shot local est évalué lorsqu'il est exécutable ; ses sorties invalides sont comptées. Le classifieur Allociné ne remplace jamais le routeur support. Appliquer le [barème du projet](../evaluation/PROJET.md), qui prévoit explicitement comment documenter une indisponibilité matérielle sans inventer de résultat.

| Défi | Hypothèse et manipulation dans le code existant | Interprétation et production |
|---|---|---|
| 1 — Fixer le contrat | Compléter `project_contract` dans `700239142b32`, comparer les baselines sur validation puis vérifier la relecture J3 dans `c1afa8e5e760`. | Même tâche, labels, données et métrique. Une tête nouvellement initialisée n'est pas une baseline zéro-shot pertinente. |
| 2 — Traiter les sorties | Dans `c173e4de9ec1`, inspecter `ZERO_PROMPT`, le décodage glouton et la règle `canonical` → `label2id.get(..., -1)`. Sur CPU, examiner seulement ce sous-bloc avec des chaînes jouets annoncées comme telles ; sur GPU, lire les sorties réelles de validation. | Distinguer ponctuation tolérée, label valide et texte invalide. Ne pas choisir à la main un label dans une réponse ambiguë. Valider aussi les entrées limites de `classify_demo`. |
| 3 — Décider avec les erreurs | Après gel des choix, exécuter `6e58371ddca3` sur les vingt nouveaux scénarios, puis compléter les cinq lignes `error_analysis` et `decision` dans `5be5c869e87a`. Si l'encodeur est disponible, lire le bootstrap apparié déjà fourni. | Tableau commun, coût, sorties invalides, cinq erreurs et décision proportionnée. L'intervalle éventuel ne rend pas un corpus fictif représentatif ; une absence de gain est une conclusion recevable. |

Le travail garde le budget du sujet : **75 min cadrage/relecture/baselines ; 75 min comparaison puis test et erreurs ; 40 min démo/documentation ; 40 min soutenances ; 10 min sauvegarde**. Pour plus de huit binômes, utiliser la galerie déjà prévue, sans ajouter des passages hors horaire. La publication privée reste optionnelle ; `PUBLISH_PRIVATE = False` ne doit pas être modifié pour obtenir une bonne note.

| Minute | Production du binôme |
|---:|---|
| 30 | Contrat rempli et identification de l'archive J3 ou de son absence |
| 60 | Baseline et premiers résultats de validation, avec hypothèse de comparaison |
| 90 | Modèles effectivement disponibles et sorties comparables sur validation |
| 120 | Choix figés, règle de parsing et décision d'ouvrir le test documentés |
| 150 | Tableau du défi commun et cinq erreurs/cas limites analysés |
| 180 | Fonction de démo testée, model card et recommandation rédigées |
| 210 | Soutenances en cours ; chaque membre explique une décision |
| 240 | Remise complète et phrase individuelle : « ma preuve est…, ma limite est… » |

## Règle commune de conduite des TP

À chaque changement de rôle, l'analyste montre **une hypothèse, une sortie et une décision**. Le pilote ne passe pas à l'expérience suivante tant que son partenaire ne sait pas expliquer l'objet observé. Un binôme avancé réalise le défi suivant ; un binôme en difficulté réduit l'exemple avec la remédiation indiquée, sans sauter l'analyse pour lancer un calcul plus grand.

Les tableaux de passage sont des points d'observation inclus dans le temps, pas huit présentations collectives supplémentaires. Le formateur circule, demande une preuve à l'écran ou sur papier et relève les blocages partagés. Si un calcul GPU continue, les étudiants annotent des erreurs, auditent les cibles ou préparent leur grille ; une barre de progression ne constitue pas à elle seule un travail pratique.

Ce guide a été relié aux identifiants des cellules de l'édition livrée. Après toute régénération qui réordonne ou insère des cellules, vérifier à nouveau les ancres et les titres de section. Les assertions CPU et les références de cellules valides ne remplacent pas la répétition générale dans [Colab](COLAB.md) ou, si fourni, [Runpod L4](RUNPOD_OPTION.md).
