# Option Runpod L4 — les mêmes TP dans JupyterLab

**NLP Avancé (BERT, GPT, Hugging Face) · M2 IA · 35 heures.**

Le parcours de référence reste Colab T4. Cette option s'applique uniquement si le formateur fournit un accès Runpod à chaque étudiant ou binôme. Ce document ne crée aucune machine, ne choisit aucun abonnement et ne fournit aucun identifiant. L'environnement Runpod doit faire l'objet de sa propre répétition avant le cours.

## Ouvrir l'espace déjà attribué

Utiliser l'accès communiqué individuellement. Pour un Pod disposant d'une image compatible, la [documentation Runpod](https://docs.runpod.io/pods/connect-to-a-pod) indique **Connect**, puis le service **JupyterLab**. L'existence et l'authentification de ce service dépendent de l'image préparée. Ne pas inventer un mot de passe par défaut ni diffuser l'URL d'une session authentifiée.

Importer les `.ipynb` et travailler dans l'emplacement persistant indiqué, généralement un volume sous `/workspace`. Le nom du dossier seul ne prouve pas sa persistance : vérifier la configuration fournie. Créer un dossier individuel et conserver une copie locale du pack et des rendus.

## Vérifier avant un entraînement

Dans les cellules de diagnostic du notebook, relever Python, PyTorch, CUDA, les bibliothèques et le GPU. Vérifier que `torch.cuda.is_available()` est vrai, puis lire `torch.cuda.get_device_name(0)` et la mémoire. Un GPU annoncé dans la console n'est pas forcément celui visible par le noyau Jupyter.

La [fiche NVIDIA L4](https://www.nvidia.com/en-us/data-center/l4/) annonce 24 Go et le calcul Tensor Core FP16/BF16. Le parcours conserve par défaut la configuration FP16 prévue pour T4/L4. BF16 reste facultatif si matériel et logiciel le supportent, notamment lorsque `torch.cuda.is_bf16_supported()` le confirme. Toute variante doit être documentée et répétée. Ne pas activer FP16 et BF16 simultanément dans la configuration d'entraînement.

Utiliser la préparation et les versions du cours. L'image PyTorch fournie peut avoir une autre version : lire les contraintes avant de remplacer des paquets. Redémarrer le noyau si nécessaire après installation. Les cellules propres à `google.colab` restent facultatives ; dans JupyterLab, importer et télécharger depuis l'explorateur de fichiers.

Si aucun GPU n'est détecté, suspendre le calcul lourd et transmettre le diagnostic au formateur. Ne pas recréer ou redimensionner une machine attribuée à quelqu'un d'autre. Les sections CPU restent utilisables pendant la résolution.

## Garder une comparaison reproductible

Conserver modèles, splits, seeds, longueurs et budgets du parcours de référence. Enregistrer l'image/environnement utilisé, les versions, le GPU, le dtype et les temps mesurés. Une L4 peut permettre d'autres budgets, mais aucun facteur d'accélération T4/L4 n'est garanti.

**Expérience facultative de vingt minutes, prise dans le temps d'investigation déjà prévu :** utiliser un modèle chargé et un ensemble fixe d'entrées, effectuer un échauffement puis modifier seulement la **taille du batch d'inférence**. Garder textes, longueur maximale, modèle, dtype et décodage constants. Relever mémoire maximale et temps d'inférence ; distinguer le chargement initial. Vérifier les prédictions et interpréter les écarts. Ne pas modifier aussi la longueur ou le modèle. Cette activité ne prolonge pas les 35 heures et ne change pas le barème.

Le corpus réel garde les mêmes partitions et la même tâche sur tous les GPU. Les valeurs absentes sont « non mesuré » ; ne pas reprendre le temps d'un autre étudiant comme sa propre mesure.

## Sauvegarder puis arrêter le calcul

Avant de quitter, enregistrer le notebook, télécharger JSON, modèles et adaptateurs produits, puis vérifier leur ouverture sur son ordinateur. Fermer l'onglet Jupyter ne suffit pas à arrêter une machine.

Suivre la consigne du formateur pour **arrêter le Pod attribué**, puis vérifier son état. D'après la [documentation Runpod](https://docs.runpod.io/pods/manage-pods), l'arrêt libère le GPU mais le stockage conservé peut rester facturé. Le disque de conteneur peut être perdu ; un volume persistant a un autre cycle de vie. La suppression définitive est distincte et destructive : elle appartient au propriétaire du compte, après sauvegarde.

Ne pas arrêter une machine partagée encore utilisée par un autre groupe. Aucun jeton Runpod/Hugging Face ne doit figurer dans une cellule, un ZIP ou une capture partagée. Une publication Hub/Spaces reste un choix facultatif distinct de l'accès au GPU.

## Répétition à consigner

| Point | Preuve | Statut initial |
|---|---|---|
| JupyterLab et noyau | Image, Python, accès individuel | À vérifier |
| CUDA et L4 | Nom, mémoire, dtype | À vérifier |
| Installations du cours | Versions et éventuel redémarrage | À vérifier |
| Entraînements J3/J4 | Configurations, sorties et durées réelles | À exécuter |
| Relecture modèle/adaptateur | Prédictions après rechargement | À exécuter |
| Téléchargement des rendus | Fichiers ouverts hors du Pod | À vérifier |
| Fin de séance | Sauvegarde et état arrêté confirmé | À vérifier |

La validation statique ne remplit pas cette grille. Le rapport `output/VALIDATION.md` décrit uniquement les vérifications effectivement réalisées lors de la livraison.
