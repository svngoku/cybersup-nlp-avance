# Projet final — Un assistant NLP pour le support client

**Travail en binôme · 240 minutes au J5, soutenance et remise comprises · barème sur 20.**

Le projet réutilise les artefacts de la semaine. Son but est de recommander un système pour une tâche précise à partir de preuves comparables. Il n'est pas demandé de créer un chatbot généraliste ni de lancer un grand entraînement en quatre heures.

## Parcours principal : router une demande

À partir des textes fictifs fournis, prédire la catégorie de chaque demande. Conserver le schéma des labels et le découpage par scénarios du notebook. Réutiliser le classifieur entraîné au J3 en important `modele_classification.zip`. La métrique principale est le macro-F1 ; compléter avec effectifs par classe, matrice de confusion et analyse d'erreurs.

Comparer au minimum :

1. Une référence triviale (classe majoritaire) et la baseline TF-IDF + classifieur du notebook.
2. Le modèle adapté du J3, rechargé et identifié.
3. Lorsque le runtime le permet, un **zero-shot génératif** à partir du modèle Instruct initial, avec les labels autorisés décrits dans le prompt et sans exemples de démonstration. Fixer prompt, décodage et règle de lecture des sorties sur validation.

Les trois approches reçoivent les **mêmes demandes test**, prédisent les **mêmes labels** et sont évaluées avec la **même métrique**. Une sortie du LLM hors liste est une prédiction invalide, comptée comme incorrecte ; publier aussi le taux de sorties valides. Ne pas supprimer les exemples qui échouent.

Une tête de classification fraîchement initialisée n'est pas une baseline zero-shot sémantique. Un modèle Instruct a déjà été entraîné auparavant : « zero-shot » signifie ici absence d'exemples de démonstration dans le prompt pour cette tâche, pas absence de tout apprentissage antérieur.

## Protocole à figer avant le test

Rédiger une fiche d'une demi-page : tâche et sortie, catégories, population fictive, groupes/splits, taille de chaque split, métrique, baseline, modèle/revision, budget, règle de sélection et gestion des sorties invalides. Les transformations apprises utilisent les données autorisées par le split. La sélection du modèle, du prompt et du seuil éventuel utilise la validation.

Les exemples test du projet ne servent ni à choisir les hyperparamètres ni à écrire un prompt qui reconnaît leurs formulations. Si un exemple ou scénario a déjà servi au réglage pendant la semaine, il appartient au développement ; documenter ce fait et utiliser le test réservé fourni. Si le test final est consulté plusieurs fois pour choisir un système, renommer honnêtement ce jeu « validation » et ne plus revendiquer une estimation indépendante.

Les splits étant accessibles dans un notebook pédagogique, leur protection repose sur le respect du protocole. Des données fictives groupées réduisent certaines fuites, mais ne reproduisent pas la variété d'une population réelle.

## Plan de travail

| Étape | Minutes | Preuve |
|---|---:|---|
| Cadrer tâche, métrique et rôles | 15 | Fiche de protocole |
| Recharger l'artefact J3 et auditer les splits | 20 | Prédictions de contrôle et tailles |
| Construire les baselines | 40 | Validation, paramètres et budget |
| Comparer le modèle adapté et le zero-shot disponible | 45 | Tableau sur validation commune |
| Figer les choix ; test final et erreurs | 30 | Résultats finaux avec effectifs |
| Préparer la démonstration | 20 | Fonction testée sur entrées nominales et limites |
| Rédiger la model card et la recommandation | 20 | Une à deux pages |
| Soutenir | 40 | Huit binômes maximum, cinq minutes chacun ; galerie sinon |
| Sauvegarder et remettre | 10 | Dossier complet |
| **Total** | **240** | |

## Livrables

- Notebook avec réponses et sorties, exécutable dans l'environnement indiqué, ou limitations d'exécution clairement marquées.
- Tableau de comparaison : système, split, nombre d'exemples, macro-F1, validité des sorties, temps de prédiction, matériel et budget. Marquer « non exécuté » lorsque nécessaire, jamais zéro à la place d'une mesure absente.
- Au moins cinq exemples d'erreurs ou cas limites, avec texte, référence, prédiction et catégorie d'échec.
- Exports de résultats et identification de l'artefact rechargé ; conserver tokenizer, labels et configuration nécessaires.
- [Model card](MODEL_CARD.md) complétée et recommandation : système retenu, raison, limite, prochaine validation.
- Contribution individuelle de chaque membre et aide extérieure utilisée.

La démonstration peut être une interface Gradio ou un scénario de prédictions dans le notebook. Elle doit traiter explicitement une entrée vide, un texte long et un cas ambigu. Aucune URL publique n'est exigée.

## Barème sur 20

| Critère | Points | Attribution |
|---|---:|---|
| Protocole et absence de fuite | 4 | 1 tâche/labels ; 1 groupes/splits ; 1 sélection sur validation ; 1 test figé |
| Comparaison équitable | 4 | 1 référence simple ; 1 modèle adapté identifié ; 1 mêmes entrées/métriques ; 1 zero-shot défini ou indisponibilité documentée avec plan reproductible |
| Évaluation et analyse | 4 | 1 métrique/effectifs ; 1 sorties invalides et erreurs ; 1 robustesse ; 1 conclusion proportionnée aux données |
| Reproductibilité | 3 | 1 versions/seed/modèles ; 1 exports ; 1 relecture ou limitation explicitement constatée |
| Démonstration et model card | 3 | 1 cas nominal ; 1 entrées limites ; 1 documentation complète |
| Soutenance et compréhension individuelle | 2 | 1 argumentation ; 1 réponses des deux membres |
| **Total** | **20** | |

Les moyens matériels ne doivent pas décider de la note. Si le GPU manque, utiliser un artefact de démonstration **réel et attribué** fourni par le formateur, ou documenter précisément le calcul non réalisé et analyser les baselines exécutées. Le critère associé évalue alors le protocole et l'analyse ; la compétence d'exécution GPU reste à reprendre. Une recommandation de ne pas déployer peut recevoir tous les points.

Une fuite non corrigée invalide les conclusions de performance et les points correspondants du protocole. Les autres acquis restent évaluables. Un meilleur score brut n'accorde aucun bonus automatique.

## Variantes à faire valider au début du J5

**Avis réels en français :** si vous choisissez la variante Allociné du J3, le projet porte sur le sentiment positif/négatif et reprend `modele_allocine.zip`. Le modèle support `modele_classification.zip` n'est pas adapté à ces labels. Les 200 exemples test déjà évalués au J3 ne peuvent plus être présentés comme un nouveau test indépendant au J5 : réserver avant tout réglage un autre sous-ensemble du test d'origine ou déclarer explicitement la comparaison comme réanalyse du test J3. Garder les mêmes exemples pour les systèmes comparés et déclarer les volumes réels.

**Résumé :** le TP06 fournit `adaptateur_resume.zip`, entraîné pour cette tâche, à comparer au modèle initial sur des sources réservées et avec la même grille. L'adaptateur support du TP05 ne doit pas être substitué à celui-ci.

Une tâche métier différente est possible si elle reste comparable et réalisable avec les artefacts de la semaine. Pour le résumé : comparer une baseline extractive, le modèle initial et le modèle adapté **seulement si celui-ci a été adapté à la même tâche** ; utiliser les mêmes sources et une grille de factualité/couverture. Pour NER : garder le même schéma d'entités et évaluer les spans exacts ; un classifieur global ne sert pas de comparaison.

Les étudiants ne doivent pas comparer un score de classification à un score ROUGE ni attribuer au SFT sur une tâche un gain sur une autre sans expérience. Le parcours principal classification est le plus sûr pour terminer dans le temps imparti.
