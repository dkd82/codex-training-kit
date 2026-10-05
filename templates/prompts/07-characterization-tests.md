# Modèle de prompt : tests de caractérisation avant un refactoring (v1.0)

À utiliser avec : un agent de code (Kilo Code : *Code*).

## Objectif
Écrivez des tests de caractérisation pour `{{function}}` avant que je la refactore.

## Contexte
- Fichier : `{{file}}`. Elle est appelée depuis {{callers}} avec ce prétraitement : {{preprocessing}}.
- Données disponibles : {{data_files}}.

## Contraintes
- Ne modifiez pas le source. Le fichier golden est généré par le code ACTUEL.
- Gardez une copie de l'implémentation actuelle dans le fichier de test comme **oracle**.

## Exemples
Des signaux aléatoires incluant des égalités et des plateaux, plusieurs valeurs de chaque paramètre (dont 0), des entrées de longueur 0 à 3.

## Format
`tests/test_characterization.py`, un petit script qui écrit `tests/golden/<name>.json`.

## Vérification
Tous les tests passent sur l'implémentation actuelle, inchangée. Montrez la sortie.
