# Spécification — module de remises (TP 3)

Créer le module `facturation/remises.py`, ses tests `tests/test_remises.py` et sa documentation `docs/remises.md`.

## Règles métier
1. **Remise de volume, par ligne** (sur le total HT de la ligne) :
   - quantité ≥ 50 : 10 %
   - quantité ≥ 10 : 5 %
   - sinon : 0 %
2. **Code promo** (un seul code par facture, optionnel), appliqué sur le total HT **après** la remise de volume :
   - `BIENVENUE10` : 10 %
   - `FIDELE5` : 5 %
   - un code inconnu lève `ValueError` ; sans code, pas de remise promo.
   - la casse et les espaces autour du code sont ignorés (`" bienvenue10 "` est valide).
3. **Plafond** : la remise totale (volume + promo) ne peut pas dépasser **15 %** du total HT brut.
   Si elle le dépasse, on ramène la remise totale à 15 % du brut (la remise promo est réduite en conséquence).
4. **Hors périmètre** : la TVA n'est pas gérée par ce module (il ne produit que des montants HT).

## API attendue
```python
@dataclass(frozen=True)
class ResultatRemises:
    total_ht_brut: Decimal
    remise_volume: Decimal
    remise_promo: Decimal      # après application éventuelle du plafond
    remise_totale: Decimal
    total_ht_net: Decimal

def taux_remise_volume(quantite: int) -> Decimal: ...
def taux_code_promo(code: str | None) -> Decimal: ...
def calculer_remises(facture: Facture, code_promo: str | None = None) -> ResultatRemises: ...
```

## Contraintes
- `Decimal` uniquement, arrondi au centime avec `facturation.calculs.arrondir`.
- Réutiliser `total_ligne_ht` existant, ne pas modifier les autres modules.
- Tests `pytest` couvrant : les seuils de volume (9, 10, 49, 50), le code promo (valide, inconnu, casse, absent),
  le plafond (cas où il s'applique et cas où il ne s'applique pas), la facture vide.

## Exemple de référence
Facture de 2 lignes : 50 × 10,00 € (brut 500,00) et 10 × 50,00 € (brut 500,00) → brut 1 000,00.
- Remise de volume : 10 % de 500,00 = 50,00 + 5 % de 500,00 = 25,00 → **75,00**.
- Code `BIENVENUE10` : 10 % de (1 000,00 − 75,00) = **92,50**.
- Total = 167,50 ; plafond 15 % de 1 000,00 = 150,00 → remise promo ramenée à **75,00**, remise totale **150,00**,
  total HT net **850,00**.

## Documentation attendue (`docs/remises.md`)
Objectif, règles, exemple chiffré (celui ci-dessus), et comment appeler `calculer_remises`.
