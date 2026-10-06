# TP 2 — Appeler un prompt en ligne de commande avec l'API OpenAI (Windows PowerShell). À COMPLÉTER.
param([string]$FichierPrompt = "prompt.txt")

if (-not $env:OPENAI_API_KEY) { throw "Définissez OPENAI_API_KEY (jamais dans ce fichier !)" }
if (-not $env:OPENAI_MODEL)   { throw "Définissez OPENAI_MODEL (un modèle disponible sur votre compte)" }

$prompt = Get-Content $FichierPrompt -Raw -Encoding UTF8

# TODO 1 : construire le corps JSON  { model = ...; input = $prompt }  puis le convertir avec ConvertTo-Json
# TODO 2 : appeler POST https://api.openai.com/v1/responses avec Invoke-RestMethod
#          (en-tête Authorization : "Bearer <clé>", ContentType application/json)
# TODO 3 : afficher uniquement le texte de la réponse.
#          Indice : $reponse.output contient des éléments de type "message" ; leur .content contient des
#          éléments de type "output_text" dont le champ .text est la réponse.
