# Modèle de prompt : explorer une base de code (v1.0)

À utiliser avec : un agent en lecture seule (Kilo Code : *Ask*).

## Objectif
Expliquez-moi ce projet : {{what_it_does}}.

## Contexte
- Dossiers : {{folders}}. Points d'entrée que je connais déjà : {{entry_points}}.
- Lisez d'abord le fichier d'instructions du projet s'il y en a un.

## Contraintes
- Lecture seule : ne modifiez aucun fichier et n'exécutez pas le code.
- Citez le chemin de fichier et le nom de fonction pour chaque affirmation. Dites ce dont vous n'êtes pas sûr au lieu de deviner.

## Format
1. Les points d'entrée.
2. Une ligne par module.
3. Le flux de données de {{input}} à {{output}}, en étapes numérotées.
4. Où vit l'état global ou de niveau module.

## Vérification
Terminez par les trois affirmations dont vous êtes le moins sûr, pour que je puisse les vérifier en ouvrant les fichiers.
