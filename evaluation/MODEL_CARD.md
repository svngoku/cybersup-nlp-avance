# Model card — à compléter

Ce modèle est un prototype pédagogique. Remplacer les champs entre crochets par des observations réelles. Une absence de mesure se note **non mesuré** ; une exécution absente se note **non exécuté**. Ne pas inventer une licence ni une performance.

## Identification

- Nom du projet : [nom]
- Auteurs et contributions : [noms et rôles]
- Date et version : [date, version du notebook]
- Tâche et sortie attendue : [catégorie, entités, résumé…]
- Modèle de base / révision : [identifiant exact, commit si connu]
- Tokenizer / template de chat : [identifiant et particularités]
- Artefact remis : [modèle complet ou adaptateur, nom du fichier]
- Licence du modèle de base et source : [lien vers la carte/licence exacte]
- Licence/statut de l'adaptateur et des données : [droits vérifiés, sans supposer qu'une licence couvre tout]

## Usage prévu

[Qui utiliserait cette sortie ? Quelle décision accompagne-t-elle ? Quel contrôle humain est prévu ?]

Usages hors périmètre : [données réelles non évaluées, décisions sensibles, langues ou longueurs non testées…]

## Données et préparation

- Origine : [corpus fictif intégré / autre source autorisée]
- Unité d'observation et annotation : [texte, scénario, règle de label]
- Langue(s), catégories et effectifs : [table]
- Déduplication et groupes de paraphrases : [méthode]
- Train / validation / test : [effectifs, seed, groupes, empreintes si disponibles]
- Nettoyage et transformations apprises : [quoi, pourquoi, sur quel split]
- Limites de représentativité : [variété, taille, ambiguïtés, artificiel/réel]

## Adaptation et environnement

- Logiciels et versions : [Python, PyTorch, Transformers, PEFT, TRL…]
- Matériel effectivement utilisé : [GPU exact / CPU, mémoire observée]
- Seed, longueur maximale, batch, accumulation : [valeurs]
- Budget : [epochs/steps, durée mesurée, exemples vus]
- Paramètres entraînables : [nombre et proportion, couches visées]
- LoRA/quantification si applicable : [rang, alpha, modules, dtype, bits]
- Statut : [exécuté par le groupe / démonstration attribuée / non exécuté]

## Évaluation

Protocole figé : [moment de gel du prompt et des réglages, règle de parsing, usage du test].

| Système | Split / n | Métrique principale | Validité de sortie | Temps et matériel | Limite |
|---|---|---|---|---|---|
| Baseline simple | [ ] | [ ] | [ ] | [ ] | [ ] |
| Zero-shot, si pertinent | [ ] | [ ] | [ ] | [ ] | [ ] |
| Modèle adapté | [ ] | [ ] | [ ] | [ ] | [ ] |

Ajouter effectifs par classe, matrice de confusion ou grille humaine selon la tâche. Pour un résumé : distinguer fidélité, couverture et forme. Pour NER : préciser le niveau d'évaluation, les frontières et les types. Pour la latence : distinguer chargement et inférence, donner le nombre et la longueur des entrées.

## Erreurs et limites

| Cas | Référence / source | Sortie | Type d'erreur | Conséquence |
|---|---|---|---|---|
| [1] | [ ] | [ ] | [ ] | [ ] |
| [2] | [ ] | [ ] | [ ] | [ ] |
| [3] | [ ] | [ ] | [ ] | [ ] |
| [4] | [ ] | [ ] | [ ] | [ ] |
| [5] | [ ] | [ ] | [ ] | [ ] |

Tests d'entrée vide, texte long, négation et ambiguïté : [observations].

Incertitudes non résolues : [petit test, corpus artificiel, scores instables, disponibilité GPU, expérience manquante…].

## Relecture et démonstration

Fichiers nécessaires : [poids/adaptateur, tokenizer, configuration, mapping des labels].

Contrôle de rechargement : [date, environnement neuf ou non, entrées comparées et résultat].

Mode de démo : [notebook, Gradio local, partage choisi] ; visibilité : [aucune publication / privée / publique choisie].

## Recommandation

[Choix recommandé et justification ; une limite concrète ; prochaine expérience nécessaire avant élargissement de l'usage.]

## Sources

[Liens des données, du modèle, de la documentation/API et des aides utilisées.]
