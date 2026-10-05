# Modèle de prompt : planifier une fonctionnalité (v1.0)

À utiliser avec : un agent de planification (Kilo Code : *Plan*). Plan uniquement, pas de code.

## Objectif
{{feature_in_one_sentence}}

## Contexte
- Projet : {{project}}. Fichiers que je pense concernés : {{files}}.
- Critères d'acceptation :
  - AC1 {{criterion_1}}
  - AC2 {{criterion_2}}
  - AC3 {{criterion_3}}

## Contraintes
- Plan uniquement : n'écrivez ni ne modifiez encore de code.
- Le plus petit changement qui satisfait les critères. Aucune nouvelle dépendance. Les sorties existantes ne doivent pas changer : {{what_must_not_change}}.

## Format
Des étapes numérotées dans un ordre sûr (types et utilitaires d'abord, câblage ensuite, ligne de commande en dernier). Pour chaque étape : les fichiers touchés et comment la vérifier (une commande ou un test).

## Vérification
Listez les risques et les questions auxquelles vous avez besoin que je réponde avant d'implémenter.
