"""Interface en ligne de commande : python -m facturation <commande>."""

from __future__ import annotations

import argparse
from datetime import date
from decimal import Decimal
from pathlib import Path

from .calculs import total_ht, total_ttc, total_tva
from .models import Client, Facture, LigneFacture
from .stockage import (
    charger_clients,
    charger_factures,
    sauvegarder_clients,
    sauvegarder_factures,
)


def _parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="facturation", description="Mini-outil de facturation")
    p.add_argument("--data", default="donnees", help="dossier de données (défaut : donnees)")
    sp = p.add_subparsers(dest="commande", required=True)

    c = sp.add_parser("ajouter-client", help="ajoute un client")
    c.add_argument("--id", required=True)
    c.add_argument("--nom", required=True)
    c.add_argument("--email", required=True)

    f = sp.add_parser("creer-facture", help="crée une facture")
    f.add_argument("--numero", required=True)
    f.add_argument("--client", required=True, help="identifiant du client")
    f.add_argument("--emission", required=True, help="AAAA-MM-JJ")
    f.add_argument("--echeance", required=True, help="AAAA-MM-JJ")
    f.add_argument(
        "--ligne",
        action="append",
        required=True,
        help='"description;quantite;prix_ht[;taux_tva]" (répétable)',
    )
    f.add_argument("--statut", default="emise")

    sp.add_parser("lister", help="liste les factures")

    a = sp.add_parser("afficher", help="affiche une facture avec ses totaux")
    a.add_argument("numero")
    return p


def _parse_ligne(texte: str) -> LigneFacture:
    morceaux = texte.split(";")
    if len(morceaux) not in (3, 4):
        raise ValueError(f"Ligne invalide : {texte!r}")
    tva = Decimal(morceaux[3]) if len(morceaux) == 4 else Decimal("0.20")
    return LigneFacture(morceaux[0], int(morceaux[1]), Decimal(morceaux[2]), tva)


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    dossier = Path(args.data)
    f_clients = dossier / "clients.json"
    f_factures = dossier / "factures.json"

    if args.commande == "ajouter-client":
        clients = charger_clients(f_clients)
        clients.append(Client(args.id, args.nom, args.email))
        sauvegarder_clients(f_clients, clients)
        print(f"Client {args.id} ajouté.")

    elif args.commande == "creer-facture":
        factures = charger_factures(f_factures)
        facture = Facture(
            numero=args.numero,
            client_id=args.client,
            date_emission=date.fromisoformat(args.emission),
            date_echeance=date.fromisoformat(args.echeance),
            lignes=[_parse_ligne(t) for t in args.ligne],
            statut=args.statut,
        )
        factures.append(facture)
        sauvegarder_factures(f_factures, factures)
        print(f"Facture {facture.numero} créée : {total_ttc(facture)} € TTC")

    elif args.commande == "lister":
        for f in charger_factures(f_factures):
            print(f"{f.numero}  {f.client_id:<10} {f.statut:<9} {total_ttc(f):>10} €")

    elif args.commande == "afficher":
        for f in charger_factures(f_factures):
            if f.numero == args.numero:
                print(f"Facture {f.numero} — client {f.client_id} — {f.statut}")
                for ligne in f.lignes:
                    print(f"  {ligne.description} x{ligne.quantite} @ {ligne.prix_unitaire_ht}")
                print(f"  HT  : {total_ht(f)}")
                print(f"  TVA : {total_tva(f)}")
                print(f"  TTC : {total_ttc(f)}")
                return 0
        print(f"Facture {args.numero} introuvable.")
        return 1
    return 0
