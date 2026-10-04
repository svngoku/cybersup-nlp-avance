# Programme — NLP Avancé (BERT, GPT, Hugging Face)

**M2 IA · Formateur : Chrys NIONGOLO. Volume confirmé : 5 × 7 heures = 35 heures. Environnement : Colab T4 ; Runpod L4 facultatif si fourni.**

Les durées indiquent du temps pédagogique effectif, hors pauses et déjeuner. Exemple de journée : 9 h–10 h 30, pause de 15 min, 10 h 45–12 h 15 ; déjeuner ; 13 h 15–15 h 15, pause de 15 min, 15 h 30–17 h 30. L'école peut déplacer les horaires en conservant **180 minutes le matin et 240 minutes l'après-midi**. Les blocs des tableaux sont des temps cumulés, pas des horaires civils.

## Objectifs du cours

1. Comprendre le traitement du langage naturel et les représentations vectorielles (embeddings).
2. Mettre en œuvre des modèles pré-entraînés (BERT, GPT) via Hugging Face.
3. Fine-tuner des LLMs sur des tâches métier (classification, NER, résumé).

| Objectif annoncé | Ancrage dans la semaine | Évidence pédagogique |
|---|---|---|
| NLP et représentations vectorielles | J1, TP01 | Texte → tokens → vecteurs ; comparaison de recherche |
| BERT, GPT et Hugging Face | J2–J3, TP02–04 | Architecture expliquée, pipeline exécuté et masque vérifié |
| Fine-tuning par tâche | J3–J5, TP03–07 | Classification/NER adaptées, LoRA support et résumé, évaluation commune |

BERT/GPT servent de repères architecturaux. DistilBERT multilingue et Qwen sont les modèles exécutés sous budget ; Qwen illustre les décodeurs causaux, sans être un modèle OpenAI GPT. Les détails de l'[option Runpod L4](RUNPOD_OPTION.md) changent le matériel, pas les objectifs ni les 35 heures.

## Compétences opérationnelles évaluables

À l'issue de la semaine, l'étudiant doit pouvoir :

1. Définir une tâche NLP, construire un découpage pertinent et expliquer la provenance des données.
2. Comparer une représentation lexicale et une représentation dense sur des exemples et une mesure explicite.
3. Calculer une petite attention, vérifier ses dimensions et expliquer un masque causal.
4. Adapter un encodeur à la classification et à la NER, puis analyser ses erreurs.
5. Préparer un petit corpus SFT et expliquer ce que LoRA et la quantification changent réellement.
6. Comparer des systèmes sur la même tâche, documenter les limites et présenter une démonstration contrôlée.

Prérequis : Python, tableaux NumPy, bases de PyTorch, split entraînement/validation/test, gradient et produit matriciel. Les dérivations longues, le préentraînement à grande échelle, le RLHF et les agents autonomes restent des prolongements, pas des objectifs à faire tenir dans ces 35 heures.

## Rythme des matinées

Chaque matin comprend neuf blocs de 20 minutes : **12 minutes d'explication, 5 minutes de prédiction/calcul/tri en binôme, 3 minutes de mise en commun**. Ce découpage est une consigne d'animation : ne pas parler vingt minutes sans faire travailler le groupe. Les questions détaillées et les remédiations sont dans le guide formateur et les notes du présentateur.

## Jour 1 — Du texte à une représentation exploitable

| Temps matin | Notion | Activité et preuve observable |
|---|---|---|
| 0–20 | Diagnostic et tâches NLP | Classer quatre besoins : recherche, classification, NER, génération |
| 20–40 | Corpus, annotation et provenance | Annoter une demande ambiguë et expliciter la règle |
| 40–60 | Découpage et fuites | Ranger des paraphrases du même scénario dans un même split |
| 60–80 | Sac de mots et TF-IDF | Comparer deux documents qui partagent un mot rare |
| 80–100 | Tokenisation et identifiants | Segmenter « remboursement », un nom propre et un emoji |
| 100–120 | BPE et vocabulaire | Effectuer deux fusions sur un minuscule corpus |
| 120–140 | Embeddings et contexte | Distinguer index de vocabulaire, vecteur et sens en contexte |
| 140–160 | Cosinus et recherche | Calculer un cosinus à deux dimensions et classer des voisins |
| 160–180 | Protocole du TP | Écrire l'hypothèse « les embeddings aident sur les paraphrases » |
| **Total matin** | **180 min** | |

| Après-midi — notebook 01 | Minutes | Livrable intermédiaire |
|---|---:|---|
| Import Colab, corpus, lecture des exemples | 20 | Périphérique, versions et rôle de chaque colonne |
| Baseline lexicale TF-IDF | 45 | Requêtes, voisins et premier tableau d'erreurs |
| Tokenisation/BPE et effets du vocabulaire | 45 | Deux découpages commentés et impact sur la longueur |
| Embeddings multilingues et similarité | 50 | Comparaison sur les mêmes requêtes |
| Ablation et cas difficiles : négation, faute, paraphrase | 50 | Une variable modifiée, résultat et interprétation |
| Restitution, quiz J1 et export | 30 | Notebook et `resultats/j1_resultats.json` |
| **Total après-midi** | **240** | |

## Jour 2 — Comprendre ce que fait un Transformer

| Temps matin | Notion | Activité et preuve observable |
|---|---|---|
| 0–20 | Rappel et génération décalée | Donner les couples entrée/cible de « le colis arrive » |
| 20–40 | De la récurrence à l'attention | Suivre une information à travers une séquence de quatre tokens |
| 40–60 | Queries, keys, values | Donner le rôle de chaque projection avec une recherche en catalogue |
| 60–80 | Produit scalaire et softmax | Calculer une ligne de poids ; vérifier leur somme |
| 80–100 | Masques causal et padding | Colorier les positions autorisées dans une matrice 4 × 4 |
| 100–120 | Multi-têtes, résidus et positions | Suivre les dimensions d'une séquence à travers un bloc |
| 120–140 | Encodeur, décodeur, encodeur-décodeur | Choisir une famille pour trois tâches et justifier |
| 140–160 | Pipeline, logits et décodage | Décomposer tokenisation → modèle → post-traitement |
| 160–180 | Température et protocole d'observation | Prédire ce qui change en sampling et en greedy |
| **Total matin** | **180 min** | |

| Après-midi — notebook 02 | Minutes | Livrable intermédiaire |
|---|---:|---|
| Installation et prédictions avant exécution | 20 | Schéma annoté de Q, K, V |
| Attention numérique et contrôles des dimensions | 50 | Matrices et sommes des lignes |
| Masques et test de non-accès au futur | 45 | Assertion et contre-exemple sans masque |
| Encodeur multilingue / remplissage d'un masque | 40 | Sorties expliquées ; pas de confusion avec un chatbot |
| Génération, chat template et paramètres | 55 | Même prompt, deux configurations, erreurs relevées |
| Débrief, quiz J2 et export | 30 | Notebook et trace des expériences |
| **Total après-midi** | **240** | |

## Jour 3 — Adapter un modèle à une tâche

| Temps matin | Notion | Activité et preuve observable |
|---|---|---|
| 0–20 | Transfert et tête de classification | Identifier les paramètres préentraînés et la tête nouvelle |
| 20–40 | Perte et mini-batch | Relier label, logits, probabilité et erreur |
| 40–60 | Dataset, tokenizer et collator | Expliquer le padding dynamique sur trois phrases |
| 60–80 | Trainer et courbes d'apprentissage | Diagnostiquer une loss train qui baisse seule |
| 80–100 | Mesures de classification | Calculer précision, rappel et F1 d'une classe |
| 100–120 | NER, spans et BIO | Annoter « Lina travaille à Lyon » |
| 120–140 | Sous-tokens et labels ignorés | Aligner les étiquettes après découpage d'un mot |
| 140–160 | F1 par entité et erreurs | Comparer frontière fausse, type faux et bonne entité |
| 160–180 | Budget et protocole | Figer splits, baseline et budget avant de lancer le TP |
| **Total matin** | **180 min** | |

| Après-midi — notebooks 03 puis 04 | Minutes | Livrable intermédiaire |
|---|---:|---|
| 03 : audit du support, baseline et tokenisation | 25 | Classes, groupes, collator et référence |
| 03 : adaptation au support client | 45 | Configuration, entraînement borné et prédictions |
| 03 : comparaison, erreurs et export du support | 30 | Comparaison sur validation ; `modele_classification.zip` pour J5 |
| 03 : transfert appliqué sur Allociné et export | 40 | 1 000 train / 200 validation / 200 test, splits conservés ; `modele_allocine.zip` pour le sentiment |
| **Sous-total classification** | **140** | |
| 04 : annotation BIO et alignement | 25 | Tableau mot → sous-tokens → labels |
| 04 : entraînement borné et prédictions | 35 | Sorties sur phrases nouvelles |
| 04 : F1 par entité et analyse de frontières | 25 | Trois erreurs classées |
| 04 : débrief, quiz J3 et export | 15 | Notebook et résultats |
| **Sous-total NER** | **100** | |
| **Total après-midi** | **240** | |

Le transfert Allociné est distinct du fil rouge : sentiment positif/négatif et catégories de support ne sont pas interchangeables. Les volumes effectifs, partitions et labels apparaissent dans les résultats. Le petit sous-ensemble utilisé ne permet pas de revendiquer un score sur le benchmark complet. En cas d'échec de téléchargement, poursuivre le parcours synthétique et documenter cette expérience réelle comme non exécutée.

## Jour 4 — SFT, LoRA et évaluation de la génération

| Temps matin | Notion | Activité et preuve observable |
|---|---|---|
| 0–20 | Préentraînement, instruction et SFT | Placer trois exemples dans la bonne étape |
| 20–40 | Format des conversations et cible | Repérer quels tokens contribuent à la loss |
| 40–60 | Curation et qualité des réponses | Accepter, corriger ou écarter six exemples |
| 60–80 | Déduplication et groupes de scénarios | Détecter une paraphrase commune au train et au test |
| 80–100 | LoRA : mise à jour de faible rang | Compter les paramètres de deux matrices minces |
| 100–120 | QLoRA, mémoire et T4 | Séparer poids quantifiés, calcul et paramètres entraînables |
| 120–140 | Résumé, extraction et hallucination | Repérer une date inventée dans un résumé fluide |
| 140–160 | Métriques et grille humaine | Comparer similarité lexicale, couverture et fidélité |
| 160–180 | Protocole du TP et plans de repli | Définir prompts figés, budget et traces à conserver |
| **Total matin** | **180 min** | |

| Après-midi — notebooks 05 puis 06 | Minutes | Livrable intermédiaire |
|---|---:|---|
| 05 : corpus SFT, curation, groupes et format | 35 | Exemples corrigés et contrôle du template |
| 05 : référence avant adaptation | 20 | Sorties initiales sur prompts figés |
| 05 : configuration LoRA/QLoRA et entraînement | 55 | Paramètres entraînables, précision et budget effectif |
| 05 : comparaison, erreurs et sauvegarde | 35 | Avant/après et `adaptateur_lora.zip` |
| 05 : bilan et transition | 15 | Hypothèse acceptée, rejetée ou indécidable |
| **Sous-total SFT** | **160** | |
| 06 : données de résumé, curation et référence initiale | 20 | Sources réservées et sorties avant adaptation |
| 06 : adaptation LoRA autonome au résumé | 25 | Adaptateur spécifique ; base figée et budget borné |
| 06 : comparaison et annotation humaine | 20 | Mêmes sources test, faits, dates, couverture et concision |
| 06 : cas adverses, quiz J4 et export | 15 | `adaptateur_resume.zip` et limite documentée |
| **Sous-total résumé** | **80** | |
| **Total après-midi** | **240** | |

## Jour 5 — Comparer, démontrer et défendre son projet

| Temps matin | Notion | Activité et preuve observable |
|---|---|---|
| 0–20 | Récupération des acquis | Expliquer un échec rencontré la veille |
| 20–40 | Baselines et équité de comparaison | Repérer un tableau comparant des tâches différentes |
| 40–60 | Validation, test et incertitude | Dire ce qu'autorise une différence sur dix exemples |
| 60–80 | Évaluation des LLM | Définir format valide, résultat correct et erreur factuelle |
| 80–100 | Robustesse et cas hors périmètre | Tester une négation, un texte vide et une demande ambiguë |
| 100–120 | Démo Gradio et contrat d'entrée | Concevoir un état vide et un message de limite |
| 120–140 | Model card, données et provenance | Transformer « marche bien » en résultat documenté |
| 140–160 | Export, rechargement et Hub facultatif | Lister les fichiers requis et le contrôle de relecture |
| 160–180 | Revue du protocole de projet | Faire valider une comparaison réalisable en quatre heures |
| **Total matin** | **180 min** | |

| Après-midi — notebook 07 / projet | Minutes | Livrable intermédiaire |
|---|---:|---|
| Cadrage et rôles | 15 | Tâche, labels, métrique, test et règle de décision |
| Relecture du modèle J3 et des données | 20 | Artefact rechargé, séparation confirmée |
| Baselines | 40 | Majoritaire/TF-IDF ; zero-shot si disponible et pertinent |
| Comparaison avec le modèle adapté | 45 | Mêmes exemples, labels et budget déclaré |
| Choix figés, test final et erreurs | 30 | Tableau final, effectifs et cas d'échec |
| Démonstration contrôlée | 20 | Fonction de prédiction testée ; interface si possible |
| Documentation et recommandation | 20 | Model card et conclusion argumentée |
| Soutenances | 40 | Jusqu'à huit binômes : quatre minutes + une question |
| Sauvegarde, quiz J5 et remise | 10 | Notebook, résultats et fiche individuelle |
| **Total après-midi** | **240** | |

Au-delà de huit binômes, utiliser une galerie en deux rotations de vingt minutes, avec une grille de relecture croisée et une question individuelle par étudiant. La durée reste 240 minutes. Le formateur annonce ce format dès le J1 et recueille les livrables avant la galerie.

## Charge et progression

| Modalité | Par jour | Sur cinq jours |
|---|---:|---:|
| Théorie active, exemples, mini-calculs et questions | 180 min | 900 min = 15 h |
| TP, analyse, restitution et projet | 240 min | 1 200 min = 20 h |
| **Total** | **420 min = 7 h** | **2 100 min = 35 h** |

Chaque TP possède un parcours essentiel et des investigations. Si le rythme ralentit, retirer d'abord une extension ou une expérience supplémentaire. Conserver l'analyse d'erreurs, l'export et le débrief. Les lectures externes préparent ou prolongent le cours ; elles ne sont pas un travail obligatoire caché dans les 35 heures.
