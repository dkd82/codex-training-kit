#!/usr/bin/env python3
"""Hook PreToolUse : bloque les commandes Bash qui contiennent un motif dangereux. À COMPLÉTER (TP 8).

Codex envoie un objet JSON sur l'entrée standard à chaque commande Bash qu'il s'apprête à exécuter
(voir la documentation officielle des hooks pour le détail des champs : session_id, cwd, tool_name,
tool_input, etc.). Pour rester robuste si le nom exact d'un champ change d'une version à l'autre,
ce hook ne suppose pas de chemin JSON précis : il cherche directement les motifs interdits dans le
texte brut reçu.

Convention (documentation officielle) : code de sortie 0 = commande autorisée ; code de sortie 2 =
commande bloquée, avec la raison écrite sur la sortie d'erreur (stderr), que Codex affiche.
"""

from __future__ import annotations

import re
import sys

# TODO 1 : complétez cette liste avec au moins ces trois motifs interdits (des expressions
# régulières) :
#   - une suppression de la racine du disque : "rm -rf /" (mais pas "rm -rf /un/dossier")
#   - une suppression de tout le dossier personnel : "rm -rf ~"
#   - une clé d'API OpenAI laissée en clair : "sk-" suivi d'au moins 10 caractères alphanumériques
MOTIFS_INTERDITS: list[str] = [
]


def motif_trouve(texte: str) -> str | None:
    """Retourne le premier motif interdit trouvé dans `texte`, ou None si rien n'est trouvé.

    TODO 2 : parcourez MOTIFS_INTERDITS et utilisez re.search(motif, texte) pour chercher
    chaque motif. Retournez le motif dès qu'il est trouvé (ou None si aucun ne correspond).
    """
    raise NotImplementedError


def main() -> int:
    """Point d'entrée du hook : lit le JSON envoyé par Codex sur l'entrée standard.

    TODO 3 : lisez sys.stdin (sys.stdin.read()), cherchez un motif interdit avec motif_trouve, et :
      - s'il y en a un, écrivez un message explicite sur stderr (print(..., file=sys.stderr))
        et retournez 2 (bloqué) ;
      - sinon, retournez 0 (autorisé).
    """
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
