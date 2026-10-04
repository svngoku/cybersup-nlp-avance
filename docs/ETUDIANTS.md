# NLP Avancé (BERT, GPT, Hugging Face) — consignes étudiantes

**M2 IA · Cybersup · Chrys NIONGOLO · cinq journées de sept heures.**

Vous allez construire et comparer plusieurs systèmes à partir de textes de support client fictifs. Le matin, vous manipulez les idées sur de petits exemples. L'après-midi, vous les vérifiez dans les notebooks. Il n'est pas attendu de mémoriser toutes les API : il faut expliquer les entrées, les sorties, les choix et les limites de chaque expérience.

## Démarrer

Décompressez le pack, puis importez le premier `.ipynb` dans [Google Colab](https://colab.research.google.com/). Enregistrez une copie à votre nom. Le [guide Colab](COLAB.md) détaille le GPU, l'installation, la sauvegarde et les solutions en cas de quota. Aucun accès au dépôt du formateur n'est nécessaire.

Si l'école vous fournit un accès individuel Runpod L4, suivez le [guide Runpod](RUNPOD_OPTION.md) pour ouvrir les mêmes notebooks dans JupyterLab. Vous n'avez pas à créer ou payer une machine pour suivre le parcours de référence.

| Jour | Notebook | Résultat attendu |
|---|---|---|
| 1 | `01_j1_textes_recherche.ipynb` | Comparer recherche lexicale et embeddings, expliquer des erreurs |
| 2 | `02_j2_attention_transformers.ipynb` | Vérifier attention et masques, expliquer des générations |
| 3 | `03_j3_classification.ipynb` puis `04_j3_ner.ipynb` | Classifieur comparé à une baseline ; extraction analysée au niveau des entités |
| 4 | `05_j4_sft_lora.ipynb` puis `06_j4_resume_evaluation.ipynb` | LoRA support puis LoRA résumé autonome ; comparaison avant/après et contrôle humain |
| 5 | `07_j5_projet.ipynb` | Comparaison finale, démonstration et model card |

Les petits corpus artificiels permettent de comprendre les mécanismes ; un bon résultat dessus ne démontre pas une qualité sur de vrais clients. Le transfert Allociné utilise de vrais avis de films en français : sa tâche est le sentiment positif/négatif, sur 1 000 exemples d'entraînement et 200 par split d'évaluation. Ne confondez pas ces labels avec les catégories de support. L'extension IMDb utilise des textes anglais et reste facultative.

## Travailler à deux, comprendre individuellement

Alternez toutes les trente minutes : une personne manipule, l'autre prédit les sorties, vérifie le protocole et prend les notes. Avant une cellule importante, écrivez ce que vous pensez observer. Après son exécution, expliquez ce qui confirme ou contredit cette attente. Chacun doit pouvoir expliquer une cellule et une erreur sans l'aide de son binôme.

Pour chaque expérience, remplissez ce journal dans une cellule Markdown :

| Élément | À renseigner |
|---|---|
| Question | Ce que l'expérience cherche à départager |
| Hypothèse | Une prédiction qui pourrait être fausse |
| Variable modifiée | Une modification précise par rapport à la référence |
| Conditions constantes | Données, split, métrique, modèle ou budget conservés |
| Observation | Valeur mesurée, effectif et exemple d'erreur |
| Interprétation | Ce que les observations permettent de conclure |
| Limite | Ce que cette expérience ne permet pas encore de conclure |

Une cellule exécutée sans commentaire ne suffit pas à expliquer une expérience. Vous pouvez vous aider de la documentation ou d'un assistant de code, mais vous devez signaler l'aide utilisée, vérifier les propositions et pouvoir défendre le résultat.

## Éviter les comparaisons trompeuses

Gardez les paraphrases d'un même scénario dans le même split. Choisissez les réglages sur validation. Réservez le test pour la comparaison finale, une fois les choix figés. Comparez les systèmes sur la même tâche, les mêmes exemples et les mêmes catégories. Une sortie générative non conforme au format demandé compte comme un échec selon la règle définie ; on ne l'enlève pas après coup.

Le modèle le plus grand ne doit pas obligatoirement gagner. Documenter une absence d'amélioration peut être un excellent travail. N'inventez pas de résultats : si un calcul n'a pas été exécuté, indiquez-le.

## Conserver et remettre votre travail

À la fin de chaque après-midi, enregistrez le notebook avec vos réponses et téléchargez les JSON de résultats. Au J3, gardez `modele_classification.zip` pour le J5 et l'export séparé `modele_allocine.zip` si produit. Au J4, conservez `adaptateur_lora.zip` et `adaptateur_resume.zip`, qui correspondent à deux adaptations distinctes. Le runtime Colab peut disparaître ; ses fichiers ne sont pas vos sauvegardes.

Pour le projet final, remettez : le notebook, le tableau de comparaison, les résultats exportés, la [model card](../evaluation/MODEL_CARD.md) et une conclusion courte. Le [sujet du projet](../evaluation/PROJET.md) précise le barème. Préparez quatre minutes de présentation : problème, protocole, résultat, erreur et recommandation ; chaque membre répond à une question.

Les [25 questions de quiz](../evaluation/QUIZ.md) vous permettent de vérifier les acquis. Les [ressources](../ressources/RESSOURCES_VERIFIEES.md) sont classées par usage ; commencez par la lecture liée au problème que vous rencontrez.

## Partager seulement ce que vous choisissez

Le cours ne demande aucune publication publique. N'incluez aucune donnée réelle de client ni aucun secret dans les notebooks. Hub et Spaces sont des prolongements volontaires. Si une démo Colab requiert un lien public et que vous ne souhaitez pas le créer, présentez les prédictions dans le notebook : la qualité de votre protocole reste évaluable.
