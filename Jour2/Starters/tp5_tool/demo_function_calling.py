"""Démo de function calling avec l'API OpenAI (API Responses). À COMPLÉTER (TP 5, partie A).

Usage :  python demo_function_calling.py "Quel est le statut de la facture F-001 ?"
Prérequis : pip install openai   +   variable OPENAI_API_KEY   (+ OPENAI_MODEL si besoin)
"""

from __future__ import annotations

import json
import os
import sys

import outils

MODELE = os.environ.get("OPENAI_MODEL", "gpt-4.1")  # adaptez selon les modèles disponibles sur votre compte

# TODO 1 : déclarer l'outil `statut_facture` au format API :
#   {"type": "function", "name": ..., "description": ..., "parameters": {JSON Schema}, "strict": True}
# Rappel du mode strict : additionalProperties = False et TOUTES les propriétés dans "required".
TOOLS: list[dict] = []


def executer_outil(nom: str, arguments_json: str) -> str:
    """Exécute l'outil demandé par le modèle et retourne le résultat sous forme de texte JSON.

    TODO 2 : décoder arguments_json ; si nom == "statut_facture", appeler outils.statut_facture ;
             sinon lever ValueError. Retourner json.dumps(resultat, ensure_ascii=False).
    """
    raise NotImplementedError


def main(question: str) -> None:
    from openai import OpenAI

    client = OpenAI()  # lit OPENAI_API_KEY dans l'environnement
    input_list = [{"role": "user", "content": question}]

    # TODO 3 : 1er appel  client.responses.create(model=MODELE, tools=TOOLS, input=input_list)
    # TODO 4 : ajouter response.output à input_list ; pour chaque item de type "function_call",
    #          exécuter l'outil (executer_outil(item.name, item.arguments)) et ajouter
    #          {"type": "function_call_output", "call_id": item.call_id, "output": <résultat>}
    # TODO 5 : 2e appel avec input_list complété, puis afficher response.output_text
    raise NotImplementedError


if __name__ == "__main__":
    main(" ".join(sys.argv[1:]) or "Quel est le statut de la facture F-001 ?")
