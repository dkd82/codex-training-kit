# Critères de revue pour une revue de pull request assistée par IA

Le relecteur IA est un premier passage CONSULTATIF. Un relecteur humain décide.

## Vérifier
- Exactitude numérique : unités, conventions dB (amplitude vs puissance), erreur de décalage d'index, dtype, gestion des NaN.
- Tableaux d'entrée modifiés en place (aliasing) quand l'appelant ne s'y attend pas.
- Changements de comportement non couverts par un test ; un test qui ne peut pas échouer.
- Constantes codées en dur qui devraient être des paramètres.
- Nouvelle dépendance : existe-t-elle, est-elle maintenue, est-elle nécessaire ?

## Ignorer
- Le formatage et l'ordre des imports (gérés par le linter).
- Les préférences de nommage qui ne sont pas dans le fichier de conventions.

## Format de sortie
Listez au maximum 7 commentaires. Pour chacun : fichier:ligne, gravité (haute / moyenne / basse),
ce qui ne va pas, une correction suggérée en une phrase. Dites « aucun problème trouvé » s'il n'y en a pas.
Ne réécrivez pas le fichier entier.
