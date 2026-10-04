# Vérifications des notebooks — 4 octobre 2026

Les sept paires de notebooks ont été générées et leurs vérifications statiques et calculs légers ont été exécutés localement. **Aucun entraînement de modèle, aucun téléchargement de poids, aucune exécution Colab T4 ou Runpod L4 n’a été effectué pendant cette vérification.** Les notebooks distribués conservent des sorties vides : les étudiants produiront leurs propres mesures.

## Environnement utilisé

- Génération et contrôles structurels : Python 3.14.6 sur macOS ARM64.
- Vérifications des cellules avec dépendances : environnement temporaire isolé créé avec uv 0.12.5, Python 3.11.14, macOS 27.0 ARM64.
- Versions : NumPy 2.1.3, pandas 2.2.3, Matplotlib 3.10.6, scikit-learn 1.7.2, tokenizers 0.22.0, Transformers 4.56.2, Datasets 4.1.1, huggingface-hub 0.35.3, seqeval 1.2.2, rouge-score 0.1.2.
- Jinja2 3.1.6 ajouté à cet environnement de vérification pour rendre les chat templates. La première tentative du harness sans PyTorch a signalé cette dépendance absente ; la seconde exécution complète a réussi. Le runtime du cours requiert PyTorch CUDA préinstallé.
- PyTorch, CUDA, PEFT, TRL et bitsandbytes n’ont pas été exécutés dans ce harness CPU.

## Structure et séparation des éditions

Commande reproductible dans le dossier du cours :

```sh
python3 scripts/build_notebooks.py --smoke
```

Ce contrôle a réussi. Il régénère 14 notebooks, parse les cellules Python, vérifie les corpus et exécute les contrôles mathématiques légers prévus par le générateur.

Un contrôle structurel complémentaire a vérifié :

- exactement sept notebooks étudiants et sept corrigés ;
- cellules de code identiques entre chaque paire ;
- cellules de correction uniquement dans l’édition formateur ;
- identifiants de cellules uniques dans chaque fichier ;
- absence de sorties préremplies et de compteurs d’exécution ;
- syntaxe Python valide pour toutes les cellules, y compris celles d’entraînement et de publication optionnelle.

La validité syntaxique n’établit pas l’exécution des cellules GPU ou la disponibilité des services externes.

## Calculs et données effectivement exécutés

Un harness temporaire a chargé les cellules directement depuis les notebooks étudiants, en remplaçant uniquement l’affichage par une fonction silencieuse et en excluant installation, modèles et entraînements. Il a effectué les contrôles suivants.

| Élément | Vérification exécutée | Résultat |
|---|---|---|
| J1 : recherche TF-IDF | Construction des 12 fiches, matrice TF-IDF, cosinus, Recall@k et MRR sur huit requêtes de validation | Exécution réussie ; aucune valeur imposée au résultat |
| J1 : tokenizer BPE | Apprentissage de deux petits vocabulaires et inspection des tokens/inconnus | Exécution réussie |
| J2 : attention NumPy | Dimensions, sommes des poids, triangle causal et perturbation d’une valeur future | Assertions réussies |
| J3 : corpus support | 80 textes uniques, groupes de paraphrases disjoints entre train/validation/test | Assertions réussies |
| J3 : baseline | Entraînement TF-IDF + régression logistique et macro-F1 de validation | Exécution réussie |
| J3 : NER | Parsing de 24 phrases annotées et validité BIO | Assertions réussies |
| J3 : alignement réel | Téléchargement du tokenizer DistilBERT, word_ids, labels -100 et vérification des longueurs pour les 24 phrases | Exécution réussie ; aucun poids du modèle téléchargé |
| J4 : curation SFT | Injection puis rejet d’un doublon, d’une question vide, d’une réponse vide et d’un courriel de test | 84 lignes initiales, 80 conservées |
| J4 : chat template réel | Téléchargement du tokenizer Qwen, sérialisation prompt/completion et calcul des longueurs | Longueur maximale observée : 134 tokens, sous la limite 512 |
| J4 : résumé | Constitution des 16 comptes rendus train, deux validation et quatre test, identifiants/textes/références uniques | Assertions réussies |
| J4 : ROUGE | Exécution du tokenizer Unicode et de ROUGE-L sur les résumés extractifs et l’exemple de négation | Exécution réussie ; aucun résumé génératif présenté comme mesuré |
| J5 : nouveau défi | Contrôle des vingt textes de défi, sans duplication exacte du corpus support J3/J4 | Assertions réussies |

Le tokenizer DistilBERT vérifié est celui de [distilbert-base-multilingual-cased](https://huggingface.co/distilbert/distilbert-base-multilingual-cased). Le chat template vérifié est celui de [Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct). Le téléchargement de ces fichiers de tokenisation ne constitue pas une exécution des modèles.

## Parcours réel Allociné

Le téléchargement de [tblard/allocine](https://huggingface.co/datasets/tblard/allocine) et la cellule de préparation du TP03 ont été exécutés avec Datasets 4.1.1.

- Schéma observé : review et label, labels ordonnés neg/pos.
- Partitions observées : 160 000 train, 20 000 validation, 20 000 test.
- Sous-échantillons du notebook, graine 42 : 1 000 train, 200 validation et 200 test, sans migration entre partitions officielles.
- Répartition observée : train 496 négatifs / 504 positifs ; validation 106 / 94 ; test 111 / 89.
- Aucun doublon exact après normalisation de casse et d’espaces, ni à l’intérieur ni entre ces trois sous-échantillons.

L’absence de doublons exacts ne prouve pas l’absence de paraphrases, de films ou d’auteurs communs. Le fine-tuning et les scores du classifieur Allociné n’ont pas été exécutés dans ce contrôle CPU.

## Vérification documentaire des API

Les versions fixées existent sur PyPI. Les métadonnées de dépendances consultées indiquent notamment TRL 0.23.1 avec Transformers >=4.56.1 et Datasets >=3.0.0, compatibles avec les versions retenues. Cela vérifie les contraintes déclarées, pas toutes les combinaisons GPU du runtime.

Les signatures et paramètres ont été comparés aux documentations et sources versionnées :

- [Transformers 4.56.2 — Trainer](https://huggingface.co/docs/transformers/v4.56.2/en/main_classes/trainer) : processing_class, eval_strategy, fp16, bf16, gradient_checkpointing_kwargs.
- [TRL 0.23.1 — SFTTrainer](https://huggingface.co/docs/trl/v0.23.1/en/sft_trainer) : format prompt/completion, max_length, completion_only_loss, assistant_only_loss et processing_class.
- [PEFT — quantification](https://huggingface.co/docs/peft/en/developer_guides/quantization) : préparation du modèle quantifié, LoRA et quantification NF4. Le cours fixe fp16 et désactive bf16 pour son parcours T4.

La loss de completion est inspectée dans les notebooks à partir du batch réel produit par SFTTrainer. **Cette inspection doit encore être exécutée dans le runtime GPU du cours.** Elle n’a pas été remplacée par une prétendue mesure locale.

## Ce qui reste à exécuter avant diffusion

- Exécuter chaque notebook de bout en bout dans un runtime neuf Colab T4 ; faire de même sur L4 si cette option est retenue.
- Vérifier téléchargement des poids, mémoire disponible, durées, entraînements classification/NER/SFT/résumé et générations.
- Vérifier les vrais labels masqués de SFTTrainer, les exports de poids/adaptateurs et leur rechargement.
- Examiner les comparaisons avant/après sans attendre un gain garanti, puis conserver les erreurs et les versions effectives.
- Tester l’interface Gradio dans le contexte retenu. Le serveur, le tunnel et la publication Hub n’ont pas été lancés ici.

Les temps de 240 minutes par après-midi sont des budgets pédagogiques incluant analyse et restitution. Ils ne correspondent pas à des durées d’entraînement certifiées. La disponibilité d’un T4 gratuit n’est pas garantie.
