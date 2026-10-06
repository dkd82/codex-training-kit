"""Tests de caractérisation du module hérité `legacy.devis`.

Ils figent le comportement ACTUEL (y compris ses bizarreries) afin de refactorer sans rien casser.
Règle du TP : ces tests doivent rester verts pendant tout le refactor. Ne les modifiez pas pour les faire passer.
"""

import importlib

import pytest

from legacy import devis as module_devis


@pytest.fixture
def devis():
    """Recharge le module avant chaque test : l'état global (historique des devis) repart de zéro."""
    return importlib.reload(module_devis)


def _d(client, lignes, pays="FR", vip=False):
    return {"client": client, "lignes": lignes, "pays": pays, "vip": vip}


def test_client_standard_france(devis):
    assert devis.traiter(_d("ACME", [("Stylo", 10, 1.5)])) == (
        "Client: ACME\nTotal brut: 15.0\nTotal HT: 15.0\nTVA: 3.0\nTotal TTC: 18.0\n"
    )


def test_remise_standard_au_dessus_du_seuil_allemagne(devis):
    sortie = devis.traiter(_d("Globex", [("Serveur", 2, 1200.0), ("Câble", 5, 3.99)], pays="DE"))
    assert sortie == (
        "Client: Globex\nTotal brut: 2419.95\nRemise: 242.0\nTotal HT: 2177.95\n"
        "TVA: 413.81\nTotal TTC: 2591.77\n"
    )


def test_vip_sous_le_seuil(devis):
    # VIP : 5 % sous 1000 (total = 1000 exactement n'est PAS au-dessus du seuil)
    sortie = devis.traiter(_d("Mille", [("Lot", 1, 1000.0)], vip=True))
    assert "Remise: 50.0\n" in sortie


def test_vip_au_dessus_du_seuil_belgique(devis):
    assert devis.traiter(_d("Initech", [("Licence", 3, 400.0)], pays="BE", vip=True)) == (
        "Client: Initech\nTotal brut: 1200.0\nRemise: 180.0\nTotal HT: 1020.0\n"
        "TVA: 214.2\nTotal TTC: 1234.2\n"
    )


def test_pays_inconnu_pas_de_tva(devis):
    assert devis.traiter(_d("Hooli", [("Conseil", 1, 999.99)], pays="US")) == (
        "Client: Hooli\nTotal brut: 999.99\nTotal HT: 999.99\nTVA: 0\nTotal TTC: 999.99\n"
    )


def test_devis_vide_bizarreries_conservees(devis):
    # Bizarrerie actuelle : "Total brut: 0" (entier) mais "TVA: 0.0" (flottant). À préserver.
    assert devis.traiter(_d("Vide", [])) == (
        "Client: Vide\nTotal brut: 0\nTotal HT: 0\nTVA: 0.0\nTotal TTC: 0.0\n"
    )


def test_resume_sans_devis(devis):
    assert devis.resume() == "Aucun devis"


def test_resume_apres_plusieurs_devis(devis):
    devis.traiter(_d("ACME", [("Stylo", 10, 1.5)]))
    devis.traiter(_d("Globex", [("Serveur", 2, 1200.0), ("Câble", 5, 3.99)], pays="DE"))
    devis.traiter(_d("Initech", [("Licence", 3, 400.0)], pays="BE", vip=True))
    assert devis.resume() == (
        "Nombre de devis: 3\nTotal TTC cumulé: 3843.97\nDevis le plus élevé: 2591.77\n"
    )
