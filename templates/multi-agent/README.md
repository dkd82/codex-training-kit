# Modèles multi-agents

**Commencez avec un seul agent.** N'en ajoutez d'autres que lorsqu'un agent seul atteint une limite concrète.

## Quand plusieurs agents valent la peine

| Situation | Pourquoi ça aide |
|---|---|
| La tâche ne tient plus dans une seule fenêtre de contexte | Les sous-agents explorent séparément et renvoient de courts résumés, donc le contexte principal reste propre |
| Sous-tâches indépendantes sur des fichiers différents | Ils peuvent tourner en même temps sans toucher aux mêmes fichiers |
| Rôles ou permissions différents | Un explorateur en lecture seule, un rédacteur limité à `tests/`, un relecteur sans droit de modification |
| Vérification indépendante | Un relecteur dans un contexte neuf n'hérite pas des hypothèses de l'auteur |

## Quand rester avec un seul agent

- La tâche est petite ou bien cadrée : la coordination coûte plus qu'elle ne rapporte.
- Les étapes sont couplées ou séquentielles : chacune dépend de la précédente.
- Vous ne pouvez pas encore vérifier la sortie d'un seul agent : plus d'agents, c'est plus de sorties à contrôler.
- Le coût, la latence ou la traçabilité comptent : plus de tokens, plus d'attente, un débogage plus difficile.

**Un test utile :** pouvez-vous décrire, en une phrase chacune, les tâches que vous donneriez aux sous-agents, et vérifier le résultat de chacune ? Sinon, la tâche n'est pas prête à être découpée.

## Quatre schémas courants

1. **Orchestrateur et exécutants** : un agent découpe la tâche et délègue.
2. **Exécutants en parallèle** : des sous-tâches indépendantes tournent en même temps (sur des fichiers différents !).
3. **Pipeline** : par exemple planificateur, puis implémenteur, puis relecteur, avec des passations explicites.
4. **Auteur et relecteur indépendant** : un second agent, dans un contexte neuf, vérifie le travail du premier.

## Comment ça marche dans Kilo Code (d'après la documentation, septembre 2026)

- Les **sous-agents** sont des agents avec `mode: subagent` (voir `../kilo-project-kit/.kilo/agents/`). Ils sont appelés par un agent via son outil `task`, ou par vous avec `@nom-de-l-agent`.
  Quand un sous-agent termine, seul un **résumé** remonte à l'agent parent. Un sous-agent ne peut pas vous poser de questions directement lorsqu'un agent l'a invoqué.
- Les agents avec accès complet aux outils (**Code, Plan, Debug**) peuvent déléguer eux-mêmes aux sous-agents. L'ancien agent **Orchestrator** est marqué *obsolète* dans la documentation actuelle : on ne bascule plus dessus avant une tâche complexe. Les anciennes versions de l'extension peuvent encore l'afficher.
- **Contrôlez qui peut être appelé** avec `permission.task` (par exemple autoriser `reviewer` et `test-writer`, demander confirmation pour les autres). Le réglage `steps` d'un agent limite le nombre d'itérations qu'il peut exécuter.
- Sous-agents intégrés cités dans la documentation : **`explore`** (exploration rapide du code en lecture seule) et **`general`**.
- **Agent Manager** (VS Code) : lancez plusieurs sessions en parallèle, éventuellement chacune dans son propre **git worktree** (un checkout séparé sur sa propre branche), puis relisez et appliquez les changements. Il nécessite un dépôt git.
- Les tâches au premier plan rendent leur résultat avant que le parent continue ; les tâches en arrière-plan laissent le parent continuer et livrent leur résultat plus tard.

## À retenir

- Un sous-agent ne sait que ce que vous lui dites : **rédigez un brief précis** (`brief-template.md`). Les passations perdent de l'information.
- **Ne laissez jamais deux agents modifier le même fichier.** Donnez aux agents parallèles des branches ou des worktrees séparés.
- Les erreurs se cumulent : une mauvaise hypothèse précoce peut se propager. Gardez des résumés courts et vérifiables.
- **Vous êtes l'orchestrateur de référence** : vous intégrez, lancez les tests et lisez chaque diff, quel que soit celui qui a écrit le code.
- Mesurez : cela a-t-il vraiment fait gagner du temps par rapport à un agent seul ? Sinon, restez simple.

## Fichiers

- `brief-template.md` : le brief à donner à chaque sous-agent ou session.
- `delegation-prompt.md` : un prompt pour un agent Code ou Plan qui peut déléguer à des sous-agents.
- `../kilo-project-kit/.kilo/agents/` : les sous-agents `reviewer` et `test-writer`, prêts à adapter.
