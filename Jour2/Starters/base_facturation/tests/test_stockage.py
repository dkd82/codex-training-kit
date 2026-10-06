from datetime import date
from decimal import Decimal

from facturation.models import Client, Facture, LigneFacture
from facturation.stockage import (
    charger_clients,
    charger_factures,
    sauvegarder_clients,
    sauvegarder_factures,
)


def test_aller_retour_clients(tmp_path):
    chemin = tmp_path / "clients.json"
    clients = [Client("C1", "ACME", "contact@acme.example")]
    sauvegarder_clients(chemin, clients)
    assert charger_clients(chemin) == clients


def test_aller_retour_factures(tmp_path):
    chemin = tmp_path / "factures.json"
    factures = [
        Facture(
            "F-001",
            "C1",
            date(2025, 1, 10),
            date(2025, 2, 9),
            [LigneFacture("Stylo", 10, Decimal("1.50"))],
            "emise",
        )
    ]
    sauvegarder_factures(chemin, factures)
    assert charger_factures(chemin) == factures


def test_fichier_absent(tmp_path):
    assert charger_factures(tmp_path / "absent.json") == []
