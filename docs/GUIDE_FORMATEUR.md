# Guide d'animation — NLP Avancé (BERT, GPT, Hugging Face)

**Chrys NIONGOLO · 35 heures · 15 heures de théorie active et 20 heures de pratique.**

Ce guide organise la classe et les remédiations. Les explications détaillées par diapositive se trouvent dans les notes du PowerPoint et dans `output/Notes-presentateur.md`. Le [programme](PROGRAMME_35H.md) fixe les durées ; il n'est pas nécessaire de projeter chaque slide au même rythme.

Pour préparer les manipulations à projeter, ouvrir le [fil conducteur pratique](FIL_CONDUCTEUR_PRATIQUE.md) : dix microdémonstrations pointent vers les sections et identifiants des cellules existantes, avec prédiction, geste à effectuer, explication et remédiation. Les défis de l'après-midi et les points de passage de trente minutes transforment les exécutions en preuves de compréhension, sans ajouter de temps aux 35 heures. Ce document contient des réponses et reste réservé au formateur ; les étudiants utilisent leur notebook sans corrigé.

Les trois objectifs sont : **comprendre le traitement du langage naturel et les représentations vectorielles (embeddings) ; mettre en œuvre des modèles pré-entraînés (BERT, GPT) via Hugging Face ; fine-tuner des LLMs sur des tâches métier (classification, NER, résumé).** Le programme relie chaque objectif aux notebooks et aux preuves attendues. Expliquer que DistilBERT représente le côté encodeur et que Qwen illustre le côté décodeur causal : on enseigne la famille GPT sans prétendre charger un modèle propriétaire OpenAI.

Si un accès individuel [Runpod L4](RUNPOD_OPTION.md) est fourni, conserver les mêmes données, scripts et critères. Sa mémoire supplémentaire permet une expérience de budget, pas un changement silencieux du niveau d'exigence. Répéter les notebooks dans cet environnement avant la séance ; une validation Colab n'est pas automatiquement une validation Runpod.

## Préparer une semaine qui se pratique

Le fil rouge est un support client fictif. Réutiliser les mots « demande », « catégorie », « entité », « réponse » et « résumé » toute la semaine, mais faire préciser la sortie attendue : une catégorie n'est pas une réponse générée. Les petits corpus sont conçus pour comprendre une opération et son évaluation ; annoncer cette limite avant le premier score.

Chaque explication suit quatre étapes : **un problème concret → une prédiction de l'étudiant → un calcul ou une exécution → une interprétation**. Par exemple, avant de montrer un embedding, demander si « Je n'ai toujours rien reçu » doit retrouver « Où est mon colis ? ». Faire prédire le voisin lexical, puis le voisin dense. Le contre-exemple rend utile la notion de représentation.

Avant la semaine, effectuer la répétition générale du [guide Colab](COLAB.md), enregistrer les sorties réelles et préparer un exemple de résultat décevant. Ne pas promettre une amélioration à chaque fine-tuning. Les résultats réels de la répétition, s'ils sont conservés, doivent porter leurs versions, date, GPU et statut « démonstration formateur ».

## Installer un cadre de travail clair

Les étudiants travaillent en binômes : le **pilote** manipule, l'**analyste** prédit les sorties et tient le journal. Inverser toutes les trente minutes. Lors d'une restitution, interroger d'abord l'analyste du dernier segment ; chacun doit pouvoir expliquer une cellule sans regarder le corrigé.

Au tableau, conserver trois colonnes : « hypothèse », « observation », « décision ». Une bonne observation n'est pas « cela fonctionne », mais « sur ces douze requêtes de validation, deux paraphrases changent de voisin ; la négation reste un échec ». Demander de citer le nombre d'exemples plutôt qu'un pourcentage isolé.

Pendant un calcul, laisser une minute silencieuse avant l'échange. Pour les blocs de vingt minutes, viser douze minutes d'explication, cinq de travail actif et trois de correction. Si plus d'un tiers du groupe ne peut expliquer la sortie, reprendre un exemple plus petit avant d'introduire une nouvelle API. Les seuils servent l'animation, pas la notation.

## Questions de diagnostic — réparties dans les activités du J1

Utiliser ces questions au fil de l'accueil, de l'introduction et des rappels concernés ; elles ne forment pas un créneau supplémentaire. Le diagnostic de deux minutes à la fin de l'introduction vérifie les familles de représentations ; le quiz de fin de matinée reprend les prérequis encore fragiles.

| Question courte | Attendu | Si difficulté |
|---|---|---|
| Une demande client donne-t-elle forcément une seule étiquette ? | La règle de tâche doit décider des cas multi-intentions | Annoter trois demandes ensemble |
| Pourquoi ne pas choisir les paramètres sur le test ? | Il perd son indépendance par rapport à la sélection | Dessiner trois boîtes de données |
| Dimensions de (4 × 3) multiplié par (3 × 2) ? | 4 × 2 | Faire correspondre deux lignes et colonnes |
| Que représente la loss ? | Un objectif d'optimisation défini, pas toute la qualité métier | Comparer deux erreurs de même poids mais de coûts différents |
| Un réseau peut-il recevoir une chaîne Python directement ? | Une représentation/tokenisation est nécessaire | Montrer texte → IDs → tenseur |
| Qu'enregistre-t-on pour rejouer une expérience ? | Données/splits, modèle, versions, paramètres, seed, matériel | Fournir un exemple de journal à compléter |

Les bases de machine learning et de deep learning ont été travaillées dans les cours voisins. Faire des rappels ciblés, sans répéter une semaine de théorie. Un niveau M2 justifie de lire les dimensions et les hypothèses ; il ne justifie pas de laisser une formule sans exemple.

## Jour 1 — Faire sentir la différence entre mot, token et vecteur

**Démarrer par les repères, avant les formules.** Après cinq minutes d'accueil, les huit nouvelles diapositives occupent 45 minutes. Faire nommer les objets et lire les exemples avant de présenter les méthodes. Pour TF-IDF, distinguer les contributions de Luhn, Spärck Jones et Salton ; pour Word2Vec, lire CBOW puis Skip-gram ; pour GloVe/fastText, comparer l'information apprise ; pour ELMo/BERT, expliquer ce que le contexte change. Les [sources historiques](SOURCES_INTRO_NLP.md) précisent chercheurs, équipes et dates de prépublication/publication. Les dates situent les idées, elles ne constituent pas un objectif de mémorisation. Les notes de chaque diapositive donnent un déroulé, une question, une réponse et une remédiation.

Commencer avec « Le colis est arrivé » et « Le colis n'est pas arrivé ». Demander la conséquence métier d'effacer la négation. On peut simplifier la ponctuation selon la tâche, mais aucune recette de nettoyage n'est universelle. La casse peut porter de l'information pour des noms propres ; les emojis peuvent porter le sentiment. Faire écrire ce que chaque transformation retire.

Pour TF-IDF, imaginer un index de bibliothèque : un terme présent partout distingue peu de documents. L'analogie ne suffit pas pour expliquer la formule ; calculer un exemple à trois documents, puis montrer que les variantes de lissage produisent des nombres différents. Dans le TP, le vocabulaire et l'IDF se calculent sur le corpus autorisé par le protocole, jamais sur le test de classification.

Pour le cosinus, utiliser deux flèches : `(1, 1)` et `(1, 0)` ont un cosinus d'environ `0,707`. Multiplier une flèche par dix ne change pas l'angle. La similarité ne représente ni une probabilité de vérité ni une preuve que les phrases ont le même sens. Une négation peut rester proche de la phrase affirmative.

Pour le tokenizer, utiliser l'analogie d'un dictionnaire de pièces : l'ID est l'adresse d'une pièce, pas son importance. Un vocabulaire personnalisé peut segmenter mieux un domaine ; ses IDs ne correspondent plus forcément aux lignes d'embedding d'un modèle déjà entraîné. L'entraîner au J1 sert à comprendre le mécanisme. Le brancher tel quel sur DistilBERT ne constitue pas un fine-tuning valide.

**Contrôle avant TP :** chaque binôme explique une fuite par paraphrase et prévoit un cas où la recherche lexicale sera utile, par exemple un numéro de commande exact. **Arrêt utile :** si les scores d'embeddings sont difficiles à interpréter, afficher trois voisins et les lire, sans ajouter un nouveau modèle.

## Jour 2 — Enseigner l'attention avec des dimensions visibles

Présenter Q comme ce qu'une position cherche, K comme ce à quoi elle peut correspondre et V comme l'information à mélanger. Ce sont des projections apprises de vecteurs, pas trois colonnes de mots annotées à la main. L'analogie du catalogue explique la sélection ; le calcul explique le mélange.

Partir d'une query et de deux keys. Si les scores sont `0` et `ln(3)`, le softmax donne `1/4` et `3/4`. Avec les valeurs `2` et `10`, la sortie est `8`. Demander ensuite si l'attention « choisit seulement 10 » : non, elle produit ici une moyenne pondérée. Ajouter les dimensions avant de passer à quatre positions.

Pour une self-attention à quatre tokens et dimension de tête deux : Q et K ont la forme `4 × 2`, les scores `4 × 4` et les poids aussi. Le facteur de normalisation utilise `sqrt(d_k)`, donc `sqrt(2)` ici. Avec plusieurs têtes, `d_k` est la dimension **par tête**. Le masque de padding ignore des positions artificielles ; le masque causal interdit l'accès aux positions futures. Les deux répondent à des problèmes différents.

Faire dessiner les masques avant le code. Au temps trois, le modèle causal peut regarder les positions un, deux et trois ; la cible correspond au token suivant. Modifier un token futur ne doit pas changer une sortie passée lorsque les autres conditions sont identiques. Cette observation est une preuve concrète de causalité dans le petit exemple, pas une évaluation complète d'un LLM.

Pour les architectures, partir de la sortie : un label global, un label par token ou une suite de tokens à produire. BERT représente un contexte bidirectionnel pour les tâches d'encodage ; un GPT génère avec attention causale ; l'encodeur-décodeur relie une entrée complète à une sortie. Certaines tâches peuvent être réalisées par plusieurs familles : on discute alors coût, qualité et protocole.

**Contrôle avant TP :** un étudiant indique les dimensions, l'autre prédit les cases masquées. **Piège à anticiper :** la température modifie une distribution utilisée pour l'échantillonnage ; avec une sélection purement greedy, changer une température positive ne change pas l'argmax, hors détails numériques.

## Jour 3 — Séparer comprendre le pipeline et optimiser les scores

Dessiner la chaîne du notebook : `Dataset → tokenizer → collator → modèle → loss → gradients → mise à jour`. Demander ce qui est appris et ce qui est seulement une transformation. `Trainer` orchestre cette chaîne ; il ne garantit ni de bons labels, ni de bons splits, ni une métrique pertinente.

Lors du chargement d'un encodeur pour une nouvelle classification, expliquer l'initialisation de la tête. Un avertissement de poids nouvellement initialisés est attendu dans ce contexte. Il ne faut ni cacher tous les avertissements, ni prendre chaque avertissement pour une panne. Vérifier le nombre de labels et leur correspondance.

Un exemple de métrique : six vrais positifs, deux faux positifs et quatre faux négatifs donnent précision `6/8`, rappel `6/10` et F1 `12/18`. Demander pourquoi on ne moyenne pas directement précision et rappel. Pour une classification multiclasse, le macro-F1 calcule un F1 par classe puis en fait la moyenne ; rappeler les effectifs et les classes absentes éventuelles.

Pour NER, écrire les mots, puis leurs sous-tokens sur une deuxième ligne, puis les labels sur une troisième. Si « Niongolo » est découpé en plusieurs morceaux, choisir une politique d'alignement cohérente. Le parcours peut superviser le premier sous-token et ignorer les suivants avec `-100`. Ce nombre indique « ne pas inclure dans la loss », pas « ce token n'existe pas ». Le masque d'attention et le masque de loss sont distincts.

Au niveau des entités, prédire seulement « Paris » quand la référence est « Paris Gare de Lyon » ne constitue pas une entité exacte correcte. Une accuracy élevée sur la classe `O` peut masquer une mauvaise extraction. Faire lire des erreurs de frontière et de type avant de chercher un nouvel hyperparamètre.

Le transfert sur Allociné apporte de vrais avis français, des formulations plus longues et de l'ambiguïté. Faire identifier le changement de tâche : sentiment d'un avis de film et intention d'un client ne sont pas interchangeables. Utiliser les 1 000/200/200 exemples du parcours en conservant les partitions d'origine. Les scores du sous-ensemble ne sont pas ceux du benchmark complet. Son export `modele_allocine.zip` reste distinct du modèle support ; le projet principal J5 reprend le support.

**Contrôle avant fin J3 :** télécharger `modele_classification.zip`, puis vérifier sa relecture et des prédictions identiques. **Si le GPU manque :** réussir l'annotation, l'alignement, les métriques et la baseline CPU ; déclarer explicitement que le fine-tuning n'a pas été exécuté. Un résultat de démonstration fourni par le formateur conserve cette attribution.

## Jour 4 — Rendre SFT et LoRA tangibles

Le préentraînement apprend à prédire dans de nombreux textes ; le SFT adapte à des réponses attendues sur des exemples. Un modèle « Instruct » a déjà subi une adaptation : le comparer avant/après notre TP mesure une adaptation supplémentaire. Ce n'est pas une comparaison entre modèle brut et chatbot entièrement construit par les étudiants.

Faire auditer un exemple contenant une réponse assurée mais non justifiée : « Votre remboursement aura lieu demain ». Si la source ne donne aucun délai, la réponse cible enseigne une invention. Une meilleure cible explique ce qui est connu et ce qui manque. La curation agit sur le comportement appris, pas seulement sur le format JSON.

Présenter LoRA comme une correction structurée d'une matrice figée. Pour une matrice `1024 × 1024`, une correction de rang huit utilise `1024 × 8 + 8 × 1024 = 16 384` paramètres au lieu de `1 048 576`. Ce rapport de 64 porte sur cette mise à jour de matrice, pas sur toute la mémoire GPU ni sur la durée. Les activations, gradients, états d'optimiseur et tokens restent à compter.

Pour QLoRA, distinguer le stockage quantifié des poids de base et le calcul utilisé pendant le passage avant/arrière. Les adaptateurs sont entraînables ; les poids de base restent figés dans le parcours. Sur la T4 visée, suivre la configuration FP16 du notebook et le contrôle de matériel ; ne pas recopier aveuglément une recette BF16 prévue pour un autre GPU. La quantification ne rend pas toutes les opérations ni tous les paramètres « quatre bits ».

Vérifier un exemple tokenisé avant l'entraînement : rôles, texte réellement rendu, cible et labels ignorés. Le template de chat fait partie du contrat du modèle. Un PAD qui partage l'ID d'EOS exige un masquage tenant compte des positions de padding ; masquer tous les tokens de cet ID peut supprimer aussi des EOS utiles.

Pour les résumés, donner une source très courte : « Colis annoncé mardi. Reçu jeudi. Emballage abîmé. Aucun remboursement confirmé. » Un résumé qui annonce un remboursement peut sembler fluide et partager beaucoup de mots avec la référence ; il reste infidèle. Les évaluateurs notent les affirmations étayées et les omissions, sans voir d'abord le nom du modèle.

Le TP06 réalise sa propre adaptation LoRA au résumé. Comparer le modèle initial et l'adaptateur de résumé sur les mêmes sources réservées, avec la baseline extractive et la grille humaine. Un adaptateur support du TP05 ne devient pas un adaptateur de résumé par changement de prompt. Les exports restent séparés : `adaptateur_lora.zip` pour le support, `adaptateur_resume.zip` pour le résumé.

**Contrôle avant entraînement :** afficher paramètres entraînables, dtype, longueur maximale et budget ; collecter la référence sur les prompts figés. **Si la loss descend mais pas la qualité :** conserver l'observation, vérifier le masquage et les données, puis distinguer surapprentissage, format et qualité linguistique. Ne pas modifier le test pour embellir le résultat.

## Jour 5 — Défendre une conclusion limitée par les preuves

Utiliser un tableau à une ligne par système et des colonnes communes : tâche, split, nombre d'exemples, métrique, latence mesurée, budget, erreurs. Un zero-shot génératif reçoit les mêmes labels autorisés et les mêmes entrées que le classifieur. Fixer le prompt sur validation. Une sortie hors format doit être comptée, pas supprimée du tableau.

La précision d'un temps mesuré dépend du matériel, de l'échauffement et de la longueur d'entrée/sortie. Chronométrer un petit ensemble commun, distinguer téléchargement/chargement et prédiction. Les mesures de ce TP ne sont pas des garanties de capacité d'un service.

Faire tester le prototype par un autre binôme avec texte vide, texte long, négation et cas ambigu. L'interface doit expliquer ce qu'elle prédit et ses limites. Une capture d'écran ne prouve pas un rechargement ; un rechargement ne prouve pas un service de production. Une démo Gradio est facultative si son lancement dans Colab exige un lien public non souhaité : le test de la fonction et les sorties notebook restent présentables.

Le [projet](../evaluation/PROJET.md) se termine dans les 240 minutes, avec une réutilisation du modèle J3 plutôt qu'un entraînement lancé au dernier moment. Jusqu'à huit groupes : cinq minutes par groupe. Au-delà : deux rotations de galerie, collecte des dossiers et vérification individuelle. Noter la justification et la traçabilité, sans classement au score.

## Objections et remédiations rapides

| Ce que dit l'étudiant | Réponse et action immédiate |
|---|---|
| « Pourquoi faire TF-IDF si les LLM existent ? » | Comparer sur un identifiant exact, le temps de chargement et le budget ; les résultats doivent décider de la pertinence |
| « Token 900 est plus proche de 901 que de 20. » | Permuter deux IDs et leurs lignes d'embedding ; les IDs ne portent pas de métrique sémantique |
| « Une attention forte explique la décision. » | Modifier la phrase et observer ; des poids d'attention ne sont pas à eux seuls une attribution causale |
| « Plus d'epochs donne forcément mieux. » | Relire la courbe de validation et une erreur nouvelle |
| « Le modèle a 95 %, c'est prêt. » | Demander le dénominateur, le split, les classes, les erreurs et la population réelle |
| « LoRA apprend toute la connaissance du domaine. » | Rechercher un fait absent des exemples ; distinguer apprentissage de comportement et source de vérité |
| « Quantifié signifie moins intelligent. » | Proposer une mesure sur la tâche ; le compromis dépend du modèle, de la quantification et du test |
| « ROUGE élevé veut dire résumé vrai. » | Ajouter une négation ou une date fausse en gardant les autres mots |
| « Je peux retoucher le prompt après avoir vu le test. » | Renommer ce test en validation et prévoir un nouveau test indépendant |
| « Colab a perdu mes fichiers. » | Repartir du notebook sauvegardé, des JSON et archives téléchargés ; le runtime n'est pas un disque permanent |

## Évaluer sans décourager l'investigation

Utiliser les cinq questions quotidiennes du [quiz](../evaluation/QUIZ.md) comme diagnostic ; elles peuvent être discutées à deux puis reformulées individuellement. Leur corrigé précise les éléments à attendre. Le projet est noté sur 20 ; si une note globale est souhaitée, l'école peut retenir 80 % projet et 20 % quiz individuel converti sur 20. Annoncer la règle avant le cours.

Accepter « résultat indécidable avec ce petit jeu » si le raisonnement est correct. Récompenser une erreur analysée et une recommandation de ne pas déployer. Demander à chacun une phrase de sortie : **« Je sais maintenant…, ma preuve est…, ma prochaine vérification serait… »**

## Définitions et rappels au fil du cours

Les notes commencent par les définitions utiles à la diapositive, chacune avec un exemple et un point de vigilance. Faire reformuler une notion, puis tester la reformulation sur un exemple. Au besoin, projeter la page indiquée du lexique plutôt que quitter le support. Le [glossaire écrit](GLOSSAIRE_NLP.md) donne les mêmes repères. MRR et Recall@k disposent de deux calculs guidés sur les mêmes classements au J1, puis d’un rappel au J5.

Le [guide des vidéos HF](VIDEOS_HF_FORMATEUR.md) précise les extraits, les pauses par concept et les réponses attendues. Les liens sont aussi dans le PowerPoint et le PDF. Chaque activité remplace trois minutes d’explication dans le créneau existant. Préparer le passage avant la séance, commenter en français et conserver la possibilité d’utiliser directement le schéma du cours.
