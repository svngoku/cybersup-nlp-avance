# Ressources vérifiées et parcours de lecture

**Consultation : 4 octobre 2026.** Vérifié signifie ici que la ressource a été ouverte et que son rôle pédagogique a été contrôlé. Cela ne signifie pas que tous ses notebooks ont été exécutés, ni que ses API sont compatibles sans adaptation avec la pile du cours.

Le socle est le cours Hugging Face en français pour les bases et les tâches classiques. Les chapitres avancés 10–11 consultés sont en anglais ; les explications, consignes et exercices de notre cours restent en français. Stanford apporte la profondeur théorique. Aucun achat n'est requis.

## Lectures essentielles : une ressource pour un problème précis

| ID | Source primaire / langue | Utilisation concrète | Activité liée |
|---|---|---|---|
| R01 | [HF — Introduction au cours](https://huggingface.co/learn/llm-course/fr/chapter1/1), FR | Carte de l'écosystème et architectures ; point d'entrée | J1 : situer tâches, modèles et bibliothèques |
| R02 | [scikit-learn — Extraction de texte](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction), EN | Comprendre vocabulaire, TF-IDF et n-grammes | TP01 : baseline et erreur sur paraphrase |
| R03 | [HF — Entraîner un tokenizer](https://huggingface.co/learn/llm-course/fr/chapter6/2), FR | Observer un vocabulaire appris et les segments obtenus | TP01 : comparer longueurs et segmentation |
| R04 | [HF — BPE](https://huggingface.co/learn/llm-course/fr/chapter6/5), FR | Faire des fusions avant d'appeler une bibliothèque | J1/TP01 : exercice manuel puis contrôle |
| R05 | [HF — Derrière le pipeline](https://huggingface.co/learn/llm-course/fr/chapter2/2), FR | Décomposer tokenisation, modèle, post-traitement | TP02 : afficher les objets intermédiaires |
| R06 | [Vaswani et al. — Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017, EN | Source des opérations d'attention ; lire la section 3 | J2 : dimensions, échelle et masque sur petit exemple |
| R07 | [Devlin et al. — BERT](https://arxiv.org/abs/1810.04805), 2018/2019, EN | Comprendre le préentraînement bidirectionnel et l'adaptation | J2/J3 : expliquer l'encodeur et sa nouvelle tête |
| R08 | [HF — Trainer en français](https://huggingface.co/learn/llm-course/fr/chapter3/3), FR | Comprendre l'organisation d'un fine-tuning | TP03 : refaire le schéma de la boucle |
| R09 | [HF — Datasets](https://huggingface.co/learn/llm-course/fr/chapter5/1), FR | Lire, transformer et inspecter les données | TP03/05 : audit des colonnes, labels et groupes |
| R10 | [HF — Classification de tokens](https://huggingface.co/learn/llm-course/fr/chapter7/2), FR | Relier mots, sous-tokens et étiquettes | TP04 : annotation BIO, alignement et F1 d'entités |
| R11 | [HF — Résumé de textes](https://huggingface.co/learn/llm-course/fr/chapter7/5), FR | Situer la tâche et les limites d'une évaluation automatique | TP06 : baseline extractive et contrôle de fidélité |
| R12 | [HF — Introduction à Argilla](https://huggingface.co/learn/llm-course/en/chapter10/1), EN | Penser annotation, curation et retour humain | J4 : accepter/corriger/rejeter six exemples ; aucun serveur Argilla requis |
| R13 | [HF — Introduction au fine-tuning LLM](https://huggingface.co/learn/llm-course/en/chapter11/1), EN | Situer SFT, données et adaptation | TP05 : expliciter le comportement à apprendre |
| R14 | [HF — LoRA](https://huggingface.co/learn/llm-course/en/chapter11/4), EN | Comprendre la mise à jour de faible rang | J4 : compter les paramètres, expliquer l'adaptateur |
| R15 | [HF PEFT — Quantification](https://huggingface.co/docs/peft/developer_guides/quantization), EN | Relier chargement quantifié, préparation et adaptateurs | TP05 : vérifier la préparation k-bit et les paramètres entraînables |
| R16 | [HF — Introduction à Gradio](https://huggingface.co/learn/llm-course/fr/chapter9/1), FR | Transformer une fonction NLP en démonstration | J5 : contrat d'entrée/sortie et états limites |
| R17 | [Stanford CS224N, Winter 2026](https://web.stanford.edu/class/cs224n/), EN | Approfondir vecteurs, attention et évaluation | Exercices guidés originaux ; les devoirs entiers dépassent notre budget |

Les lectures longues sont des références, pas des devoirs de lecture intégrale pendant la semaine. Avant une séance, choisir une section et une question à laquelle elle doit répondre. Les notebooks HF servent de pistes complémentaires ; les notebooks distribués ici sont autonomes et adaptés au cas fil rouge.

## Documentation opérationnelle : suivre la version du TP

| ID | Référence | Ce qu'il faut vérifier |
|---|---|---|
| R18 | [Transformers 4.56.2 — Trainer](https://huggingface.co/docs/transformers/v4.56.2/en/main_classes/trainer) | Arguments et cycle d'évaluation de la version épinglée ; certains exemples FR emploient d'anciens noms |
| R19 | [Transformers 4.56.2 — Token classification](https://huggingface.co/docs/transformers/v4.56.2/en/tasks/token_classification) | Alignement, labels ignorés et évaluation |
| R20 | [Transformers 4.56.2 — Chat templates](https://huggingface.co/docs/transformers/v4.56.2/en/chat_templating) | Rôles, tokens spéciaux et différence entraînement/génération |
| R21 | [TRL 0.23.1 — SFTTrainer](https://huggingface.co/docs/trl/v0.23.1/en/sft_trainer) | Format prompt/complétion, loss et configuration |
| R22 | [bitsandbytes — Installation](https://huggingface.co/docs/bitsandbytes/main/en/installation) | Compatibilité CUDA/matériel, NF4/FP4 et contraintes de version |
| R23 | [Google Colab — FAQ](https://research.google.com/colaboratory/faq.html) | Allocation variable, limites et persistance des runtimes |
| R24 | [NVIDIA — Fiche T4](https://www.nvidia.cn/content/dam/en-zz/Solutions/Data-Center/tesla-t4/t4-tensor-core-datasheet.pdf) | Mémoire et calcul FP16/FP32 ; ne pas extrapoler un temps d'entraînement |
| R25 | [Gradio — Sharing your app](https://gradio.app/main/guides/sharing-your-app) | Différence interface locale, lien de partage et hébergement ; cas Colab |
| R26 | [HF Hub — Paramètres des dépôts](https://huggingface.co/docs/hub/en/repositories-settings) | Visibilité privée/publique choisie avant une publication facultative |
| R27 | [HF Hub — Model cards](https://huggingface.co/docs/hub/en/model-cards) | Documenter usage, données, évaluation et limites |
| R28 | [scikit-learn — Métriques](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics) | Macro-F1, confusion, classes et dénominateurs |
| R29 | [Runpod — Connexion à un Pod](https://docs.runpod.io/pods/connect-to-a-pod) | JupyterLab sur une image compatible déjà fournie |
| R30 | [Runpod — Gestion des Pods](https://docs.runpod.io/pods/manage-pods) | Sauvegarde, arrêt du calcul et distinction avec suppression |
| R31 | [NVIDIA — L4](https://www.nvidia.com/en-us/data-center/l4/) | 24 Go de mémoire, FP16 et BF16 ; aucune durée de TP déduite de la fiche |

## Modèles et données : lire les cartes avant de comparer

| ID | Artefact retenu | Rôle et limites | Licence indiquée lors de la consultation |
|---|---|---|---|
| M01 | [paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) | Embeddings de phrases pour recherche multilingue ; la proximité ne garantit pas équivalence ni factualité | Apache-2.0 sur la carte |
| M02 | [distilbert-base-multilingual-cased](https://huggingface.co/distilbert/distilbert-base-multilingual-cased) | Encodeur pour fill-mask et adaptation classification/NER ; une tête neuve doit être entraînée | Apache-2.0 sur la carte |
| M03 | [Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) | Petit modèle Instruct pour génération et adaptation sous budget ; capacités françaises à évaluer localement | Apache-2.0 sur la carte |
| D01 | Corpus support-client fictifs intégrés | Exemples originaux, petites tailles et scénarios contrôlés ; aucune performance réelle revendiquée | Création du présent cours ; voir provenance |
| D02 | [IMDb sur HF](https://huggingface.co/datasets/stanfordnlp/imdb) et [page Stanford](https://ai.stanford.edu/~amaas/data/sentiment/) | Extension facultative en anglais pour éprouver un pipeline sur d'autres textes ; ne pas présenter comme jeu français | Carte HF : « other » ; lire les conditions du jeu source avant réutilisation |
| D03 | [Allociné, dépôt du créateur](https://huggingface.co/datasets/tblard/allocine) | Transfert TP03 sur de vrais avis français : 1 000 train / 200 validation / 200 test. Partitions d'origine conservées ; classifieur séparé du support | MIT indiquée sur la carte ; citer le créateur et la source des avis |

Les poids des modèles, IMDb et les avis Allociné ne sont pas embarqués dans les packs du cours. Une licence du modèle ne couvre pas automatiquement toutes les données, marques ou ressources mentionnées par sa carte. La carte Allociné annonce des films disjoints entre splits ; le sous-échantillonnage conserve ces partitions. Un résultat de sentiment cinéma ne valide pas une tâche de support client.

## Approfondissements ciblés

| ID | Source | Proposition de travail |
|---|---|---|
| A01 | [Hu et al. — LoRA](https://arxiv.org/abs/2106.09685), 2021 | Relier les dimensions de A/B au compte de paramètres ; discuter la portée de l'hypothèse de faible rang |
| A02 | [Dettmers et al. — QLoRA](https://arxiv.org/abs/2305.14314), 2023 | Distinguer quantification des poids, adaptation et gestion de mémoire ; ne pas transposer les résultats du papier à notre petit corpus |
| A03 | [Daniel Voigt Godoy — First LLM fine-tuning](https://huggingface.co/blog/dvgodoy/fine-tuning-llm-hugging-face), billet d'auteur hébergé sur HF | Lire après TP05 pour retrouver le pipeline ; vérifier les versions et adapter le dtype au GPU |
| A04 | [Cours HF Agents — entrée française](https://huggingface.co/learn/agents-course/fr/unit0/introduction) | Bonus après les 35 h : distinguer modèle, outil et boucle d'agent ; pas de déploiement requis cette semaine |

Le billet A03 est une explication pratique de son auteur, pas une garantie officielle de compatibilité de toutes ses cellules. Les sources techniques de référence restent la documentation versionnée et les articles originaux.

## Rectifications du tableau initial de ressources

Plusieurs liens du brief pointaient vers une autre ressource que le titre annoncé. Le chapitre HF 11/4 traite de **LoRA**, pas des devoirs Stanford. Les devoirs sont accessibles depuis CS224N : la page consultée est **Winter 2026**, tandis que les vidéos publiques qu'elle recommande sont celles de **2024**. Les quatre thèmes annoncés sur cette page sont : vecteurs de mots ; bases des réseaux, dérivées de tenseurs et parsing ; self-attention/Transformers ; benchmarking et évaluation des LLM.

La traduction française ne doit pas être supposée complète pour les chapitres avancés. Le chapitre 10 consulté commence par Argilla ; il est exploité pour la curation, sans imposer son installation. Les chapitres 11 et leurs exemples sont lus en anglais, puis reformulés dans le cours. Aucun nombre garanti de notebooks français n'est attribué au cours Agents. Le cours Udemy et le relais de blog évoqués dans le brief ne sont pas nécessaires au parcours : aucune inscription payante n'est demandée.
