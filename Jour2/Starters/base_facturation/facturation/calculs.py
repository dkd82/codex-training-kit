"""Calculs de montants. Tous les montants sont des Decimal, arrondis au centime."""

from __future__ import annotations

from decimal import ROUND_HALF_UP, Decimal

from .models import Facture, LigneFacture

CENTIME = Decimal("0.01")


def arrondir(montant: Decimal) -> Decimal:
    """Arrondit au centime supérieur à partir de 0,005 (arrondi commercial)."""
    return montant.quantize(CENTIME, rounding=ROUND_HALF_UP)


def total_ligne_ht(ligne: LigneFacture) -> Decimal:
    return arrondir(ligne.prix_unitaire_ht * ligne.quantite)


def total_ht(facture: Facture) -> Decimal:
    return sum((total_ligne_ht(ligne) for ligne in facture.lignes), Decimal("0.00"))


def total_tva(facture: Facture) -> Decimal:
    return sum(
        (arrondir(total_ligne_ht(ligne) * ligne.taux_tva) for ligne in facture.lignes),
        Decimal("0.00"),
    )


def total_ttc(facture: Facture) -> Decimal:
    return total_ht(facture) + total_tva(facture)
