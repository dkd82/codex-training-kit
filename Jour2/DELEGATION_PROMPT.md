# Prompt de délégation pour l'orchestrateur (agent Code)

Prêt à coller dans une session **Code** de Kilo Code ouverte à la racine de `lab2.3_multi_agent/`
(avec le `.kilo/kilo.jsonc` et les `.kilo/agents/` de ce dossier en place). Version concrète de
`pulselab-tp-participants/templates/multi-agent/delegation-prompt.md` pour ce TP.

```
Tâche : livrer les trois morceaux indépendants du TP 2.3 sur pulselab, chacun sur sa propre branche, puis intégrer.

Vous pouvez utiliser des sous-agents, mais uniquement pour les morceaux indépendants :
- `explorer-a` (lecture seule) pour écrire docs/ARCHITECTURE.md : voir briefs/BRIEF_A.md pour le brief complet ;
- `fit-b` pour ajouter fit_decay_with_error à pulselab/fit.py : voir briefs/BRIEF_B.md ;
- `export-c` pour ajouter pulselab/export.py : voir briefs/BRIEF_C.md.

Règles :
- Avant d'appeler un sous-agent, passez sur sa branche (docs-arch / feat-fit-uncertainty / feat-json-export)
  pour que son unique commit ne touche que ses fichiers autorisés.
- Donnez à chaque sous-agent son brief mot pour mot (collez le contenu du fichier briefs/BRIEF_*.md correspondant).
- Ne laissez jamais deux sous-agents modifier le même fichier.
- Faites l'intégration vous-même une fois que les trois ont rendu compte : fusionnez les trois branches dans `multi-agent`,
  branchez fit_decay_with_error dans report.py (nouvelle colonne tau_err_s) et write_json dans
  scripts/run_analysis.py (--format {csv,json}), mettez à jour tests/golden/summary_expected.csv
  volontairement avec la raison dans le message de commit, lancez python -m pytest -q, et montrez-moi le diff
  avant de commiter quoi que ce soit.
```

Vous pouvez aussi appeler un sous-agent directement, une session à la fois, sans orchestrateur Code :
`@fit-b` suivi du contenu de `briefs/BRIEF_B.md`, puis répétez pour `@export-c` et `@explorer-a`
sur leurs propres branches — voir `MULTI_AGENT_KILO.md` pour les deux façons de lancer ce TP.
