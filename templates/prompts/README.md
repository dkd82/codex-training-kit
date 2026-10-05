# Modèles de prompts

Des prompts réutilisables, indépendants de l'outil, construits sur les **six blocs** : objectif, contexte, contraintes, exemples, format, vérification.
Copiez-en un, remplacez chaque `{{placeholder}}`, supprimez ce dont vous n'avez pas besoin. Gardez vos versions adaptées dans votre propre dépôt (par exemple dans `prompts/`), versionnées et relues comme du code.

| Fichier | À utiliser pour | Agent Kilo Code |
|---|---|---|
| `01-explore-codebase.md` | comprendre un projet inconnu, preuves à l'appui | Ask |
| `02-plan-feature.md` | planifier un changement sur plusieurs fichiers avant tout code | Plan |
| `03-root-cause-analysis.md` | trouver la cause d'un bug, sans correctif pour l'instant | Ask |
| `04-bugfix.md` | corriger un bug une fois la cause connue | Code |
| `05-new-function.md` | écrire une nouvelle fonction numérique | Code |
| `06-write-tests.md` | planifier puis écrire des tests | Plan, puis Code |
| `07-characterization-tests.md` | figer le comportement actuel avant un refactoring | Code |
| `08-refactor-with-contract.md` | refactorer avec invariants et incréments | Plan, puis Code |
| `09-review-diff.md` | obtenir une revue consultative d'un diff | Ask |
| `10-property-based-tests.md` | écrire des tests par propriétés | Code |

Dans Kilo Code, joignez des fichiers avec `@/chemin/vers/fichier`, la sortie du terminal avec `@terminal`, et votre diff non commité avec `@git-changes`.
Les mêmes prompts fonctionnent avec n'importe quel autre assistant : seule la façon de joindre le contexte change.
