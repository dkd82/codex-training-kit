# Starters — Jour 1 (TP 1 à 3) — Formation OpenAI Codex

Les consignes détaillées sont dans le **Guide du participant — Jour 1** (HTML interactif ou Word).
Toutes les commandes du guide se lancent depuis ce dossier `Starters/`.

| Dossier | TP | Contenu |
|---|---|---|
| `tp1_initialiser/` | TP 1 | cahier des charges seul : Codex génère le projet |
| `tp2_api/` | TP 2 | scripts d'appel à l'API (Bash, PowerShell, Python) à compléter, `prompt.txt` à écrire |
| `base_facturation/` | TP 3 | **base commune** : code, 9 tests, `AGENTS.md`, cahiers des charges (`specs/`, dont `remises.md`) |

## Prérequis
Python 3.11+, Git, Codex installé, un IDE. Pour le TP 2 : une clé d'API OpenAI (variable d'environnement `OPENAI_API_KEY`)
et un modèle disponible (`OPENAI_MODEL`). **Ne jamais écrire une clé d'API dans un fichier.**

## Vérifier la base
```bash
cd base_facturation
python -m venv .venv
# Windows PowerShell : .venv\Scripts\Activate.ps1      macOS/Linux : source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest -q          # attendu : 9 tests au vert
```
