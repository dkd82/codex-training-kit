"""« API interne » factice (lecture seule) utilisée pour le TP 5.

Lancer :  python api_interne/serveur.py            (port 8765 par défaut)
Variables : PORT, INTERNAL_API_KEY (défaut : demo-key)

Routes (toutes en GET, en-tête  X-API-Key  obligatoire) :
  /clients/<id>            -> fiche client
  /clients/<id>/factures   -> factures du client
  /factures/<numero>       -> détail d'une facture
"""

from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

DONNEES = json.loads((Path(__file__).with_name("donnees.json")).read_text(encoding="utf-8"))


def _cle_attendue() -> str:
    return os.environ.get("INTERNAL_API_KEY", "demo-key")


class Handler(BaseHTTPRequestHandler):
    def _repondre(self, code: int, corps: object) -> None:
        octets = json.dumps(corps, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(octets)))
        self.end_headers()
        self.wfile.write(octets)

    def do_GET(self) -> None:  # noqa: N802 (nom imposé par http.server)
        if self.headers.get("X-API-Key") != _cle_attendue():
            return self._repondre(401, {"erreur": "clé d'API invalide"})
        morceaux = [m for m in self.path.split("?")[0].split("/") if m]
        if len(morceaux) == 2 and morceaux[0] == "clients":
            client = next((c for c in DONNEES["clients"] if c["id"] == morceaux[1]), None)
            return self._repondre(200, client) if client else self._repondre(404, {"erreur": "client introuvable"})
        if len(morceaux) == 3 and morceaux[0] == "clients" and morceaux[2] == "factures":
            return self._repondre(200, [f for f in DONNEES["factures"] if f["client_id"] == morceaux[1]])
        if len(morceaux) == 2 and morceaux[0] == "factures":
            facture = next((f for f in DONNEES["factures"] if f["numero"] == morceaux[1]), None)
            return self._repondre(200, facture) if facture else self._repondre(404, {"erreur": "facture introuvable"})
        return self._repondre(404, {"erreur": "route inconnue"})

    def log_message(self, format: str, *args: object) -> None:  # silence
        pass


def creer_serveur(port: int = 0) -> ThreadingHTTPServer:
    """Crée le serveur (port=0 : port libre choisi par le système)."""
    return ThreadingHTTPServer(("127.0.0.1", port), Handler)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8765"))
    serveur = creer_serveur(port)
    print(f"API interne sur http://127.0.0.1:{serveur.server_address[1]}  (Ctrl+C pour arrêter)")
    serveur.serve_forever()
