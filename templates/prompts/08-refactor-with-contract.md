# Modèle de prompt : refactoring avec un contrat (v1.0)

À utiliser avec : un agent de planification pour le plan (Kilo Code : *Plan*), puis un agent de code, un incrément par prompt (*Code*).

## Contrat de refactoring (c'est vous qui l'écrivez, pas l'agent)
```
Objectif :       {{what_improves_in_one_sentence}}
Invariants :     {{what_must_not_change : sorties, CLI, fichiers golden}}
Interdit :       nouvelles dépendances, modification de tests/golden/*, affaiblissement ou suppression d'une assertion, toucher des fichiers hors du plan
Terminé quand :  {{commands_that_must_succeed}} ; {{searches_that_must_return_nothing}}
Retour arrière : un commit par incrément sur la branche {{branch}} ; `git restore .` ou `git revert`
```

## Prompt 1 : le plan
Plan uniquement, ne modifiez aucun fichier. Refactorez {{scope}} comme suit : {{target_design}}.
Respectez le contrat ci-dessus. Donnez un plan ordonné en incréments pour que les tests puissent tourner après chaque incrément : fichiers touchés, risques, et la commande qui prouve chaque incrément.

## Prompt 2..n : un incrément
Exécutez uniquement l'incrément {{n}} du plan. Règles : ne touchez pas tests/golden/ ; aucune nouvelle dépendance ; n'affaiblissez aucune assertion ; si un test doit changer, dites-le-moi d'abord.
Lancez les tests et montrez le résultat. Arrêtez-vous après cet incrément.

## Après chaque incrément
Lancez les tests, lisez le diff (fichiers de tests d'abord), commitez.
