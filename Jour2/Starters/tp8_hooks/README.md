# tp8_hooks — TP 8 (bonus) : hook et commande personnalisée

## Démarrage

```bash
git init
python -m venv .venv
# Windows PowerShell : .venv\Scripts\Activate.ps1      macOS/Linux : source .venv/bin/activate
python -m pip install pytest
python -m pytest -q          # doit échouer tant que le hook n'est pas complété : c'est normal
```

## Contenu

| Fichier | Rôle |
|---|---|
| `.codex/hooks/bloquer_commandes_risquees.py` | le hook à compléter (3 `TODO`) |
| `.codex/hooks.json` | la déclaration du hook (déjà prête) |
| `tests/test_hook.py` | auto-évaluation : `python -m pytest -q` |
| `prompts_perso/nouvelle-fonctionnalite.md` | commande personnalisée à compléter, à copier dans `~/.codex/prompts/` |

Consignes détaillées : voir le Guide du participant, TP 8 (bonus).
