from datetime import date
from decimal import Decimal

from facturation.calculs import arrondir, total_ht, total_ttc, total_tva
from facturation.models import Facture, LigneFacture


def _facture(lignes):
    return Facture("F-001", "C1", date(2025, 1, 10), date(2025, 2, 9), lignes, "emise")


def test_arrondi_commercial():
    assert arrondir(Decimal("1.005")) == Decimal("1.01")
    assert arrondir(Decimal("1.004")) == Decimal("1.00")


def test_totaux_une_ligne():
    f = _facture([LigneFacture("Stylo", 10, Decimal("1.50"))])
    assert total_ht(f) == Decimal("15.00")
    assert total_tva(f) == Decimal("3.00")
    assert total_ttc(f) == Decimal("18.00")


def test_totaux_taux_mixtes():
    f = _facture(
        [
            LigneFacture("Livre", 2, Decimal("10.00"), Decimal("0.055")),
            LigneFacture("Cahier", 1, Decimal("5.00"), Decimal("0.20")),
        ]
    )
    assert total_ht(f) == Decimal("25.00")
    assert total_tva(f) == Decimal("2.10")  # 1,10 + 1,00
    assert total_ttc(f) == Decimal("27.10")


def test_facture_vide():
    assert total_ttc(_facture([])) == Decimal("0.00")
