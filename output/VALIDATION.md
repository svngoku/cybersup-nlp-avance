# Validation et préparation de la séance

État au 4 octobre 2026.

- 121 diapositives éditables et autant de notes du présentateur.
- 28 tableaux natifs dans le support.
- 15 illustrations et architectures originales, avec sources SVG et descriptions accessibles.
- 10 formules rendues en images depuis LaTeX ; sources, légendes des symboles et explications détaillées conservées.
- 5 journées de 420 minutes, soit 35 heures hors pauses et déjeuner.
- 14 notebooks valides en JSON et syntaxe Python, sans sorties préremplies.
- Export PDF du support. Les notes détaillées se consultent dans PowerPoint ou Notes-presentateur.md.
- Pack étudiant contrôlé par liste autorisée, sans PowerPoint contenant les notes, corrigés ou guide formateur.
- Template original conservé. Empreinte SHA256 : `d9e8da6adbc57a0abb31a0930e362f43069c5cb1b89f60bea3e1a454e188400d`.
- Template source inclus dans le pack formateur pour permettre sa régénération dans le runtime approprié.

## Vérifications CPU partielles

Les vérifications CPU partielles réellement exécutées sont détaillées dans docs/VERIFICATIONS_CPU.md, inclus dans le pack formateur. Leur portée est limitée aux opérations explicitement consignées.

## Limites de cette validation

Le chargement des poids des modèles, les entraînements GPU et l'enchaînement complet des notebooks sur Google Colab T4 ou Runpod L4 restent à exécuter avant la séance. Les scores et durées GPU ne sont pas préremplis. La syntaxe correcte ne garantit ni les téléchargements du Hub, ni la mémoire disponible, ni la compatibilité d'un runtime futur. Consulter docs/COLAB.md et docs/RUNPOD_OPTION.md pour la répétition et les solutions de repli. Les corpus fictifs servent à comprendre la mécanique et ne constituent pas un benchmark métier ; le transfert sur un sous-ensemble Allociné ne vaut pas évaluation complète du benchmark.
