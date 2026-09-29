# Starters — Jour 2 (TP 4 à 7, + TP 8 bonus) — Formation OpenAI Codex

Les consignes détaillées sont dans le **Guide du participant — Jour 2** (HTML interactif ou Word).
Toutes les commandes du guide se lancent depuis ce dossier `Starters/`.

| Dossier | TP | Contenu |
|---|---|---|
| `base_facturation/` | TP 4 et 6 | projet fil rouge de départ : code, 9 tests, `AGENTS.md`, cahiers des charges (`specs/`, dont `relances.md`). Si vous avez suivi le Jour 1, vous pouvez utiliser votre propre copie. |
| `tp4_action/` | TP 4 | coquille de skill `nouvelle-feature` + spécification de test (export CSV) |
| `tp5_tool/` | TP 5 | API interne factice, `outils.py` / `serveur_mcp.py` / démo function calling à compléter, 16 tests |
| `tp6_agents/` | TP 6 | deux agents (`architecte`, `developpeur`) à compléter |
| `tp7_refactor/` | TP 7 | code hérité `legacy/devis.py` + 8 tests de caractérisation |
| `tp8_hooks/` | TP 8 *(bonus)* | un hook `PreToolUse` à compléter + une commande personnalisée (`/prompts:`) à compléter, 6 tests |

## Prérequis
Python 3.11+, Git, Codex installé, un IDE. Pour le TP 5 (partie A) : une clé d'API OpenAI (`OPENAI_API_KEY`) et un modèle disponible (`OPENAI_MODEL`).
**Ne jamais écrire une clé d'API dans un fichier.**

## À savoir
- `tp5_tool` est livré avec des tests qui **échouent** tant que `outils.py` n'est pas complété : c'est voulu (auto-évaluation).
- `tp7_refactor` doit être **au vert** dès le départ : ses tests protègent le comportement pendant le refactor.
- `tp8_hooks` est **bonus** : à faire si le temps le permet en fin de journée, sinon en autonomie après la formation.
