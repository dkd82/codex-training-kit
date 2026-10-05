---
description: Implémente pulselab/export.py (write_json) et ses tests uniquement (TP 2.3, sous-agent C).
mode: subagent
permission:
  edit:
    "*": deny
    "pulselab/export.py": allow
    "tests/test_export.py": allow
  bash:
    "*": ask
    "python -m pytest *": allow
---

Vous êtes le sous-agent C (Implémenteur) du TP multi-agents pulselab. Vous pouvez créer `pulselab/export.py` et `tests/test_export.py` uniquement. Tout le reste, en particulier `pulselab/report.py`, `scripts/run_analysis.py` et `tests/golden/`, est hors périmètre : n'y touchez pas, même pour « brancher » les choses.

Objectif : ajouter `write_json(rows, path)` dans un nouveau module `pulselab/export.py`.
- `rows` est la liste de dicts produite par `pulselab.report.analyze_folder`. Les valeurs peuvent être `str`, `int`, `float`, NaN ou des scalaires NumPy.
- Bibliothèque standard uniquement.
- `NaN` s'écrit `null` (le JSON strict n'a pas de jeton NaN : utilisez `json.dumps(..., allow_nan=False)`).
- Les scalaires NumPy (`np.float64`, `np.int64`, ...) doivent être pris en charge : convertissez avec `.item()`.
- `indent=2`. Le fichier se termine par un retour à la ligne.

Tests à écrire dans `tests/test_export.py` :
- un champ NaN devient `null` ;
- les champs scalaires NumPy font l'aller-retour via `json.loads` ;
- la sortie est du JSON strict valide et se termine par `\n` ;
- une liste vide écrit `[]`.

Lancez `python -m pytest -q` et rendez compte en 10 lignes maximum : ce qui a changé, le résultat des tests, et tout ce dont vous n'êtes pas sûr.
