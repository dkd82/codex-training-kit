# Modèle de prompt : écrire des tests (v1.0)

À utiliser avec : un agent de planification pour le plan (Kilo Code : *Plan*), puis un agent de code pour les tests (*Code*).

## Objectif
Écrivez des tests pytest pour `{{function_or_module}}`.

## Contexte
- Tests existants : {{test_file}}. Comportement à figer (ne PAS modifier le source) : {{behaviour}}.
- Faits connus : {{known_facts}} (par exemple : un run sans impulsions doit donner NaN).

## Contraintes
- Étape 1, plan uniquement : proposez un plan de tests et attendez mon approbation. Étape 2 : écrivez les tests.
- Chaque test vérifie une vraie valeur (pas de `is not None`, pas de `> 0` seul). Ne recalculez jamais la valeur attendue avec le code testé.
- Utilisez `pytest.approx` avec une tolérance que vous pouvez justifier. Données aléatoires avec graine fixée uniquement. Tests uniquement : ne modifiez pas le source.

## Format
Étape 1 : un tableau : comportement | nom du test | le changement d'une seule ligne dans le source que ce test doit détecter. Étape 2 : le fichier de tests.

## Vérification
- Lancez les tests et montrez le résultat.
- Je casserai ensuite le code volontairement (ou lancerai un script de mutation) pour vérifier que les tests peuvent échouer.
