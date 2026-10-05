# Prompt pour un agent qui peut déléguer

À utiliser avec un agent Code ou Plan. Adaptez les noms aux sous-agents définis dans votre projet (`.kilo/agents/`).

```
Tâche : {{task_in_one_sentence}}

Vous pouvez utiliser des sous-agents, mais uniquement pour les morceaux indépendants :
- `explore` (intégré, lecture seule) pour cartographier {{area}} et renvoyer un résumé de 10 lignes maximum ;
- `test-writer` pour écrire les tests de {{function}} dans tests/ uniquement ;
- `reviewer` (contexte neuf) pour relire le diff final.

Règles :
- Donnez à chaque sous-agent un brief écrit : objectif, fichiers autorisés, hors périmètre, livrable, vérification.
- Ne laissez jamais deux sous-agents modifier le même fichier.
- Faites l'intégration vous-même (câblage, ligne de commande, fichiers golden), lancez `python -m pytest -q`, et montrez-moi le diff avant de commiter quoi que ce soit.
- Si la tâche est petite ou fortement couplée, faites-la vous-même sans sous-agents et dites-moi pourquoi.
```

Vous pouvez aussi appeler un sous-agent directement : `@reviewer relis mon dernier changement`.
