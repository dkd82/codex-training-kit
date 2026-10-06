"""Stockage JSON des clients et des factures (un fichier par type)."""

from __future__ import annotations

import json
from datetime import date
from decimal import Decimal
from pathlib import Path

from .models import Client, Facture, LigneFacture


def _ecrire(chemin: Path, donnees: list[dict]) -> None:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(json.dumps(donnees, indent=2, ensure_ascii=False), encoding="utf-8")


def _lire(chemin: Path) -> list[dict]:
    if not chemin.exists():
        return []
    return json.loads(chemin.read_text(encoding="utf-8"))


def sauvegarder_clients(chemin: Path, clients: list[Client]) -> None:
    _ecrire(chemin, [{"id": c.id, "nom": c.nom, "email": c.email} for c in clients])


def charger_clients(chemin: Path) -> list[Client]:
    return [Client(**d) for d in _lire(chemin)]


def sauvegarder_factures(chemin: Path, factures: list[Facture]) -> None:
    _ecrire(
        chemin,
        [
            {
                "numero": f.numero,
                "client_id": f.client_id,
                "date_emission": f.date_emission.isoformat(),
                "date_echeance": f.date_echeance.isoformat(),
                "statut": f.statut,
                "lignes": [
                    {
                        "description": ligne.description,
                        "quantite": ligne.quantite,
                        "prix_unitaire_ht": str(ligne.prix_unitaire_ht),
                        "taux_tva": str(ligne.taux_tva),
                    }
                    for ligne in f.lignes
                ],
            }
            for f in factures
        ],
    )


def charger_factures(chemin: Path) -> list[Facture]:
    factures = []
    for d in _lire(chemin):
        lignes = [
            LigneFacture(
                description=ligne["description"],
                quantite=ligne["quantite"],
                prix_unitaire_ht=Decimal(ligne["prix_unitaire_ht"]),
                taux_tva=Decimal(ligne["taux_tva"]),
            )
            for ligne in d["lignes"]
        ]
        factures.append(
            Facture(
                numero=d["numero"],
                client_id=d["client_id"],
                date_emission=date.fromisoformat(d["date_emission"]),
                date_echeance=date.fromisoformat(d["date_echeance"]),
                lignes=lignes,
                statut=d["statut"],
            )
        )
    return factures
