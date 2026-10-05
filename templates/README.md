# Modèles

Des fichiers réutilisables à adapter dans votre équipe. Copiez-les dans votre propre dépôt, modifiez-les, relisez-les comme du code.

| Dossier | Contenu |
|---|---|
| `prompts/` | Dix modèles de prompts indépendants de l'outil, construits sur les six blocs (explorer, planifier, cause racine, correction de bug, nouvelle fonction, tests, tests de caractérisation, contrat de refactoring, revue, tests par propriétés) |
| `kilo-project-kit/` | Une configuration Kilo Code prête à copier : `kilo.jsonc` (instructions + **permissions**), `AGENTS.md`, `.kilo/rules/`, `.kilo/agents/` (reviewer, test-writer, docs-writer), `.kilo/skills/` (3 skills), `.kilo/commands/` (4 commandes slash) |
| `multi-agent/` | Quand plusieurs agents valent la peine et quand non, comment fonctionnent les sous-agents de Kilo Code, un modèle de brief, un prompt de délégation |
| `team/` | Charte, checklist de revue, journal IA, plan de pilote, fiche de workflow |
| `automation/` | Hook pre-commit avec une étape IA consultative, critères de revue pour un bot, un brouillon de CI |

## Ce qui a été vérifié, et ce qui ne l'a pas été

**Vérifié**
- Les emplacements de fichiers, les noms de clés et les règles des fichiers Kilo Code ont été lus dans la **documentation officielle (kilo.ai/docs) en septembre 2026** (les sources sont listées dans `../Bonnes_Pratiques_Codage_IA.md`).
- La syntaxe a été validée par un script : `kilo.jsonc` se parse (commentaires retirés), chaque `SKILL.md` a un `name` valide (minuscules, chiffres, tirets, 64 caractères au plus, égal au nom de son dossier) et une `description` (1024 caractères au plus), chaque agent et chaque commande a un frontmatter YAML valide qui n'utilise que des clés citées dans la documentation.
- `automation/precommit.py` a été rejoué dans un dépôt git temporaire (six scénarios).

**Non vérifié**
- Le kit n'a **pas été exécuté dans Kilo Code** par son auteur (Kilo n'était pas installé là où les fichiers ont été écrits). Utilisez le test de fumée de `kilo-project-kit/README.md`.
- La documentation de Kilo Code évolue vite et n'est pas toujours cohérente avec elle-même (valeurs par défaut des permissions, ordre des règles dans les exemples). Vérifiez votre version installée.
- `automation/ci-example.yml` n'a jamais été exécuté.

## Conventions utilisées dans les modèles

- `{{doubles_accolades}}` dans les prompts : à remplacer par votre propre valeur.
- `<chevrons>` dans les fichiers (AGENTS.md, charte) : une valeur à renseigner.
