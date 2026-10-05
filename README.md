# NLP Avancé (BERT, GPT, Hugging Face)

**M2 IA · Cybersup · Chrys NIONGOLO · 5 jours · 35 heures · Colab T4 ; Runpod L4 en option si fourni.**

Dépôt privé du cours : [svngoku/cybersup-nlp-avance](https://github.com/svngoku/cybersup-nlp-avance). Distribuer aux étudiants le pack qui leur est destiné : le dépôt formateur contient les corrigés et les notes pédagogiques.

Une semaine pour transformer du texte en un système NLP que l'on sait expliquer, comparer et présenter. Chaque journée comprend **3 heures de théorie active le matin et 4 heures de pratique l'après-midi**, hors pauses. Les exemples, consignes et corrigés sont en français. Le fil rouge est un service client fictif : retrouver une réponse, classer une demande, extraire des entités et produire un résumé fidèle.

Les modèles entraînés sur les petits corpus pédagogiques ne constituent pas des systèmes de production. Aucun score cible n'est imposé : une expérience honnête, reproductible et bien expliquée vaut davantage qu'un chiffre élevé obtenu avec une fuite de données.

## Objectifs du cours

1. Comprendre le traitement du langage naturel et les représentations vectorielles (embeddings).
2. Mettre en œuvre des modèles pré-entraînés (BERT, GPT) via Hugging Face.
3. Fine-tuner des LLMs sur des tâches métier (classification, NER, résumé).

| Objectif | Séances et notebooks | Preuve attendue |
|---|---|---|
| 1 — NLP et embeddings | J1, TP01 ; rappel J2 | Comparaison TF-IDF/embeddings, segmentation et analyse des voisins |
| 2 — BERT/GPT avec Hugging Face | J2–J3, TP02–04 | Pipeline expliqué, masque vérifié, encodeur et décodeur utilisés |
| 3 — Adaptation à une tâche | J3–J5, TP03–07 | Classification et NER adaptées ; LoRA sur support et résumé ; évaluation comparable |

« BERT » et « GPT » désignent les familles architecturales étudiées. Les TP utilisent **DistilBERT multilingue** pour l'encodage et **Qwen2.5-0.5B-Instruct** comme décodeur causal. Qwen n'est pas un modèle OpenAI GPT ; cette distinction est enseignée explicitement. Le terme « LLM » de l'objectif couvre ici l'adaptation de modèles de langage, avec une taille volontairement réduite pour les manipulations.

## Supports à ouvrir

| Public | Fichier | Usage |
|---|---|---|
| Formateur | [PowerPoint du cours](output/CYBERSUP-NLP-M2-35h-autoporteur.pptx) | Version autoporteuse, définitions, lexique et notes du présentateur |
| Tous | [PDF de projection](output/CYBERSUP-NLP-M2-35h-autoporteur.pdf) | Version autoporteuse avec lexique, sans notes du présentateur |
| Formateur | [Notes détaillées](output/Notes-presentateur.md) | Explications orales, exemples, questions et réponses par diapositive |
| Formateur | `CYBERSUP-NLP-M2-Pack-formateur.zip` | Archive livrée séparément : support, notes, guides et corrigés |
| Étudiants | `CYBERSUP-NLP-M2-Pack-etudiant.zip` | Archive livrée séparément : notebooks et consignes étudiantes |
| Tous | [Programme des 35 heures](docs/PROGRAMME_35H.md) | Objectifs, horaires pédagogiques et preuves attendues |
| Tous | [Ressources vérifiées](ressources/RESSOURCES_VERIFIEES.md) | Lectures ciblées et exercices associés |
| Tous | [Origines et idées des méthodes NLP](docs/SOURCES_INTRO_NLP.md) | Chercheurs, institutions, dates et sources primaires |

Les archives se distribuent séparément. Après décompression du pack formateur, les liens vers les supports, les notes et le rapport de validation fonctionnent depuis sa racine.

Le [guide formateur](docs/GUIDE_FORMATEUR.md) prépare l'animation ; il complète les notes du PowerPoint. Les [consignes étudiantes](docs/ETUDIANTS.md) et le [guide Colab](docs/COLAB.md) permettent de démarrer sans accès à un dépôt GitHub. Le [guide Runpod L4](docs/RUNPOD_OPTION.md) s'applique uniquement si l'école fournit cet accès ; aucune machine n'est provisionnée par le cours.

Le [fil conducteur pratique, réservé au formateur](docs/FIL_CONDUCTEUR_PRATIQUE.md) relie chaque journée à deux microdémonstrations dans les cellules réelles des notebooks : question à prédire, manipulation, observation et retour au schéma. Il fournit aussi trois défis gradués par après-midi et une preuve à montrer toutes les trente minutes. Ces activités occupent les créneaux existants des 35 heures ; aucun livre supplémentaire n'est nécessaire pour animer les notions en classe.

Le [glossaire NLP](docs/GLOSSAIRE_NLP.md) reprend les définitions avec exemples et renvois aux diapositives. Le lexique projetable figure en fin de support ; ses pages sont des références et n’ajoutent pas de temps aux 35 heures. Le [guide vidéo formateur](docs/VIDEOS_HF_FORMATEUR.md) fournit sept liens Hugging Face, les questions de pause et les réponses attendues.

## Parcours pratique

| Jour | Matin : comprendre et prédire | Après-midi : construire et vérifier |
|---|---|---|
| 1 | Introduction NLP, TF-IDF, Word2Vec, GloVe/fastText, contexte ; corpus et tokenisation | [01 — Textes et recherche](notebooks/etudiants/01_j1_textes_recherche.ipynb), 240 min |
| 2 | Attention, masques, encodeur/décodeur, génération | [02 — Attention et Transformers](notebooks/etudiants/02_j2_attention_transformers.ipynb), 240 min |
| 3 | Fine-tuning, pertes, `Trainer`, NER et alignement | [03 — Classification](notebooks/etudiants/03_j3_classification.ipynb), 140 min ; [04 — NER](notebooks/etudiants/04_j3_ner.ipynb), 100 min |
| 4 | Curation, SFT, LoRA/QLoRA, résumé et factualité | [05 — SFT et LoRA](notebooks/etudiants/05_j4_sft_lora.ipynb), 160 min ; [06 — Adaptation au résumé](notebooks/etudiants/06_j4_resume_evaluation.ipynb), 80 min |
| 5 | Comparaisons, robustesse, démo et documentation | [07 — Projet](notebooks/etudiants/07_j5_projet.ipynb), 240 min, soutenances comprises |

Les corrigés correspondants sont dans `notebooks/formateur/`, avec le suffixe `_corrige.ipynb`. Ne distribuer aux étudiants que leur pack dédié.

Après cinq minutes d'accueil, le J1 commence par **45 minutes d'introduction** : vocabulaire du NLP, sac de mots et TF-IDF, Word2Vec (CBOW/Skip-gram), GloVe, fastText et représentations contextuelles. Huit diapositives relient chaque idée à un exemple, à ses origines et à une courte activité. Les notes détaillent les chercheurs, institutions, nuances historiques et réponses attendues. Ce créneau est inclus dans les trois heures du matin ; les quatre heures de TP sont conservées.

## Démarrage

1. Décompresser le pack puis importer un `.ipynb` dans [Google Colab](https://colab.research.google.com/). Ne pas importer le ZIP entier.
2. Enregistrer une copie personnelle ; exécuter la préparation du notebook dans un runtime neuf.
3. Utiliser le CPU pour les mécanismes élémentaires ; demander un GPU T4 pour les sections Transformer et les entraînements. Lire le périphérique réellement détecté.
4. Exécuter dans l'ordre, compléter les cellules d'investigation, puis télécharger le notebook et les résultats.
5. Conserver l'archive `modele_classification.zip` produite au J3 pour le projet du J5 ; conserver aussi l'adaptateur du J4 si l'on choisit cette extension.

Les corpus fictifs intégrés isolent les mécanismes. Le TP03 comprend aussi un transfert sur **Allociné, de vrais avis en français : 1 000 train, 200 validation et 200 test**, prélevés dans leurs partitions d'origine. Ce classifieur de sentiment et son export `modele_allocine.zip` sont distincts du classifieur de support conservé pour le J5. Le TP06 réalise une adaptation LoRA autonome au résumé et produit `adaptateur_resume.zip`, distinct de l'adaptateur support du TP05.

Les poids des modèles, le corpus réel et les dépendances nécessitent Internet. Les modèles retenus sont `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, `distilbert/distilbert-base-multilingual-cased` et `Qwen/Qwen2.5-0.5B-Instruct`. Leurs cartes et licences sont référencées dans la [provenance](ressources/PROVENANCE.md). IMDb reste une extension facultative **en anglais**.

La pile pédagogique fixe notamment Transformers 4.56.2, Datasets 4.1.1, TRL 0.23.1 et PEFT 0.17.1. Utiliser les cellules d'installation fournies et la documentation versionnée, sans mettre à jour toutes les bibliothèques au milieu d'un TP.

## Évaluation et limites de validation

Le [projet](evaluation/PROJET.md) fournit le barème sur 20 et le protocole de comparaison. Le [quiz](evaluation/QUIZ.md) comprend 25 questions originales ; son [corrigé](evaluation/CORRIGES_QUIZ.md) est réservé au formateur. Une [model card à compléter](evaluation/MODEL_CARD.md) accompagne les rendus.

Le statut des vérifications est détaillé dans le [rapport de validation](output/VALIDATION.md). **L'exécution complète dans une session Google Colab T4, ou Runpod L4 si cette option est retenue, reste à effectuer avant le cours.** Un contrôle statique ou une exécution CPU partielle ne valide ni l'allocation d'un GPU, ni les téléchargements de poids dans ces environnements, ni la durée des entraînements. Le [guide Colab](docs/COLAB.md) donne la répétition générale à réaliser et les parcours de repli.

Le cours s'appuie principalement sur le [cours Hugging Face en français](https://huggingface.co/learn/llm-course/fr/chapter1/1), complété par les chapitres avancés en anglais et [Stanford CS224N](https://web.stanford.edu/class/cs224n/). Les notebooks et exercices du présent pack sont des constructions pédagogiques originales. Aucune publication sur GitHub, le Hub ou Spaces n'est nécessaire pour suivre le cours.

## Contrôles du dépôt

L'intégration continue régénère les notebooks, vérifie leur reproductibilité, exécute les petits calculs CPU et contrôle la structure des supports et des packs. Elle ne télécharge pas les poids et ne lance pas d'entraînement GPU. Pour reproduire ces contrôles, installer NumPy 2.1.3, exécuter `python scripts/build_notebooks.py --smoke`, créer le dossier `.build`, puis exécuter `python scripts/validate_and_pack.py`.
