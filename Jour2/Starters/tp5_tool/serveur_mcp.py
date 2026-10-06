"""Serveur MCP exposant les outils de outils.py à Codex. À COMPLÉTER (TP 5).

Lancement (Codex le lance pour vous une fois déclaré) :  python serveur_mcp.py
Déclaration dans Codex :  codex mcp add facturation-interne -- python <chemin absolu>/serveur_mcp.py
Vérification dans Codex :  /mcp
"""

from __future__ import annotations

try:  # mcp >= 2
    from mcp.server.mcpserver import MCPServer as _Serveur
except ImportError:  # mcp 1.x
    from mcp.server.fastmcp import FastMCP as _Serveur

import outils

mcp = _Serveur("facturation-interne")

# TODO : exposer `statut_facture` et `lister_factures_client` comme outils MCP.
# Indice : décorer une fonction avec  @mcp.tool()  ; sa docstring et ses annotations de types
# deviennent la description et le schéma de l'outil vu par le modèle. Soignez la docstring !


if __name__ == "__main__":
    mcp.run()  # transport stdio par défaut
