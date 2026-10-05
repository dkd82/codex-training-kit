#!/usr/bin/env python
"""Hook pre-commit (modèle : adaptez SOURCE_DIRS et TEST_CMD ci-dessous).

  BLOQUANT (déterministe) :   scan de secrets, vérification de syntaxe, tests rapides.
  CONSULTATIF (ne bloque jamais) : revue IA facultative du diff indexé.

Installer le hook une fois :   python tools/precommit.py --install

Conseil IA facultatif : définissez AI_REVIEW_CMD avec une commande qui lit le diff
sur stdin et affiche des commentaires sur stdout (utilisez votre outil approuvé par l'entreprise).
Facultatif : AI_REVIEW_TIMEOUT (secondes, 60 par défaut).
"""
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAX_DIFF_CHARS = 20_000
SOURCE_DIRS = ["pulselab", "scripts", "tests"]   # dossiers dont la syntaxe est vérifiée : ADAPTEZ à votre projet
TEST_CMD = [sys.executable, "-m", "pytest", "-x", "-q", "-p", "no:cacheprovider"]   # tests rapides : ADAPTEZ si besoin
SECRET_PATTERNS = [
    re.compile(r"""(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['"][^'"\s]{8,}['"]"""),
    re.compile(r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True).stdout


def staged_diff():
    return git("diff", "--cached", "--unified=3")


def check_secrets(diff):
    added = [line[1:] for line in diff.splitlines() if line.startswith("+") and not line.startswith("+++")]
    hits = [line.strip() for line in added if any(p.search(line) for p in SECRET_PATTERNS)]
    if hits:
        print("[BLOCK] possible secret in the staged changes:")
        for h in hits[:5]:
            print("   ", h[:80])
        return False
    return True


def run_step(name, cmd):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"[BLOCK] {name} failed:")
        print((r.stdout + r.stderr)[-1500:])
        return False
    print(f"[ ok  ] {name}")
    return True


def ai_advice(diff):
    """Consultatif uniquement : tout problème ici est signalé puis ignoré."""
    cmd = os.environ.get("AI_REVIEW_CMD")
    if not cmd or not diff.strip():
        return
    timeout = int(os.environ.get("AI_REVIEW_TIMEOUT", "60"))
    try:
        r = subprocess.run(shlex.split(cmd), input=diff[:MAX_DIFF_CHARS], capture_output=True,
                           text=True, timeout=timeout)
        if r.returncode != 0:
            print(f"[warn ] AI review command failed (exit {r.returncode}); ignored.")
        elif r.stdout.strip():
            print("[advice] AI review (not blocking):")
            print(r.stdout.strip())
    except subprocess.TimeoutExpired:
        print(f"[warn ] AI review timed out after {timeout}s; ignored.")
    except OSError as e:
        print(f"[warn ] AI review command could not start ({e}); ignored.")


def install():
    hook = ROOT / ".git" / "hooks" / "pre-commit"
    hook.write_text("#!/bin/sh\nexec python tools/precommit.py\n")
    hook.chmod(0o755)
    print("installed", hook)


def main():
    if "--install" in sys.argv:
        install()
        return 0
    diff = staged_diff()
    ok = check_secrets(diff)
    ok = ok and run_step("syntax", [sys.executable, "-m", "compileall", "-q", *SOURCE_DIRS])
    ok = ok and run_step("fast tests", TEST_CMD)
    if ok:
        ai_advice(diff)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
