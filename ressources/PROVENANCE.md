# Provenance et règles de réutilisation

**Inventaire et consultation : 4 octobre 2026.** Les références complètes et leur rôle figurent dans [RESSOURCES_VERIFIEES.md](RESSOURCES_VERIFIEES.md). Les numéros ci-dessous désignent les diapositives internes des PPTX fournis.

## Template Cybersup fourni

Le support dérive de `CYBERSUP - TEMPLATE DATA_IA.pptx`, fourni dans ce dossier. Sa mise en page et son identité visuelle servent de base au cours ; le fichier original est conservé. La qualité de cette reprise doit être vérifiée séparément de celle du contenu pédagogique.

Le présentateur du cours est **Chrys NIONGOLO**. Les exemples de biographie, photo ou certifications présents dans un template ne sont pas des informations vérifiées sur le formateur. Aucune biographie ne doit en être déduite.

## Supports pédagogiques fournis

| Support local | Diapositives / idée examinée | Réutilisation pédagogique |
|---|---|---|
| `08-NLP-avec-Deep-Learning.pptx` | 4 et 9 : entrée/cible décalées | Nouvel exemple en français pour la prédiction du token suivant |
| Même support | 8 et 12 : IDs et embedding | Explication séparant index de vocabulaire et vecteur appris |
| Même support | 11–15 : Embedding, GRU, Dense | Rappel historique limité avant l'attention ; pas de long entraînement RNN imposé |
| Même support | 16 et 31 : température et génération | Expérience de décodage ; distinction sampling/greedy |
| `Comprendre les Transformers et les mécanismes d'attention.pptx` | 2–12 : récurrence, encodeur-décodeur et attention | Transition visuelle reformulée avant Q/K/V |
| Même support | 13–19 : produits QK et mélange des valeurs | Exemples numériques originaux avec dimensions contrôlées |
| Même support | 23–29 : self-attention et têtes | Décomposition en têtes et vérification de `d_k` |
| Même support | 34–37 : masque causal et sortie décalée | Mini-exercice de matrice de masque et test de non-accès au futur |

Ces fichiers servent de repères conceptuels et restent dans le dossier de travail. Le cours ne redistribue pas leurs diapositives intégrales dans les packs, ni ne suppose une licence générale de redistribution. Les auteurs et droits de ces supports n'étant pas établis par leurs seuls titres, aucune attribution inventée n'est ajoutée.

### Rectifications techniques apportées aux exemples repris

Dans le support attention, la diapositive 18 annonce une dimension `(1, 1, 4)` mais affiche cinq poids ; nos exemples font correspondre exactement positions et poids. La diapositive 26 contient `Vi = K[0]` dans une illustration : les valeurs doivent provenir de V. Après un découpage de 256 dimensions en huit têtes de 32 dimensions, la normalisation doit utiliser `sqrt(32)` par tête ; la diapositive 27 indique encore `sqrt(256)`. Les schémas et exercices du présent cours suivent les dimensions par tête.

Le support RNN évoque un minimum de caractères pour obtenir des résultats réalistes : nous n'en faisons pas un seuil universel. Taille des données, architecture, préentraînement, objectif et critère de qualité changent cette exigence. Les cibles peuvent être des indices de classe plutôt qu'un one-hot explicite selon la loss et la bibliothèque. Les explications sur GRU restent un rappel des mécanismes, sans assimiler exactement ses portes à celles d'un LSTM.

## Continuité avec les autres cours Cybersup

Les dossiers voisins `deep-learning-intro` et `machine-learning-avancés` ont été consultés pour le format de livraison, le découpage en 35 heures, les consignes d'import Colab, la séparation étudiant/formateur et la place des notes orales. Le présent cours reprend ces conventions, pas leurs anciens scores, leurs résultats de CI ou leurs affirmations d'exécution.

Les connaissances réactivées sont split/validation, métriques, gradients, tenseurs et attention. Les exemples, quiz, rubriques de projet et scénarios de support client sont rédigés pour cette semaine de NLP. Les présentations antérieures ne constituent pas un prérequis documentaire à distribuer.

## Sources externes

Le [cours Hugging Face](https://huggingface.co/learn/llm-course/fr/chapter1/1) est crédité comme socle. Sa page précise une licence Apache 2.0 ; cela ne doit pas être étendu aux artefacts tiers auxquels il renvoie. Le parcours français couvre nos lectures de base ; les chapitres avancés 10–11 consultés sont en anglais. Les exercices du pack sont adaptés à notre durée, au français et à des données fictives, avec les liens vers les lectures originales.

[Stanford CS224N](https://web.stanford.edu/class/cs224n/) sert de référence théorique. Nous ne recopions ni les devoirs ni leurs solutions. Les petits calculs guidés sont originaux et visent les mêmes notions : représentation, dimensions, attention et protocole d'évaluation. Les articles Attention Is All You Need, BERT, LoRA et QLoRA sont référencés pour leurs concepts ; leurs figures et tableaux de performances ne deviennent pas des résultats du cours.

### Introduction historique du J1

Les dates, chercheurs, institutions et contributions de l'introduction sont documentés dans [SOURCES_INTRO_NLP.md](../docs/SOURCES_INTRO_NLP.md), à partir des publications originales et de leurs notices institutionnelles ou éditoriales. Les formulations françaises et exemples sont originaux. Les repères distinguent notamment IDF/TF-IDF, vecteurs statiques/contextuels et prépublication/publication ; aucune figure, photo ou page de ces articles n'est recopiée. La fiche peut accompagner les deux packs : elle ne contient pas de corrigé.

## Corpus et modèles

Les données du fil rouge sont de courts textes fictifs intégrés aux notebooks, conçus pour l'enseignement. Les noms, lieux et identifiants illustrent des cas synthétiques ; ils ne proviennent pas de dossiers réels de clients. La présence de scénarios artificiels proches rend nécessaire un split groupé et limite la portée des scores. Aucun résultat obtenu sur ce corpus n'est présenté comme un benchmark public ou une validation métier.

Le parcours appliqué du TP03 complète ces exemples avec [Allociné, publié par Théophile Blard](https://huggingface.co/datasets/tblard/allocine) : des avis français, une cible de sentiment et une licence MIT indiquée sur la carte. Celle-ci annonce des films disjoints entre splits. Le cours prélève 1 000/200/200 avis dans les partitions d'origine, ne les redistribue pas dans les ZIP et exporte un modèle séparé `modele_allocine.zip`. Les résultats de ce sous-ensemble ne sont pas ceux du benchmark complet. La licence déclarée du dépôt n'est pas une revendication de propriété des avis ni de la marque Allociné.

Le TP06 adapte spécifiquement le modèle au résumé sur des exemples pédagogiques avec sources réservées et produit `adaptateur_resume.zip`. L'adaptateur support du TP05 reste séparé ; aucune qualité de résumé ne lui est attribuée par simple analogie.

Les modèles sont téléchargés depuis leurs dépôts d'origine :

| Modèle | Source de licence consultée | Usage |
|---|---|---|
| Multilingual MiniLM L12 v2 | [Carte du modèle](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) : Apache-2.0 | Représentations de phrases |
| DistilBERT multilingual cased | [Carte du modèle](https://huggingface.co/distilbert/distilbert-base-multilingual-cased) : Apache-2.0 | Encodeur et adaptation classification/NER |
| Qwen2.5-0.5B-Instruct | [Carte du modèle](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) : Apache-2.0 | Génération et adaptation SFT/LoRA |

Ces mentions concernent les dépôts précis consultés, pas tous les modèles de ces familles. Les poids ne sont pas ajoutés aux archives du cours. Les étudiants conservent dans leurs résultats l'identifiant et, si disponible, la révision effectivement utilisés.

IMDb est proposé comme extension facultative : textes anglais, source [Stanford / Maas et al.](https://ai.stanford.edu/~amaas/data/sentiment/), [carte HF](https://huggingface.co/datasets/stanfordnlp/imdb) indiquant une licence « other ». Le pack ne contient pas une copie du dataset et ne lui attribue pas une licence Apache/CC par défaut. Lire ses conditions avant toute redistribution ou publication.

## Distribution et traçabilité

Le pack étudiant doit exclure les corrigés, les notes du présentateur et tout support formateur révélant des réponses. Le PowerPoint avec ses notes appartient au pack formateur. Une version de projection distribuée aux étudiants doit être dépourvue de ces notes. Les sources PPTX fournies et les poids téléchargés ne sont pas nécessaires dans le pack étudiant.

Aucune licence globale de ce dossier ne doit être interprétée comme une autorisation couvrant toutes les ressources tierces. Les sources sont liées, les exemples pédagogiques reformulés et les modifications décrites ici. Aucune publication publique ou dépôt distant n'est requis pour la livraison du cours. Les éventuels exports Hub des étudiants restent un choix explicite, documenté avec leur visibilité.

## Option matérielle

Runpod L4 est une option pour des accès éventuellement fournis par le formateur, pas une ressource déjà créée. Les instructions utilisent la [connexion JupyterLab officielle](https://docs.runpod.io/pods/connect-to-a-pod), la [gestion du cycle de vie des Pods](https://docs.runpod.io/pods/manage-pods) et la [fiche NVIDIA L4](https://www.nvidia.com/en-us/data-center/l4/). Aucun identifiant, secret ou URL d'accès personnel n'est incorporé au support. Le matériel effectivement disponible et l'exécution restent à vérifier pendant la répétition.
