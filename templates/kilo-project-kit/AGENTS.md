# <nom du projet> : guide pour les humains et les assistants IA

<!-- Kilo Code charge AGENTS.md depuis la racine du projet (le nom du fichier est en majuscules). Restez bref : environ 40 lignes.
     N'écrivez que ce que l'assistant ne peut pas deviner à partir du code. Remplacez chaque <placeholder>. -->

## Ce qu'est ce projet
<Une ou deux phrases : ce qu'il calcule, sur quelles données.>

## Commandes
- Installation : `<pip install -r requirements.txt>`
- Tests : `<python -m pytest -q>`
- Lancement : `<python scripts/run_analysis.py --data data --out summary.csv>`

## Organisation
- `<package>/` : <une ligne par module>
- `scripts/` : points d'entrée en ligne de commande. `tests/` : pytest. `tests/golden/` : sorties de référence.

## Conventions scientifiques
- Les unités sont dans les noms et les docstrings : `_V`, `_s`, `_hz`, `_db`.
- <Indiquez votre convention dB : rapport d'amplitudes 20*log10, rapport de puissances 10*log10.>
- Ne jamais modifier un tableau d'entrée en place : renvoyer un nouveau tableau.
- Préférer NumPy/SciPy vectorisé ; une boucle Python sur des échantillons nécessite un commentaire qui explique pourquoi.
- Les docstrings précisent les unités et le comportement pour NaN et une entrée vide.

## Règles pour les changements
- Un changement de comportement numérique nécessite un test ET une phrase dans la description de la pull request.
- `tests/golden/*` ne change que volontairement, avec la raison dans le message de commit.
- Ne pas affaiblir ou supprimer un test existant pour le faire passer.
- Aucune nouvelle dépendance sans demander. Aucun chemin absolu. Aucun secret. Aucun gros fichier de données.

## En cas de doute
Posez une question plutôt que de deviner une convention scientifique (dB, fenêtrage, retrait de tendance, unités).
