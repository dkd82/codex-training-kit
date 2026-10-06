"""Auto-évaluation du TP 5 : `python -m pytest -q` doit passer au vert quand outils.py est complété."""

import threading

import pytest

from api_interne.serveur import creer_serveur
import outils


@pytest.fixture(scope="module", autouse=True)
def api():
    serveur = creer_serveur(0)
    threading.Thread(target=serveur.serve_forever, daemon=True).start()
    env = pytest.MonkeyPatch()
    env.setenv("INTERNAL_API_URL", f"http://127.0.0.1:{serveur.server_address[1]}")
    env.setenv("INTERNAL_API_KEY", "demo-key")
    yield
    env.undo()
    serveur.shutdown()
    serveur.server_close()


def test_statut_facture():
    f = outils.statut_facture("F-001")
    assert f["statut"] == "emise" and f["total_ttc"] == "18.00"


def test_statut_facture_introuvable():
    with pytest.raises(LookupError):
        outils.statut_facture("F-999")


@pytest.mark.parametrize("mauvais", ["", "F001", "f-001", "F-1", "F-001; DROP TABLE", "../etc/passwd", "F-001/../x", "F-001" + chr(10)])
def test_numero_invalide_refuse_avant_appel(mauvais):
    with pytest.raises(ValueError):
        outils.statut_facture(mauvais)


def test_lister_factures_client():
    numeros = {f["numero"] for f in outils.lister_factures_client("C1")}
    assert numeros == {"F-001", "F-002"}


@pytest.mark.parametrize("mauvais", ["", "1", "c1", "C1/../x", "C1 OR 1=1"])
def test_client_invalide(mauvais):
    with pytest.raises(ValueError):
        outils.lister_factures_client(mauvais)
