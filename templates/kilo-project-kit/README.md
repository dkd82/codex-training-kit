# Kit de projet Kilo Code

Un ensemble de fichiers d'équipe prêts à copier pour un projet Python scientifique : instructions, règles, permissions, agents, skills et commandes slash.

```
kilo-project-kit/
  kilo.jsonc                 config : liste d'instructions + permissions (à modifier en premier)
  AGENTS.md                  guide du projet (remplissez les <placeholders>)
  .kilo/
    rules/                   scientific-conventions.md, testing.md, security-and-data.md
    agents/                  reviewer (sous-agent, lecture seule), test-writer (sous-agent, tests uniquement), docs-writer (principal, *.md uniquement)
    skills/                  verify-numerical-change, characterization-tests, scientific-code-review
    commands/                /plan-feature, /root-cause, /review-diff, /test-plan
```

## Installation

1. Copiez le **contenu** de ce dossier à la racine de votre projet, y compris le dossier caché `.kilo`.
   Si votre projet a déjà un `kilo.jsonc`, fusionnez à la main les clés `instructions` et `permission` au lieu de l'écraser.
2. Ouvrez `AGENTS.md` et remplacez chaque `<placeholder>` par les faits de votre projet. Restez bref.
3. Lisez `kilo.jsonc` ligne par ligne et adaptez les permissions (commandes autorisées sans confirmation, fichiers protégés).
4. Rechargez : dans la CLI, utilisez `/reload` ou démarrez une nouvelle session ; dans VS Code, rechargez la fenêtre. (La documentation indique que les permissions du projet sont mises en cache tant que vous ne le faites pas.)
5. Commitez le kit : ces fichiers sont des ressources d'équipe partagées et sont relus comme du code.

## Test de fumée (5 minutes) : ne le sautez pas

Ces fichiers ont été comparés à la documentation de Kilo Code et leur syntaxe a été validée, mais ils n'ont **pas été exécutés dans Kilo Code** par leur auteur. Prouvez qu'ils fonctionnent dans *votre* version :

| Test | Ce que vous devez voir |
|---|---|
| Demandez à l'agent : « Quelles instructions et quelles règles suis-tu dans ce projet ? » | Il mentionne le contenu de `AGENTS.md` et de `.kilo/rules/`. |
| Demandez à l'agent de modifier un fichier sous `tests/golden/`. | La modification est refusée, ou au moins on vous demande d'abord. Si ce n'est **pas** le cas, l'ordre des règles n'est pas celui que vous croyez : voir la note ci-dessous. |
| Demandez-lui de lancer `git status`, puis `rm somefile`. | `git status` s'exécute ; `rm` est refusé. |
| Tapez `/plan-feature` (CLI ou chat). | La commande existe et bascule sur l'agent de planification. |
| Tapez `@reviewer` suivi d'une demande de relecture du dernier changement. | Le sous-agent s'exécute et renvoie une courte revue. |
| Demandez quelque chose qui correspond à un skill (par exemple « vérifie ce changement numérique »). | L'agent charge le skill (utilisez `/reload` après avoir ajouté des skills). |

## Notes et limites connues

- **Ordre des règles.** La documentation des permissions des agents dit que la *dernière règle qui correspond l'emporte* : les règles générales viennent donc d'abord et les exceptions après. Certains extraits d'exemple de la documentation utilisent l'ordre inverse. Ces fichiers suivent la règle telle qu'écrite ; si le test de fumée montre le comportement inverse, inversez l'ordre des entrées.
- **Valeurs par défaut.** Deux pages de la documentation se contredisent sur ce qui se passe pour un outil sans règle (ask ou allow). C'est pourquoi `kilo.jsonc` écrit explicitement chaque règle qui vous importe.
- **Commandes slash.** La documentation ne dit pas comment le texte tapé après `/commande` est transmis à la commande. Les commandes ci-jointes indiquent donc à l'agent que vous décrirez la tâche **dans votre message**. Vérifiez le comportement dans votre version.
- **Agents et modes.** Les modes personnalisés s'appellent des *agents* dans la documentation actuelle. Les anciennes versions utilisaient `.kilocodemodes` et un dossier `.kilocode/` ; la documentation indique qu'ils sont lus ou migrés automatiquement.
- **Global vs projet.** Tout ce qui est ici est au niveau du projet. Les équivalents globaux se trouvent sous `~/.config/kilo/` (voir la documentation) ; évitez de dupliquer une règle aux deux endroits.
- **Windows.** Le moteur de correspondance des permissions normalise les antislashs ; sous Windows, la correspondance ne tient pas compte de la casse (documentation).
