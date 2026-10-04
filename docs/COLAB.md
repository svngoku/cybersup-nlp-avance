# Colab — préparation, sauvegarde et repli

Le parcours vise **Google Colab avec une NVIDIA T4** pour les sections d'entraînement. Le CPU suffit aux calculs élémentaires, aux baselines lexicales et à plusieurs analyses. La disponibilité et le type de GPU ne sont pas garantis par l'offre gratuite ; voir la [FAQ officielle Colab](https://research.google.com/colaboratory/faq.html). Les durées des activités comprennent la lecture et l'analyse, et ne prédisent pas le temps exact de calcul.

Si le formateur fournit un accès Runpod L4, suivre [RUNPOD_OPTION.md](RUNPOD_OPTION.md). L'accès est facultatif ; Colab reste le parcours de référence.

## Ouvrir et lancer un notebook

1. Décompresser le pack étudiant sur son ordinateur.
2. Ouvrir [Google Colab](https://colab.research.google.com/), puis **Fichier → Importer un notebook**. Sélectionner un `.ipynb`, jamais le ZIP du pack.
3. Enregistrer une copie dans Drive, par exemple `Nom_Prenom_J1.ipynb`. Aucun montage Drive n'est nécessaire pour exécuter les TP.
4. Pour les parties GPU : **Exécution → Modifier le type d'exécution → GPU T4**, si proposé. Le libellé exact peut varier.
5. Exécuter la cellule de préparation, puis les imports et le diagnostic du matériel. Si un redémarrage est demandé après installation, redémarrer puis reprendre depuis les imports selon les indications du notebook.
6. Lire le périphérique détecté et les versions. Sélectionner « GPU » dans l'interface ne prouve pas que le code utilise CUDA.
7. Exécuter les cellules dans l'ordre. Les notebooks sont autonomes, sauf l'import volontaire de l'archive du J3 dans le projet du J5.

Les corpus fictifs sont intégrés aux notebooks. Le parcours appliqué Allociné, les dépendances et les modèles sont téléchargés à la demande ; Internet reste nécessaire. Le parcours principal ne requiert ni jeton Hugging Face ni clé d'API payante. Ne pas relancer l'installation au milieu d'une expérience qui fonctionne.

## Budget pratique

| Parcours | Matériel et conduite |
|---|---|
| J1 TF-IDF/BPE, J2 petites matrices | CPU ; ne pas réserver un GPU uniquement pour ces opérations |
| Embeddings, fill-mask, génération courte | CPU possible selon temps disponible ; GPU utile si disponible |
| J3 classification et NER | T4 visée, séquences courtes et nombre d'étapes borné ; suivre les valeurs du notebook |
| J4 LoRA/QLoRA | T4 visée ; un seul modèle chargé à la fois ; FP16 adapté au parcours T4, ne pas activer BF16 par imitation |
| J5 comparaison/démo | Recharger l'archive J3 ; ne pas refaire tout l'entraînement pour une démonstration |

La fiche [NVIDIA T4](https://www.nvidia.cn/content/dam/en-zz/Solutions/Data-Center/tesla-t4/t4-tensor-core-datasheet.pdf) décrit 16 Go de mémoire et le calcul FP16/FP32. La mémoire réellement disponible dans une session dépend des allocations déjà présentes. La [documentation bitsandbytes](https://huggingface.co/docs/bitsandbytes/main/en/installation) précise les contraintes de calcul et d'installation de NF4/FP4. Cette compatibilité matérielle n'est pas une preuve d'exécution de notre notebook.

En cas de manque mémoire, sauvegarder d'abord. Libérer les modèles inutilisés ou repartir d'un runtime neuf, réduire la longueur maximale puis la taille de batch ; conserver un budget documenté. L'accumulation de gradients peut augmenter le batch effectif sans augmenter le micro-batch. Ne jamais réduire seulement le nombre d'exemples test pour gagner de la mémoire : traiter le test en petits lots.

## Sauvegarder à chaque séance

Télécharger le notebook avec ses réponses, les fichiers `resultats/` utiles et les archives exportées. Le stockage du runtime est temporaire. Garder le ZIP du modèle J3 et l'adaptateur J4 sur son ordinateur ou dans son Drive ; ils ne sont pas automatiquement transférés dans une nouvelle session. Au J5, importer l'archive avec le panneau Fichiers ou la cellule prévue, puis vérifier sa relecture.

Un adaptateur LoRA n'est pas un modèle complet : sa réutilisation demande le modèle de base et son tokenizer compatibles. Conserver l'identifiant et la révision lorsqu'elle est disponible, la configuration de quantification, les versions et le template de chat.

Conserver les tâches distinctes : `modele_classification.zip` concerne le support ; `modele_allocine.zip`, le sentiment ; `adaptateur_lora.zip`, le SFT support ; `adaptateur_resume.zip`, l'adaptation au résumé. Le TP06 compare son propre adaptateur au modèle initial sur les mêmes sources réservées.

## Si le GPU n'est pas disponible

**Repli A — individuel CPU.** Terminer l'audit des données, le tokenizer, TF-IDF, les calculs d'attention, les métriques et la grille d'analyse humaine. Les petites inférences restent possibles selon le budget. Ne pas lancer un entraînement long à l'aveugle sur CPU.

**Repli B — binôme avec T4.** Un binôme disposant d'une session exécute le calcul ; les deux étudiants préparent et analysent. Le journal précise qui a exécuté et sur quel matériel. Les rôles alternent.

**Repli C — démonstration formateur.** Utiliser uniquement un artefact et des résultats effectivement obtenus lors de la répétition, avec leur provenance. L'étudiant rédige l'analyse et marque « entraînement observé / non exécuté personnellement ». Aucun résultat GPU préfabriqué n'est fourni comme s'il avait été mesuré.

Ces replis préservent les apprentissages d'analyse, mais **ne valident pas la compétence d'exécution d'un fine-tuning GPU**. Prévoir une reprise ultérieure de cette manipulation si elle doit être certifiée. Les cours restent réalisables sans payer un abonnement en urgence.

## Démonstration Gradio et Hub

La [documentation Gradio](https://gradio.app/main/guides/sharing-your-app) indique que Colab peut créer un lien de partage pour rendre une application accessible. Ne pas traiter un lien `gradio.live` comme un espace privé. Le lancement de l'interface reste volontaire ; si l'exposition publique n'est pas choisie, présenter la fonction de prédiction et ses sorties dans le notebook, ou exécuter localement une démo sans partage après téléchargement du modèle.

La publication Hub/Spaces est une extension. Elle n'est nécessaire ni pour le TP ni pour la note. Si l'étudiant la choisit : vérifier les fichiers et leurs droits, créer un dépôt privé, vérifier sa visibilité, s'authentifier dans l'interface ou une saisie masquée (`getpass`), puis recharger l'artefact depuis le dépôt. Ne jamais coller un jeton dans une cellule sauvegardée, un rendu ou un message. Voir les [paramètres de dépôt Hugging Face](https://huggingface.co/docs/hub/en/repositories-settings).

## Répétition générale avant la promotion

**Statut initial : exécution complète Colab T4 à réaliser.** Les contrôles locaux et statiques figurent dans le rapport de validation livré ; ils ne remplacent pas cette répétition.

| Vérification | Preuve à conserver | État à renseigner |
|---|---|---|
| Import de chaque notebook depuis le pack distribué | Notebook exact, date, versions | À faire dans Colab |
| Téléchargement de chaque tokenizer et modèle | Identifiant, révision si disponible, absence de token requis | À faire dans Colab |
| Détection T4 et dtype | Diagnostic CUDA/GPU et mémoire | À faire dans Colab |
| Parcours essentiels 01 à 07 | Exécution depuis runtime neuf, erreurs éventuelles | À faire dans Colab |
| J3 classification et NER | Configurations, courbes, métriques, durée mesurée | À faire dans Colab |
| J4 adaptation et comparaison avant/après | Modèle de base, adaptateur, prompts et sorties | À faire dans Colab |
| Export J3 puis import J5 | Relecture et prédictions concordantes | À faire dans Colab |
| Export adaptateur puis relecture | Configuration conservée et sortie observée | À faire dans Colab |
| Démo sans publication involontaire | Mode utilisé et résultat fonctionnel | À faire dans Colab |
| Repli CPU | Sections terminées et opérations sautées explicitement | À répéter |

Si un TP dépasse le temps de calcul réservé, réduire le budget d'entraînement **avant** la séance et consigner la variante. L'objectif est un pipeline visible et une comparaison défendable, pas un record de performance.

## Erreurs fréquentes

| Symptôme | Première action raisonnable |
|---|---|
| CUDA indisponible | Vérifier le type de runtime, lire le diagnostic, basculer vers un repli si quota épuisé |
| Import ou dépendance incompatible | Repartir d'une session neuve avec la cellule fournie ; conserver l'erreur et les versions |
| Erreur de mémoire | Garder les exports, libérer l'ancien modèle, réduire batch/longueur |
| Poids de tête nouvellement initialisés | Vérifier que c'est bien une nouvelle tête de tâche, puis entraîner ; ne pas supprimer tous les avertissements |
| Labels NER mal alignés | Afficher tokens, `word_ids` et labels avant de relancer un entraînement |
| Génération répète le prompt | Décoder les nouveaux tokens seulement et vérifier le template de chat |
| Résultat différent d'un autre binôme | Comparer seed, split, révision, dtype, budget et paramètres de génération |
| Archive J3 introuvable | Réimporter la copie téléchargée ; ne pas supposer qu'un runtime précédent existe encore |
