# NLP Avancé (BERT, GPT, Hugging Face) — Notes du présentateur

Chrys NIONGOLO · Cybersup · M2 IA · 35 heures

## 1. NLP Avancé (BERT, GPT, Hugging Face)

Jour 0 · accueil · 0 min

ACCUEIL, inclus dans les cinq premières minutes du jour 1. Présenter le contrat : les étudiants doivent pouvoir expliquer une décision et montrer une preuve, pas seulement exécuter un notebook. Le fil rouge est un service de support fictif ; aucun message client réel n'est requis. Partir de cette demande : « J'ai payé deux fois et mon colis n'arrive pas. » Deux besoins coexistent : identifier une intention et conserver des informations précises. Au fil de la semaine, nous construirons une recherche de messages, une classification, une extraction d'entités et une réponse structurée. Annoncer que les petits modèles ont des limites visibles : une expérience qui échoue proprement est un résultat exploitable. Les supports sont en français ; quelques références avancées sont en anglais. Les 35 heures correspondent au travail pédagogique effectif, hors pauses. Le GPU T4 est visé, mais l'accès gratuit à Colab n'est pas garanti. Les voies CPU et les expériences de secours sont prévues dans les guides. OBJECTIFS OFFICIELS : les trois objectifs visibles sont repris littéralement du cadrage. BERT désigne ici la famille des encodeurs ; la pratique utilise son dérivé DistilBERT multilingue. GPT désigne la famille des décodeurs causaux ; la pratique locale emploie Qwen, qui n'est pas un checkpoint GPT d'OpenAI. La classification et la NER adaptent un encodeur, tandis que le résumé dispose d'un SFT LoRA dédié du petit modèle causal. EXTENSION MATÉRIEL : si Chrys fournit un accès Runpod L4 par étudiant, les mêmes expériences peuvent y être exécutées. Colab T4 reste le parcours de référence ; vérifier environnement, précision supportée et mémoire au démarrage, puis noter le matériel réellement utilisé. L'accès L4 n'est ni requis ni supposé disponible.



- https://huggingface.co/learn/llm-course/fr/chapter1/1
- https://web.stanford.edu/class/cs224n/

## 2. Objectifs du cours

Jour 0 · accueil · 0 min

ACCUEIL : cette diapositive est présentée dans les cinq minutes d'ouverture du jour 1, sans ajout au volume de 35 heures. Lire les trois objectifs officiels puis les relier aux livrables : recherche de fiches pour les représentations ; attention, modèle masqué et génération pour les architectures ; entraînements supervisés pour les tâches métier. Préciser que BERT est pratiqué via DistilBERT multilingue et que la famille causale associée à GPT est illustrée par Qwen, qui n'est pas un checkpoint GPT d'OpenAI. Classification et NER adaptent un encodeur ; le résumé dispose d'un LoRA dédié du petit modèle causal. La compréhension sera vérifiée par des calculs, des observations et des décisions argumentées.





## 3. Cinq jours, cinq preuves de compréhension

Jour 0 · accueil · 0 min

Présenter cette carte pendant l'accueil du jour 1. La progression suit une même chaîne : définir la tâche, préparer des exemples, construire une référence simple, modifier un seul facteur, mesurer et expliquer. Le matin comporte des calculs courts, des prédictions avant démonstration et des discussions en binôme ; il ne s'agit pas de trois heures de monologue. L'après-midi comprend quatre étapes avec un livrable visible. Dans chaque binôme, le pilote manipule le notebook et l'analyste prédit le résultat, relève les hypothèses et vérifie les sorties ; alterner les rôles régulièrement. Les notebooks étudiants comportent des questions et les versions formateur des corrigés. Le jeu pédagogique est artificiel : il facilite les observations mais ne démontre aucune performance métier. Les expérimentations optionnelles sur des données réelles doivent conserver provenance et séparation des jeux. Demander aux étudiants de garder un journal contenant une hypothèse, une observation et une décision par jour. Ce journal alimente la soutenance du vendredi. Le premier jour manipule 12 fiches FAQ, 8 requêtes de validation et 6 requêtes finales. La classification sur 80 demandes fictives groupées par scénario commence au jour 3. Ce même jour, 40 minutes du budget classification servent à une extension réelle Allociné, avec un export de sentiment distinct de l'artefact support utilisé au projet.



- https://huggingface.co/learn/llm-course/fr/chapter1/1

## 4. Jour 1 · Du texte à une représentation

Jour 1 · matin · 5 min

DURÉE : 5 min, accueil des deux diapositives précédentes inclus. Faire écrire individuellement une définition du NLP en une phrase puis demander un exemple de sortie attendue. Retenir une formulation opérationnelle : transformer du langage en une sortie utile, avec un protocole pour vérifier cette utilité. Annoncer les trois questions de la journée : quelle information conserver, quelle représentation construire, quelle preuve demander ? Le TP part de douze fiches FAQ et de requêtes françaises dont on connaît la fiche pertinente. Les huit requêtes de validation servent à comparer les réglages ; les six requêtes finales restent réservées. La classification à cinq intentions sera pratiquée au jour 3. Vérifier que les étudiants savent ouvrir un notebook et identifier une cellule de texte et une cellule de code. Le GPU n'est pas nécessaire pour TF-IDF. Transition : deux phrases contenant presque les mêmes mots peuvent vouloir dire des choses différentes ; la première activité rend cette difficulté tangible.





## 5. Même vocabulaire, intention différente

Jour 1 · matin · 10 min

DÉROULÉ : 2 min de lecture individuelle, 4 min de classement en binôme, 4 min de mise en commun. Demander une intention parmi les cinq labels puis autoriser la réponse « ambigu ». Pour le premier exemple, « retour » n'indique pas un retour de produit : l'intention dominante est compte. Pour le second, retour et facturation sont tous deux défendables. La bonne réponse dépend de la politique d'annotation ; il faut la documenter plutôt qu'accuser le modèle. Faire constater qu'un mot déclencheur peut servir de raccourci trompeur. QUESTION : supprimer les petits mots aide-t-il toujours ? RÉPONSE : non ; supprimer « ne » et « pas » peut inverser le sens. Observer aussi les pronoms : « il ne fonctionne plus » nécessite parfois le contexte précédent. Insister sur la distinction entre ambiguïté linguistique et mauvaise annotation. Dans le TP, les binômes conserveront les exemples qui mettent leur représentation en difficulté et expliqueront pourquoi. Une machine ne peut pas résoudre un cahier des charges qui laisse la sortie attendue indéfinie.





## 6. Une tâche = une entrée et une sortie vérifiable

Jour 1 · matin · 10 min

DÉROULÉ : expliquer les cinq lignes en 4 min, faire reformuler une tâche métier en 3 min, corriger collectivement en 3 min. Partir de « automatiser le support » : cette demande est trop large pour choisir une métrique. La décomposer en orientation, extraction de références, recherche d'un cas proche et rédaction d'une réponse. Faire préciser la granularité : un label par message, un label par mot ou une séquence produite ? QUESTION : un chatbot est-il une tâche unique ? RÉPONSE : c'est souvent une application qui combine plusieurs tâches. Une sortie plausible peut être inutile si elle ne correspond pas à l'action souhaitée. Ne pas confondre intention de l'utilisateur, sentiment et urgence : « Très mécontent du délai » peut être négatif, relever de livraison et rester non urgent. Le TP utilisera un même message pour examiner plusieurs représentations, puis le projet choisira une tâche principale et un critère de succès. Demander un exemple de sortie incorrecte avant de montrer les modèles : cela rend l'évaluation concrète dès le début.



- https://huggingface.co/learn/llm-course/fr/chapter1/2

## 7. Le jeu de données est déjà une décision de modèle

Jour 1 · matin · 10 min

DÉROULÉ : 3 min pour décrire les objets, 4 min d'audit de trois exemples, 3 min de restitution. Dans le TP1, une fiche possède un identifiant, un titre et un texte ; une requête possède une fiche attendue. Il y a douze fiches, huit requêtes de validation et six requêtes finales. L'index documentaire est connu du système : on peut ajuster sa représentation sur ces fiches sans utiliser les requêtes test pour régler le moteur. QUESTION : la fiche attendue est-elle toujours unique ? RÉPONSE : c'est notre convention pédagogique ; un vrai service peut accepter plusieurs réponses pertinentes. Faire lire une requête ambiguë et demander si le problème vient du moteur ou de la référence choisie. Le corpus fictif est inspectable mais ne représente pas la diversité de vrais clients. Les groupes de paraphrases et les labels d'intention seront introduits dans le TP3 de classification ; ne pas chercher ces champs dans le TP1. Dans l'atelier, on décrit les limites avant d'afficher les scores. Une table de deux ambiguïtés précises vaut davantage que l'affirmation générale « les données sont propres ».



- https://huggingface.co/learn/llm-course/fr/chapter5/1

## 8. Une fuite de données peut fabriquer un bon score

Jour 1 · matin · 10 min

DÉROULÉ : 3 min de démonstration sur six cartes, 4 min de répartition en binôme, 3 min de correction. Sur les cartes, placer deux variantes de trois demandes. Une répartition aléatoire ligne par ligne peut placer une formulation dans train et sa quasi-copie dans test. L'évaluation mesure alors une reconnaissance de variantes proches. Faire proposer une séparation par groupe de scénario et vérifier l'intersection des identifiants. QUESTION : retirer les labels du test suffit-il à supprimer la fuite ? RÉPONSE : non ; ajuster le vocabulaire ou l'IDF sur l'ensemble des textes transmet déjà de l'information du test. La baseline du TP doit être une pipeline ajustée uniquement sur train. Expliquer que la séparation par client, document ou période peut être plus pertinente dans un vrai projet. La stratification conserve approximativement les proportions ; elle ne garantit pas l'absence de fuite. Les étudiants doivent formuler quelle nouveauté leur test simule. Le test final n'est pas un tableau de bord à consulter après chaque petite modification. CAS RECHERCHE DU TP1 : le vocabulaire et l'IDF sont ajustés sur les fiches de l'index, qui font partie des documents disponibles au système. Les requêtes finales ne servent pas à modifier l'index ou choisir les réglages. Le découpage train/validation/test par groupes sera appliqué au TP3 de classification.



- https://scikit-learn.org/stable/common_pitfalls.html#data-leakage

## 9. Sac de mots : compter avant de comprendre

Jour 1 · matin · 10 min

DÉROULÉ : 3 min de lecture de matrice, 4 min de construction d'une nouvelle ligne, 3 min de discussion. Expliquer que les colonnes forment un vocabulaire choisi ; les mots absents de cette petite table sont ignorés pour l'exemple. Demander le vecteur de « retard de facture » : [0, 1, 1]. Puis comparer « le client accuse le vendeur » et « le vendeur accuse le client » : les comptes unigrammes coïncident malgré une relation inversée. QUESTION : cette limite rend-elle la méthode inutile ? RÉPONSE : non ; de nombreuses intentions possèdent des indices lexicaux très discriminants et la baseline est rapide à auditer. Introduire brièvement les bigrammes, qui conservent un ordre local comme « pas reçu », sans donner une compréhension générale de la phrase. Mentionner que la matrice est creuse : la plupart des cases valent zéro. Dans le TP, afficher les termes les plus associés à chaque classe et chercher les raccourcis. L'interprétabilité d'un poids aide à diagnostiquer, mais elle ne prouve pas une causalité linguistique. COMPLÉMENT À EXPLICITER : Simple, interprétable, mais l'ordre des mots disparaît.



- https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction

## 10. TF-IDF : un terme rare peut mieux distinguer

Jour 1 · matin · 10 min

ANIMATION — 10 min
4 min de calcul guidé, 3 min de calcul en binôme, 3 min de correction. Partir de quatre fiches qui contiennent toutes « bonjour », alors qu’une seule contient « remboursement ».

LECTURE ORALE
« Le poids du terme t dans le document d est sa fréquence dans ce document, multipliée par le logarithme naturel du nombre total de documents divisé par le nombre de documents contenant ce terme. » Lire d’abord la fréquence locale, puis le facteur de rareté dans le corpus.

SYMBOLES, DIMENSIONS ET UNITÉS
t désigne un terme du vocabulaire ; d un document. tf(t,d) est ici un compte entier d’occurrences, non normalisé. df(t) compte les documents distincts contenant t : répéter t dix fois dans un document n’ajoute qu’un à df. N est le nombre de documents du corpus. ln est le logarithme naturel, de base e. N/df(t) est un rapport sans unité ; w(t,d) est un score scalaire sans unité, pas une probabilité. Une collection de ces poids forme une matrice documents × termes.

CALCUL PAS À PAS
1. Fixer N = 4 et df(remboursement) = 1.
2. Calculer le rapport 4/1 = 4, puis ln(4) ≈ 1,386.
3. Si remboursement apparaît deux fois dans la fiche, tf = 2 : le poids brut vaut 2 × 1,386 ≈ 2,773.
4. Pour bonjour présent dans les quatre fiches, df = 4 et ln(4/4) = ln(1) = 0 : le poids simplifié vaut zéro.

HYPOTHÈSES ET PIÈGE
Cette formule pédagogique utilise une fréquence brute, sans lissage ni normalisation finale, avec df strictement positif. TfidfVectorizer applique par défaut un IDF lissé, un décalage et une normalisation : il ne faut pas exiger les mêmes chiffres dans le TP. En classification, ajuster sur train ; dans la recherche du TP1, ajuster sur les fiches connues de l’index, sans choisir les réglages sur les requêtes finales.

QUESTION / RÉPONSE
« Un mot rare est-il forcément utile ? » Non : il peut être une faute, une référence ou du bruit. Lire les termes dominants et vérifier la pertinence des fiches retrouvées.

REPÈRES DU CORPS DE DIAPOSITIVE
• tf : nombre d'occurrences dans le document.
• df : nombre de documents contenant le terme ; N : total de documents.
• Si N = 4 : df = 1 donne log(4) ≈ 1,39 ; df = 4 donne 0.

SOURCE LATEX DE LA FORMULE
w_{t,d}=\operatorname{tf}(t,d)\,\ln\!\left(\frac{N}{\operatorname{df}(t)}\right)

Source de l'image de formule — LaTeX
w_{t,d}=\operatorname{tf}(t,d)\,\ln\!\left(\frac{N}{\operatorname{df}(t)}\right)

Légende projetée
t : terme ; d : document
tf(t,d) : occurrences de t dans d
df(t) : documents contenant t
N : nombre de documents du corpus
w(t,d) : poids TF-IDF, sans unité

N = 4, df = 1, tf = 2 : w = 2 × ln(4) ≈ 2,773 avec la formule simplifiée.

- https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting

## 11. Une baseline de recherche tient dans une chaîne claire

Jour 1 · matin · 10 min

DÉROULÉ : 3 min d'explication, 4 min de prédiction de comportement, 3 min de discussion. La requête et chaque fiche deviennent des vecteurs TF-IDF dans le même vocabulaire. Le cosinus fournit un score par fiche ; on classe ces scores. Dans notre TP, chaque requête possède une seule fiche attendue. Recall@3 vaut un si cette fiche est parmi les trois premières ; le rang réciproque vaut un divisé par son rang, et MRR moyenne ces valeurs. QUESTION : faut-il remplacer la baseline dès qu'un Transformer est disponible ? RÉPONSE : on le décide en comparant pertinence, coût et erreurs sur les mêmes requêtes. Une référence exacte peut favoriser le lexical, tandis qu'une paraphrase peut favoriser un embedding. Faire anticiper une requête sans aucun terme connu : ses scores peuvent être tous nuls, et l'ordre de départage devient déterminant. Dans le TP, on compare unigrammes et bigrammes sur validation, puis on fige le choix avant test. La régression logistique sera ajoutée au jour 3 pour transformer une représentation lexicale en classifieur à cinq intentions.



- https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction

## 12. Lire une confusion au lieu d'admirer un pourcentage

Jour 1 · matin · 10 min

DÉROULÉ : 3 min de lecture, 4 min de calcul, 3 min d'interprétation. Insister sur l'orientation de la matrice : les lignes correspondent aux labels réels et les colonnes aux prédictions. Il y a dix messages de chaque classe. La diagonale contient 8 + 9 = 17 décisions correctes. Pour livraison, la précision vaut 8/9, environ 0,89, car neuf messages ont été prédits livraison ; le rappel vaut 8/10 = 0,80. Faire calculer les mêmes quantités pour facturation puis demander lequel des deux systèmes serait préférable si les erreurs avaient des coûts différents. QUESTION : un score de 85 % suffit-il pour déployer ? RÉPONSE : non, il manque la taille et la représentativité du test, le coût des erreurs et le comportement hors distribution. Les nombres affichés sont inventés pour le calcul, pas obtenus par nos notebooks. Ce calcul prépare la classification du jour 3 ; le TP1 de recherche utilise Recall@k et MRR plutôt qu’une matrice de confusion. Au TP3, vérifier les totaux et relier chaque cellule non diagonale à des textes concrets. Le jour 3 introduira le macro-F1 pour les cinq classes. COMPLÉMENT À EXPLICITER : Les 3 erreurs méritent une lecture ligne par ligne.



- https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics

## 13. Tokeniser : choisir les unités lues par le modèle

Jour 1 · matin · 10 min

DÉROULÉ : 4 min d'explication, 3 min de proposition de découpages, 3 min de comparaison. L'exemple de sous-mots est illustratif : ne pas annoncer que tous les tokenizers découpent remboursement ainsi. Le découpage exact se mesure avec le tokenizer choisi. Introduire un token comme une unité du vocabulaire et un identifiant comme son indice numérique. QUESTION : un token est-il toujours un mot ? RÉPONSE : non ; il peut être un fragment, un signe ou une représentation liée aux octets. Faire comparer « l'abonnement », une adresse électronique et un emoji. Le nombre de caractères n'indique pas directement le nombre de tokens ; cette différence affecte longueur maximale, coût et troncature. Ne pas présenter les sous-mots comme des morphèmes garantis : leur découpage est souvent appris à partir de fréquences. Le TP affichera tokens, identifiants et reconstruction pour des phrases françaises. Pour l'adaptation d'un modèle existant, on garde son tokenizer ; entraîner un nouveau tokenizer constitue un exercice distinct, pas un remplacement compatible automatique.



- https://huggingface.co/learn/llm-course/fr/chapter2/4

## 14. Prétraiter le français sans effacer le sens

Jour 1 · matin · 10 min

DÉROULÉ : 2 min pour lire les cas, 5 min en groupes, 3 min de restitution. Chaque groupe défend une transformation et nomme un cas où elle serait nuisible. Lowercasing peut aider une baseline lexicale en regroupant des variantes, mais supprimer l'information de casse utile à la NER. Retirer les accents peut réduire certaines variantes tout en fusionnant des mots différents. Supprimer systématiquement ponctuation, négation et emojis peut effacer des indices de sens. QUESTION : faut-il lemmatiser avant un Transformer ? RÉPONSE : généralement, on commence avec le texte attendu par son tokenizer et on ne transforme que pour une raison validée expérimentalement. L'anonymisation doit préserver la nature de l'information si la tâche en dépend : remplacer toutes les références par une chaîne identique peut rendre l'extraction artificiellement facile. Le corpus de formation est fictif ; les étudiants ne doivent pas ajouter leurs messages privés pour rendre la démonstration plus réaliste. Relier cette activité au TP : conserver le texte brut, produire une version transformée séparée et comparer les erreurs au lieu d'écraser la source.



- https://huggingface.co/learn/llm-course/fr/chapter6/4

## 15. BPE à la main : fusionner les paires fréquentes

Jour 1 · matin · 10 min

DÉROULÉ : 3 min de calcul guidé, 4 min en binôme, 3 min de correction. Notre exemple simplifié ignore volontairement marqueurs de fin de mot et conventions d'octets. Compter les occurrences avec la fréquence des mots : b-a vaut 3 + 2 + 1 = 6 ; a-s vaut 3 + 2 = 5 ; s-s et s-e valent 2 ; a-l vaut 1. Après fusion b-a, les mots deviennent ba-s, ba-s-s-e et ba-l. La paire ba-s vaut cinq et devient la deuxième fusion : bas, bas-s-e, ba-l. QUESTION : peut-on garder les comptes initiaux pour la deuxième étape ? RÉPONSE : non, les unités ont changé. Faire proposer le découpage d'un mot nouveau composé de symboles connus. Souligner qu'apprentissage du vocabulaire et tokenisation d'un texte sont deux phases différentes : la seconde réapplique les fusions dans leur ordre. En cas d'égalité, une règle de départage doit être définie. Le tokenizer entraîné en TP permet d'observer la compression ; il ne doit pas être branché directement sur les embeddings préentraînés de DistilBERT. COMPLÉMENT À EXPLICITER : Recompter ensuite les paires sur le nouveau découpage.



- https://huggingface.co/learn/llm-course/fr/chapter6/5

## 16. Des tokens aux tenseurs : trois objets différents

Jour 1 · matin · 10 min

DÉROULÉ : 4 min de distinction des objets, 3 min d'appariement par binôme, 3 min de correction. Les identifiants affichés sont fictifs ; on ne peut pas déduire leur valeur sans lire le tokenizer. Un identifiant 5678 n'est pas plus proche sémantiquement de 5679 que de 4 : c'est une adresse dans une table, pas une mesure. Le modèle récupère ensuite un vecteur par adresse. La cinquième case vaut ici zéro comme identifiant de padding illustratif et reçoit un masque nul ; les deux vecteurs ont bien cinq positions. Le véritable identifiant de padding dépend du tokenizer. QUESTION : pourquoi grouper des phrases courtes et longues pose-t-il un problème ? RÉPONSE : un batch doit être représenté par un tenseur rectangulaire ; on ajoute du padding et on indique les positions valides. Demander aux étudiants de détecter volontairement une incompatibilité de longueur. Le jour 3 distinguera attention_mask et labels ignorés à -100 ; ils ne rendent pas le même service. Dans le TP, afficher les dimensions constitue un premier réflexe de diagnostic, avant toute recherche compliquée d'erreur.



- https://huggingface.co/learn/llm-course/fr/chapter2/5

## 17. Un embedding rapproche des usages similaires

Jour 1 · matin · 10 min

CONCEPT ET ANIMATION
DÉROULÉ : 3 min d'analogie géométrique, 4 min de prédictions de voisinage, 3 min de discussion. Placer mentalement des messages sur une carte : « Où est mon colis ? » peut être proche de « Je n'ai toujours rien reçu », même sans partager tous les termes. Le dessin est une intuition ; les dimensions réelles ne correspondent généralement pas à des axes nommables tels que politesse ou urgence. Distinguer embeddings statiques de mots, représentations contextualisées de tokens et embeddings de phrases obtenus par une méthode d'agrégation adaptée.

QUESTION : moyenner n'importe quels vecteurs de tokens suffit-il toujours pour une bonne recherche ? RÉPONSE : non, l'objectif d'apprentissage de l'encodeur compte. Le TP utilisera un modèle de phrases multilingue explicitement conçu pour des représentations comparables. Inviter les étudiants à proposer un synonyme, une négation et un mot de domaine absent des exemples. La ressemblance géométrique ne prouve ni vérité ni identité d'intention. Une bonne recherche restitue des candidats à vérifier, particulièrement quand les messages mélangent plusieurs demandes.

LECTURE GUIDÉE DU SCHÉMA
1. Commencer par les textes d’entrée : deux formulations différentes d’un même besoin et une formulation de thème différent. Les flèches vers l’encodeur représentent une transformation calculée, pas une simple égalité entre phrases.
2. Suivre texte → tokenizer → représentations contextualisées → agrégation adaptée à la phrase. La sortie est un vecteur de D coordonnées par texte ; le modèle de phrases utilise une méthode de pooling et d’apprentissage conçue pour comparer ces vecteurs.
3. Lire les flèches de comparaison comme des calculs de similarité sur les vecteurs. Une proximité géométrique indique un signal de recherche, pas une probabilité de vérité.
4. Les points en deux dimensions sont une illustration pédagogique : ce ne sont pas des mesures du TP et les axes ne représentent pas des propriétés linguistiques garanties. Une projection réelle peut déformer les distances.
5. Faire reformuler la sortie attendue : le moteur retourne des voisins classés. Il ne génère pas encore de réponse et ne vérifie pas les faits. Question : une négation peut-elle rester proche ? Oui, car le thème peut rester presque identique.

REPÈRES DU CORPS DE DIAPOSITIVE À EXPLICITER
Accroche : Une représentation dense apprend des régularités à partir de textes.
• Un vecteur de mots n'est pas une liste de définitions.
• Une représentation de phrase permet la recherche sémantique.
• Le modèle multilingue relie plusieurs formulations et langues.
• La qualité dépend de l'apprentissage et du domaine.

Description accessible du schéma
Deux vecteurs illustratifs colis et livraison pointent dans des directions voisines ; facture pointe ailleurs. Deux phrases proches évoquent un colis non reçu.
Les positions 2D sont illustratives ; la proximité ne prouve pas un sens identique.

Repères associés à l'illustration
Une représentation dense apprend des régularités à partir de textes.
Un vecteur de mots n'est pas une liste de définitions.
Une représentation de phrase permet la recherche sémantique.
Le modèle multilingue relie plusieurs formulations et langues.
La qualité dépend de l'apprentissage et du domaine.

- https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2

## 18. Cosinus : comparer une direction plutôt qu'une taille

Jour 1 · matin · 10 min

ANIMATION — 10 min
4 min de calcul au tableau, 3 min de variante en binôme, 3 min d’interprétation. Dessiner deux vecteurs orientés dans la même direction mais de longueurs différentes.

LECTURE ORALE
« Le cosinus entre u et v est leur produit scalaire, divisé par le produit de leurs longueurs. » Faire identifier le numérateur qui mesure leur alignement, puis le dénominateur qui retire l’effet des amplitudes.

SYMBOLES, DIMENSIONS ET UNITÉS
u et v sont deux vecteurs réels non nuls de même dimension D. Le symbole T indique la transposée : uᵀv est un scalaire égal à la somme u₁v₁ + … + u_Dv_D. La norme ‖u‖₂ est la racine carrée de u₁² + … + u_D² ; le petit 2 nomme la norme euclidienne. Les dimensions d’un embedding sont des caractéristiques apprises sans unité physique imposée. Le rapport final est sans unité et compris entre −1 et 1 ; ce n’est pas une probabilité de vérité.

CALCUL PAS À PAS
1. Prendre u = (1,0) et v = (1,1).
2. Le produit scalaire vaut 1×1 + 0×1 = 1.
3. Les normes valent √(1²+0²) = 1 et √(1²+1²) = √2.
4. Le cosinus vaut 1/√2 ≈ 0,707.
5. Avec v = (2,0), numérateur et dénominateur valent 2 : cosinus = 1. Avec v = (0,1), le numérateur est nul : cosinus = 0.

HYPOTHÈSES ET PIÈGE
La formule exige deux vecteurs non nuls. Une requête TF-IDF sans terme connu peut produire un vecteur nul ; inspecter le comportement de la bibliothèque et les ex æquo. Si les embeddings sont déjà normalisés à une norme de un, le produit scalaire égale le cosinus. Ne pas comparer les scores bruts de modèles différents comme des probabilités calibrées.

QUESTION / RÉPONSE
« Multiplier v par dix change-t-il ce cosinus ? » Non pour un facteur positif : sa direction ne change pas. « Un score de 0,9 garantit-il une bonne fiche ? » Non : lire les voisins et mesurer la pertinence sur les requêtes de validation.

REPÈRES DU CORPS DE DIAPOSITIVE
• u = (1, 0), v = (2, 0) → cosinus = 1.
• u = (1, 0), w = (0, 1) → cosinus = 0.
• u = (1, 0), z = (1, 1) → cosinus ≈ 0,71.

SOURCE LATEX DE LA FORMULE
\operatorname{cos}(\mathbf{u},\mathbf{v})=\frac{\mathbf{u}^{\mathsf T}\mathbf{v}}{\lVert\mathbf{u}\rVert_2\,\lVert\mathbf{v}\rVert_2}

Source de l'image de formule — LaTeX
\operatorname{cos}(\mathbf{u},\mathbf{v})=\frac{\mathbf{u}^{\mathsf T}\mathbf{v}}{\lVert\mathbf{u}\rVert_2\,\lVert\mathbf{v}\rVert_2}

Légende projetée
u, v : vecteurs de même dimension D
uᵀv : produit scalaire, somme de D produits
‖u‖₂, ‖v‖₂ : longueurs euclidiennes
cos(u,v) : similarité comprise entre −1 et 1

u = (1,0), v = (1,1) : produit = 1 ; normes = 1 et √2 ; cosinus ≈ 0,707.

- https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html

## 19. Une proximité sémantique peut cacher une contradiction

Jour 1 · matin · 10 min

DÉROULÉ : 2 min de prédiction, 5 min de confrontation de cas, 3 min de synthèse. Demander si les deux phrases du titre devraient être éloignées. La réponse dépend de l'objectif : pour retrouver des échanges sur une livraison, la proximité thématique est utile ; pour décider qu'une livraison a eu lieu, elle est dangereuse. L'embedding ne doit donc pas être évalué hors de son usage. QUESTION : plus le vecteur est grand, meilleure est la représentation ? RÉPONSE : la dimension seule ne suffit pas ; l'objectif d'apprentissage, les données et l'évaluation comptent. Faire construire trois requêtes et leur document pertinent de référence avant de lancer la recherche. Une question hors domaine doit pouvoir conduire à « aucun résultat suffisamment fiable », mais le seuil n'est pas universel. Dans le TP, comparer lexical et sémantique sur le même ensemble de requêtes, avec une colonne expliquant la pertinence. Éviter de choisir après coup uniquement les phrases qui rendent le modèle impressionnant. Ces contre-exemples deviendront des tests de robustesse du projet.



- https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html

## 20. Choisir une représentation avec une expérience

Jour 1 · matin · 10 min

DÉROULÉ : 3 min pour lire les hypothèses, 4 min pour proposer un protocole, 3 min de correction. Les forces du tableau sont des hypothèses raisonnables, pas des résultats promis. Un système lexical peut gagner lorsqu'une référence exacte ou un nom rare est décisif. Un encodeur de phrases peut rapprocher des formulations différentes tout en négligeant un numéro de commande. QUESTION : comment comparer deux méthodes dont les scores ont des échelles différentes ? RÉPONSE : comparer la pertinence des résultats, par exemple la présence du bon document dans les trois premiers, et non le niveau brut du cosinus. Introduire Recall@k de manière concrète pour une requête à document pertinent unique : vaut un si le document attendu est dans les k premiers, zéro sinon. La moyenne sur les requêtes est notre indicateur pédagogique ; pour plusieurs documents pertinents, il faut préciser la définition utilisée. Dans le TP, produire un tableau de cas gagnés et perdus par chaque méthode puis une recommandation limitée au corpus observé. Une recherche hybride est une piste bonus, pas une obligation avant la première évaluation. Ajouter MRR : si les rangs des bonnes fiches sont 1, 2 et 4, les rangs réciproques valent 1, 0,5 et 0,25, soit une MRR d'environ 0,583. Le TP calcule cette mesure sur les mêmes requêtes.



- https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html

## 21. Vérifier les acquis avant le TP

Jour 1 · matin · 15 min

DÉROULÉ : 4 min de réponses individuelles, 5 min de confrontation en binôme, 6 min de correction. Réponse 1 : éviter qu'une quasi-copie du scénario d'entraînement se retrouve dans le test et donne une estimation trop optimiste. Réponse 2 : non, l'unité dépend du tokenizer et peut être un sous-mot, un caractère, un signe ou un fragment lié aux octets. Réponse 3 : non, la similarité géométrique n'est pas une probabilité de vérité. Réponse 4 : une requête contenant une référence exacte ou un terme métier rare peut favoriser le lexical ; il faut le vérifier. Demander aux étudiants de justifier chaque réponse avec un exemple du matin. Si plus d'un tiers confond identifiant et embedding, reprendre les trois objets de la diapositive correspondante pendant la correction. Terminer par une prédiction écrite : quelle méthode gagnera sur les requêtes de leur binôme ? Elle sera confrontée aux résultats l'après-midi. Le quiz est formatif et sert à décider de l'accompagnement, pas à établir un classement des étudiants.





## 22. TP 1A · Auditer les fiches et les requêtes

Jour 1 · apres-midi · 35 min

ORGANISATION : 10 min d'ouverture et de diagnostic d'environnement, 15 min d'exploration des fiches et des requêtes, 10 min de tokenisation simple et restitution. Ouvrir notebooks/etudiants/01_j1_textes_recherche.ipynb. Le pilote exécute, l'analyste note une prédiction avant chaque sortie ; inverser les rôles régulièrement. Le GPU n'est pas requis. La tâche consiste à retrouver une fiche parmi douze, pas à classer les quatre-vingts tickets du jour 3. POINT DE CONTRÔLE : chaque binôme montre une requête, son identifiant de fiche attendu et explique pourquoi cette référence est défendable. RÉSULTAT ATTENDU : les étudiants distinguent l'index documentaire, les questions de validation et les questions finales. Ne pas exploiter ces dernières pour ajuster les fiches ou les réglages. Comparer séparation par espaces et expression régulière sur une phrase française contenant apostrophe, prix et négation. Si l'import des bibliothèques bloque, continuer l'association manuelle des requêtes aux fiches et revenir ensuite à l'environnement. Conserver les décisions dans le journal d'expérience.





## 23. TP 1B · Construire la recherche lexicale

Jour 1 · apres-midi · 50 min

ORGANISATION : 10 min de lecture de la chaîne, 15 min de recherche lexicale, 15 min de comparaison unigrammes/bigrammes, 10 min d'analyse. Faire prédire si « pièce pour ma comptabilité » retrouvera la fiche facture. L'analyste vérifie que le vocabulaire et l'IDF sont ajustés sur les fiches connues de l'index, sans utiliser les requêtes finales comme données de réglage. POINT DE CONTRÔLE : montrer les trois premières fiches, leurs scores et le rang de la bonne référence. RÉSULTAT ATTENDU : une table Recall@1, Recall@3 et MRR avec huit requêtes de validation ; aucun seuil de performance n'est imposé. Lire les termes dominants pour expliquer un résultat lexical. Faire repérer le cas où une requête n'active aucun terme connu et où tous les scores sont nuls. EXTENSION : construire une phrase dont la négation piège l'unigramme et discuter l'effet du bigramme. Ne pas ajouter une régression logistique ici : la tâche est une recherche, la classification sera traitée au jour 3. Garder les configurations comparées.





## 24. TP 1C · Inspecter et entraîner un tokenizer

Jour 1 · apres-midi · 40 min

ORGANISATION : 10 min d'inspection, 20 min de BPE et d'expériences, 10 min de comparaison. Relier chaque sortie au calcul manuel du matin. Le BPE est entraîné sur les fiches documentaires, sans exploiter les requêtes finales pour choisir son vocabulaire. POINT DE CONTRÔLE : le binôme explique pourquoi les deux tailles cibles produisent des découpages différents et pourquoi la taille réellement obtenue peut être inférieure à la cible. Les phrases proposées incluent une négation, N'Djamena et une faute avec emoji. RÉSULTAT ATTENDU : une table texte, tokens, nombre d'unités et nombre d'inconnus. Le corpus minuscule ne couvre pas tous les caractères ; [UNK] peut apparaître et doit être expliqué. Le tokenizer nouvellement entraîné reste pédagogique : il ne remplace pas celui d'un modèle préentraîné. EXTENSION : comparer l'effet attendu d'un BPE sur octets, sans prétendre qu'il résoudrait toute difficulté sémantique. Ne pas présenter une réduction du nombre de tokens comme une amélioration automatique de la compréhension. Faire verbaliser vocabulaire, identifiant et embedding.



- https://huggingface.co/learn/llm-course/fr/chapter6/2

## 25. TP 1D · Comparer, tester et expliquer la recherche

Jour 1 · apres-midi · 115 min

ORGANISATION : 55 min pour les embeddings et leur comparaison, puis 60 min pour l'analyse, le choix, le test et la restitution, conformément au parcours du notebook. Modèle : sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2. Encoder les douze fiches et normaliser les vecteurs permet d'utiliser leur produit scalaire comme cosinus. POINT DE CONTRÔLE : les deux méthodes reçoivent les mêmes huit requêtes de validation et la même référence pertinente. RÉSULTAT ATTENDU : une table de classements et de métriques, puis le choix d'une méthode effectivement exécutée. Les six requêtes finales sont évaluées seulement après ce choix ; une seule erreur change Recall@1 d'environ 0,167. La projection PCA en deux dimensions est une vue partielle, pas une preuve de performance. Si le téléchargement est indisponible, désactiver USE_PRETRAINED et terminer proprement le protocole lexical en signalant l'étape absente. Lire deux erreurs précises et distinguer manque lexical, négation, ambiguïté et référence discutable. Conclure par une recommandation limitée au corpus observé et proposer un protocole sur cent questions réelles autorisées.



- https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2

## 26. Jour 2 · Comprendre les Transformers

Jour 2 · matin · 5 min

DURÉE : 5 min. Faire restituer la différence entre token et embedding par deux étudiants. Présenter le problème : une représentation de « compte » devrait changer entre « mon compte est bloqué » et « le vendeur compte trois colis ». Le contexte doit donc modifier le vecteur utilisé pour une décision. Annoncer la progression : un mécanisme de pondération très concret, des matrices de dimensions vérifiables, puis une architecture complète. Ne pas commencer par le schéma entier d'un Transformer : il devient lisible une fois chaque opération motivée. Les exemples numériques sont volontairement petits et construits pour le cours. L'après-midi reproduira les calculs avec NumPy ou PyTorch avant d'utiliser les modèles. Préciser que visualiser des poids d'attention ne donne pas automatiquement l'explication causale d'une décision. Le but est de comprendre les calculs et les limites de l'observation. LIVRABLE DE LA JOURNÉE : À produire : calcul vérifié et comparaison de décodages.



- https://arxiv.org/abs/1706.03762

## 27. Prédire la suite : une cible obtenue sans annotation manuelle

Jour 2 · matin · 10 min

DÉROULÉ : 3 min de lecture du décalage, 4 min de construction d'un autre exemple, 3 min de discussion. Reprendre l'intuition du support NLP avec Deep Learning fourni : les entrées et les cibles sont décalées d'une position. Notre table est au niveau de mots pour être lisible ; le vrai modèle travaille avec ses tokens. Faire compléter « Le colis arrive… » avec plusieurs suites possibles : demain, lundi, endommagé. Aucune n'est intrinsèquement l'unique suite vraie sans contexte. QUESTION : a-t-on besoin de rédiger une étiquette pour chaque token ? RÉPONSE : le texte fournit la cible suivante, mais son choix et sa qualité restent essentiels. Expliquer teacher forcing sans jargon supplémentaire : pendant l'entraînement, on fournit les vrais tokens précédents, pas uniquement les prédictions du modèle. En génération, une erreur peut influencer la suite. Le masque causal empêche de voir les cibles futures pendant l'entraînement. Dans le TP, faire vérifier le décalage une seule fois ; certaines classes de modèles calculent ce décalage en interne, et il ne faut pas le refaire par erreur. COMPLÉMENT À EXPLICITER : L'entraînement utilise le vrai préfixe ; la génération utilise sa propre sortie.



- https://huggingface.co/learn/llm-course/fr/chapter7/6

## 28. Pourquoi permettre aux tokens de se consulter ?

Jour 2 · matin · 10 min

DÉROULÉ : 3 min d'exemple linguistique, 4 min de schéma au tableau, 3 min de discussion. Écrire « Le client a reçu le colis après plusieurs appels ; il était abîmé ». Demander quel nom peut désigner il et quelles connaissances seraient nécessaires pour trancher. L'objectif n'est pas d'affirmer que l'attention résout l'ambiguïté, mais de motiver l'accès à plusieurs positions. Dessiner une chaîne pour la récurrence et des flèches entre tokens pour l'attention. L'entraînement d'un Transformer peut traiter de nombreuses positions en parallèle sous les masques appropriés, alors que la génération autorégressive reste séquentielle token par token. QUESTION : supprimer la récurrence supprime-t-il toute dépendance temporelle ? RÉPONSE : non, l'ordre et le masque continuent de structurer l'information. Une matrice d'attention dense comporte n² couples de positions, ce qui explique une partie du coût des longs contextes. Mentionner que des implémentations optimisent la mémoire et que tous les modèles ne réalisent pas exactement la forme pédagogique. Le TP travaille d'abord sur quelques tokens pour rendre chaque lien inspectable.



- https://arxiv.org/abs/1706.03762

## 29. Q, K, V : demander, comparer, récupérer

Jour 2 · matin · 10 min

CONCEPT ET ANIMATION
DÉROULÉ : 4 min d'analogie, 3 min de reformulation, 3 min de limites de l'analogie. Utiliser un catalogue de bibliothèque : la requête exprime le besoin, les clés servent à comparer les notices et les valeurs contiennent ce que l'on récupère. Dans un Transformer, les mêmes représentations de tokens peuvent être projetées en trois espaces par des matrices apprises. Ce ne sont ni des mots-clés choisis à la main ni des champs explicitement nommés dans le texte.

QUESTION : si K et V viennent du même token, sont-ils forcément égaux ? RÉPONSE : non ; W_K et W_V sont des projections différentes. Souligner ce point car confondre V avec K détruit le sens du calcul de récupération. En self-attention, Q, K et V proviennent de la même séquence de représentations ; en cross-attention, Q provient du côté qui interroge et K, V de l'autre séquence. Faire expliquer ces deux cas sur une traduction courte. Le TP vérifiera que changer V modifie la sortie sans changer les poids, si Q et K sont conservés.

LECTURE GUIDÉE DU SCHÉMA
1. Partir de X, la matrice des représentations de tokens. Les trois flèches sortantes appliquent W_Q, W_K et W_V : elles partagent l’entrée mais pas nécessairement les paramètres ni les valeurs obtenues.
2. Suivre la branche Q et la branche K jusqu’au produit QKᵀ. Une ligne correspond à une requête et une colonne à une clé : leurs intersections sont les scores de compatibilité.
3. Lire mise à l’échelle, masque éventuel et softmax comme des étapes qui produisent une distribution par requête. La branche V ne calcule pas ces poids ; elle fournit le contenu à combiner.
4. La jonction poids × V retourne une représentation par requête. Pour trois tokens et des valeurs à deux coordonnées, la sortie possède trois lignes et deux colonnes.
5. En self-attention, les trois branches viennent de la même séquence. En cross-attention, Q vient du côté qui interroge tandis que K et V viennent de l’autre séquence. Ne pas dessiner une entrée textuelle différente pour chaque projection de la self-attention. Question : changer V modifie-t-il les poids à Q et K fixés ? Non.

REPÈRES DU CORPS DE DIAPOSITIVE À EXPLICITER
• Query Q : ce que la position courante cherche.
• Key K : ce que chaque position propose pour être repérée.
• Value V : l'information transmise si la position est retenue.
• Ces trois représentations proviennent de projections apprises.

Description accessible du schéma
La séquence X alimente trois projections apprises WQ, WK et WV, produisant respectivement queries, keys et values avec leurs rôles distincts.
En self-attention, Q, K et V proviennent de trois projections apprises du même X.

Repères associés à l'illustration
Query Q : ce que la position courante cherche.
Key K : ce que chaque position propose pour être repérée.
Value V : l'information transmise si la position est retenue.
Ces trois représentations proviennent de projections apprises.

- https://huggingface.co/learn/llm-course/fr/chapter1/4

## 30. Les dimensions racontent le calcul

Jour 2 · matin · 10 min

DÉROULÉ : 4 min de vérification de produits, 3 min de dimensions manquantes, 3 min de correction. Commencer par X : une ligne par token, une colonne par caractéristique. Pour passer de quatre à deux caractéristiques, W_Q et W_K ont ici la forme 4 × 2. Le produit QK transposé donne bien 3 × 3 : trois requêtes comparent trois clés. Chaque ligne d'attention contiendra trois poids dont la somme vaut un après softmax. QUESTION : pourquoi AV retourne-t-il trois lignes et non une seule ? RÉPONSE : on calcule une combinaison de valeurs pour chaque requête. Le batch et les têtes ajoutent des axes dans une implémentation réelle ; on les introduira après ce cas simple. Faire diagnostiquer un faux résultat ayant quatre poids pour trois clés. Ce contrôle dimensionnel détecte une erreur avant même de regarder les nombres. Insister sur d_k : c'est la dimension d'une clé pour une tête, pas automatiquement la dimension totale du modèle. Dans le TP, les assertions de formes devront accompagner les résultats numériques.

FORMULE GLOBALE POUR RELIER LE SCHÉMA AUX DIMENSIONS
Source LaTeX : \operatorname{Attention}(Q,K,V)=\operatorname{softmax}\!\left(\frac{QK^{\mathsf T}}{\sqrt{d_k}}+M\right)V.
Lecture : comparer chaque requête aux clés, mettre à l’échelle, ajouter le masque, normaliser chaque ligne sur les clés, puis combiner les valeurs. Pour n_q requêtes, n_k clés et des valeurs de dimension d_v : Q est n_q × d_k, K est n_k × d_k, V est n_k × d_v. Le produit QKᵀ et le masque additif M sont n_q × n_k ; M vaut zéro pour un accès autorisé et −∞ pour un accès interdit. La sortie est n_q × d_v. Dans notre cas jouet, n_q = n_k = 3 et d_k = d_v = 2 : (3×2)(2×3) donne 3×3, puis (3×3)(3×2) donne 3×2. Les axes de batch et de têtes sont omis pour la lisibilité. Ne pas confondre ce masque additif M avec un vecteur binaire attention_mask ni avec labels = −100 : ces représentations interviennent à des endroits différents.



- https://arxiv.org/abs/1706.03762

## 31. Étape 1 · Calculer les scores de correspondance

Jour 2 · matin · 10 min

DÉROULÉ : 3 min de calcul guidé, 4 min avec une nouvelle requête, 3 min de correction. Pour q = (1,0), le produit avec A vaut 1×1 + 0×0 = 1 ; avec B il vaut zéro ; avec C il vaut un. Faire reprendre le calcul avec q = (0,1), qui produit [0,1,1]. L'objectif est de rendre visible qu'une autre position peut chercher une autre information. QUESTION : les scores 1,0,1 sont-ils des probabilités ? RÉPONSE : non, ils ne somment pas à un et pourraient être négatifs. Le produit scalaire tient compte des directions et des amplitudes ; il n'est pas automatiquement un cosinus. Il n'y a pas encore de valeur récupérée : nous avons seulement établi des compatibilités. Les vecteurs sont inventés pour le calcul et ne constituent pas une mesure réelle de mots français. Inviter chaque binôme à changer une clé pour que B gagne. Cette manipulation prépare le TP : on doit pouvoir prédire l'effet d'une modification de Q ou K avant d'exécuter la cellule. COMPLÉMENT À EXPLICITER : Un score plus élevé reçoit davantage de poids après softmax.





## 32. Étape 2 · Mise à l'échelle et softmax

Jour 2 · matin · 10 min

ANIMATION — 10 min
4 min de calcul collectif, 3 min de vérification par binôme, 3 min d’interprétation. Conserver la même requête et les trois clés de la diapositive précédente.

LECTURE ORALE
« Le poids a indice i est l’exponentielle du score i divisé par racine de d indice k, rapportée à la somme de ces exponentielles pour toutes les clés. » Les trois opérations sont : mettre les scores à l’échelle, les exponentier, puis normaliser la ligne.

SYMBOLES, DIMENSIONS ET UNITÉS
q et kᵢ sont des vecteurs de dₖ coordonnées ; sᵢ = qᵀkᵢ est leur produit scalaire. dₖ est un entier : la dimension d’une clé dans cette tête, pas la dimension totale du modèle. n compte les clés ; i désigne celle dont on veut le poids, j parcourt les clés dans la somme Σ. exp(x) signifie e puissance x. Les scores et les poids sont des nombres sans unité physique. Pour une requête, la sortie comporte n poids scalaires positifs ou nuls après masquage, totalisant un.

CALCUL PAS À PAS
1. Les scores sont [1 ; 0 ; 1] et dₖ = 2.
2. Diviser par √2 ≈ 1,414 donne [0,707 ; 0 ; 0,707].
3. Exponentier donne environ [2,028 ; 1 ; 2,028].
4. Additionner : le dénominateur vaut environ 5,056.
5. Diviser chaque terme : les poids valent environ [0,401 ; 0,198 ; 0,401]. Vérifier 0,401 + 0,198 + 0,401 = 1.

HYPOTHÈSES ET PIÈGE
Ces trois clés sont autorisées. Avec un masque, ajouter −∞ au score interdit avant softmax, ce qui donne un poids nul. Il faut au moins une clé autorisée par ligne. Diviser par √dₖ contrôle l’échelle des scores ; cela ne les transforme pas en cosinus. Pour la stabilité, soustraire le maximum des scores mis à l’échelle avant l’exponentielle : la distribution reste identique.

QUESTION / RÉPONSE
« Si tous les scores autorisés sont nuls ? » Les exponentielles valent toutes un, donc les trois poids valent un tiers. « Sur quel axe normaliser ? » Sur les clés, séparément pour chaque requête.

REPÈRES DU CORPS DE DIAPOSITIVE
• Scores : [1, 0, 1] ; d_k = 2.
• Scores divisés par √2 : [0,707 ; 0 ; 0,707].
• Exponentielles ≈ [2,03 ; 1 ; 2,03].

SOURCE LATEX DE LA FORMULE
a_i=\frac{\exp(s_i/\sqrt{d_k})}{\sum_{j=1}^{n}\exp(s_j/\sqrt{d_k})}

Source de l'image de formule — LaTeX
a_i=\frac{\exp(s_i/\sqrt{d_k})}{\sum_{j=1}^{n}\exp(s_j/\sqrt{d_k})}

Légende projetée
sᵢ = qᵀkᵢ : score face à la clé i
dₖ : nombre de coordonnées par clé
n : nombre de clés ; i, j : indices
exp : exponentielle ; Σ : somme sur les clés
aᵢ : poids attribué à la valeur i

Scores [1 ; 0 ; 1], dₖ = 2 → poids ≈ [0,401 ; 0,198 ; 0,401] ; somme = 1.

- https://arxiv.org/abs/1706.03762

## 33. Étape 3 · Mélanger les valeurs

Jour 2 · matin · 10 min

ANIMATION — 10 min
4 min de calcul coordonnée par coordonnée, 3 min de variante, 3 min de correction. Lire la table des poids et valeurs avant de regarder le résultat.

LECTURE ORALE
« Le vecteur de sortie o est la somme, pour les trois positions, du poids a indice i multiplié par le vecteur de valeur v indice i. » Le poids est un nombre ; il multiplie toutes les coordonnées du vecteur correspondant.

SYMBOLES, DIMENSIONS ET UNITÉS
i parcourt les trois clés et leurs valeurs associées. aᵢ est le poids scalaire sans unité calculé par softmax ; les trois poids somment à un. vᵢ est ici un vecteur de deux caractéristiques apprises, donc de dimension dᵥ = 2. Σ additionne des vecteurs de même dimension. o possède aussi deux coordonnées : l’attention ne transforme pas directement cette sortie en mot. Pour plusieurs requêtes, on assemble leurs lignes et le produit matriciel A V a la forme nombre de requêtes × dᵥ.

CALCUL PAS À PAS
1. Multiplier a_A = 0,401 par v_A = (2,0) : contribution (0,802 ; 0).
2. Multiplier a_B = 0,198 par v_B = (0,2) : contribution (0 ; 0,396).
3. Multiplier a_C = 0,401 par v_C = (2,2) : contribution (0,802 ; 0,802).
4. Additionner les premières coordonnées : 0,802 + 0 + 0,802 = 1,604.
5. Additionner les secondes : 0 + 0,396 + 0,802 = 1,198. Les écarts avec un calcul logiciel proviennent des poids arrondis.

HYPOTHÈSES ET PIÈGE
Conserver Q, K et le masque garde les poids constants, même si V change. Ne pas remplacer V par K : K sert à choisir les contributions et V porte leur contenu. Des poids d’attention observés ne prouvent pas à eux seuls la cause complète d’une décision du réseau.

QUESTION / RÉPONSE
« Si v_B devient (0,20), que change-t-on ? » Son poids reste 0,198 ; sa contribution devient (0 ; 3,96). La sortie arrondie devient (1,604 ; 4,762). Le changement de contenu ne recalcule pas les compatibilités.

REPÈRES DU CORPS DE DIAPOSITIVE


SOURCE LATEX DE LA FORMULE
\mathbf{o}=\sum_{i=1}^{3}a_i\mathbf{v}_i\approx\begin{pmatrix}1{,}604\\1{,}198\end{pmatrix}

Source de l'image de formule — LaTeX
\mathbf{o}=\sum_{i=1}^{3}a_i\mathbf{v}_i\approx\begin{pmatrix}1{,}604\\1{,}198\end{pmatrix}

Légende projetée
aᵢ : poids de la position i
vᵢ : vecteur de valeur à 2 coordonnées
Σ : addition des 3 contributions pondérées
o : vecteur de sortie, dimension 2

0,401(2,0) + 0,198(0,2) + 0,401(2,2) ≈ (1,604 ; 1,198).



## 34. Le masque causal empêche de lire la réponse future

Jour 2 · matin · 10 min

CONCEPT ET ANIMATION
DÉROULÉ : 3 min de lecture de la matrice, 4 min de masque sur papier, 3 min de correction. À la position de colis, le modèle peut utiliser Le et colis pour prédire arrive, mais pas regarder arrive directement. Le masque triangulaire exprime cette restriction pour toutes les positions simultanément. Ajouter une valeur extrêmement négative aux scores interdits fait tendre leur exponentielle vers zéro ; cela se fait avant le softmax.

QUESTION : mettre les poids interdits à zéro après softmax sans renormaliser donne-t-il la même opération ? RÉPONSE : non, la somme des poids devient généralement inférieure à un. Distinguer le masque causal du masque de padding : le premier interdit l'accès au futur, le second aux positions artificielles de remplissage. Les deux peuvent se combiner. Faire vérifier que chaque ligne garde au moins une clé autorisée pour éviter un softmax indéfini.

Dans le TP, on compare les sorties avec et sans masque et on explique pourquoi une loss d'entraînement sans masque pourrait être trompeusement basse pour une tâche autorégressive. COMPLÉMENT À EXPLICITER : Le padding et la causalité répondent à deux besoins distincts.

LECTURE GUIDÉE DU SCHÉMA
1. Lire les lignes comme les positions qui interrogent et les colonnes comme les positions qu’elles peuvent consulter. La position courante et le passé restent visibles ; le futur est interdit pour ce décodeur causal.
2. Avec « Le | colis | arrive », la ligne « colis » consulte « Le » et « colis », mais pas « arrive ». L’accès à soi est autorisé : la sortie de cette position servira à prédire le token suivant.
3. Les cases masquées correspondent à un ajout de −∞ avant softmax, donc à des poids nuls. Les flèches autorisées transportent le contexte ; elles ne transportent pas les labels de référence directement vers la prédiction.
4. Distinguer causalité et padding : le futur contient de vrais tokens interdits par la tâche, alors que le padding remplit des places artificielles. Les masques se combinent mais ne signifient pas la même chose.
5. Le schéma représente une famille causale de type GPT/Qwen. Un encodeur de type BERT peut consulter les deux côtés de l’entrée valide ; il ne reçoit pas automatiquement ce triangle causal. Question : une bonne loss sans masque démontre-t-elle une bonne génération ? Non, elle peut profiter des cibles futures.

REPÈRES DU CORPS DE DIAPOSITIVE À EXPLICITER
• Ajouter −∞ aux scores interdits avant softmax.
Table de référence — Requête / clé | Le | colis | arrive
Le | visible | masqué | masqué
colis | visible | visible | masqué
arrive | visible | visible | visible

Description accessible du schéma
Matrice de masque causal quatre par quatre : zéro sur et sous la diagonale, moins l’infini au-dessus. La troisième position ne lit que les trois premières positions.
Le masque s’ajoute aux scores avant softmax : le futur reçoit une probabilité nulle.

Repères associés à l'illustration
Ajouter −∞ aux scores interdits avant softmax.
Requête / clé | Le | colis | arrive
Le | visible | masqué | masqué
colis | visible | visible | masqué
arrive | visible | visible | visible

- https://huggingface.co/learn/llm-course/fr/chapter1/6

## 35. Plusieurs têtes : plusieurs comparaisons apprises

Jour 2 · matin · 10 min

CONCEPT ET ANIMATION
DÉROULÉ : 4 min de schéma, 3 min de calcul de dimensions, 3 min de critique. Partir de deux lecteurs examinant la même phrase avec des critères différents. Cette analogie motive plusieurs comparaisons, mais ne signifie pas qu'une tête serait programmée pour les sujets et une autre pour la politesse. Pour le Transformer standard illustré, répartir 256 dimensions entre huit têtes donne 32 dimensions par tête. Le facteur d'échelle de chaque tête dépend alors de racine de 32.

QUESTION : huit têtes signifient-elles huit modèles indépendants ? RÉPONSE : non ; leurs résultats sont combinés dans un réseau entraîné conjointement. Indiquer que certaines architectures modernes utilisent des nombres différents de têtes de requêtes et de clés/valeurs ; ce bonus ne change pas le calcul jouet. Faire identifier l'erreur « diviser par racine de 256 dans chaque tête de dimension 32 ».

Dans le TP, deux jeux de projections construits permettront d'observer des poids différents sur la même entrée. Exiger un commentaire sur ce qui a été calculé, sans inventer une interprétation linguistique à partir de quelques couleurs.

LECTURE GUIDÉE DU SCHÉMA
1. Suivre la même séquence d’entrée vers plusieurs branches : chaque tête possède ses projections Q, K et V et effectue son propre calcul d’attention.
2. Dans le cas standard illustré, d_model = 256 et h = 8 donnent d_k = d_v = 32 par tête. Chaque facteur de mise à l’échelle utilise √32, pas √256.
3. Les flèches parallèles aboutissent à huit sorties de dimension 32 par token. La concaténation les place côte à côte et reconstitue 256 coordonnées ; elle n’en fait pas une moyenne.
4. La projection de sortie mélange ensuite ces 256 coordonnées. Toutes les têtes sont entraînées conjointement dans le même réseau.
5. Les branches distinctes ne signifient pas une tête « sujet », une tête « verbe » ou une autre compétence garantie. Certaines architectures utilisent des clés/valeurs partagées ou d’autres conventions ; ce schéma explique le multi-head standard. Question : huit têtes sont-elles huit modèles indépendants ? Non, leurs sorties alimentent les couches communes.

REPÈRES DU CORPS DE DIAPOSITIVE À EXPLICITER
• Chaque tête utilise ses propres projections Q, K et V.
• Les sorties sont concaténées puis reprojetées.
• Exemple : d_model = 256 et 8 têtes → d_k = 32.
• Les têtes ne portent pas des rôles linguistiques garantis.

Description accessible du schéma
Deux branches d’attention parallèles reçoivent X, utilisent des projections différentes, puis rejoignent une concaténation et une projection de sortie WO.
Chaque tête apprend ses projections ; leurs sorties sont concaténées puis reprojetées.

Repères associés à l'illustration
Chaque tête utilise ses propres projections Q, K et V.
Les sorties sont concaténées puis reprojetées.
Exemple : d_model = 256 et 8 têtes → d_k = 32.
Les têtes ne portent pas des rôles linguistiques garantis.

- https://arxiv.org/abs/1706.03762

## 36. Un bloc ne se limite pas à l'attention

Jour 2 · matin · 10 min

CONCEPT ET ANIMATION
DÉROULÉ : 4 min d'assemblage, 3 min d'exemple numérique, 3 min de questions. Dessiner x puis une transformation f(x), avec un chemin direct qui produit x + f(x). Si x = [1,2] et f(x) = [0,5,−0,5], la somme vaut [1,5,1,5] ; il ne s'agit ni d'une concaténation ni d'une moyenne obligatoire. Le MLP est appliqué aux représentations de chaque position avec des paramètres partagés ; l'attention a déjà échangé de l'information entre positions.

QUESTION : le résiduel signifie-t-il que le réseau ne peut rien oublier ? RÉPONSE : non, les transformations suivantes peuvent modifier l'information, mais le chemin direct facilite le passage des représentations et des gradients. Présenter la normalisation comme un contrôle d'échelle interne, sans la confondre avec le softmax sur les clés. L'ordre exact des opérations et le type de normalisation varient selon les architectures ; le schéma est une lecture fonctionnelle.

Dans le TP, l'inspection du modèle doit retrouver ces familles de composants, sans exiger de réimplémenter tout le Transformer.

LECTURE GUIDÉE DU SCHÉMA
1. Ce dessin montre explicitement un bloc Post-LN de type BERT : lire entrée → self-attention → addition résiduelle + normalisation → MLP/FFN → addition résiduelle + normalisation → sortie.
2. Une flèche de contournement transporte l’entrée d’un sous-bloc jusqu’à l’addition correspondante. L’autre branche transporte sa transformation. Les deux tenseurs doivent avoir la même forme pour l’addition ; ce n’est pas une concaténation.
3. L’attention échange de l’information entre positions. Le FFN transforme ensuite les caractéristiques de chaque position avec les mêmes paramètres appliqués à toutes les positions ; ses dimensions internes peuvent s’élargir puis revenir à d_model.
4. La normalisation porte sur les caractéristiques selon la définition de la couche ; elle n’est pas le softmax sur les clés. Les axes du batch et de la longueur restent présents dans l’entrée et la sortie.
5. L’ordre Post-LN ne doit pas être présenté comme universel : des architectures causales utilisent une normalisation avant les sous-couches, et des variantes comme RMSNorm. Question : peut-on déplacer la normalisation sans changer le modèle ? Non, cela définit une autre organisation du bloc.

REPÈRES DU CORPS DE DIAPOSITIVE À EXPLICITER
Accroche : Attention + réseau positionnel + connexions résiduelles + normalisation.
• L'attention échange de l'information entre positions.
• Le MLP transforme les caractéristiques à chaque position.
• Le chemin résiduel additionne entrée et transformation.
• La normalisation contrôle l'échelle des représentations.

Description accessible du schéma
Un bloc Post-LN relie entrée, attention, addition du premier résidu, LayerNorm, réseau positionnel FFN, addition du second résidu, LayerNorm et sortie.
Exemple Post-LN de type BERT ; d’autres Transformers placent la normalisation autrement.

Repères associés à l'illustration
Attention + réseau positionnel + connexions résiduelles + normalisation.
L'attention échange de l'information entre positions.
Le MLP transforme les caractéristiques à chaque position.
Le chemin résiduel additionne entrée et transformation.
La normalisation contrôle l'échelle des représentations.

- https://arxiv.org/abs/1607.06450
- https://arxiv.org/abs/1512.03385

## 37. Sans information de position, l'ordre manque

Jour 2 · matin · 10 min

DÉROULÉ : 3 min d'exemple, 4 min de discussion en binôme, 3 min de correction. Reprendre les deux phrases du titre : le sac de mots échoue parce que les comptes ne disent pas qui rembourse qui. Une self-attention sans information de position possède une propriété d'équivariance aux permutations ; elle ne dispose pas directement de l'ordre à partir des identités seules. L'information positionnelle donne un moyen de le prendre en compte. QUESTION : ajouter le nombre de position à l'identifiant du token suffit-il ? RÉPONSE : non, le modèle utilise une représentation ou une transformation conçue et apprise dans son architecture, pas une modification arbitraire des adresses du vocabulaire. Donner l'intuition de positions absolues et de relations relatives sans dérouler toutes les formules. Les modèles modernes peuvent employer des rotations des requêtes et clés ; c'est une extension. Faire discuter un long échange dont l'information importante est au milieu : accepter une longueur ne garantit pas de retrouver tous les détails. Le TP limitera volontairement les longueurs pour maîtriser le coût et observer la troncature.



- https://arxiv.org/abs/2104.09864

## 38. Encodeur, décodeur, encodeur-décodeur

Jour 2 · matin · 10 min

CONCEPT ET ANIMATION
DÉROULÉ : 4 min de comparaison, 3 min de choix par tâche, 3 min de justification. L'encodeur peut faire dépendre la représentation d'un token des mots à gauche et à droite de l'entrée, sous réserve du masque de padding. Le décodeur causal construit une sortie en ne consultant que le préfixe autorisé. L'encodeur-décodeur encode une entrée puis génère une sortie en consultant aussi cette représentation via cross-attention.

QUESTION : un décodeur peut-il faire de la classification ? RÉPONSE : oui, par génération contrainte ou avec une tête adaptée ; le tableau indique des usages fréquents, pas une interdiction. De même, un résumé peut être obtenu par un décodeur instructionnel, ce que nous ferons avec un petit modèle. Faire choisir une famille pour extraire les noms présents dans un message puis pour rédiger une réponse. Demander quel objet est évalué : labels alignés ou texte généré.

Dans le TP, DistilBERT multilingue et Qwen illustrent deux usages ; leur comparaison ne permet pas de conclure que toute une famille est supérieure à l'autre. Le nom BERT du titre du cours désigne la famille illustrée par DistilBERT multilingue. Le nom GPT renvoie à l'architecture causale ; Qwen utilisé au TP est un autre checkpoint de cette famille, pas un modèle GPT d'OpenAI.

LECTURE GUIDÉE DU SCHÉMA
1. Lire chaque architecture comme une chaîne entrée → représentations → sortie ; comparer surtout les accès au contexte, pas les couleurs des boîtes.
2. L’encodeur de type BERT reçoit une séquence et contextualise chaque position avec les tokens valides des deux côtés. Une tête adaptée produit ensuite un label global ou des labels par token. Un encodeur seul n’est pas automatiquement un générateur causal.
3. Le décodeur de type GPT/Qwen reçoit un préfixe, utilise une attention causale puis produit des logits de prochain token. Le token choisi est réinjecté dans le préfixe pour continuer. Cette génération reste autorégressive même si les positions d’entraînement sont calculées ensemble.
4. L’encodeur-décodeur de type T5 encode la source. Son décodeur consulte son propre préfixe par self-attention causale et les représentations source par cross-attention. La flèche entre encodeur et décodeur transporte le contexte source, pas les futurs mots cibles.
5. Les usages ne sont pas des interdictions : un décodeur peut classifier via un prompt et résumer sans encodeur séparé. Les TP emploient DistilBERT multilingue, dérivé de BERT, et Qwen pour la famille causale ; Qwen n’est pas un checkpoint GPT d’OpenAI.

REPÈRES DU CORPS DE DIAPOSITIVE À EXPLICITER
• BERT : encodeur ; GPT : décodeur causal ; T5 : encodeur-décodeur.
Table de référence — Famille | Contexte consulté | Exemple d'usage
Encodeur | Toute l'entrée valide | Classification, NER
Décodeur causal | Préfixe disponible | Génération de texte
Encodeur-décodeur | Entrée + préfixe de sortie | Traduction, résumé

Description accessible du schéma
Trois colonnes comparent BERT encodeur bidirectionnel, GPT décodeur causal, et T5 avec encodeur, décodeur causal et liaison de cross-attention depuis le texte source.
BERT encode ; GPT génère causalement ; T5 relie encodeur et décodeur par cross-attention.

Repères associés à l'illustration
BERT : encodeur ; GPT : décodeur causal ; T5 : encodeur-décodeur.
Famille | Contexte consulté | Exemple d'usage
Encodeur | Toute l'entrée valide | Classification, NER
Décodeur causal | Préfixe disponible | Génération de texte
Encodeur-décodeur | Entrée + préfixe de sortie | Traduction, résumé

- https://huggingface.co/learn/llm-course/fr/chapter1/5
- https://huggingface.co/learn/llm-course/fr/chapter1/7

## 39. Préentraînement et adaptation ne répondent pas à la même question

Jour 2 · matin · 10 min

DÉROULÉ : 3 min de comparaison des objectifs, 4 min d'appariement exemple-objectif, 3 min de correction. Écrire « Le colis est [MASK] » et « Le colis est… ». Dans le premier cas, le modèle peut disposer d'un contexte de droite ; dans le second, il prédit une continuation à partir du préfixe. Les objectifs construisent des représentations utiles, mais ne donnent pas automatiquement nos cinq labels de support. QUESTION : charger un modèle préentraîné avec une nouvelle tête à cinq sorties fournit-il déjà un classifieur fiable ? RÉPONSE : non ; la tête peut être initialisée aléatoirement et doit apprendre la correspondance. Distinguer checkpoint de base, checkpoint adapté à une tâche et modèle instructionnel. Le terme préentraîné décrit une histoire d'apprentissage, pas une garantie d'adéquation. Faire demander aux étudiants ce qu'ils doivent lire dans une model card avant utilisation : langue, tâche, licence, données et limites. L'après-midi, le modèle masqué sert à observer le contexte, tandis que le jour 3 entraînera réellement la tête et l'encodeur sur notre jeu.



- https://huggingface.co/learn/llm-course/fr/chapter1/10
- https://arxiv.org/abs/1810.04805

## 40. Décomposer pipeline() pour savoir ce qui se passe

Jour 2 · matin · 10 min

CONCEPT ET ANIMATION
DÉROULÉ : 3 min de schéma, 4 min d'inspection guidée, 3 min de questions. Présenter pipeline comme une interface pratique qui assemble des opérations, pas comme une nouvelle architecture. Le tokenizer convertit le texte ; le modèle produit des logits ou d'autres tenseurs ; le post-traitement transforme ces sorties en objets lisibles. Pour une tâche masquée, on récupère des candidats de tokens ; pour une classification, des labels et scores ; pour une génération, une continuation.

QUESTION : pourquoi préciser le modèle plutôt que laisser un défaut ? RÉPONSE : pour connaître la langue, la tâche et la version effectivement testées. Faire lire un identifiant de modèle, puis chercher la dimension des sorties.

Dans le TP, utiliser distilbert/distilbert-base-multilingual-cased pour le langage masqué ne signifie pas qu'il connaît nos cinq intentions. Un score élevé sur une suggestion lexicale n'atteste pas que la phrase est vraie. Demander une prédiction avant exécution sur une phrase contenant une négation. Le jour 3 remplacera cette commodité par une lecture plus explicite du tokenizer, du collator et du Trainer.

LECTURE GUIDÉE DU SCHÉMA
1. Commencer par le texte brut et la tâche explicitement choisie. Le tokenizer crée les identifiants, masques et éventuels tokens spéciaux ; la flèche représente une préparation des données.
2. Le modèle reçoit les tenseurs, pas directement les mots affichés. Il produit des sorties numériques dont la forme dépend de la tâche : logits de classes, logits de tokens ou représentations.
3. Le post-traitement interprète ces sorties : top-k de tokens pour fill-mask, scores de classes pour une classification, ou texte décodé pour une génération. Le label lisible dépend de la configuration sauvegardée.
4. pipeline() assemble ces étapes mais ne crée pas une nouvelle architecture et n’entraîne pas automatiquement un modèle. Le checkpoint doit être compatible avec la tâche choisie.
5. Dans notre démonstration masquée, DistilBERT propose des candidats de token. Il ne connaît pas pour autant nos cinq intentions de support. Question : que signifie une flèche vers un score élevé ? Une transformation numérique dans cette tâche, pas une validation factuelle ni une mesure de fiabilité métier.

REPÈRES DU CORPS DE DIAPOSITIVE À EXPLICITER
Accroche : Prétraitement → tenseurs → modèle → post-traitement.
• Choisir explicitement la tâche et le checkpoint.
• Inspecter tokenizer, formes et configuration des labels.
• Ne pas confondre score du modèle et fiabilité métier.
• Comparer une phrase normale et une phrase piège.

Description accessible du schéma
Un message est tokenisé en identifiants et masque, traité par le modèle qui produit des logits, puis post-traité pour obtenir une catégorie.
pipeline() assemble ces étapes ; inspecter chacune aide à localiser une erreur.

Repères associés à l'illustration
Prétraitement → tenseurs → modèle → post-traitement.
Choisir explicitement la tâche et le checkpoint.
Inspecter tokenizer, formes et configuration des labels.
Ne pas confondre score du modèle et fiabilité métier.
Comparer une phrase normale et une phrase piège.

- https://huggingface.co/learn/llm-course/fr/chapter2/2

## 41. Décoder : choisir parmi plusieurs suites possibles

Jour 2 · matin · 10 min

DÉROULÉ : 4 min d'explication, 3 min de calcul de noyau, 3 min de critique. Donner la distribution [0,50 ; 0,30 ; 0,15 ; 0,05]. Avec top-p = 0,8, les deux premiers candidats suffisent car leur masse cumulée atteint 0,8 ; leurs probabilités sont ensuite renormalisées avant tirage. Avec top-k = 3, on conserve les trois premiers. QUESTION : une température plus faible rend-elle le modèle plus exact ? RÉPONSE : elle modifie la diversité, pas la connaissance ni la fidélité aux faits. Pour des logits [2,0], T = 1 donne environ [0,88,0,12], tandis que T = 2 donne environ [0,73,0,27]. Préciser que ces réglages interviennent dans le décodage, sans changer les poids appris. Dans les API, do_sample contrôle l'échantillonnage ; une température fournie avec un décodage glouton n'est pas un test valide de diversité. Le TP conservera le prompt et le modèle, ne changera qu'un réglage à la fois, et enregistrera plusieurs sorties lorsque le tirage est aléatoire.



- https://huggingface.co/docs/transformers/main_classes/text_generation

## 42. Observer une génération avec un protocole

Jour 2 · matin · 10 min

DÉROULÉ : 3 min de conception, 4 min en binôme, 3 min de discussion. Proposer une demande précise : « Résume en une phrase : le colis AB123 est arrivé mardi avec un article manquant. » Avant toute exécution, demander les faits qui doivent être conservés et ceux qui ne peuvent pas être inventés. Un modèle peut produire une réponse fluide mais remplacer mardi par mercredi ou inventer un remboursement. QUESTION : une réponse courte est-elle forcément une bonne réponse ? RÉPONSE : non, la contrainte de longueur est distincte de la fidélité. Expliquer max_new_tokens comme un plafond de tokens générés, pas de mots ni de longueur totale du prompt. Le template de conversation du tokenizer prépare les rôles attendus par le modèle ; le texte brut et la version instructionnelle ne sont pas interchangeables sans vérification. Le TP emploie Qwen/Qwen2.5-0.5B-Instruct pour rendre les expériences accessibles, avec des capacités modestes à documenter. Enregistrer une table de résultats ; ne pas sélectionner uniquement la sortie la plus flatteuse parmi plusieurs essais.



- https://huggingface.co/docs/transformers/chat_templating
- https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct

## 43. Pouvez-vous expliquer l'attention sans le schéma ?

Jour 2 · matin · 15 min

DÉROULÉ : 4 min individuelles, 5 min d'explication entre pairs, 6 min de correction. Réponse 1 : K sert à calculer les compatibilités ; V contient l'information à combiner. Réponse 2 : 32, donc racine de 32, même si la dimension totale du modèle est 256. Réponse 3 : les positions interdites doivent recevoir une probabilité nulle au sein d'une distribution normalisée sur les positions autorisées. Réponse 4 : pour un échantillonnage, la distribution devient plus ou moins concentrée ; les paramètres du modèle ne changent pas et l'exactitude n'est pas garantie. Ajouter une question orale : quelle est la forme de la matrice d'attention pour quatre requêtes et six clés ? Réponse : 4 × 6, avant les axes de batch et de têtes. Demander à un binôme d'expliquer les trois étapes avec des mots avant de ressortir les symboles. Si le calcul reste fragile, le premier atelier dispose d'un chemin entièrement numérique avec vérification des sommes et des dimensions.





## 44. TP 2A · Refaire QKᵀ, softmax et AV

Jour 2 · apres-midi · 60 min

ORGANISATION : 10 min de reprise des nombres, 20 min de construction du calcul, 15 min d'expériences, 15 min de correction croisée. Ouvrir notebooks/etudiants/02_j2_attention_transformers.ipynb. Le calcul est exécutable sur CPU ; il constitue la priorité avant le téléchargement de modèles. POINT DE CONTRÔLE : afficher séparément scores bruts, scores mis à l'échelle, poids et sortie ; vérifier que le nombre de poids correspond au nombre de clés. Faire expliquer une multiplication à la main par chaque membre du binôme. RÉSULTAT ATTENDU : les poids correspondent aux valeurs prévues à l'arrondi près. Si le softmax est appliqué sur le mauvais axe, exploiter l'erreur : quelle somme vaut un et quelle question le calcul répond-il alors ? EXTENSION : comparer la stabilité numérique avec de grands scores et une soustraction du maximum. Chaque modification doit avoir une prédiction écrite avant l'exécution. Le but n'est pas de réécrire une bibliothèque complète mais de rendre le mécanisme vérifiable.





## 45. TP 2B · Rendre le futur inaccessible

Jour 2 · apres-midi · 60 min

ORGANISATION : 15 min sur le masque, 15 min sur le padding, 15 min sur les têtes, 15 min d'analyse. POINT DE CONTRÔLE : un étudiant choisit une position et montre exactement quelles clés elle peut consulter. Les poids masqués doivent être nuls et les poids autorisés former une distribution, sauf cas invalide explicitement détecté. Faire comparer la sortie d'une position avant et après modification d'un token futur ; dans une attention causale correctement construite à cette étape, cette modification ne doit pas influencer la position antérieure. RÉSULTAT ATTENDU : la causalité devient une propriété testée, pas une couleur sur un schéma. Pour les têtes, vérifier la dimension d_k après séparation. EXTENSION : créer volontairement une ligne entièrement masquée et expliquer les valeurs non définies. Débrief : un masque incorrect peut donner une excellente performance d'entraînement grâce à une information indisponible lors de l'usage. Cette expérience relie les calculs du jour aux principes de fuite de données du jour 1.





## 46. TP 2C · Observer un encodeur préentraîné

Jour 2 · apres-midi · 60 min

ORGANISATION : 10 min de lecture de la model card, 15 min de chargement et formes, 20 min d'expériences, 15 min de restitution. Modèle : distilbert/distilbert-base-multilingual-cased. Le notebook utilise la tâche de langage masqué pour observer l'effet du contexte ; il ne faut pas appeler cela un entraînement de classification. POINT DE CONTRÔLE : remplacer le bon marqueur de masque fourni par le tokenizer, puis montrer le nombre de candidats et les scores. RÉSULTAT ATTENDU : les suggestions changent avec le contexte, mais peuvent être inadaptées au métier ou linguistiquement imparfaites. Faire comparer « Je me rends à [MASK] » à une phrase qui désambiguïse un lieu. Si le modèle ne télécharge pas, poursuivre avec les formes de tenseurs et le calcul d'attention, en marquant l'observation du modèle comme non exécutée. EXTENSION : choisir une phrase où un seul masque ne correspond pas à un mot entier et expliquer la limite liée aux sous-mots. Ne pas interpréter le score de token comme une preuve factuelle.



- https://huggingface.co/distilbert/distilbert-base-multilingual-cased

## 47. TP 2D · Comparer les stratégies de génération

Jour 2 · apres-midi · 60 min

ORGANISATION : 10 min de préparation, 20 min de générations contrôlées, 15 min d'évaluation, 15 min de restitution. Le T4 améliore la durée de l'expérience ; le mode réduit limite le nombre de demandes et les tokens produits. POINT DE CONTRÔLE : vérifier que les variantes utilisent le même message rendu par le template et que do_sample correspond au réglage étudié. Enregistrer toutes les sorties de l'expérience, y compris les ratés. RÉSULTAT ATTENDU : la diversité peut varier sans que la fidélité s'améliore. Demander un cas où la version gloutonne est erronée et un cas où une sortie échantillonnée respecte mieux ou moins bien la consigne. EXTENSION : tester deux formulations de prompt en conservant un décodage fixe. Ne pas mélanger cette expérience avec une comparaison de modèles. Faire écrire la conclusion sous forme conditionnelle : « Sur nos demandes et avec ces réglages… ». Conserver le modèle et les habitudes d'inspection pour les jours 4 et 5.



- https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct

## 48. Jour 3 · Adapter un modèle à une tâche

Jour 3 · matin · 5 min

DURÉE : 5 min. Reprendre le résultat du jour 2 : un modèle préentraîné possède des régularités générales mais ne connaît pas automatiquement les cinq catégories de notre support. Aujourd'hui, les exemples annotés définissent la tâche. Présenter les deux granularités : une décision pour tout le message en classification ; une décision alignée sur les mots en NER. Le même encodeur peut servir de base, mais la tête et la structure des labels changent. Annoncer que la difficulté la plus instructive sera souvent l'alignement des données et l'évaluation, pas l'appel à Trainer. Les petits jeux servent à comprendre la boucle, pas à garantir un gain face à TF-IDF. Les artefacts sauvegardés permettront une réutilisation au jour 5 sans dépendre d'une session Colab restée ouverte. Dans les 140 minutes de classification, le parcours support occupe 100 minutes et une extension réelle Allociné 40 minutes. Cette dernière adapte un classifieur de sentiment binaire sur 1000 critiques train, 200 validation et 200 test ; son artefact est exporté séparément et n'est pas le routeur support utilisé au jour 5. LIVRABLE DE LA JOURNÉE : À produire : modèles sauvegardés et erreurs comparées à la baseline.



- https://huggingface.co/learn/llm-course/fr/chapter3/1

## 49. Un encodeur et une tête répondent à notre question

Jour 3 · matin · 10 min

CONCEPT ET ANIMATION
DÉROULÉ : 4 min d'explication, 3 min de suivi d'un exemple, 3 min de questions. Prendre « Impossible de modifier mon mot de passe » et suivre son trajet : tokenizer, encodeur, représentation utilisée par la tête, cinq logits. Les labels sont livraison, facturation, compte, retour et technique ; leur ordre numérique doit être conservé pendant entraînement, sauvegarde et inférence.

QUESTION : si l'on inverse deux noms de labels après entraînement, le réseau s'en aperçoit-il ? RÉPONSE : non, les mêmes nombres seront affichés sous de mauvais noms. Une tête neuve comporte des paramètres non entraînés pour cette tâche ; l'avertissement de chargement correspondant peut donc être attendu, mais doit être compris. Distinguer geler l'encodeur et entraîner seulement la tête d'un fine-tuning de tous les paramètres autorisés. Ce sont deux expériences différentes. Le TP commence avec une configuration explicitement documentée. Faire vérifier la forme batch × nombre de classes des logits, puis montrer que softmax les transforme en distribution sans fournir une garantie de calibration.

LECTURE GUIDÉE DU SCHÉMA
1. Lire message → tokenizer → encodeur préentraîné → représentation utilisée pour la décision → tête de classification → cinq logits. Les cinq sorties correspondent à livraison, facturation, compte, retour et technique selon le mapping sauvegardé.
2. L’encodeur retourne d’abord des représentations par position. La stratégie de lecture globale dépend du modèle ; ne pas imposer à toutes les architectures une moyenne ou un pooler BERT absent du checkpoint réel.
3. La tête transforme cette représentation globale en un vecteur de cinq nombres par message. Le softmax utilisé à l’inférence donne des scores de classes ; la loss d’entraînement reçoit les logits selon l’API.
4. Une flèche depuis le vrai label vers la loss exprime la comparaison supervisée. Le label ne fait pas partie du message d’entrée. Les gradients reviennent vers les paramètres autorisés : tête et encodeur dans le fine-tuning complet du TP.
5. L’encodeur peut être préentraîné alors que la tête à cinq sorties est neuve. Question : charger cette tête suffit-il pour parler de zéro-shot fiable ? Non, elle doit apprendre la correspondance avec les intentions. Les sorties sont batch × 5, distinctes des sorties NER batch × longueur × labels.

REPÈRES DU CORPS DE DIAPOSITIVE À EXPLICITER
Accroche : Message → représentations → tête à 5 sorties → scores de classes.
• Le checkpoint apporte des paramètres préentraînés.
• La tête relie la représentation aux labels de notre tâche.
• id2label et label2id doivent rester cohérents.
• Le fine-tuning peut mettre à jour l'encodeur et la tête.

Description accessible du schéma
Un encodeur transforme quatre tokens en quatre vecteurs. Une branche agrège une représentation globale vers cinq classes ; une autre conserve les quatre positions vers des logits NER.
Une tête globale prédit une classe ; une tête NER prédit des labels par token.

Repères associés à l'illustration
Message → représentations → tête à 5 sorties → scores de classes.
Le checkpoint apporte des paramètres préentraînés.
La tête relie la représentation aux labels de notre tâche.
id2label et label2id doivent rester cohérents.
Le fine-tuning peut mettre à jour l'encodeur et la tête.

- https://huggingface.co/docs/transformers/tasks/sequence_classification

## 50. La loss pénalise la probabilité donnée à la bonne réponse

Jour 3 · matin · 10 min

ANIMATION — 10 min
4 min de calcul, 3 min de classement d’exemples, 3 min de correction. Comparer deux modèles face au même message et au même label de référence.

LECTURE ORALE
« La loss de cet exemple est l’opposé du logarithme naturel de la probabilité attribuée à la vraie classe y. » Ce n’est pas le logarithme de la probabilité de la classe prédite si celle-ci est fausse.

SYMBOLES, DIMENSIONS ET UNITÉS
y est un indice entier parmi C classes. Le réseau produit C logits, c’est-à-dire C scores réels avant normalisation. Leur softmax produit C probabilités positives qui somment à un ; pᵧ désigne la composante correspondant au vrai label. ln est le logarithme naturel de base e. L est un scalaire non négatif pour cet exemple ; avec un logarithme naturel, on parle de nats, unité conventionnelle d’information. Une loss de batch agrège les exemples selon la réduction choisie, souvent une moyenne.

CALCUL PAS À PAS
1. La vraie classe est compte et le modèle lui attribue pᵧ = 0,8.
2. ln(0,8) ≈ −0,223 ; changer le signe donne L ≈ 0,223.
3. Un autre modèle attribue pᵧ = 0,2 : ln(0,2) ≈ −1,609, donc L ≈ 1,609.
4. Pour pᵧ = 0,5, la pénalité vaut environ 0,693. Classer ces trois modèles selon leur pénalité sur cet exemple.

HYPOTHÈSES ET PIÈGE
Il s’agit d’une classification à label unique, sans pondération ni label smoothing dans cette explication. Quand pᵧ tend vers zéro, la pénalité augmente sans borne ; une implémentation numérique stable travaille à partir des logits. CrossEntropyLoss attend normalement les logits : ne pas lui appliquer auparavant un softmax simplement parce que la formule pédagogique utilise pᵧ. Une baisse de loss train ne démontre ni généralisation ni amélioration de chaque classe.

QUESTION / RÉPONSE
« Un modèle peut-il améliorer sa loss sans changer son argmax ? » Oui : il peut donner davantage de probabilité à la bonne classe tout en gardant le même label prédit. Le TP suit aussi macro-F1 et les erreurs concrètes.

REPÈRES DU CORPS DE DIAPOSITIVE
• Si p(correcte) = 0,8 : L ≈ 0,223.
• Si p(correcte) = 0,2 : L ≈ 1,609.
• La cible indique la classe correcte ; les logits viennent du modèle.

SOURCE LATEX DE LA FORMULE
\mathcal{L}=-\ln(p_y)

Source de l'image de formule — LaTeX
\mathcal{L}=-\ln(p_y)

Légende projetée
y : indice de la vraie classe
pᵧ : probabilité donnée à cette classe
ln : logarithme naturel, base e
L : loss scalaire, exprimée en nats

pᵧ = 0,8 → L ≈ 0,223 ; pᵧ = 0,2 → L ≈ 1,609 : moins croire la vraie classe coûte davantage.

- https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html

## 51. Une étape d'apprentissage en cinq actions

Jour 3 · matin · 10 min

DÉROULÉ : 4 min pour suivre une étape, 3 min d'ordonnancement de cartes, 3 min de correction. Expliquer le gradient comme une information locale sur la direction de modification des paramètres pour réduire la loss. L'optimiseur applique une mise à jour contrôlée par le learning rate et son état. En PyTorch, les gradients s'accumulent tant qu'on ne les remet pas à zéro ; cette propriété est parfois utilisée volontairement. QUESTION : l'évaluation doit-elle mettre à jour les poids ? RÉPONSE : non, on mesure le modèle avec un mode adapté et sans calcul de gradients inutile. Faire distinguer model.train(), qui configure certains comportements comme le dropout, de l'appel qui déclenche réellement une optimisation. Trainer automatise cette orchestration mais ne décide pas si les données ou les métriques sont correctes. Dans le TP, identifier les objets qui fournissent modèle, arguments, jeux, tokenizer, collator et métriques. Le but est de pouvoir localiser une erreur : données avant le forward, labels dans la loss, réglages dans la boucle, ou post-traitement dans l'évaluation.



- https://huggingface.co/learn/llm-course/fr/chapter3/4

## 52. Padding dynamique : payer pour le batch réel

Jour 3 · matin · 10 min

DÉROULÉ : 4 min de calcul, 3 min de comparaison en binôme, 3 min de correction. Trois phrases de longueur 12, 20 et 25 demandent 3×128 = 384 positions si tout est complété à 128. Un padding dynamique au maximum du batch demande 3×25 = 75 positions. Avec une phrase de 120 tokens, le gain tombe à 24 positions. QUESTION : le padding dynamique garantit-il toujours un entraînement plus rapide ? RÉPONSE : il réduit souvent le travail inutile, mais le gain dépend du matériel, des formes et de l'implémentation. Certaines configurations arrondissent les longueurs à un multiple efficace ; il faut observer la mesure réelle. Distinguer padding et troncature : le premier ajoute des places, la seconde supprime une partie de l'entrée. Troncature peut retirer l'indice déterminant placé en fin de message. Dans le TP, inspecter un batch après le collator plutôt que seulement le dataset avant assemblage. Les étudiants doivent expliquer la forme des input_ids et de l'attention_mask, puis vérifier les positions ignorées dans les labels quand la tâche l'exige. COMPLÉMENT À EXPLICITER : Le masque indique les positions de remplissage.



- https://huggingface.co/learn/llm-course/fr/chapter3/2

## 53. Batch, pas et époque : ne pas mélanger les compteurs

Jour 3 · matin · 10 min

ANIMATION — 10 min
4 min de calcul, 3 min de variantes, 3 min de correction. Faire distinguer un passage dans le réseau et une mise à jour de l’optimiseur.

LECTURE ORALE
« Le batch effectif vaut le batch par GPU, multiplié par le nombre de micro-batchs accumulés, multiplié par le nombre de GPU qui traitent des données différentes. » La formule compte les exemples qui contribuent à une mise à jour complète.

SYMBOLES, DIMENSIONS ET UNITÉS
B_GPU est un nombre d’exemples par micro-batch sur chaque GPU. A est le nombre entier de micro-batchs dont les gradients s’accumulent avant l’optimiseur ; ici A n’est pas la matrice LoRA ni la matrice d’attention, car les notations sont locales aux diapositives. G est le nombre de GPU en parallélisme de données. B_eff est exprimé en exemples par mise à jour. Une époque est un passage sur le jeu, indépendamment de cette formule.

CALCUL PAS À PAS
1. Avec B_GPU = 8, A = 4 et G = 1, calculer 8 × 4 × 1 = 32 exemples par mise à jour complète.
2. Sur 240 exemples, un GPU traite 240/8 = 30 micro-batchs par époque.
3. Sept groupes de quatre micro-batchs consomment 28 micro-batchs, soit 224 exemples.
4. Le groupe restant contient deux micro-batchs, soit 16 exemples : si le Trainer le conserve et effectue une mise à jour finale, on observe huit mises à jour, dont la dernière est partielle.

HYPOTHÈSES ET PIÈGE
La formule suppose des micro-batchs complets et de même taille, des exemples distincts par GPU et un parallélisme de données. Le dernier groupe, drop_last et le Trainer peuvent modifier le compte exact. Accumuler économise les activations simultanées mais coûte des passages supplémentaires ; cela n’est pas identique dans tout détail à un batch physique de 32. Le learning rate règle l’amplitude de la mise à jour, pas le nombre d’exemples.

QUESTION / RÉPONSE
« Augmenter A charge-t-il les quatre lots simultanément ? » Non : on les traite successivement et on conserve leurs gradients accumulés. Vérifier les compteurs réels du TP avant d’annoncer une durée.

REPÈRES DU CORPS DE DIAPOSITIVE
• Exemple : 240 exemples et batch 8 → 30 micro-batchs par époque.
• Accumulation 4 → environ 8 mises à jour, selon le dernier groupe.
• Le learning rate contrôle l'amplitude des mises à jour.

SOURCE LATEX DE LA FORMULE
B_{\mathrm{eff}}=B_{\mathrm{GPU}}\times A\times G

Source de l'image de formule — LaTeX
B_{\mathrm{eff}}=B_{\mathrm{GPU}}\times A\times G

Légende projetée
B_GPU : exemples par micro-batch et par GPU
A : nombre de micro-batchs accumulés
G : nombre de GPU en parallèle de données
B_eff : exemples par mise à jour complète

8 exemples/GPU × 4 micro-batchs accumulés × 1 GPU = 32 exemples par mise à jour complète.

- https://huggingface.co/docs/transformers/main_classes/trainer

## 54. Choisir le modèle sur validation, conclure sur test

Jour 3 · matin · 10 min

DÉROULÉ : 3 min de rappel, 4 min de scénario de sélection, 3 min de correction. Donner trois checkpoints dont les macro-F1 de validation sont 0,72, 0,78 et 0,75, alors que la loss train continue de baisser. Le checkpoint retenu est celui choisi par le critère déclaré, ici le deuxième. QUESTION : peut-on prendre le troisième parce que son score test est meilleur ? RÉPONSE : cela utilise le test pour sélectionner et invalide son rôle d'estimation finale indépendante. Une fois le résultat test observé, les prochaines décisions appartiennent à un nouveau cycle de développement et demandent idéalement une nouvelle évaluation indépendante. Faire discuter ce qu'il faut faire lorsque validation est minuscule : interpréter prudemment les différences, inspecter les exemples et éviter de présenter un dixième de point comme décisif. Dans le TP, l'objectif est la traçabilité d'une comparaison, pas une recherche massive d'hyperparamètres. Les graines et versions améliorent la reproductibilité mais n'effacent pas toutes les variations matérielles. Conserver la configuration réellement exécutée à côté du modèle sauvegardé.



- https://scikit-learn.org/stable/modules/cross_validation.html

## 55. Macro-F1 : donner une voix à chaque classe

Jour 3 · matin · 10 min

ANIMATION — 10 min
4 min de calcul, 3 min d’interprétation, 3 min de correction. Commencer par une seule classe considérée face à toutes les autres.

LECTURE ORALE
« F un est deux fois précision fois rappel, divisé par précision plus rappel. Le macro-F un est la somme des F un de chaque classe, divisée par le nombre de classes. » Distinguer ces deux niveaux d’agrégation.

SYMBOLES, DIMENSIONS ET UNITÉS
P est la précision : vrais positifs divisés par vrais positifs plus faux positifs. R est le rappel : vrais positifs divisés par vrais positifs plus faux négatifs. F₁ est leur moyenne harmonique, qui pénalise un déséquilibre entre les deux. C est le nombre de classes évaluées ; c est l’indice parcouru dans la somme ; F₁,c est le score de la classe c. Tous les scores sont des scalaires sans unité entre zéro et un. Le support est le nombre d’exemples vrais d’une classe : il se rapporte à côté du score mais ne pondère pas la moyenne macro.

CALCUL PAS À PAS
1. Pour une classe, prendre 4 vrais positifs, 1 faux positif et 4 faux négatifs.
2. P = 4/(4+1) = 0,8 ; R = 4/(4+4) = 0,5.
3. Le numérateur de F₁ vaut 2 × 0,8 × 0,5 = 0,8 ; le dénominateur vaut 1,3.
4. F₁ = 0,8/1,3 ≈ 0,615.
5. Dans un autre exemple à deux classes, des F₁ de 0,90 et 0,30 donnent (0,90+0,30)/2 = 0,60. Ne pas recalculer F₁ à partir de la moyenne des précisions et des rappels : ce serait généralement différent.

HYPOTHÈSES ET PIÈGE
Définir les classes incluses dans l’agrégation et la convention lorsque les dénominateurs sont nuls. Afficher les effectifs : un score sur trois exemples reste fragile. Macro n’est ni micro ni pondéré, et l’égalité de poids des classes ne démontre pas l’équité envers tous les sous-groupes.

QUESTION / RÉPONSE
« Une classe fréquente pèse-t-elle davantage dans macro-F1 ? » Non, chaque F1 de classe a le même poids. Dans le TP, lire aussi la matrice de confusion et les cinq lignes par classe.

REPÈRES DU CORPS DE DIAPOSITIVE
• Précision : parmi mes prédictions de la classe, lesquelles sont justes ?
• Rappel : parmi les vrais exemples de la classe, lesquels sont retrouvés ?
• Macro : toutes les classes ont le même poids.

SOURCE LATEX DE LA FORMULE
F_1=\frac{2PR}{P+R},\qquad F_{1,\mathrm{macro}}=\frac{1}{C}\sum_{c=1}^{C}F_{1,c}

Source de l'image de formule — LaTeX
F_1=\frac{2PR}{P+R},\qquad F_{1,\mathrm{macro}}=\frac{1}{C}\sum_{c=1}^{C}F_{1,c}

Légende projetée
P : précision ; R : rappel d’une classe
F₁ : moyenne harmonique de P et R
C : nombre de classes ; c : indice
F₁,c : F1 calculé pour la classe c
F₁,macro : moyenne des C scores par classe

TP = 4, FP = 1, FN = 4 → P = 0,8 ; R = 0,5 ; F₁ ≈ 0,615. Deux F₁ de 0,9 et 0,3 donnent macro = 0,6.

- https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html

## 56. Diagnostiquer avant de multiplier les époques

Jour 3 · matin · 10 min

DÉROULÉ : 3 min de lecture, 4 min de diagnostic en binôme, 3 min de correction. Préciser que le tableau donne des hypothèses, pas des diagnostics automatiques. Un score presque parfait peut provenir d'une vraie tâche simple ; on vérifie avant de conclure à une fuite. Une loss constante peut venir de paramètres gelés, de labels erronés ou d'un learning rate inadapté. QUESTION : pourquoi ne pas augmenter directement les époques quand le modèle échoue ? RÉPONSE : cela peut amplifier une erreur de données et consommer le budget sans résoudre la cause. Faire proposer la vérification la moins coûteuse pour chaque ligne. Un petit batch sur lequel le modèle arrive à surapprendre peut servir de test de fonctionnement de la chaîne, mais n'évalue aucune généralisation. Dans le TP, l'étudiant doit montrer un batch brut, les labels et la forme des logits avant de demander une aide sur l'optimiseur. En cas de mémoire GPU insuffisante, réduire batch et longueur puis relancer proprement ; ne pas charger plusieurs modèles simultanément sans besoin. Noter les modifications effectuées dans le journal.



- https://huggingface.co/learn/llm-course/fr/chapter8/4

## 57. NER : retrouver des segments et leur type

Jour 3 · matin · 10 min

DÉROULÉ : 4 min d'annotation, 3 min de nouvel exemple, 3 min de correction. Les types PER et LOC illustrent la convention ; le notebook décrit son schéma réel d'entités et ses identifiants. B signifie début, I intérieur ou continuation, O extérieur. Marie Dupont forme une seule entité à deux mots. QUESTION : pourquoi ne pas écrire PER sur les deux mots sans B et I ? RÉPONSE : les marqueurs aident à distinguer les frontières, notamment lorsque deux entités de même type se suivent. Faire annoter « Marie rencontre Paul à Lyon ». Les deux personnes commencent chacune par B-PER. La NER ne consiste pas à connaître tout ce qui est vrai sur Marie ; elle repère un segment selon un schéma défini. Une entité peut ne pas être un nom de personne : dans le support, une référence de commande peut être utile si son type est défini. Souligner l'importance des limites : inclut-on un titre, une apostrophe, un article ? Le TP applique une convention fixe et mesure les segments complets, pas seulement le nombre de mots correctement étiquetés.



- https://huggingface.co/learn/llm-course/fr/chapter7/2

## 58. Un mot annoté peut devenir plusieurs sous-tokens

Jour 3 · matin · 10 min

CONCEPT ET ANIMATION
DÉROULÉ : 4 min d'alignement guidé, 3 min sur un deuxième exemple, 3 min de correction. Les sous-tokens affichés sont illustratifs : utiliser le tokenizer réel pour connaître le découpage exact. Le jeu est annoté au niveau des mots, tandis que le modèle reçoit des sous-tokens. word_ids permet de relier chaque sous-token à son mot d'origine ; les tokens spéciaux ont généralement une valeur None. Nous choisissons ici de conserver le label sur le premier sous-token et d'ignorer les suivants dans la loss.

QUESTION : le deuxième morceau de Dupont est-il alors invisible au modèle ? RÉPONSE : non ; il reste dans l'entrée et peut contribuer aux représentations, mais il n'ajoute pas une cible supervisée. Une autre convention propage les labels à tous les morceaux, en adaptant B vers I pour les continuations ; elle doit être appliquée de manière cohérente. Le TP inspecte les alignements avant l'entraînement. Faire montrer la correspondance sur un nom long et un mot avec apostrophe pour rendre les erreurs immédiatement visibles.

LECTURE GUIDÉE DU SCHÉMA
1. Suivre trois niveaux alignés : mots annotés, sous-tokens réellement lus, puis cibles de loss. Les flèches de word_ids relient chaque sous-token à son mot d’origine.
2. Dans l’exemple illustratif, Marie porte word_id 0 et B-PER ; Du puis ##pont portent tous deux word_id 1, car ils représentent Dupont. Le découpage exact dépend du tokenizer et doit être observé dans le TP.
3. Notre convention conserve I-PER sur Du, premier sous-token du deuxième mot de l’entité, et met −100 sur ##pont. Les tokens spéciaux ont word_id None et une cible −100.
4. −100 indique une position ignorée par la loss, pas une nouvelle classe. La flèche du sous-token vers l’encodeur existe toujours : ##pont reste lisible dans le contexte avec attention_mask = 1.
5. Lors de l’évaluation, utiliser le même filtrage pour garder une cible et une prédiction par mot selon cette convention. Question : pourquoi ne pas supprimer ##pont de l’entrée ? Le nom serait modifié et le contexte perdu. Le schéma dissocie clairement visibilité de l’entrée et supervision de la sortie.

REPÈRES DU CORPS DE DIAPOSITIVE À EXPLICITER
• Convention du TP : superviser le premier sous-token de chaque mot.
Table de référence — Token illustratif | word_id | Label retenu
<début> | None | −100
Marie | 0 | B-PER
Du | 1 | I-PER
##pont | 1 | −100
<fin> | None | −100

Description accessible du schéma
Marie, Dupont et Lyon sont alignés avec CLS, Marie, Du, double dièse pont, Lyon et SEP. Les labels sont moins cent, B-PER, I-PER, moins cent, B-LOC, moins cent.
Convention du TP : superviser le premier sous-token ; −100 ignore les autres dans la loss.

Repères associés à l'illustration
Convention du TP : superviser le premier sous-token de chaque mot.
Token illustratif | word_id | Label retenu
<début> | None | −100
Marie | 0 | B-PER
Du | 1 | I-PER
##pont | 1 | −100
<fin> | None | −100

- https://huggingface.co/docs/transformers/tasks/token_classification

## 59. Deux masques, deux questions différentes

Jour 3 · matin · 10 min

DÉROULÉ : 4 min de distinction, 3 min de cas à classer, 3 min de correction. Reprendre le sous-token ##pont : il peut avoir attention_mask = 1 et label = -100. Le réseau a besoin de le lire pour représenter le nom, même si notre convention n'évalue que le premier morceau. Un token de padding doit être exclu du contexte utile et de la loss selon la configuration de la tâche. QUESTION : -100 est-il une classe supplémentaire à prédire ? RÉPONSE : non, c'est une valeur ignorée par la fonction de loss utilisée ici. Les logits ne comportent pas une catégorie nommée -100. Faire diagnostiquer une implémentation qui ajoute cette valeur à id2label : elle mélange cible et convention de calcul. La valeur d'ignore_index relève de l'API, il faut la vérifier plutôt que la supposer pour tout framework. Dans le TP, afficher un batch complet après DataCollatorForTokenClassification. Le test important est la correspondance entre positions valides, labels supervisés et mots reconstruits. Cette distinction sera réutilisée au jour 4 pour superviser seulement la réponse d'un exemple SFT.



- https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html
- https://huggingface.co/docs/transformers/main_classes/data_collator

## 60. Des logits aux entités : ne pas perdre l'alignement

Jour 3 · matin · 10 min

DÉROULÉ : 4 min de suivi d'un exemple, 3 min de reconstruction en binôme, 3 min de correction. Pour un batch de deux phrases de longueur dix et sept labels, les logits ont la forme 2 × 10 × 7. L'argmax sur le dernier axe donne une classe par position. Il faut ensuite filtrer les positions dont la cible vaut -100 pour comparer des séquences alignées selon notre convention. QUESTION : peut-on aplatir toutes les phrases et passer une liste de labels à la métrique ? RÉPONSE : la métrique de segments a besoin des frontières de séquences ; concaténer peut créer ou fusionner des entités à tort. Faire présenter texte, mots, tokens, cibles et prédictions côte à côte. Un bon score par token dominé par O peut masquer un modèle qui ne retrouve aucune entité complète. Le décodage naïf par argmax peut produire une séquence BIO invalide ; le comportement de la métrique et l'éventuel post-traitement doivent être documentés. Dans le TP, le tableau de reconstruction est le principal point de contrôle avant l'appel à seqeval.



- https://huggingface.co/docs/transformers/tasks/token_classification

## 61. En NER, la frontière fait partie de la réponse

Jour 3 · matin · 10 min

DÉROULÉ : 4 min de jugement manuel, 3 min de calcul, 3 min de correction. Sur trois entités de référence et trois entités prédites, si seule AB123 a les bonnes frontières et le bon type, la précision et le rappel stricts valent tous deux un tiers ; F1 vaut donc un tiers. Le modèle peut pourtant avoir correctement étiqueté beaucoup de tokens O. QUESTION : repérer Marie au lieu de Marie Dupont mérite-t-il un crédit ? RÉPONSE : une métrique de recouvrement partiel pourrait le faire, mais le score strict affiché ici exige la correspondance exacte ; il faut nommer la règle. Présenter seqeval comme un outil de calcul dont le mode et le schéma comptent. Les séquences invalides peuvent être interprétées différemment selon les réglages ; inspecter les options et les tests jouets du notebook. Dans le TP, calculer à la main un cas de frontière puis vérifier le résultat logiciel. Ne jamais comparer un F1 par token avec un F1 par entité comme si l'unité d'évaluation était identique. COMPLÉMENT À EXPLICITER : Préciser schéma BIO/IOB2 et mode strict de la métrique.



- https://github.com/chakki-works/seqeval

## 62. Une convention d'annotation vaut mieux qu'un débat sans règle

Jour 3 · matin · 10 min

DÉROULÉ : 2 min d'annotation individuelle, 5 min de comparaison, 3 min de rédaction d'une règle. Proposer « Mme Dupont travaille chez Orange à Orange ». Le même texte Orange désigne une organisation puis un lieu selon le contexte. Ne pas imposer une réponse sans expliquer le schéma : l'exercice montre pourquoi une simple liste de mots ne suffit pas. QUESTION : que signifie un désaccord entre modèle et référence si la référence est ambiguë ? RÉPONSE : il peut s'agir d'un défaut du guide d'annotation ou d'un exemple nécessitant arbitrage, pas automatiquement d'un défaut du réseau. Demander une règle courte avec un exemple positif et un contre-exemple. Distinguer corriger une erreur démontrée de label et réécrire le test pour améliorer son score : toute correction doit être documentée et ne doit pas être opportuniste. Le corpus fictif du TP peut rendre certaines formes d'entités trop régulières ; signaler cette limite. Pour un vrai projet, prévoir un échantillon relu par plusieurs annotateurs et une procédure de résolution. Le jour 5 réutilisera cette logique dans l'analyse d'erreurs.





## 63. Comparer un Transformer à la baseline équitablement

Jour 3 · matin · 10 min

DÉROULÉ : 3 min de lecture, 4 min de conception d'une table, 3 min de discussion. Le Transformer consomme des tokens et la baseline des termes TF-IDF ; cette différence est précisément ce que l'on veut comparer. En revanche, changer simultanément les exemples de test et la métrique empêche d'attribuer le résultat au modèle. QUESTION : si le Transformer gagne d'un point sur un très petit test, peut-on conclure qu'il est meilleur ? RÉPONSE : on peut rapporter le résultat observé, mais il faut examiner l'incertitude, les erreurs et le coût. Une baseline peut rester préférable si la différence est fragile et si elle se recharge en une fraction du temps. Faire proposer des colonnes : modèle, configuration, taille test, macro-F1, temps d'entraînement, temps d'inférence, mémoire et limites. Les durées doivent préciser le matériel et exclure ou inclure les téléchargements de manière cohérente. Dans le TP, privilégier une analyse de cinq cas où les méthodes divergent. Le jour 5 ajoutera une baseline zéro-shot avec un petit LLM et la même discipline de comparaison.





## 64. Sauvegarder pour recharger, pas seulement pour archiver

Jour 3 · matin · 10 min

DÉROULÉ : 3 min de scénario de perte de session, 4 min de checklist concrète, 3 min de discussion. Un entraînement terminé n'est pas un livrable réutilisable si ses poids restent uniquement en mémoire du notebook. La sauvegarde doit contenir les fichiers nécessaires au modèle et au tokenizer, ainsi que les noms des labels. QUESTION : pourquoi tester après rechargement alors que la prédiction fonctionne avant sauvegarde ? RÉPONSE : le rechargement révèle les dépendances cachées à l'état de la session, au mapping ou à une variable non sauvegardée. Faire choisir trois phrases de contrôle, enregistrer les sorties, puis comparer le comportement après rechargement en mode évaluation. Ne pas promettre une identité bit à bit entre tous matériels ; vérifier au minimum la cohérence attendue dans l'environnement utilisé. Le TP exporte une archive pour le jour 5 et un fichier de prédictions avec identifiants. Les caches de téléchargement ne remplacent pas cette archive. Aucun identifiant d'accès au Hub ne doit se retrouver dans les notebooks ou fichiers exportés. La publication en ligne sera optionnelle et séparée de la preuve locale.



- https://huggingface.co/learn/llm-course/fr/chapter4/3

## 65. Du batch à la métrique : retrouver les responsabilités

Jour 3 · matin · 15 min

DÉROULÉ : 4 min de réponses, 5 min de confrontation, 6 min de correction. Réponse 1 : non, la mémorisation et les fuites peuvent donner un résultat trompeur. Réponse 2 : le token peut rester utile au contexte tout en étant ignoré dans la supervision, comme une continuation de sous-mot selon notre convention. Réponse 3 : c'est une erreur de frontière pour une évaluation stricte de l'entité complète. Réponse 4 : le tokenizer et la configuration, notamment id2label et label2id, sont nécessaires à une inférence cohérente. Ajouter un mini-cas : les labels prédits sont tous « livraison » alors que le score semble bon ; demander trois contrôles avant de modifier le learning rate. Attendre distribution, mapping, métrique et lecture d'exemples. Les réponses doivent être argumentées avec une opération du pipeline. Pendant la correction, identifier les binômes qui ont besoin d'un accompagnement sur word_ids ; le premier bloc NER leur donne le temps de valider l'alignement avant de lancer l'apprentissage.





## 66. TP 3A · Préparer et entraîner le classifieur

Jour 3 · apres-midi · 70 min

ORGANISATION : 15 min de préparation des groupes et de la baseline, 15 min de vérification des batchs, 25 min d'entraînement et d'exercices pendant l'attente, 15 min de première évaluation. Ouvrir notebooks/etudiants/03_j3_classification.ipynb. Les cinq labels du parcours support sont livraison, facturation, compte, retour et technique. Ce bloc de 70 minutes commence les 100 minutes consacrées au support ; le bloc suivant ajoute 30 minutes de comparaison/export puis 40 minutes Allociné. POINT DE CONTRÔLE : montrer un texte, son label numérique, les dimensions du batch et les cinq logits avant le lancement. RÉSULTAT ATTENDU : une boucle cohérente et une configuration réellement exécutée, sans promesse de score. Sur CPU, utiliser le chemin réduit et indiquer sa portée. Pendant le calcul, travailler l'analyse de la baseline ou le macro-F1. En cas de mémoire insuffisante, modifier un seul levier. Les versions, tailles et réductions du corpus doivent être conservées avec les résultats. La suite du TP ne mélange pas intention support et sentiment cinéma.





## 67. TP 3B · Comparer puis transférer à des critiques réelles

Jour 3 · apres-midi · 70 min

ORGANISATION : 30 min pour terminer les 100 minutes du parcours support, puis 40 min pour l'extension réelle Allociné ; le total du notebook reste 140 minutes. D'abord comparer TF-IDF et DistilBERT sur les mêmes identifiants support, lire leurs désaccords et exporter l'archive rechargeable destinée au jour 5. Ensuite inspecter la provenance et le schéma du jeu Allociné, charger 1000 critiques train, 200 validation et 200 test, puis suivre le chemin d'adaptation borné du notebook. La tâche change : sentiment binaire d'une critique, pas cinq intentions de support. POINT DE CONTRÔLE : vérifier le nouveau mapping, les tailles effectives et la séparation des sorties de fichiers. RÉSULTAT ATTENDU : comparer l'expérience fictive très contrôlée à des formulations réelles, en documentant l'entraînement effectivement réalisé. Aucun gain de score n'est promis. L'export Allociné reste séparé ; il ne doit jamais être rechargé comme routeur client au projet. Si le téléchargement ou le budget GPU bloque, marquer l'extension non exécutée et conserver le protocole reproductible. Les quarante minutes sont incluses dans la journée, sans devoir caché en supplément.



- https://huggingface.co/datasets/tblard/allocine

## 68. TP 3C · Aligner les mots, les sous-tokens et les labels

Jour 3 · apres-midi · 50 min

ORGANISATION : 10 min de lecture du schéma, 20 min d'alignement, 10 min de cas difficiles, 10 min de vérification croisée. Ouvrir notebooks/etudiants/04_j3_ner.ipynb. Chaque binôme doit expliquer au moins une phrase contenant un mot découpé en plusieurs tokens. POINT DE CONTRÔLE : les positions supervisées correspondent exactement à la convention choisie et chaque label numérique est relié au nom attendu. Vérifier le batch après collator, car le padding intervient à cet endroit. RÉSULTAT ATTENDU : aucun token spécial ni continuation ignorée ne contribue à la loss. Le texte et les tokens restent visibles pour la contextualisation selon leur masque. Si l'alignement échoue, ne pas lancer l'entraînement pour « voir si cela passe ». EXTENSION : comparer sur papier la supervision du premier sous-token et la propagation des labels, en adaptant les étiquettes B/I. Le corrigé sert à vérifier l'explication, pas seulement à copier une fonction. Faire verbaliser pourquoi -100 ne représente pas une nouvelle catégorie d'entité.





## 69. TP 3D · Mesurer des entités complètes

Jour 3 · apres-midi · 50 min

ORGANISATION : 20 min d'entraînement court et de calcul manuel, 15 min d'évaluation, 10 min de sauvegarde, 5 min de restitution. POINT DE CONTRÔLE : comparer une entité partielle, une entité de mauvais type et une entité exacte avec le résultat de la métrique. RÉSULTAT ATTENDU : un score d'entités dont le schéma et le mode sont connus, accompagné d'exemples reconstruits au niveau des mots. Ne pas remplacer ce score par une accuracy dominée par les tokens O. Si le calcul prend plus de temps que prévu, terminer les évaluations manuelles et sauvegarder l'état disponible en indiquant le nombre de pas exécutés. EXTENSION : demander à un autre binôme une phrase contenant une entité de même forme dans un contexte différent. Le petit corpus fictif ne prouve pas la robustesse à des noms ou des documents réels. La restitution finale doit préciser ce que le modèle a appris, ce que l'alignement garantit et ce que l'évaluation ne permet pas encore de conclure.



- https://github.com/chakki-works/seqeval

## 70. Jour 4 · Adapter un petit LLM efficacement

Jour 4 · matin · 5 min

DURÉE : 5 min. Revenir au vocabulaire : préentraînement apprend de nombreuses régularités ; SFT adapte un comportement à partir d'exemples supervisés. Notre objectif n'est pas de créer un grand modèle généraliste, mais d'observer une adaptation contrôlée sur un petit modèle instructionnel. Le checkpoint retenu est Qwen/Qwen2.5-0.5B-Instruct afin de limiter les besoins. Un T4 reste une ressource contrainte et sa disponibilité sur Colab gratuit n'est pas garantie. LoRA sera la voie pédagogique principale ; la quantification 4 bits constitue une variante explicitement mesurée, pas une promesse que tout modèle tient en mémoire. Annoncer qu'un meilleur respect du format n'est pas automatiquement une meilleure connaissance. Le résumé sert ensuite à montrer qu'une réponse bien rédigée peut perdre ou inventer un fait. Si un accès Runpod L4 par étudiant est fourni, il constitue une extension d'exécution du même protocole. Vérifier le GPU, la précision et les versions avant d'utiliser le notebook ; rapporter les mesures L4 séparément de celles du T4. Le parcours principal reste autonome sur Colab T4. LIVRABLE DE LA JOURNÉE : À produire : adaptateur, comparaison avant/après et audit de faits.



- https://huggingface.co/learn/llm-course/en/chapter11/1

## 71. Prompt, RAG ou fine-tuning : quel problème résoudre ?

Jour 4 · matin · 10 min

DÉROULÉ : 3 min de comparaison, 4 min de choix sur cas, 3 min de discussion. Donner trois besoins : répondre en JSON, connaître le stock du jour, utiliser systématiquement un ton de support. Le premier peut souvent commencer par une consigne et une validation de format ; le stock réclame un accès aux données pertinentes ; le style peut motiver une adaptation si les prompts ne suffisent pas. QUESTION : le fine-tuning est-il une base documentaire fiable ? RÉPONSE : il peut modifier les associations du modèle, mais ne garantit ni rappel exact ni mise à jour contrôlée des faits. RAG désigne ici la recherche de documents ajoutés au contexte avant génération ; ce module en explique le choix sans construire un système complet. Les approches peuvent se combiner. Dans le TP, on compare le modèle de base et l'adaptateur avec le même prompt et les mêmes cas réservés. Faire nommer l'hypothèse attendue : améliorer le format ou le comportement observé, pas acquérir magiquement toutes les connaissances du domaine. Le choix final dépend d'une mesure et des contraintes d'exploitation.



- https://arxiv.org/abs/2005.11401
- https://huggingface.co/learn/llm-course/en/chapter11/1

## 72. SFT : montrer les réponses que l'on souhaite obtenir

Jour 4 · matin · 10 min

DÉROULÉ : 4 min de définition, 3 min de construction d'un exemple, 3 min de correction. Prendre une demande de support et une réponse structurée qui reconnaît le problème sans inventer d'action réalisée. L'apprentissage reste une prédiction de tokens, mais les textes présentés sont des démonstrations du comportement recherché. QUESTION : SFT signifie-t-il que tous les poids sont nécessairement mis à jour ? RÉPONSE : non ; SFT décrit le type de supervision, tandis que LoRA décrit quels paramètres on entraîne. Il est possible de réaliser un SFT avec une adaptation complète ou avec des adaptateurs. Distinguer instruction, contexte et réponse cible. Une réponse cible qui affirme « votre remboursement est effectué » sans outil ni preuve enseigne précisément cette mauvaise habitude. Dans le TP, les données sont fictives et les réponses sont examinées avant entraînement. Faire écrire à chaque binôme une bonne et une mauvaise démonstration pour la même entrée. Les différences doivent être justifiées par un comportement observable. La baisse de loss indique une meilleure prédiction des exemples supervisés ; elle ne suffit pas à démontrer le transfert.



- https://huggingface.co/learn/llm-course/en/chapter11/2

## 73. Une bonne démonstration enseigne aussi les limites

Jour 4 · matin · 10 min

DÉROULÉ : 2 min de lecture, 5 min de rédaction en binôme, 3 min de comparaison. Demander une réponse courte qui ne dépasse pas l'information disponible. Le modèle peut reformuler une demande de vérification mais ne doit pas prétendre avoir consulté un compte bancaire ou réalisé un remboursement. QUESTION : faut-il enseigner uniquement des cas faciles avec toutes les informations ? RÉPONSE : non, sinon le modèle apprend mal à demander une précision ou à signaler une limite. Les cas ambigus et les demandes hors périmètre appartiennent à la distribution d'usage visée. Faire comparer deux réponses de forme identique dont l'une invente un délai et l'autre reste conditionnelle. Une consigne de style ne remplace pas la factualité. Dans le TP, les binômes auditent plusieurs paires prompt/completion avant le lancement. Les réponses peuvent être synthétiques à condition d'être identifiées comme telles et relues. La provenance, la licence et les données personnelles deviennent importantes pour tout jeu externe ; aucun texte réel de client n'est nécessaire à cet atelier pédagogique.





## 74. Curater : garder des exemples utiles et traçables

Jour 4 · matin · 10 min

DÉROULÉ : 3 min de méthode, 4 min d'audit de quatre paires, 3 min de décision. Proposer un doublon exact, une paraphrase, une réponse qui contredit l'entrée et un exemple beaucoup plus long que les autres. Demander lequel supprimer, regrouper ou corriger et quelle trace garder. Dédupliquer ne signifie pas supprimer aveuglément toutes les ressemblances : certaines variations sont utiles, mais elles doivent rester dans un même groupe lorsqu'elles dérivent du même scénario. QUESTION : augmenter le volume avec cent paraphrases d'un même exemple apporte-t-il cent fois plus d'information ? RÉPONSE : non, cela peut surtout surpondérer un scénario et faciliter la mémorisation. Introduire un journal de curation avec identifiant, action, motif et origine. Les longueurs doivent être mesurées après application du tokenizer et du template, car la troncature peut supprimer la réponse cible. Dans le TP, le petit jeu est choisi pour être auditable entièrement. Pour une extension réelle, on distingue les données consultables des données réutilisables selon leur licence. Une bonne documentation dit ce qui a été vérifié et ce qui reste incertain.



- https://huggingface.co/learn/llm-course/en/chapter10/1

## 75. Le chat template transforme les rôles en tokens

Jour 4 · matin · 10 min

CONCEPT ET ANIMATION
DÉROULÉ : 4 min de transformation visible, 3 min de comparaison de formats, 3 min de correction. Montrer une liste de deux messages et le texte produit par apply_chat_template. Les rôles sont représentés par des marqueurs que le modèle a appris à utiliser ; ils ne sont pas une couche magique indépendante du texte.

QUESTION : peut-on copier le template d'un autre modèle parce qu'il semble lisible ? RÉPONSE : cela peut introduire un décalage avec le format appris et dégrader le comportement. Le même checkpoint et son tokenizer doivent être employés en entraînement et à l'inférence. add_generation_prompt peut préparer le début d'une réponse selon le template ; son usage dépend de la phase et du format fourni. Ne pas fabriquer à la main une réponse assistant vide sans vérifier le rendu.

Dans le TP, afficher l'exemple réellement préparé avant le Trainer. Si le texte est d'abord rendu puis tokenisé, prendre garde à ne pas ajouter deux fois les tokens spéciaux. Le nombre de tokens final inclut consignes et marqueurs ; il conditionne la place disponible pour la réponse.

LECTURE GUIDÉE DU SCHÉMA
1. Commencer par les messages structurés et leurs rôles system, user et assistant. La flèche vers le chat template effectue une sérialisation déterministe compatible avec le tokenizer du checkpoint.
2. Le texte rendu contient des marqueurs de rôles, débuts ou fins selon le modèle. La flèche suivante tokenise cette chaîne en identifiants ; elle ne rajoute pas arbitrairement les marqueurs d’un autre modèle.
3. À l’entraînement, le rendu contient la réponse cible dans le format attendu. À la génération, le préfixe prépare le début de réponse selon le template et les options utilisées. Ne pas confondre les deux chemins.
4. Les marqueurs de rôle sont appris comme partie du format ; une boîte « system » ne crée pas une garantie extérieure au modèle. La sortie à inspecter est d’abord le rendu exact, puis la liste de tokens et leur longueur.
5. Question : peut-on rendre en texte puis tokeniser en ajoutant encore tous les tokens spéciaux ? Cela peut les doubler ; suivre l’API et vérifier l’entrée réelle. Pour Qwen, conserver ensemble checkpoint et tokenizer, y compris après rechargement de l’adaptateur.

REPÈRES DU CORPS DE DIAPOSITIVE À EXPLICITER
Accroche : Une liste de messages n'est pas encore l'entrée exacte du modèle.
• system, user et assistant ont des fonctions distinctes.
• Le tokenizer applique les marqueurs attendus par le checkpoint.
• Inspecter le texte rendu et les tokens spéciaux.
• Éviter de doubler manuellement les marqueurs de début ou de fin.

Description accessible du schéma
Les messages system, user et assistant deviennent un texte avec marqueurs im_start et im_end, puis le tokenizer produit les identifiants des marqueurs et du contenu.
Exemple de marqueurs Qwen ; utiliser le template associé au checkpoint.

Repères associés à l'illustration
Une liste de messages n'est pas encore l'entrée exacte du modèle.
system, user et assistant ont des fonctions distinctes.
Le tokenizer applique les marqueurs attendus par le checkpoint.
Inspecter le texte rendu et les tokens spéciaux.
Éviter de doubler manuellement les marqueurs de début ou de fin.

- https://huggingface.co/docs/transformers/chat_templating

## 76. Superviser la réponse, garder la question dans le contexte

Jour 4 · matin · 10 min

CONCEPT ET ANIMATION
DÉROULÉ : 4 min de lecture, 3 min de surlignage des tokens, 3 min de vérification. La question reste indispensable pour conditionner la réponse, mais nous ne voulons pas optimiser le modèle pour reproduire les tokens du prompt dans cette expérience. Le notebook utilise un format conversationnel prompt/completion avec completion_only_loss=True. Il ne suppose pas que le template fournisse un masque assistant compatible : assistant_only_loss est explicitement désactivé dans cette configuration.

QUESTION : ces deux options sont-elles simplement deux noms pour la même chose ? RÉPONSE : non ; elles s'appuient sur des structures et des mécanismes différents. Le contrôle décisif consiste à inspecter les labels du batch produit par le Trainer et à décoder les positions qui contribuent à la loss. Les marqueurs de réponse supervisés dépendent du format réellement préparé. Faire montrer que des tokens du prompt portent -100 tout en restant accessibles à l'attention. Si la troncature retire toute la completion, l'exemple ne fournit plus le signal attendu.

Dans le TP, ce point de contrôle précède obligatoirement l'entraînement. COMPLÉMENT À EXPLICITER : Vérifier le batch réel : labels ignorés = −100.

LECTURE GUIDÉE DU SCHÉMA
1. Lire deux lignes superposées sur les mêmes positions : la séquence visible au modèle et la séquence de cibles qui contribuent à la loss. Les frontières prompt/completion structurent la supervision.
2. Consigne et question appartiennent au prompt : elles restent visibles au contexte mais leurs labels valent −100. Les positions de completion qui portent la réponse sont supervisées, sous le masque causal.
3. Le padding ne constitue pas un contexte utile et ne contribue pas à la loss. Cela ne le rend pas équivalent au prompt : le prompt contient de vraies informations conditionnantes.
4. Les flèches de contexte vont du préfixe autorisé vers la représentation ; les flèches de comparaison vont des logits vers les cibles. Aucune flèche ne doit suggérer que le modèle consulte un futur token pour prédire ce même token.
5. Le TP utilise completion_only_loss=True sur des objets prompt/completion et assistant_only_loss=False. Question : pourquoi inspecter le batch ? Le masque effectivement produit, les marqueurs et la troncature peuvent différer d’une supposition faite sur le texte initial. Décoder les positions dont label ≠ −100 avant d’entraîner.

REPÈRES DU CORPS DE DIAPOSITIVE À EXPLICITER
• Format prompt/completion ; completion_only_loss = True.
Table de référence — Segment | Visible au modèle | Contribue à la loss du TP
Consigne système | Oui | Non
Question utilisateur | Oui | Non
Réponse cible | Oui, causalement | Oui
Padding | Non comme contexte utile | Non

Description accessible du schéma
Une table distingue tokens, masque d’attention et labels. Les trois tokens de contexte ont attention un et label moins cent ; réponse et EOS sont supervisés ; PAD est masqué et ignoré.
Le prompt reste visible ; la loss porte ici sur la réponse et sa fin de séquence.

Repères associés à l'illustration
Format prompt/completion ; completion_only_loss = True.
Segment | Visible au modèle | Contribue à la loss du TP
Consigne système | Oui | Non
Question utilisateur | Oui | Non
Réponse cible | Oui, causalement | Oui
Padding | Non comme contexte utile | Non

- https://huggingface.co/docs/trl/sft_trainer

## 77. Le décalage causal ne doit se produire qu'une fois

Jour 4 · matin · 10 min

CONCEPT ET ANIMATION
DÉROULÉ : 4 min sur une séquence jouet, 3 min de diagnostic d'erreur, 3 min de correction. Écrire quatre tokens simplifiés : question, marqueur assistant, bonjour, fin. Pour générer bonjour, le modèle utilise le préfixe jusqu'au marqueur assistant. La classe causale et le Trainer effectuent les opérations de décalage prévues par leur contrat ; décaler manuellement les labels puis laisser le modèle les décaler à nouveau ferait apprendre une cible décalée de deux positions.

QUESTION : pourquoi vérifier la frontière entre prompt et completion ? RÉPONSE : c'est là qu'un masque mal construit peut supprimer le premier token de réponse ou superviser une partie inattendue du prompt. L'exemple est conceptuel ; on inspecte ensuite les tokens exacts du template réel. Faire distinguer trois mécanismes : masque causal pour les accès au contexte, labels -100 pour la supervision, décalage pour la prédiction suivante.

Dans le TP, afficher quelques positions avec input_id, token et label permet de détecter ces erreurs. Un simple entraînement qui « ne plante pas » ne prouve pas que la tâche optimisée est celle que l'on voulait.

LECTURE GUIDÉE DU SCHÉMA
1. Aligner une ligne de tokens d’entrée x₀, x₁, x₂… et une ligne de cibles suivantes x₁, x₂, x₃…. La flèche du logit produit à la position t doit arriver à la cible t+1.
2. Le calcul au temps t utilise le préfixe jusqu’à x_t inclus ; le masque causal empêche de lire x_{t+1} et la suite. Une entrée « Le | colis » permet au logit de la position « colis » de prédire « arrive ».
3. Dans le SFT, les positions de cible associées au prompt peuvent être ignorées par −100, tandis que les cibles de réponse comptent. Le premier token de réponse est prédit depuis la dernière position de son préfixe, pas depuis sa propre représentation future.
4. L’implémentation du modèle causal gère le décalage prévu par son contrat de loss. Le dataset peut donc présenter des labels alignés sur input_ids avant ce décalage interne : ne pas décaler encore manuellement.
5. Question : quel bug crée un décalage fait deux fois ? Le réseau apprend une cible trop éloignée d’une position supplémentaire. Inspecter quelques positions et leurs cibles, car une exécution sans erreur et une loss finie ne garantissent pas le bon alignement.

REPÈRES DU CORPS DE DIAPOSITIVE À EXPLICITER
Accroche : À chaque position, prédire le token suivant de la séquence supervisée.
• Le modèle causal calcule généralement le décalage interne de la loss.
• Le masque des labels précise quelles cibles comptent.
• Inspecter une paire entrée/cible à la frontière prompt-réponse.
• Une loss basse peut cacher une mauvaise préparation des labels.

Description accessible du schéma
Les entrées le, colis, arrive, demain, EOS sont alignées avec les cibles colis, arrive, demain, EOS, aucune. Les quatre premières sorties prédisent le token suivant.
Chaque logit à la position t vise le token t+1 ; appliquer ce décalage une seule fois.

Repères associés à l'illustration
À chaque position, prédire le token suivant de la séquence supervisée.
Le modèle causal calcule généralement le décalage interne de la loss.
Le masque des labels précise quelles cibles comptent.
Inspecter une paire entrée/cible à la frontière prompt-réponse.
Une loss basse peut cacher une mauvaise préparation des labels.

- https://huggingface.co/learn/llm-course/fr/chapter7/6
- https://huggingface.co/docs/trl/sft_trainer

## 78. LoRA : apprendre une petite correction de matrice

Jour 4 · matin · 10 min

ANIMATION — 10 min
4 min de lecture des deux branches, 3 min de calcul avec de petites matrices, 3 min de discussion. Dire explicitement que les vecteurs sont des colonnes dans cette écriture.

LECTURE ORALE
« La sortie y est la transformation de base W zéro fois x, plus alpha sur r fois la correction B fois A fois x. » Commencer par la branche gelée, puis suivre la branche entraînable dans l’ordre x, A, B, facteur d’échelle, addition.

SYMBOLES, DIMENSIONS ET UNITÉS
x contient d_in caractéristiques ; y en contient d_out. W₀ est une matrice d_out × d_in dont les paramètres restent gelés. A a la forme r × d_in et réduit l’entrée à r coordonnées. B a la forme d_out × r et remonte à la dimension de sortie. Le produit BA possède donc la même forme que W₀. r est un entier positif choisi, et le rang de BA est au plus r. α est un hyperparamètre d’échelle ; α/r est sans unité. Les coordonnées sont des caractéristiques apprises, sans unité physique imposée.

CALCUL PAS À PAS
1. Choisir d_in = d_out = 2, r = 1, α = 1 et x = (2 ; 1).
2. Prendre W₀ égal à l’identité : W₀x = (2 ; 1).
3. Prendre A = [1, −1] : Ax = 1×2 − 1×1 = 1.
4. Prendre B comme colonne (0,5 ; 1) : BAx = (0,5 ; 1).
5. α/r = 1 ; additionner les branches donne y = (2,5 ; 2). Ces valeurs sont pédagogiques et ne décrivent pas l’initialisation réelle du TP.

HYPOTHÈSES ET PIÈGE
Cette écriture correspond au facteur d’échelle LoRA standard et ignore biais et dropout pour isoler le mécanisme. On gèle W₀, mais on calcule encore sa contribution et on peut propager des gradients vers les autres éléments entraînables : gelé ne signifie pas supprimé du graphe. LoRA ne retire pas le besoin de charger la base. Les modules ciblés et les éventuels autres poids entraînables doivent être inspectés.

QUESTION / RÉPONSE
« SFT et LoRA sont-ils synonymes ? » Non : SFT nomme la supervision par démonstrations ; LoRA nomme les paramètres utilisés pour l’adaptation. Faire vérifier le nombre de paramètres réellement entraînables dans le TP.

REPÈRES DU CORPS DE DIAPOSITIVE
• W₀ reste gelée ; A et B sont entraînées.
• A réduit vers un rang r ; B remonte vers la sortie.
• La correction ΔW = BA est contrainte par son rang.

SOURCE LATEX DE LA FORMULE
\mathbf{y}=W_0\mathbf{x}+\frac{\alpha}{r}\,BA\mathbf{x}

LECTURE GUIDÉE DU SCHÉMA
1. Lire le schéma en deux branches issues de la même entrée colonne x. La branche W₀ produit la transformation de base ; elle reste calculée à chaque passe même si ses poids sont gelés.
2. Suivre la branche de correction dans l’ordre A puis B. A réduit d_in vers r ; B remonte r vers d_out. Le produit BA a donc exactement la forme de W₀.
3. Le facteur α/r multiplie la correction. La jonction finale est une addition de deux vecteurs de même dimension d_out, jamais une concaténation.
4. Les annotations entraînable et gelé désignent les paramètres mis à jour ; elles ne signifient pas qu’aucun gradient ne traverse le calcul de la branche gelée vers d’autres paramètres autorisés. Les activations restent une composante du coût.
5. Question : l’adaptateur peut-il fonctionner seul sans la base ? Non. Lors de l’inférence, recharger la base compatible et l’adaptateur, puis comparer aux sorties de base sur les mêmes cas. Le rang contraint la correction BA, pas le rang total de W₀ + (α/r)BA.

REPÈRES DU CORPS DE DIAPOSITIVE À EXPLICITER
• W₀ reste gelée ; A et B sont entraînées.
• A réduit vers un rang r ; B remonte vers la sortie.
• La correction ΔW = BA est contrainte par son rang.

Source de l'image de formule — LaTeX
\mathbf{y}=W_0\mathbf{x}+\frac{\alpha}{r}\,BA\mathbf{x}

Légende projetée
x : entrée d_in ; y : sortie d_out
W₀ : matrice gelée, d_out × d_in
A : r × d_in ; B : d_out × r
r : rang choisi pour la correction
α/r : facteur d’échelle de la correction

W₀ = I, x = (2 ; 1), A = [1, −1], B = (0,5 ; 1), α/r = 1 → y = (2,5 ; 2).

- https://arxiv.org/abs/2106.09685

## 79. LoRA : combien de paramètres apprend-on ?

Jour 4 · matin · 10 min

ANIMATION — 10 min
4 min de calcul, 3 min avec un autre rang, 3 min d’interprétation. Relier le comptage aux formes de A et B vues juste avant.

LECTURE ORALE
« Une matrice complète compte dimension de sortie fois dimension d’entrée paramètres. Les deux matrices LoRA comptent ensemble r fois la somme des dimensions d’entrée et de sortie. » La seconde ligne additionne le nombre de paramètres de A et de B ; elle ne compte pas la base gelée.

SYMBOLES, DIMENSIONS ET UNITÉS
d_in et d_out sont des nombres entiers de caractéristiques. r est la dimension intermédiaire de l’adaptateur. N_complet compte les paramètres de W₀, matrice d_out × d_in. N_LoRA compte les paramètres entraînables des matrices A, de forme r × d_in, et B, de forme d_out × r. Les deux N sont exprimés en paramètres, pas en octets. Leur conversion en mémoire dépend de la précision et des autres états stockés.

CALCUL PAS À PAS
1. Poser d_in = d_out = 1024 et r = 8.
2. La matrice complète compte 1024 × 1024 = 1 048 576 paramètres.
3. A compte 8 × 1024 = 8192 paramètres ; B en compte autant.
4. N_LoRA = 8192 + 8192 = 16 384.
5. Le rapport vaut 16 384 / 1 048 576 = 1/64 = 0,015625, soit 1,5625 %.
6. Avec r = 16, le nombre de paramètres d’adaptation double à 32 768, sans modifier le nombre de paramètres de la base.

HYPOTHÈSES ET PIÈGE
Le calcul concerne une seule matrice, sans biais entraînable ni autre module. Ce pourcentage n’est pas automatiquement celui du modèle entier : il faut sommer les modules effectivement ciblés. Les poids de base restent chargés ; le gain d’entraînement concerne notamment gradients et états de l’optimiseur des poids gelés. Les activations restent nécessaires.

QUESTION / RÉPONSE
« Doubler r garantit-il une meilleure validation ? » Non : on augmente la capacité de correction et le coût, mais peu de données peuvent favoriser la mémorisation. Le TP compare le calcul d’ordre de grandeur au compteur réel des paramètres entraînables.

REPÈRES DU CORPS DE DIAPOSITIVE
• Matrice 1 024 × 1 024 : 1 048 576 paramètres.
• Avec r = 8 : 8 × (1 024 + 1 024) = 16 384.
• La correction représente ici 1,56 % de la matrice complète.

SOURCE LATEX DE LA FORMULE
\begin{aligned}N_{\mathrm{complet}}&=d_{\mathrm{out}}d_{\mathrm{in}}\\N_{\mathrm{LoRA}}&=r\left(d_{\mathrm{in}}+d_{\mathrm{out}}\right)\end{aligned}

Source de l'image de formule — LaTeX
\begin{aligned}N_{\mathrm{complet}}&=d_{\mathrm{out}}d_{\mathrm{in}}\\N_{\mathrm{LoRA}}&=r\left(d_{\mathrm{in}}+d_{\mathrm{out}}\right)\end{aligned}

Légende projetée
d_in, d_out : dimensions d’entrée et de sortie
r : rang de l’adaptateur
N_complet : paramètres de la matrice pleine
N_LoRA : paramètres entraînables de A et B

1 024² = 1 048 576 ; r = 8 → 16 384 paramètres LoRA, soit 1,5625 % pour cette matrice.

- https://arxiv.org/abs/2106.09685
- https://huggingface.co/docs/peft/package_reference/lora

## 80. QLoRA : quantifier la base, entraîner les adaptateurs

Jour 4 · matin · 10 min

CONCEPT ET ANIMATION
DÉROULÉ : 4 min de distinction stockage/calcul, 3 min de reformulation, 3 min de questions. Quantifier consiste à représenter les poids avec un nombre réduit de valeurs possibles et des métadonnées d'échelle. NF4 est adapté à la représentation de poids selon les hypothèses de la méthode ; les opérations ne deviennent pas toutes des calculs natifs en quatre bits.

QUESTION : QLoRA met-il à jour directement chaque poids quantifié de la base ? RÉPONSE : l'approche étudiée garde la base gelée et entraîne des adaptateurs. Le chemin de préparation comprend configuration de quantification, chargement, préparation pour l'entraînement en faible précision, puis adaptation LoRA. Le notebook propose la variante bitsandbytes lorsque le matériel et l'environnement conviennent. Sur T4, on utilise une configuration de calcul FP16 explicitement compatible ; ne pas activer BF16 par habitude. Faire distinguer le modèle petit de 0,5 milliard de paramètres et les démonstrations de recherche sur des modèles beaucoup plus grands : les résultats publiés ne prédisent pas notre mémoire ni notre score.

Dans le TP, mesurer le pic réel et documenter la configuration.

LECTURE GUIDÉE DU SCHÉMA
1. Partir de la base gelée dont les poids sont stockés sous une représentation quantifiée quatre bits, avec les métadonnées nécessaires. La boîte de stockage décrit un format, pas toute l’arithmétique du réseau.
2. Suivre la flèche vers les opérations de calcul dans la précision configurée. La déquantification intervient selon les kernels et besoins du calcul ; le schéma ne signifie pas que l’on conserve nécessairement une copie complète FP16 de tous les poids en permanence.
3. La branche LoRA ajoute des paramètres entraînables en précision adaptée. Le backward fournit leurs gradients, sans transformer les poids de base quatre bits en paramètres directement mis à jour.
4. NF4 et précision de calcul répondent à deux questions distinctes. Sur le parcours T4, le notebook choisit une configuration FP16 compatible ; la disponibilité de BF16 n’est pas supposée. Le modèle quantifié est préparé avant l’entraînement des adaptateurs.
5. Question : quatre bits divisent-ils toute la mémoire par quatre par rapport à FP16 ? Non : métadonnées, paramètres non quantifiés, adaptateurs, activations, buffers et états ajoutent des coûts. Mesurer l’étape réelle plutôt que déduire le total de la seule case « poids ».

REPÈRES DU CORPS DE DIAPOSITIVE À EXPLICITER
• Poids de base stockés en 4 bits ; adaptateurs entraînés séparément.
• NF4 est un format de quantification, pas un type de calcul universel.
• Le calcul utilise une précision choisie, par exemple FP16 sur T4.
• Préparer le modèle quantifié avant d'ajouter et entraîner LoRA.

Description accessible du schéma
L’entrée se sépare entre une base W0 gelée en quatre bits et une branche LoRA A puis B et facteur alpha sur r. Les deux contributions sont additionnées en sortie. Le calcul des couches quantifiées utilise FP16 dans cet exemple.
Base stockée en NF4 ; calcul en FP16 ici ; seuls les adaptateurs sont entraînables.

Repères associés à l'illustration
Poids de base stockés en 4 bits ; adaptateurs entraînés séparément.
NF4 est un format de quantification, pas un type de calcul universel.
Le calcul utilise une précision choisie, par exemple FP16 sur T4.
Préparer le modèle quantifié avant d'ajouter et entraîner LoRA.

- https://arxiv.org/abs/2305.14314
- https://huggingface.co/docs/peft/developer_guides/quantization
- https://huggingface.co/docs/transformers/quantization/bitsandbytes

## 81. La mémoire des poids n'est pas la mémoire totale

Jour 4 · matin · 10 min

ANIMATION — 10 min
4 min d’ordre de grandeur, 3 min d’inventaire, 3 min de correction. Demander ce qu’un estimateur qui ne compte que les poids oublie pendant l’entraînement.

LECTURE ORALE
« La mémoire totale est approximativement la somme des poids, des gradients, des états de l’optimiseur, des activations et des buffers. » Le signe environ rappelle qu’il s’agit d’un modèle de comptage, pas d’une prédiction exacte du pic.

SYMBOLES, DIMENSIONS ET UNITÉS
Chaque M est une quantité de mémoire, à exprimer dans la même unité avant addition. M_poids couvre les paramètres de base et les adaptateurs. M_gradients stocke les dérivées associées aux paramètres entraînables. M_optimiseur couvre les états supplémentaires de la méthode d’optimisation. M_activations représente les valeurs intermédiaires conservées pour le backward ; elles dépendent notamment du batch et de la longueur. M_buffers couvre des tampons de travail et autres allocations. Un octet vaut huit bits ; un Go décimal vaut 10⁹ octets, tandis qu’un Gio vaut 2³⁰ octets.

CALCUL PAS À PAS
1. Avec 0,5 milliard de paramètres arrondis et 16 bits par poids, compter 2 octets par poids.
2. 0,5 × 10⁹ × 2 = 10⁹ octets, soit 1 Go de poids idéalisés.
3. À quatre bits, chaque poids utilise idéalement 0,5 octet : 0,5 × 10⁹ × 0,5 = 0,25 Go, avant métadonnées et parties non quantifiées.
4. Exemple d’addition distinct et fictif : 100 Mo de poids + 20 Mo de gradients + 40 Mo d’optimiseur + 80 Mo d’activations + 10 Mo de buffers = 250 Mo au total. Ces nombres n’ont pas été mesurés sur Qwen.

HYPOTHÈSES ET PIÈGE
Les pics des composantes, les caches, l’allocateur et les états non quantifiés compliquent le total réel. Quatre bits pour les poids ne signifie pas quatre bits pour toutes les opérations ou toutes les activations. Le checkpointing échange du recalcul contre des activations stockées. Réduire la longueur peut couper la réponse cible ; réduire le micro-batch n’efface pas tous les coûts.

QUESTION / RÉPONSE
« Les poids tiennent, donc l’entraînement tient ? » Non. Mesurer une étape complète et le pic réel avec la configuration du TP. Rapporter matériel, longueur, batch et méthode plutôt qu’une estimation présentée comme une mesure.

REPÈRES DU CORPS DE DIAPOSITIVE
• 0,5 milliard × 2 octets ≈ 1 Go pour des poids FP16 idéalisés.
• À 4 bits : ≈ 0,25 Go théorique, avant métadonnées et poids non quantifiés.
• Batch et longueur influencent fortement les activations.

SOURCE LATEX DE LA FORMULE
\begin{aligned}M_{\mathrm{total}}\approx{}&M_{\mathrm{poids}}+M_{\mathrm{gradients}}+M_{\mathrm{optimiseur}}\\&+M_{\mathrm{activations}}+M_{\mathrm{buffers}}\end{aligned}

Source de l'image de formule — LaTeX
\begin{aligned}M_{\mathrm{total}}\approx{}&M_{\mathrm{poids}}+M_{\mathrm{gradients}}+M_{\mathrm{optimiseur}}\\&+M_{\mathrm{activations}}+M_{\mathrm{buffers}}\end{aligned}

Légende projetée
M_total : mémoire totale approximative
M_poids : paramètres du modèle et adaptateurs
M_gradients, M_optimiseur : états d’apprentissage
M_activations : valeurs intermédiaires conservées
M_buffers : mémoire de travail et autres tampons

0,5 milliard × 2 octets = 1 Go de poids FP16 idéalisés, avant activations et autres états.

- https://huggingface.co/docs/transformers/perf_train_gpu_one

## 82. Quatre leviers à régler avec une raison

Jour 4 · matin · 10 min

DÉROULÉ : 3 min de présentation, 4 min de résolution d'un scénario, 3 min de correction. Scénario : la première étape échoue en mémoire, et les réponses cibles sont courtes mais les consignes très longues. Demander un ordre de diagnostic : vérifier ce qui est chargé, lire les longueurs, réduire micro-batch, puis choisir d'autres leviers sans supprimer le signal d'apprentissage. QUESTION : faut-il modifier tous les paramètres pour obtenir enfin une exécution ? RÉPONSE : une modification à la fois rend le résultat interprétable et la configuration reproductible. Le checkpointing économise de la mémoire en recalculant certaines activations pendant le backward ; il n'offre pas un gain gratuit. Les caches utiles à la génération ne sont pas toujours compatibles avec la configuration d'entraînement et doivent suivre les réglages du notebook. Le modèle reste le même au sein de la comparaison LoRA/QLoRA. Dans le TP, consigner un budget de temps et arrêter une expérience trop longue proprement en sauvegardant ce qui peut l'être. Une exécution courte valide le fonctionnement de la chaîne, pas une performance finale.



- https://huggingface.co/docs/transformers/perf_train_gpu_one

## 83. Après l'entraînement : base + adaptateur + tokenizer

Jour 4 · matin · 10 min

DÉROULÉ : 3 min de schéma de fichiers, 4 min de protocole de comparaison, 3 min de questions. Un adaptateur contient la correction apprise et sa configuration ; il dépend du modèle de base compatible. Une petite taille de fichier ne signifie pas que toute l'inférence tient dans cette taille. QUESTION : peut-on charger l'adaptateur sur n'importe quel modèle de même famille ? RÉPONSE : non, l'architecture, les modules et le checkpoint doivent être compatibles. La fusion éventuelle est une opération distincte qui dépend des formats et de la quantification ; elle n'est pas nécessaire pour la démonstration pédagogique. Dans le TP, recharger explicitement base, adaptateur et tokenizer, puis exécuter les mêmes cas réservés. Faire conserver le prompt rendu, le décodage et la limite de sortie. Mesurer séparément respect du format, contenu demandé et inventions. Une réponse améliorée isolée n'établit pas un gain global. Demander aussi un cas où l'adaptation régresse. L'objectif est une comparaison honnête avec le point de départ, accompagnée de la configuration réellement entraînée et du nombre de pas.



- https://huggingface.co/docs/peft/developer_guides/checkpoint

## 84. Résumer : conserver les faits utiles sous une contrainte

Jour 4 · matin · 10 min

CONCEPT ET ANIMATION
DÉROULÉ : 2 min de lecture, 5 min de résumés individuels puis comparaison, 3 min de débrief. Demander une phrase pour un agent de support qui reprend le dossier. Une bonne proposition serait : « Le client signale qu'un article manque dans le colis AB123 reçu mardi et demande une vérification. » Cette phrase est un exemple original de correction, pas une sortie de modèle mesurée.

QUESTION : un résumé plus court est-il toujours meilleur ? RÉPONSE : il peut omettre un fait nécessaire à l'action. Distinguer extractif, qui sélectionne du texte source, et abstrait, qui reformule ou combine. Une baseline extractive simple permet de comparer le bénéfice et le risque de la génération. Le modèle instructionnel peut résumer sans adaptation spécifique, mais ses capacités sur notre français et nos entrées courtes doivent être observées. Dans le TP06, le résumé possède son propre entraînement LoRA autonome : 16 comptes rendus fictifs train, 2 validation et 4 test, avec 12 pas prévus. L'adaptateur support du TP05 n'est pas réutilisé comme s'il était spécialisé en résumé. On compare extractif, modèle initial et modèle adapté sur les mêmes quatre sources réservées, sans promettre de gain. Les étudiants commencent par définir une liste de faits de référence.

LECTURE GUIDÉE DU SCHÉMA
1. Commencer par la source : un compte rendu contient des faits, une demande et parfois une incertitude. Repérer référence, date, problème et action avant de lire une sortie de modèle.
2. La branche extractive sélectionne des morceaux de la source ; elle peut omettre un fait important même sans introduire de mots nouveaux. La branche générative tokenise source et consigne, puis produit une séquence de résumé.
3. Pour la comparaison du TP06, distinguer modèle initial et même base avec un LoRA entraîné spécifiquement sur le résumé. Les trois méthodes reçoivent les mêmes sources réservées ; le LoRA support du TP05 n’est pas un substitut à cet adaptateur.
4. Les flèches vers l’évaluation relient chaque sortie à la référence et aux faits sources : ROUGE fournit un recouvrement lexical, la grille humaine vérifie fidélité, couverture et format.
5. Question : une flèche d’entraînement depuis la référence test vers le modèle est-elle admissible ? Non, le test reste hors adaptation et sélection. Le TP autonome utilise 16 train, 2 validation, 4 test et 12 pas prévus ; l’objectif est la maîtrise de la chaîne, pas une performance métier démontrée.

REPÈRES DU CORPS DE DIAPOSITIVE À EXPLICITER
Accroche : Source : colis AB123 reçu mardi ; un article manque ; le client demande une vérification.
• Faits à préserver : référence, date, problème et demande.
• Détails à ne pas inventer : remboursement, responsable, nouveau délai.
• Comparer une extraction simple et une génération.
• Fixer longueur et destinataire avant d'évaluer.

Description accessible du schéma
Trois faits de la source, référence AB123 reçue mardi, article manquant et vérification demandée, sont reliés à leurs formulations dans un résumé. Un remboursement effectué est signalé comme non étayé.
Chaque affirmation du résumé doit être étayée par un fait de la source.

Repères associés à l'illustration
Source : colis AB123 reçu mardi ; un article manque ; le client demande une vérification.
Faits à préserver : référence, date, problème et demande.
Détails à ne pas inventer : remboursement, responsable, nouveau délai.
Comparer une extraction simple et une génération.
Fixer longueur et destinataire avant d'évaluer.

- https://huggingface.co/learn/llm-course/fr/chapter7/5

## 85. ROUGE mesure un recouvrement, pas la vérité

Jour 4 · matin · 10 min

DÉROULÉ : 3 min d'intuition, 4 min de contre-exemples, 3 min de conclusion. Comparer la référence « Le colis est arrivé mardi » avec « Le colis n'est pas arrivé mardi ». Le recouvrement lexical peut rester élevé alors que le fait central est inversé. À l'inverse, « Livraison effectuée le mardi » peut exprimer un sens proche avec moins de mots identiques. QUESTION : faut-il abandonner toute métrique automatique ? RÉPONSE : non, elle fournit un signal reproductible si l'on comprend son objet et ses limites. Décrire le prétraitement et la tokenisation utilisés, particulièrement pour le français ; ne pas appliquer aveuglément un stemming conçu pour une autre langue. Une référence unique ne couvre pas toutes les formulations valides. Dans le TP, ROUGE accompagne une grille de fidélité factuelle et de couverture, il ne les remplace pas. Les notes humaines doivent citer un élément source pour chaque invention ou omission. Les scores des textes pédagogiques ne sont pas un benchmark général du modèle. L'intérêt de l'exercice est de voir quand l'indicateur et le jugement sur les faits divergent.



- https://aclanthology.org/W04-1013/

## 86. Relier chaque affirmation à une preuve dans la source

Jour 4 · matin · 10 min

DÉROULÉ : 4 min de classement d'affirmations, 3 min d'accord inter-évaluateurs, 3 min de correction. La grille force à décomposer un texte fluide en faits contrôlables. Chaque affirmation reçoit un passage justificatif ou l'indication qu'elle n'est pas appuyée. Les omissions demandent l'opération inverse : parcourir les faits importants de la source et vérifier leur présence dans le résumé. QUESTION : une affirmation plausible mais absente doit-elle être acceptée ? RÉPONSE : pour un résumé fidèle au document fourni, la plausibilité ne suffit pas. Distinguer contradiction directe et ajout non étayé ; les deux peuvent être problématiques mais ne sont pas identiques. Faire travailler deux évaluateurs sans se concerter, puis discuter leurs désaccords sur l'importance d'un fait. Dans le TP, une grille courte accompagne chaque résumé : fidélité, couverture, format et lisibilité. Les notes ne doivent pas être agrégées au point de masquer une invention grave. Une sortie grammaticalement élégante ne compense pas un remboursement inventé. Le jour 5 utilisera la même logique pour évaluer les réponses générées du projet.





## 87. Vérifier ce qui est réellement entraîné et évalué

Jour 4 · matin · 15 min

DÉROULÉ : 4 min individuelles, 5 min entre pairs, 6 min de correction. Réponse 1 : SFT décrit une supervision par démonstrations ; LoRA décrit une adaptation par petites matrices de rang réduit. Réponse 2 : non, la base est quantifiée pour son stockage tandis que le calcul et les adaptateurs utilisent d'autres précisions selon la configuration. Réponse 3 : cela vérifie que la réponse attendue contribue à la loss et que le prompt ou le padding ne sont pas supervisés par erreur. Réponse 4 : non, le recouvrement lexical ne prouve pas la factualité. Ajouter le calcul rapide d'une matrice 100 × 100 avec rang 4 : 10000 paramètres complets contre 800 pour A et B. Faire demander ce qui manque dans un budget basé uniquement sur les poids : activations, gradients, états et buffers. Avant le TP, chaque binôme écrit un critère de réussite observable et un critère qui invaliderait l'expérience. Cette formulation prévient la tentation de justifier après coup toute baisse de loss comme un succès.





## 88. TP 4A · Préparer les démonstrations et la supervision

Jour 4 · apres-midi · 80 min

ORGANISATION : 15 min d'environnement T4, 20 min d'audit des données, 20 min de template et longueurs, 15 min de batch et masques, 10 min de contrôle croisé. Ouvrir notebooks/etudiants/05_j4_sft_lora.ipynb. Le modèle est Qwen/Qwen2.5-0.5B-Instruct. POINT DE CONTRÔLE : chaque binôme décode les positions effectivement supervisées et montre que la completion est présente après troncature. La configuration utilise completion_only_loss=True pour le format prompt/completion ; ne pas la remplacer sans comprendre le contrat. RÉSULTAT ATTENDU : un jeu audité et une préparation explicable avant toute optimisation. Si le GPU manque, terminer intégralement l'audit, le calcul de paramètres LoRA et l'inspection du format sur la voie prévue ; consigner que l'entraînement GPU n'a pas eu lieu. EXTENSION : ajouter un exemple avec information manquante et vérifier qu'il enseigne une demande de précision, pas une invention. Le formateur valide le point de contrôle avant le lancement du bloc suivant.





## 89. TP 4B · Entraîner un adaptateur et mesurer l'effet

Jour 4 · apres-midi · 80 min

ORGANISATION : 15 min de configuration, 25 min d'entraînement et d'exercices parallèles, 20 min de comparaison, 20 min de sauvegarde et restitution. POINT DE CONTRÔLE : afficher les paramètres entraînables et vérifier que les poids de base sont gelés selon la méthode retenue. Le chemin LoRA est la référence ; la variante QLoRA dépend de l'environnement et doit être comparée à configuration documentée. RÉSULTAT ATTENDU : une expérience finie et traçable, pas une garantie d'amélioration. Mesurer mémoire et temps réellement observés, sans recopier les ordres de grandeur du matin comme s'ils étaient des mesures. Pendant l'entraînement, évaluer des sorties de base et calculer le ratio des paramètres. Après sauvegarde, recharger l'adaptateur avec la base compatible. EXTENSION : comparer un autre rang sur validation si le budget le permet, sans consulter à répétition le test. La restitution doit montrer un gain, une régression ou une absence de changement, puis une hypothèse liée aux données et au nombre de pas.





## 90. TP 4C · Fine-tuner un LoRA dédié au résumé

Jour 4 · apres-midi · 40 min

ORGANISATION : 5 min d'environnement, 10 min d'audit des données et de la supervision, 5 min de baseline extractive sur développement, 20 min d'entraînement borné et d'exercices, soit 40 minutes. Ouvrir notebooks/etudiants/06_j4_resume_evaluation.ipynb. Ce TP est autonome : il repart du modèle Qwen2.5-0.5B-Instruct et entraîne un adaptateur LoRA spécifiquement pour le résumé. Le jeu original fictif contient 16 exemples train, 2 validation et 4 test ; 12 pas sont prévus pour observer la chaîne, pas pour garantir une généralisation. POINT DE CONTRÔLE : les cibles résument les faits sources sans inventer un remboursement ou effacer une incertitude, et les réponses ne sont pas tronquées. RÉSULTAT ATTENDU : une configuration, un nombre de pas réellement exécutés et un adaptateur identifié. Les deux cas de validation servent uniquement aux choix prévus ; le test final reste réservé. Si l'entraînement ne peut pas être réalisé, conserver l'évaluation extractive et le protocole, avec la mention non exécuté pour l'adaptation. Ne pas remplacer cet entraînement par le LoRA support du TP05.





## 91. TP 4D · Comparer extractif, base et résumé adapté

Jour 4 · apres-midi · 40 min

ORGANISATION : 15 min de sorties comparatives, 15 min de métriques et audit croisé, 10 min de sauvegarde et conclusion, soit 40 minutes ; avec le bloc précédent, le TP06 totalise 80 minutes. POINT DE CONTRÔLE : extractif, modèle initial et modèle adapté reçoivent les mêmes quatre sources test, avec un prompt et un décodage comparables pour les deux modèles génératifs. RÉSULTAT ATTENDU : un tableau de sorties et de mesures effectivement observées, sans gain imposé. Avec seulement quatre tests et douze pas, l'expérience prouve surtout la maîtrise du pipeline ; elle ne démontre aucune qualité métier générale. Chaque invention ou omission est reliée à la source. Les binômes évaluent sans connaître d'abord le nom de la méthode lorsque c'est possible. Vérifier que l'archive et la model card identifient l'adaptateur résumé, sa base et les données, distincts du support. Si une variante n'a pas été exécutée, laisser sa mesure absente et l'expliquer. Une meilleure métrique lexicale peut coexister avec une erreur factuelle grave ; la conclusion doit le dire.



- https://aclanthology.org/W04-1013/

## 92. Jour 5 · Évaluer, présenter et défendre un système

Jour 5 · matin · 5 min

DURÉE : 5 min. Demander un exemple de différence entre « le code fonctionne » et « le système est utile ». Relier les productions de la semaine : représentation du jour 1, mécanisme du jour 2, adaptation du jour 3 et supervision du jour 4. Le projet final ne recommence pas tout depuis zéro ; il réutilise les artefacts et le protocole appris. La comparaison par défaut porte sur la classification du support : baseline TF-IDF, génération zéro-shot avec le petit LLM et classifieur fine-tuné si l'archive du jour 3 est disponible. Une autre tâche peut être retenue si son évaluation est définie. L'interface Gradio montre le comportement, tandis que le test réservé et l'analyse d'erreurs fournissent la preuve. La publication Hub est optionnelle ; l'évaluation et la documentation restent obligatoires. LIVRABLE DE LA JOURNÉE : À produire : résultats traçables, interface et limites explicites.



- https://web.stanford.edu/class/cs224n/

## 93. Avant le score, écrire le contrat d'évaluation

Jour 5 · matin · 10 min

DÉROULÉ : 2 min de lecture, 5 min de contrat en binôme, 3 min de mise en commun. Faire compléter une phrase : « Nous cherchons à orienter des demandes françaises parmi cinq intentions ; nous choisirons selon… ». Ajouter un critère principal, un critère de coût et une limite. QUESTION : pourquoi écrire ce contrat avant l'expérience ? RÉPONSE : pour éviter de choisir après coup le score qui favorise la méthode préférée. La population doit préciser que le corpus est fictif et limité ; « messages clients en général » serait une généralisation excessive. Un bon contrat décrit aussi les cas exclus et la conduite face à une entrée ambiguë. Dans le projet, le test final ne doit pas être utilisé pour inventer les prompts ou les règles de parsing. Le seuil d'acceptation ne peut pas être fixé honnêtement à partir d'un résultat déjà vu sans le reconnaître. Demander aux étudiants quel résultat les conduirait à conserver TF-IDF. Cette question rend possible une conclusion négative ou nuancée et évite de noter la taille du modèle plutôt que la qualité du raisonnement.





## 94. Comparer qualité, coût et fiabilité d'exécution

Jour 5 · matin · 10 min

DÉROULÉ : 3 min de lecture, 4 min de scénario de choix, 3 min de discussion. Donner deux systèmes fictifs : A atteint 0,84 de macro-F1 avec une faible latence, B atteint 0,85 mais demande beaucoup plus de mémoire et produit des erreurs de format. Les nombres servent à discuter, pas à annoncer les performances des notebooks. QUESTION : B est-il nécessairement préférable ? RÉPONSE : le choix dépend de l'incertitude, des contraintes et de la nature des erreurs. Une démo fluide peut masquer une initialisation très coûteuse ; une mesure de temps doit préciser si elle inclut le chargement. La robustesse se teste sur des cas définis, et la reproductibilité se démontre par un rechargement ou une exécution indépendante. Dans le projet, les étudiants doivent rapporter au moins une mesure de coût et un exemple d'échec. Si le GPU n'était pas disponible, ils décrivent cette limitation et ne remplacent pas une mesure absente par une estimation présentée comme réelle. L'évaluation récompense la capacité à prendre une décision soutenue par les observations disponibles.





## 95. Une baseline zéro-shot exige aussi un protocole

Jour 5 · matin · 10 min

DÉROULÉ : 4 min de construction du prompt, 3 min de cas de parsing, 3 min de correction. Zéro-shot signifie ici absence de démonstrations annotées dans le prompt pour cette tâche ; le modèle instructionnel a bien une histoire d'entraînement préalable. Lui demander l'un des cinq labels n'en fait pas un classifieur calibré. QUESTION : si la réponse est « probablement livraison, mais aussi facturation », peut-on choisir livraison à la main ? RÉPONSE : le parsing doit avoir été défini avant l'évaluation ; une intervention opportuniste fausse la comparaison. Une sortie invalide doit rester comptée dans les résultats et faire l'objet d'une mesure de validité de format. Le prompt se développe sur validation, puis est figé pour test. Éviter d'inclure accidentellement la vraie réponse dans l'entrée. Dans le projet, Qwen2.5-0.5B-Instruct sert de baseline locale modeste ; son résultat ne représente pas tous les LLM. La comparaison porte sur les mêmes messages avec les mêmes labels, et non sur une démonstration choisie face à un score agrégé d'une autre méthode.



- https://huggingface.co/docs/transformers/chat_templating

## 96. La métrique dépend de l'unité de réussite

Jour 5 · matin · 10 min

DÉROULÉ : 3 min de rappel, 4 min d'appariement de mauvais scores, 3 min de correction. Donner des exemples d'indicateurs mal choisis : accuracy de tokens pour conclure sur la NER, similarité sémantique pour prouver un fait, longueur moyenne pour juger un résumé. Demander pourquoi chaque mesure est insuffisante. QUESTION : peut-on agréger toutes les tâches dans une seule note de « qualité NLP » ? RÉPONSE : cela demande une pondération d'usage explicite ; sinon le nombre cache des unités différentes. Le tableau est un point de départ, pas une liste universelle. Pour la recherche à plusieurs documents pertinents, préciser le dénominateur de Recall@k ; pour la génération, séparer format et contenu. Dans le projet, le rapport doit relier la métrique au contrat de la diapositive précédente. Les métriques par classe ou par catégorie d'erreur donnent le contexte nécessaire à une moyenne globale. Faire calculer manuellement un exemple de la tâche choisie avant d'utiliser la bibliothèque. Cette vérification protège contre une implémentation qui retourne un nombre valide mais répond à la mauvaise question.



- https://scikit-learn.org/stable/modules/model_evaluation.html

## 97. Découper les résultats pour trouver les fragilités

Jour 5 · matin · 10 min

DÉROULÉ : 3 min de définition des tranches, 4 min de proposition par binôme, 3 min de discussion. Une moyenne peut masquer une bonne performance sur des messages simples et un échec sur des formulations longues ou ambiguës. Choisir des tranches en rapport avec l'usage, puis rapporter leur effectif. QUESTION : si une tranche contient deux exemples et les deux sont faux, peut-on annoncer que le modèle échoue toujours dans ce cas ? RÉPONSE : on a identifié un signal à investiguer, pas une fréquence fiable. Ne pas multiplier les découpages jusqu'à trouver une différence spectaculaire sans signaler l'exploration. Le corpus fictif permet de construire des contre-exemples contrôlés mais ne représente pas toutes les langues, pratiques ou populations. Dans le projet, chaque binôme choisit deux tranches à l'avance et conserve une catégorie pour les erreurs découvertes. Distinguer robustesse orthographique et équité sociale : tester quelques fautes ne démontre pas l'absence de biais envers des groupes. La restitution doit dire quelles conditions ont été observées et lesquelles restent hors du périmètre.





## 98. Un petit test produit un résultat incertain

Jour 5 · matin · 10 min

DÉROULÉ : 4 min de calcul, 3 min de comparaison, 3 min de discussion. Si un système passe de 17 à 18 réponses correctes sur vingt, son accuracy passe de 85 à 90 %. Les cinq points peuvent correspondre à un seul cas particulier. QUESTION : une différence affichée avec trois décimales est-elle plus certaine ? RÉPONSE : la précision d'affichage ne change pas la quantité d'information. Pour comparer deux systèmes, conserver l'appariement des messages aide à comprendre sur quels cas ils divergent. Un bootstrap peut donner une indication de variabilité, mais doit respecter l'unité d'indépendance ; si des paraphrases appartiennent à un même scénario, rééchantillonner les groupes est plus pertinent que traiter les lignes comme indépendantes. Les répétitions de graines répondent à une autre question : sensibilité de l'entraînement. Dans le projet court, un tableau des désaccords et des effectifs est prioritaire à une procédure statistique mal comprise. Les intervalles éventuels ne corrigent pas un test biaisé ou artificiel. Exiger une conclusion proportionnée à la taille et à la nature des observations.





## 99. Une grille humaine doit rendre les jugements comparables

Jour 5 · matin · 10 min

DÉROULÉ : 3 min de lecture, 4 min de notation indépendante, 3 min de discussion des écarts. Donner deux sorties courtes et demander à chacun une note accompagnée d'une citation du texte. Les niveaux ne deviennent utiles que si les évaluateurs partagent des exemples de ce qui compte comme une erreur. QUESTION : faut-il faire une moyenne qui permet à une belle rédaction de compenser un fait inventé ? RÉPONSE : cela dépend du contrat, mais pour le support une invention d'action peut constituer un critère bloquant distinct du score moyen. La grille donne des dimensions parallèles ; elle ne prescrit pas d'agrégation unique. Faire distinguer couverture et fidélité avec un résumé très court mais entièrement vrai. Dans le projet, deux étudiants évaluent indépendamment un petit échantillon, puis documentent leurs désaccords. Une personne qui connaît la méthode peut avoir des attentes ; masquer le nom du système réduit une partie de ce biais. Le rapport conserve les commentaires qui justifient les notes. Il ne doit pas prétendre mesurer objectivement tout aspect de la qualité avec quatre nombres.





## 100. Un LLM juge peut aider, mais il faut aussi le contrôler

Jour 5 · matin · 10 min

DÉROULÉ : 4 min de principe, 3 min de conception d'un contrôle, 3 min de discussion. Un juge automatique peut accélérer une première lecture, mais il peut préférer une réponse longue, élégante ou placée en première position. Il peut aussi partager des erreurs avec le modèle évalué. QUESTION : demander au même petit LLM s'il a bien répondu constitue-t-il une validation indépendante ? RÉPONSE : non ; l'auto-évaluation est une observation supplémentaire, pas une preuve. Faire inverser l'ordre de deux réponses identiques pour tester une sensibilité de position. Si les textes évalués contiennent des instructions, le juge doit les traiter comme des données de la tâche ; cette frontière fait partie des risques d'une évaluation automatisée. Dans le projet, le juge LLM reste optionnel et ne remplace pas la grille humaine du petit échantillon. Aucune API payante n'est nécessaire. Si un outil externe est utilisé en extension, documenter modèle, version, prompt et données envoyées. Les notes obtenues doivent être comparées à des jugements humains avant toute conclusion générale.



- https://arxiv.org/abs/2306.05685

## 101. Analyser une erreur pour décider d'une action

Jour 5 · matin · 10 min

DÉROULÉ : 3 min de lecture, 4 min sur une erreur réelle du binôme, 3 min de restitution. Chaque groupe choisit un échec et écrit trois éléments : observation exacte, hypothèse de cause, expérience minimale pour départager les hypothèses. QUESTION : peut-on conclure « le modèle manque de données » à partir d'une seule erreur ? RÉPONSE : c'est une hypothèse trop générale ; il faut préciser quelles données et quel comportement elles devraient changer. Si une référence de commande a été tronquée, ajouter des époques ne la rendra pas visible. Si le vrai label est contestable, entraîner plus longtemps peut apprendre plus fortement une incohérence. Dans le projet, une seule amélioration ciblée est suffisante si elle est testée proprement sur validation. Les étudiants doivent conserver les erreurs initiales et les nouvelles prédictions pour montrer gains et régressions. Le test réservé intervient après le choix. Une analyse qui conduit à ne pas modifier le modèle mais à clarifier la tâche peut être une excellente décision d'ingénierie.





## 102. Tester la robustesse avec des variations contrôlées

Jour 5 · matin · 10 min

DÉROULÉ : 2 min de consigne, 5 min de création de paires, 3 min de mise en commun. Chaque binôme crée deux paires : une transformation qui devrait préserver la sortie et une qui devrait la changer. Paraphraser « mon mot de passe ne fonctionne plus » peut conserver compte ; transformer « je veux retourner le produit » en « je ne veux pas retourner le produit » demande une discussion du contexte et du schéma de labels. QUESTION : faut-il forcer une des cinq classes pour une demande de recette de cuisine ? RÉPONSE : le classifieur fermé le fera probablement ; une application doit définir comment reconnaître ou traiter les entrées hors domaine. Un score maximal faible n'est pas automatiquement un détecteur fiable, et un seuil demande une validation dédiée. Dans le projet, le jeu de robustesse reste séparé du test principal et ses exemples sont documentés. Pour une interface générative, tester aussi une entrée qui demande d'ignorer la consigne, sans prétendre que quelques essais démontrent une sécurité générale. Les étudiants rapportent précisément les comportements observés.





## 103. Mesurer la latence dans des conditions compréhensibles

Jour 5 · matin · 10 min

DÉROULÉ : 4 min de protocole, 3 min de repérage d'une mesure trompeuse, 3 min de correction. Une première exécution inclut parfois téléchargement, allocation et initialisation ; les suivantes peuvent utiliser des caches. Comparer une seule première requête à la moyenne de dix requêtes à chaud serait injuste. QUESTION : pourquoi une simple différence d'horloges peut-elle sous-estimer le temps GPU ? RÉPONSE : certaines opérations sont asynchrones ; il faut attendre la fin du travail selon le protocole de mesure. Pour la génération, davantage de tokens produits augmente généralement la durée ; rapporter seulement une latence sans longueur est incomplet. La médiane donne une valeur typique et une mesure de dispersion révèle les variations, sans prétendre à un benchmark industriel sur quelques essais Colab. Dans le projet, mesurer des entrées identiques et limiter la charge. Ne pas inclure le temps humain d'annotation dans le temps d'inférence. La consommation réelle dépend de l'environnement partagé ; une mesure T4 de classe constitue un résultat local à décrire, pas une promesse de service.



- https://pytorch.org/docs/stable/generated/torch.cuda.synchronize.html

## 104. Une démo Gradio rend le comportement inspectable

Jour 5 · matin · 10 min

CONCEPT ET ANIMATION
DÉROULÉ : 3 min de parcours utilisateur, 4 min de conception en binôme, 3 min de discussion. L'interface doit permettre à une autre personne de tester le système sans comprendre le notebook. Elle affiche le label et, si utile, les scores avec une explication de leur portée.

QUESTION : faut-il charger le modèle à chaque clic ? RÉPONSE : non, on initialise une fois puis on réutilise la fonction d'inférence. Prévoir les cas simples qui interrompent souvent une démo : texte vide, longueur excessive, modèle absent ou fichier d'archive non chargé. Le partage public est désactivé par défaut dans le notebook ; une publication est une action distincte de l'évaluation locale. Dans le projet, chaque groupe fournit trois exemples : normal, difficile et échec connu. Une interface agréable et rapide facilite l'inspection mais ne remplace pas le jeu de test. Si le modèle fine-tuné n'est pas disponible, la baseline peut alimenter la démo avec un nom fidèle à ce qui est chargé. Ne pas présenter un bouton fonctionnel comme une preuve de préparation à la production.

LECTURE GUIDÉE DU SCHÉMA
1. Lire l’interface comme un parcours : texte saisi → validation de l’entrée → fonction d’inférence → sortie lisible. Une flèche de validation peut conduire à un message d’erreur clair pour une entrée vide ou trop longue.
2. Le modèle et son tokenizer sont chargés en amont une seule fois ; la fonction les réutilise à chaque requête. Le dessin ne doit pas suggérer un nouvel entraînement à chaque clic.
3. Dans la fonction, prétraitement, calcul et post-traitement restent distincts. La sortie visible peut contenir un label et des scores, avec une explication de leur portée et du modèle réellement utilisé.
4. La frontière entre notebook local et publication doit être explicite : le partage public est désactivé par défaut. Une archive locale et une démo fonctionnelle sont évaluables sans URL publique ni compte Hub.
5. Question : une requête réussie valide-t-elle le système ? Elle prouve seulement ce comportement observé. Montrer aussi un cas ambigu et un échec connu ; la qualité générale vient du protocole de test, pas de la présence d’une interface.

REPÈRES DU CORPS DE DIAPOSITIVE À EXPLICITER
• Un champ texte, une sortie lisible et quelques exemples choisis.
• Charger le modèle une fois, puis appeler une fonction d'inférence.
• Prévoir entrée vide, texte long et message d'erreur compréhensible.
• Lancement local au notebook ; partage public désactivé par défaut.



- https://www.gradio.app/guides/quickstart

## 105. Le livrable doit raconter comment le résultat a été obtenu

Jour 5 · matin · 10 min

DÉROULÉ : 3 min de distinction des documents, 4 min de rédaction d'un paragraphe, 3 min de revue croisée. Demander à un binôme de reprendre le projet d'un autre sans explication orale : quelles informations manqueraient ? Un README sert à exécuter ; la model card décrit le système et son évaluation ; la data card décrit les données et leurs limites. QUESTION : écrire « entraîné sur des données de support » suffit-il ? RÉPONSE : non, il faut préciser qu'elles sont fictives, comment elles ont été construites, leur taille et leur séparation. Rapporter les métriques réellement mesurées avec leur matériel et leur protocole. Si l'entraînement n'a pas été exécuté, le dire explicitement au lieu de conserver une valeur d'exemple. Dans le projet, la documentation comprend aussi une phrase sur les usages non démontrés, par exemple données client réelles ou déploiement multi-utilisateur. Les résultats doivent pouvoir être reliés aux prédictions sauvegardées. Les fichiers de secrets, caches inutiles et informations personnelles n'appartiennent pas à l'archive remise.



- https://huggingface.co/docs/hub/model-cards
- https://huggingface.co/docs/hub/datasets-cards

## 106. Publier sur le Hub : rendre l'artefact réutilisable

Jour 5 · matin · 10 min

DÉROULÉ : 3 min de chaîne de publication, 4 min d'audit de fichiers, 3 min de questions. Distinguer modèle, dataset et Space : ils correspondent à des artefacts différents. Une archive locale fonctionnelle peut être un livrable complet pour le cours ; la publication en ligne ajoute un partage et des obligations de documentation. QUESTION : un dépôt privé autorise-t-il l'envoi de n'importe quelles données ? RÉPONSE : non, il faut toujours avoir le droit de les utiliser et de les transférer. Le notebook rend la publication explicitement optionnelle et utilise une visibilité privée lorsque cette voie est choisie. Les tokens d'accès restent dans les mécanismes de secrets appropriés et ne sont pas écrits dans les cellules ou dans la model card. Pour un adaptateur, préciser base, révision, tokenizer et procédure de chargement ; un utilisateur ne doit pas deviner la dépendance. Dans le projet, le formateur peut évaluer la documentation et le rechargement local sans compte Hub. Une publication réussie prouve un transfert de fichiers, pas une qualité métier ni une sécurité de production.



- https://huggingface.co/docs/hub/repositories-settings
- https://huggingface.co/docs/hub/model-cards

## 107. Mini-projet : une décision défendable en binôme

Jour 5 · matin · 10 min

DÉROULÉ : 3 min de présentation du barème, 4 min de choix du périmètre, 3 min de vérification. Le barème officiel de evaluation/PROJET.md comporte six critères totalisant vingt points : protocole et absence de fuite 4 ; comparaison équitable 4 ; évaluation et analyse 4 ; reproductibilité 3 ; démonstration et model card 3 ; soutenance et compréhension individuelle 2. Le tableau regroupe visuellement les deux critères à trois points sans modifier leur attribution. Une comparaison qui montre la baseline préférable peut obtenir une excellente note si elle est correcte et argumentée. QUESTION : faut-il entraîner un nouveau modèle le jour 5 ? RÉPONSE : non, réutiliser l'artefact support du jour 3 laisse du temps pour évaluer. L'artefact Allociné prédit un sentiment et ne doit pas être confondu avec le routeur à cinq intentions. Chaque point correspond aux preuves décrites dans le sujet. L'indisponibilité du GPU est documentée avec un protocole reproductible, sans inventer une mesure. Chaque membre doit expliquer une décision de données et une erreur. Une recommandation de ne pas déployer peut recevoir tous les points.





## 108. Soutenir : problème, preuve, décision, limite

Jour 5 · matin · 10 min

DÉROULÉ : 2 min de présentation du format, 5 min de répétition en binôme, 3 min de feedback. La soutenance individuelle de groupe vise cinq minutes, auxquelles le formateur ajoute les questions selon l'effectif. Le dernier bloc d'après-midi prévoit quarante minutes de soutenance, puis dix minutes de remise : huit binômes au maximum à cinq minutes, ou une galerie simultanée avec vérification individuelle si les groupes sont plus nombreux. QUESTION : comment présenter un modèle qui n'a pas amélioré la baseline ? RÉPONSE : montrer la comparaison, expliquer les erreurs et recommander le choix le mieux soutenu ; une conclusion négative fait partie de l'ingénierie. Interdire les phrases vagues telles que « cela marche bien » sans exemple ni mesure. Chaque groupe doit montrer un cas difficile et une limite, pas seulement la meilleure entrée. Faire répartir la parole pour que les deux membres expliquent une décision. Le support final peut tenir sur une seule page avec table, exemple et conclusion. Les questions du jury portent sur la séparation des données, l'unité de métrique, le rechargement et l'action suivante la plus informative.





## 109. Avant de conclure : que peut-on réellement affirmer ?

Jour 5 · matin · 15 min

DÉROULÉ : 4 min de réponses, 5 min de discussion, 6 min de correction. Réponse 1 : la démo prouve un comportement sur les entrées essayées ; la généralisation nécessite un protocole et des données représentatives. Réponse 2 : appliquer la règle de parsing définie et compter les sorties invalides, sans correction manuelle opportuniste. Réponse 3 : cinq points d'accuracy dans cet exemple, avec une forte sensibilité aux cas du petit test ; il faut lire les désaccords et limiter la conclusion. Réponse 4 : données ou accès documenté, partitions, configuration, versions, artefact rechargeable et prédictions sauvegardées. Ajouter une dernière question personnelle : quelle erreur de raisonnement commettiez-vous en début de semaine que vous savez désormais éviter ? Les réponses peuvent mentionner token égal mot, attention égale explication, loss égale qualité, LoRA égal modèle complet ou démo égale production. Terminer par le contrat du projet : une hypothèse, une comparaison, une preuve, une décision et une limite. Les étudiants disposent ensuite de quatre heures de travail guidé.





## 110. TP 5A · Verrouiller le protocole et lancer les références

Jour 5 · apres-midi · 75 min

ORGANISATION : 15 min de contrat, 20 min de rechargement et audit des partitions, 40 min de construction des baselines, soit 75 minutes conformément au sujet de projet. Ouvrir notebooks/etudiants/07_j5_projet.ipynb. POINT DE CONTRÔLE : toutes les méthodes reçoivent les mêmes messages support, les mêmes labels de référence et une règle de sortie déclarée. Recharger l'archive du routeur support du jour 3 ; l'export de sentiment Allociné est un autre modèle et ne convient pas à cette tâche. Son absence est indiquée et ne doit pas être remplacée par une tête aléatoire présentée comme entraînée. RÉSULTAT ATTENDU : une table de prédictions de validation et une référence majoritaire puis TF-IDF. Préparer le zéro-shot du petit modèle local avec un prompt et un parsing fixes ; enregistrer toute sortie invalide. Le test final reste réservé. Si le groupe choisit NER ou résumé, adapter explicitement baseline et métrique avant le lancement. Le formateur vérifie le périmètre pour éviter un projet trop large qui empêcherait de terminer l'analyse.





## 111. TP 5B · Tester une amélioration et lire les erreurs

Jour 5 · apres-midi · 75 min

ORGANISATION : 45 min de comparaison sur validation, incluant l'analyse et une éventuelle variante, puis 30 min pour figer les choix, exécuter le test final et analyser les erreurs ; total 75 minutes. POINT DE CONTRÔLE : la modification répond à une erreur observée et son effet attendu est écrit avant exécution. Une meilleure consigne, un réglage de représentation ou la décision de conserver la baseline peut suffire ; un nouvel entraînement n'est pas obligatoire. RÉSULTAT ATTENDU : distinguer clairement développement sur validation et résultat final sur test. Afficher effectifs, métriques, sorties invalides et au moins une mesure de temps dans des conditions connues. Les cinq erreurs sont des textes précis avec catégories et hypothèses. Un petit jeu de robustesse contrôlé reste séparé du test principal et signalé comme exploratoire. Ne pas continuer à choisir des réglages après consultation du test tout en le présentant comme indépendant. Si une amélioration dégrade une catégorie, l'indiquer ; le choix final expose ce compromis. Conserver les prédictions et la configuration pour la documentation.





## 112. TP 5C · Préparer une démo et un livrable rechargeable

Jour 5 · apres-midi · 40 min

ORGANISATION : 20 min de démonstration, 20 min de model card et de recommandation, soit 40 minutes. POINT DE CONTRÔLE : un autre binôme saisit une phrase nouvelle et comprend la sortie. Une interface Gradio ou un scénario de prédictions dans le notebook peut remplir la fonction de démonstration prévue au sujet. Le partage public reste désactivé par défaut. Vérifier une entrée vide, une longue demande et un cas ambigu. RÉSULTAT ATTENDU : un artefact dont le nom correspond au modèle chargé ; si la démo utilise TF-IDF, elle doit le dire. La model card reprend les résultats réellement observés, les partitions, versions et limites du corpus fictif. Vérifier les éléments nécessaires au rechargement pendant cette préparation ; les exports définitifs occupent les dix dernières minutes du bloc suivant. La publication Hub reste facultative avec choix explicite de visibilité, et aucun token d'accès ne figure dans les fichiers. Une documentation complète est prioritaire à une décoration supplémentaire. Préparer une page contenant problème, table des résultats, erreur, décision et limite.





## 113. TP 5D · Soutenances, revue croisée et bilan

Jour 5 · apres-midi · 50 min

ORGANISATION : 40 min de soutenances, puis 10 min d'exports et de remise, soit 50 minutes. Huit binômes au maximum peuvent passer cinq minutes chacun ; au-delà, organiser une galerie simultanée avec grille de revue croisée et vérification individuelle du formateur. POINT DE CONTRÔLE : chaque membre explique une décision et répond à une question sur les données ou l'évaluation. RÉSULTAT ATTENDU : une conclusion proportionnée aux preuves ; le plus gros modèle ou le meilleur score isolé n'est pas automatiquement le meilleur projet. Appliquer le barème officiel 4/4/4/3/3/2 sur vingt. Le jury demande ce qui ferait changer la décision et quelle donnée manque encore. Les dix minutes finales servent à remettre le notebook exécuté, les résultats et l'identification des artefacts, puis un bilan individuel bref : notion comprise, erreur évitée et compétence à approfondir. Vérifier que les fichiers du runtime temporaire ont été téléchargés. Les pistes suivantes, telles que RAG ou annotation réelle, ne doivent pas être présentées comme déjà réalisées pendant la semaine.
