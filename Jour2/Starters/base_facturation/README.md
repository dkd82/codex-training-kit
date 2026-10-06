# facturation — projet fil rouge

Mini-outil de facturation en ligne de commande. C'est la **base commune** à partir du TP 3 :
tout le monde repart du même code, quel que soit le résultat obtenu au TP 1.

## Démarrage

```bash
python -m venv .venv
# Windows PowerShell : .venv\Scripts\Activate.ps1      macOS/Linux : source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Utilisation

```bash
python -m facturation ajouter-client --id C1 --nom ACME --email contact@acme.example
python -m facturation creer-facture --numero F-001 --client C1 --emission 2025-01-10 --echeance 2025-02-09 --ligne "Stylo;10;1.50"
python -m facturation lister
python -m facturation afficher F-001
```

## Contenu

| Dossier / fichier | Rôle |
|---|---|
| `facturation/` | code applicatif (`models`, `calculs`, `stockage`, `cli`) |
| `tests/` | tests `pytest` |
| `specs/` | cahiers des charges des fonctionnalités à développer |
| `AGENTS.md` | instructions persistantes pour Codex |
