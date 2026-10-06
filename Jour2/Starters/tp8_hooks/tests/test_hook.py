"""Auto-évaluation du TP 8 : `python -m pytest -q` doit passer au vert une fois le hook complété.

On simule ce que Codex envoie à un hook PreToolUse : un objet JSON sur l'entrée standard.
On vérifie uniquement le code de sortie (0 = autorisé, 2 = bloqué), conformément à la
documentation officielle des hooks — sans dépendre d'un champ JSON précis pour la commande.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / ".codex" / "hooks" / "bloquer_commandes_risquees.py"


def _lancer(commande: str) -> subprocess.CompletedProcess:
    entree = json.dumps(
        {
            "session_id": "test",
            "cwd": ".",
            "hook_event_name": "PreToolUse",
            "tool_name": "Bash",
            "tool_input": {"command": commande},
        }
    )
    return subprocess.run([sys.executable, str(SCRIPT)], input=entree, capture_output=True, text=True)


def test_commande_normale_autorisee():
    r = _lancer("git status")
    assert r.returncode == 0


def test_lecture_de_fichier_autorisee():
    r = _lancer("cat README.md")
    assert r.returncode == 0


def test_suppression_de_la_racine_bloquee():
    r = _lancer("rm -rf /")
    assert r.returncode == 2
    assert r.stderr.strip() != ""  # la raison du blocage doit être expliquée


def test_suppression_du_dossier_personnel_bloquee():
    r = _lancer("rm -rf ~")
    assert r.returncode == 2


def test_suppression_dun_dossier_precis_autorisee():
    # rm -rf sur un dossier du projet reste autorisé : seule la racine (/) ou le home (~) sont bloqués.
    r = _lancer("rm -rf build/")
    assert r.returncode == 0


def test_cle_api_en_clair_bloquee():
    r = _lancer("echo sk-abcdefghijklmnopqrstuvwxyz")
    assert r.returncode == 2
