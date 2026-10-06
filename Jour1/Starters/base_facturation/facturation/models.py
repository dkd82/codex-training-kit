"""Modèles du domaine : clients, lignes de facture et factures."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal

STATUTS = ("brouillon", "emise", "payee")


@dataclass(frozen=True)
class Client:
    id: str
    nom: str
    email: str


@dataclass(frozen=True)
class LigneFacture:
    description: str
    quantite: int
    prix_unitaire_ht: Decimal
    taux_tva: Decimal = Decimal("0.20")


@dataclass
class Facture:
    numero: str
    client_id: str
    date_emission: date
    date_echeance: date
    lignes: list[LigneFacture] = field(default_factory=list)
    statut: str = "brouillon"

    def __post_init__(self) -> None:
        if self.statut not in STATUTS:
            raise ValueError(f"Statut inconnu : {self.statut!r} (attendu : {STATUTS})")
