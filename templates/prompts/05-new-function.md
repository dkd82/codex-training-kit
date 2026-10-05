# Modèle de prompt : nouvelle fonction numérique (v1.0)

À utiliser avec : un agent de code (Kilo Code : *Code*).

## Objectif
Ajoutez `{{function_name}}({{signature}})` dans `{{module}}`. Elle {{purpose}}.

## Contexte
- Entrées : {{inputs_with_units}}. Sortie : {{output_with_units}}.
- Une fonction existante à imiter pour le style : {{example_function}}.

## Contraintes
- {{allowed_libraries}} uniquement, aucune nouvelle dépendance. Vectorisé, sauf si une boucle est justifiée dans un commentaire.
- Ne modifiez pas les entrées en place. Définissez le comportement pour une entrée vide et pour NaN : {{nan_and_empty_policy}}.

## Exemples
- Vérification analytique : {{analytical_check}}
- Exemple : {{example_input}} donne {{example_output}}.

## Format
La fonction avec une docstring qui précise les unités, puis les tests, puis une courte liste de vos hypothèses.

## Vérification
- Listez vos hypothèses et toute question que vous avez AVANT d'écrire du code.
- Les tests doivent inclure la vérification analytique et un cas limite. Lancez-les et montrez le résultat.
