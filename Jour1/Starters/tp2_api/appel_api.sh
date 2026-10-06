#!/usr/bin/env bash
# TP 2 — Appeler un prompt en ligne de commande avec l'API OpenAI (macOS / Linux / Git Bash). À COMPLÉTER.
# Prérequis : curl et jq.
set -euo pipefail

: "${OPENAI_API_KEY:?Définissez la variable OPENAI_API_KEY (jamais dans ce fichier !)}"
: "${OPENAI_MODEL:?Définissez la variable OPENAI_MODEL (un modèle disponible sur votre compte)}"

# TODO 1 : construire le corps JSON {"model": ..., "input": <contenu de prompt.txt>}
# Piège : le prompt contient des guillemets et des retours à la ligne, donc ne l'assemblez pas "à la main".
# Indice : jq -n --arg model "$OPENAI_MODEL" --rawfile input prompt.txt '{...}'
BODY=""

# TODO 2 : appeler  POST https://api.openai.com/v1/responses  avec curl
#   -H "Content-Type: application/json"
#   -H "Authorization: Bearer $OPENAI_API_KEY"
#   -d "$BODY"
# TODO 3 : afficher uniquement le texte de la réponse.
# Indice : la réponse JSON contient un tableau "output" ; les éléments de type "message" ont un tableau "content" ;
#          les éléments de type "output_text" portent le champ "text".
