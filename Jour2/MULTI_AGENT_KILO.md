# TP 2.3 avec Kilo Code — notes formateur

Ce dossier transforme le mini-atelier multi-agents du TP 2.3 (trois briefs, trois sous-agents, une
intégration) en une configuration Kilo Code concrète, pour que vous puissiez l'exécuter ou le démontrer
au lieu de seulement le décrire. C'est la version remplie des
`pulselab-tp-participants/templates/multi-agent/` (modèles génériques pour les propres projets des
participants) — ici, chaque fichier nomme les vraies fonctions, branches et tests de pulselab.

## Ce qu'il y a ici

```
.kilo/
  kilo.jsonc          configuration du projet : permissions par défaut + quels sous-agents peuvent être appelés (permission.task)
  agents/
    explorer-a.md      sous-agent A : lecture seule, ne peut écrire que docs/ARCHITECTURE.md
    fit-b.md            sous-agent B : ne peut modifier que pulselab/fit.py + tests/test_fit_uncertainty.py
    export-c.md          sous-agent C : ne peut créer que pulselab/export.py + tests/test_export.py
briefs/
  BRIEF_A.md, BRIEF_B.md, BRIEF_C.md   les trois briefs, mot pour mot (identiques à ceux de
                                         Jour2/Solutions_Prompts_Jour2.md donnés aux participants)
DELEGATION_PROMPT.md  prompt prêt à coller pour un agent Code qui orchestre les trois sous-agents
```

Copiez `.kilo/`, `briefs/` et `DELEGATION_PROMPT.md` à la racine d'un checkout du starter du Jour 2
(`pulselab_jour2_starter.zip`) avant la session — pas dans la solution de référence de ce dossier,
qui contient déjà les `fit.py` / `export.py` / tests terminés.

## Deux façons de lancer la démo

**A. Agent Manager (au plus près d'une « vraie » isolation).** Créez les trois branches
(`docs-arch`, `feat-fit-uncertainty`, `feat-json-export`) comme le montre déjà le TP, ouvrez
l'Agent Manager, et démarrez une session par branche, chacune dans son propre git worktree. Collez
le `briefs/BRIEF_*.md` correspondant comme premier message de chaque session, avec un simple agent Code
(inutile de `@mentionner` un sous-agent ici : le worktree apporte déjà l'isolation). C'est ce qui se
rapproche le plus de « trois personnes distinctes travaillant en même temps » et qui montre le mieux
*pourquoi* l'isolation compte (une session ne peut littéralement pas voir les fichiers des autres).

**B. Sous-agents dans une seule session (au plus près de ce que les briefs du TP décrivent par « les
sous-agents de votre outil s'il en a »).** Depuis une seule session Code à la racine du dépôt, laissez
l'agent appeler lui-même `task` après que vous avez collé `DELEGATION_PROMPT.md`, ou appelez chacun
directement et à la suite : passez sur sa branche, puis `@explorer-a`, `@fit-b`, `@export-c`, chacun avec
son brief. `permission.task` dans `.kilo/kilo.jsonc` autorise exactement ces trois noms ; tout autre
nom retombe sur « ask ». Un sous-agent ne renvoie qu'un résumé à celui qui l'a appelé — si vous l'avez
appelé directement, ce résumé vous revient.

Dans les deux cas, **vous faites vous-même l'étape d'intégration** (fusionner, brancher `report.py` et
`scripts/run_analysis.py`, mettre à jour le fichier golden volontairement, lancer les tests) — cette étape
n'est volontairement pas déléguée, conformément au TP et à `templates/multi-agent/README.md`
(« vous êtes l'orchestrateur de référence »).

## À quoi s'attendre, et la leçon honnête

Résultat de référence après intégration : **90 tests passent** ; le CSV golden échoue volontairement juste
après la fusion (1 échec, 89 réussites) jusqu'à ce que vous le régénériez ; run01 `tau_s` ≈ 3.683 ± 0.180 s.
Ces chiffres proviennent d'exécutions réelles du code de référence (voir le tableau *Faits vérifiés* de la
fiche de TP du Jour 2), pas d'un assistant IA particulier.

La question de débrief est volontairement « est-ce que ça en valait la peine ? » : pour un changement de
cette taille, briefer, lancer et intégrer trois sous-agents coûte généralement **plus** cher que de le faire
dans une seule session — c'est le but de l'exercice, pas un échec de la configuration.

## Non vérifié

Les fichiers `.kilo/` ci-dessus suivent la documentation de Kilo Code lue sur kilo.ai/docs en
septembre 2026 (mêmes faits que `templates/kilo-project-kit/README.md`) et n'ont été contrôlés que pour
la validité du schéma (clés de frontmatter, valeurs de permissions, `permission.task` nomme des
agents qui existent réellement). Ils n'ont **pas été exécutés dans Kilo Code**. Avant de les utiliser en
direct, lancez le test de fumée décrit dans `templates/kilo-project-kit/README.md` et vérifiez sur votre
version installée que : les `.kilo/agents/*.md` sont pris en compte (`/reload`, ou `/agents`), un simple
message `@explorer-a` atteint le sous-agent, et un chemin `edit` refusé est réellement bloqué.
La documentation de Kilo n'est pas non plus totalement cohérente sur la permission par défaut quand aucune
règle ne correspond à un outil, ni sur l'ordre des règles dans certains exemples — cette configuration
évite la question en définissant explicitement chaque règle dont ce TP a besoin.
