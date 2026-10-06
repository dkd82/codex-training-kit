# Spécification — export CSV des factures (feature de test pour le TP 4)

Objectif : vérifier que votre skill « nouvelle-feature » organise bien le travail.

Fonctionnalité : commande `python -m facturation exporter-csv --sortie factures.csv` qui écrit un fichier CSV
avec une ligne par facture : `numero;client_id;statut;date_emission;date_echeance;total_ht;total_tva;total_ttc`.

Contraintes : module `facturation/export.py`, module `csv` de la bibliothèque standard, séparateur `;`,
montants avec 2 décimales, tests `pytest`.

Vous ne devez PAS implémenter la feature à la main : c'est la skill qui doit guider Codex (plan → tests → code → doc).
