"""Outils (fonctions Python) qui interrogent l'API interne. À COMPLÉTER (TP 5).

Ces fonctions seront réutilisées à deux endroits :
  - par le serveur MCP  (serveur_mcp.py)  -> pour les donner à Codex ;
  - par la démo de function calling (demo_function_calling.py) -> pour comprendre la boucle avec l'API.

Règles de sécurité à respecter :
  - lecture seule ;
  - valider les arguments AVANT tout appel (le schéma du modèle ne remplace pas la validation) ;
  - la clé d'API vient de l'environnement, jamais du code.
"""

from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request

# Formats attendus : numéro de facture « F-001 » (une lettre, un tiret, 3 à 6 chiffres) ; client « C1 ».
NUMERO_FACTURE = re.compile(r"^[A-Z]-\d{3,6}$")
ID_CLIENT = re.compile(r"^C\d{1,6}$")


def _get(chemin: str) -> object:
    """Appelle l'API interne en GET. Fourni : ne pas modifier."""
    base = os.environ.get("INTERNAL_API_URL", "http://127.0.0.1:8765")
    requete = urllib.request.Request(base + chemin, headers={"X-API-Key": os.environ.get("INTERNAL_API_KEY", "demo-key")})
    try:
        with urllib.request.urlopen(requete, timeout=5) as reponse:
            return json.loads(reponse.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise LookupError("ressource introuvable") from e
        raise


def statut_facture(numero: str) -> dict:
    """Retourne le détail d'une facture (statut, échéance, total TTC) à partir de son numéro, ex : F-001.

    TODO : 1) valider `numero` avec NUMERO_FACTURE.fullmatch(...) (ValueError sinon ; `fullmatch` et non `match`) ;
           2) appeler _get(f"/factures/{numero}") ;
           3) retourner le dictionnaire obtenu.
    """
    raise NotImplementedError


def lister_factures_client(client_id: str) -> list[dict]:
    """Liste les factures d'un client à partir de son identifiant, ex : C1.

    TODO : valider `client_id` avec ID_CLIENT.fullmatch(...) (ValueError sinon), puis appeler _get(f"/clients/{client_id}/factures").
    """
    raise NotImplementedError
