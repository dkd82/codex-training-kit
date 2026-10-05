# Modèle de prompt : revue d'un diff (v1.0)

À utiliser avec : un agent en lecture seule dans une **session neuve** (Kilo Code : *Ask* avec `@git-changes`, ou le sous-agent `reviewer` du kit de projet).

## Objectif
Relisez les changements ci-dessous en tant que premier relecteur, CONSULTATIF. C'est un humain qui décide.

## Contexte
- Conventions du projet : le fichier d'instructions du projet. Critères de revue : `{{path_to_REVIEW_CRITERIA.md}}`.
- Les changements : {{the_diff_or_@git-changes}}

## Contraintes
- 7 commentaires au maximum, du plus grave au moins grave. Ne réécrivez pas le code. Ne commentez pas le formatage.

## Format
Pour chaque commentaire : fichier:ligne, gravité (haute / moyenne / basse), le problème, un correctif en une phrase. Ou « aucun problème trouvé ».

## Vérification
Dites quelles parties du changement vous n'avez PAS pu juger (contexte manquant), pour que je les relise moi-même.
