# Vidéos Hugging Face — guide d’animation

Les sept vidéos sont intégrées dans les pages officielles du cours HF citées ci-dessous. Les liens et leur attribution à Hugging Face ont été vérifiés le 5 octobre 2026. Les vidéos sont en anglais et les pages d’accompagnement en français. Préparer le passage, reformuler en français et utiliser les sous-titres disponibles.

Chaque activité de 3 minutes remplace une partie du créneau de la diapositive : prédiction, extrait ciblé, retour à l’exemple du cours. Ce budget ne décrit pas la durée totale de la vidéo. Aucun minutage exact n’est annoncé. Le support contient les définitions et exemples nécessaires si Internet manque. Les vidéos complètent le support ; leurs anciennes versions de code ne remplacent pas celles des TP.

## J1 · Diapositive 21 · Tokenizers Overview

[Page du cours](https://huggingface.co/learn/llm-course/fr/chapter2/4) · [Vidéo Hugging Face](https://www.youtube.com/watch?v=VFp38yj8h3A)

**Avant de regarder.** Un token est-il toujours un mot ?

**Repère de pause.** Quand les étapes texte, tokens et identifiants ont été montrées.

**Réponse attendue.** Non. L’unité dépend du tokenizer : mot, fragment, signe ou unité spéciale.

## J2 · Diapositive 48 · The Transformer architecture

[Page du cours](https://huggingface.co/learn/llm-course/fr/chapter1/4) · [Vidéo Hugging Face](https://www.youtube.com/watch?v=H39Z_720T5s)

**Avant de regarder.** Quelle partie peut consulter toute la source ? Quelle partie ne doit pas lire les tokens futurs de sortie ?

**Repère de pause.** Quand encodeur et décodeur sont distingués dans l’architecture.

**Réponse attendue.** L’encodeur consulte la source autorisée. Le décodeur causal utilise le préfixe disponible, sans tokens futurs de sortie.

## J2 · Diapositive 49 · What is Transfer Learning?

[Page du cours](https://huggingface.co/learn/llm-course/fr/chapter1/4) · [Vidéo Hugging Face](https://www.youtube.com/watch?v=BqqfQnyjmgg)

**Avant de regarder.** Qu’est-ce que l’on récupère avant l’adaptation ?

**Repère de pause.** Quand préentraînement et fine-tuning sont mis en relation.

**Réponse attendue.** Des poids préentraînés et leur configuration, avec le tokenizer compatible. La tête de tâche peut être nouvelle.

## J3 · Diapositive 61 · The Trainer API

[Page du cours](https://huggingface.co/learn/llm-course/fr/chapter3/3) · [Vidéo Hugging Face](https://www.youtube.com/watch?v=nvBXf7s7vTI)

**Avant de regarder.** Qui décide du bon label et de la bonne métrique : Trainer ou notre protocole ?

**Repère de pause.** Quand les objets fournis au Trainer sont présentés.

**Réponse attendue.** Le protocole et les données définissent la tâche. Trainer orchestre les opérations configurées.

## J3 · Diapositive 67 · Tasks: Token Classification

[Page du cours](https://huggingface.co/learn/llm-course/fr/chapter7/2) · [Vidéo Hugging Face](https://www.youtube.com/watch?v=wVHdVlPScxA)

**Avant de regarder.** Pourquoi classer toute la phrase ne suffit-il pas pour la NER ?

**Repère de pause.** Quand une étiquette est attribuée à chaque position du texte.

**Réponse attendue.** Il faut localiser les segments et leurs types, puis conserver leur alignement avec le texte.

## J4 · Diapositive 94 · Tasks: Summarization

[Page du cours](https://huggingface.co/learn/llm-course/fr/chapter7/5) · [Vidéo Hugging Face](https://www.youtube.com/watch?v=yHnr5Dk2zCI)

**Avant de regarder.** Quels faits du colis AB123 doivent survivre au résumé ?

**Repère de pause.** Quand la tâche source longue vers résumé court a été illustrée.

**Réponse attendue.** La référence, la date, l’article manquant et la demande de vérification, sans inventer un remboursement.

## J5 · Diapositive 106 · What is the ROUGE metric?

[Page du cours](https://huggingface.co/learn/llm-course/fr/chapter7/5) · [Vidéo Hugging Face](https://www.youtube.com/watch?v=TMshhnrEXlg)

**Avant de regarder.** Un recouvrement élevé suffit-il à prouver qu’un résumé est fidèle ?

**Repère de pause.** Quand le recouvrement entre résumé candidat et référence est expliqué.

**Réponse attendue.** Non. Ajouter une négation peut inverser le fait en conservant presque tous les mots. Vérifier les affirmations contre la source.
