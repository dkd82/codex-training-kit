# Instructions du projet « facturation »

Mini-outil de facturation en ligne de commande (projet fil rouge de la formation).

## Stack et commandes
- Python 3.11 ou plus, bibliothèque standard uniquement pour le code applicatif.
- Installer les outils de test : `python -m pip install -r requirements-dev.txt`
- Lancer les tests : `python -m pytest -q`
- Lancer l'application : `python -m facturation --help`

## Conventions
- Tous les montants sont des `Decimal`, jamais des `float`. Arrondi commercial au centime (`ROUND_HALF_UP`).
- Annotations de types partout ; docstrings courtes en français.
- Un module = une responsabilité (`models`, `calculs`, `stockage`, `cli`).
- Toute nouvelle fonctionnalité s'accompagne de tests `pytest` dans `tests/`.

## Règles de sécurité
- Ne jamais éditer ni supprimer les fichiers du dossier `donnees/` (données de l'utilisateur) ; dans les tests, utiliser un dossier temporaire (`tmp_path`).
- Ne jamais écrire de clé d'API ou de secret dans le code ou dans les fichiers du dépôt.
- Ne pas ajouter de dépendance externe sans le signaler explicitement.
