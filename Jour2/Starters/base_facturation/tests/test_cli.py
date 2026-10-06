from facturation.cli import main


def test_scenario_complet(tmp_path, capsys):
    d = str(tmp_path)
    assert main(["--data", d, "ajouter-client", "--id", "C1", "--nom", "ACME", "--email", "a@b.example"]) == 0
    assert (
        main(
            [
                "--data", d, "creer-facture", "--numero", "F-001", "--client", "C1",
                "--emission", "2025-01-10", "--echeance", "2025-02-09",
                "--ligne", "Stylo;10;1.50",
            ]
        )
        == 0
    )
    capsys.readouterr()
    assert main(["--data", d, "afficher", "F-001"]) == 0
    sortie = capsys.readouterr().out
    assert "TTC : 18.00" in sortie


def test_facture_introuvable(tmp_path, capsys):
    assert main(["--data", str(tmp_path), "afficher", "X"]) == 1
