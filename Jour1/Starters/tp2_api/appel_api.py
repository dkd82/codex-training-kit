"""TP 2 — Appeler un prompt avec le SDK Python OpenAI (API Responses). À COMPLÉTER.

Usage :  python appel_api.py [fichier_prompt]        (par défaut : prompt.txt)
Prérequis : pip install -r requirements.txt   +   variables OPENAI_API_KEY et OPENAI_MODEL
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


def main(chemin_prompt: str = "prompt.txt") -> None:
    prompt = Path(chemin_prompt).read_text(encoding="utf-8")
    # TODO 1 : créer le client (from openai import OpenAI ; OpenAI() lit OPENAI_API_KEY dans l'environnement)
    # TODO 2 : appeler client.responses.create(model=<OPENAI_MODEL>, input=prompt)
    # TODO 3 : afficher response.output_text
    raise NotImplementedError


if __name__ == "__main__":
    if "OPENAI_MODEL" not in os.environ:
        sys.exit("Définissez la variable OPENAI_MODEL (un modèle disponible sur votre compte).")
    main(*sys.argv[1:2])
