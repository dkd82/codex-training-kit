# Spécification — relances de paiement (TP 6)

Nouvelle fonctionnalité : détecter les factures impayées et **générer le texte** des relances.
Aucun e-mail n'est envoyé : le module produit uniquement un objet `Relance` (texte + destinataire).

## Règles métier
1. Une facture est **en retard** si son statut est `emise` **et** que sa date d'échéance est strictement
   antérieure à la date du jour (passée en paramètre, jamais `date.today()` en dur dans la logique).
2. Le **niveau de relance** dépend du nombre de jours de retard (jour du jour − échéance) :
   - 1 à 14 jours : `rappel_1`
   - 15 à 29 jours : `rappel_2`
   - 30 jours et plus : `mise_en_demeure`
   - pas en retard : aucun niveau (`None`)
3. Le texte de la relance contient : le nom du client, le numéro de facture, le montant TTC, la date
   d'échéance, le nombre de jours de retard, et un ton adapté au niveau (courtois, ferme, formel).
4. Une facture `payee` ou `brouillon` ne génère jamais de relance.

## API attendue (`facturation/relances.py`)
```python
@dataclass(frozen=True)
class Relance:
    numero_facture: str
    destinataire: str      # e-mail du client
    niveau: str            # rappel_1 | rappel_2 | mise_en_demeure
    jours_de_retard: int
    texte: str

def niveau_relance(facture: Facture, aujourdhui: date) -> str | None: ...
def factures_en_retard(factures: list[Facture], aujourdhui: date) -> list[Facture]: ...
def generer_relance(facture: Facture, client: Client, aujourdhui: date) -> Relance: ...
```

## Commande CLI
`python -m facturation relances --date AAAA-MM-JJ` affiche, pour chaque facture en retard, le niveau,
le destinataire et le texte. Sans facture en retard : afficher « Aucune relance à envoyer. ».

## Contraintes
- Réutiliser `calculs.total_ttc` et les modèles existants ; ne pas casser les tests existants.
- Aucune dépendance externe ; aucun envoi réseau.
- Tests `pytest` : chaque frontière (0, 1, 14, 15, 29, 30 jours), statuts non relançables, texte du message,
  commande CLI.

## Livrables du duo d'agents
- **Architecte** : `docs/design_relances.md` (modules touchés, signatures, cas limites, plan de tests). Pas de code applicatif.
- **Développeur** : implémentation + tests conformes au design, tests au vert.
