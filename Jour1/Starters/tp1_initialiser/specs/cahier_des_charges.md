# Cahier des charges — outil de facturation (TP 1)

## Contexte
Une petite entreprise veut un outil en ligne de commande pour gérer ses clients et ses factures.
Ce projet est le **fil rouge** de la formation : on le fait évoluer pendant les deux jours.

## Fonctionnalités attendues
1. **Clients** : ajouter un client (`id`, `nom`, `email`).
2. **Factures** : créer une facture avec un numéro, un client, une date d'émission, une date d'échéance,
   un statut (`brouillon`, `emise` ou `payee`) et une ou plusieurs lignes.
3. **Lignes** : chaque ligne a une description, une quantité (entier), un prix unitaire HT et un taux de TVA
   (20 % par défaut).
4. **Calculs** : total HT, total TVA, total TTC d'une facture.
5. **Stockage** : sauvegarde dans des fichiers JSON (un fichier pour les clients, un pour les factures).
6. **Ligne de commande** : `ajouter-client`, `creer-facture`, `lister`, `afficher <numero>`.

## Contraintes techniques
- Python 3.11 ou plus. Bibliothèque standard uniquement pour le code applicatif.
- Montants en `Decimal` (jamais `float`), arrondi commercial au centime (`ROUND_HALF_UP`).
- Annotations de types ; docstrings courtes en français.
- Tests avec `pytest`.

## Structure attendue
```
facturation/
  __init__.py
  __main__.py
  models.py       # Client, LigneFacture, Facture
  calculs.py      # totaux et arrondis
  stockage.py     # lecture / écriture JSON
  cli.py          # interface en ligne de commande
tests/
  test_calculs.py
  test_stockage.py
  test_cli.py
AGENTS.md         # instructions persistantes pour Codex
README.md
requirements-dev.txt
```

## Critères d'acceptation
- `python -m pytest -q` passe au vert.
- `python -m facturation --help` affiche les 4 commandes.
- Un scénario complet fonctionne : ajouter un client, créer une facture, la lister, l'afficher avec ses totaux.
- Exemple de référence : 10 stylos à 1,50 € HT avec TVA 20 % donnent 15,00 HT, 3,00 TVA, 18,00 TTC.
