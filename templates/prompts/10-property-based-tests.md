# Modèle de prompt : tests par propriétés (v1.0)

À utiliser avec : un agent de code (Kilo Code : *Code*). Nécessite `hypothesis` ; sinon, demandez des boucles aléatoires avec graine fixée.

## Objectif
Écrivez des tests par propriétés pour `{{function}}` dans `tests/test_properties.py`.

## Contexte
- Module : `{{module}}`. Domaine des entrées valides : {{valid_inputs_with_ranges}}.

## Contraintes
- `hypothesis` avec `max_examples=50` et `deadline=None` ; ignorez le module avec `pytest.importorskip("hypothesis")` s'il n'est pas installé.
- Des flottants finis dans une plage bornée (pas de NaN, pas d'infini) sauf si la propriété les concerne. Tolérances relatives à l'échelle des données.
- Tests uniquement : ne modifiez pas le source.

## Exemples de propriétés
- L'entrée n'est pas modifiée. Appliquer la fonction deux fois donne le même résultat (idempotence).
- Un résultat analytique connu est vérifié pour tout paramètre dans la plage valide.
- Invariance : {{invariance_e_g_adding_an_offset_does_not_change_it}}.
- L'ordre, l'espacement ou les bornes de la sortie sont respectés pour toute entrée.

## Format
Un test par propriété, avec une docstring qui énonce la propriété en une phrase.

## Vérification
Lancez `python -m pytest -q` et montrez le résultat. Dites-moi les plages d'entrée que chaque test explore.
