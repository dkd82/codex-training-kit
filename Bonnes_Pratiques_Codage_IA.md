# Coder avec l'IA : mémo de bonnes pratiques

Pour les chercheurs qui écrivent du Python scientifique avec un agent de code IA (Kilo Code). Gardez-le à côté de votre éditeur.

Fichiers complémentaires de ce dépôt : `templates/` (prompts réutilisables, instructions, permissions, agents, skills, commandes),
`Jour2/Aide-mémoire – Français.pdf` (commandes Kilo CLI), et les solutions de prompts de chaque jour.

---

## Les 10 règles

1. **Vous êtes responsable de chaque ligne que vous commitez**, quel que soit celui (ou ce) qui a écrit le premier jet.
2. **Plausible ne veut pas dire vérifié.** Un modèle de langage produit le texte le plus probable, pas un résultat contrôlé.
3. **Vérifiez avec quelque chose qui peut échouer** : un test, un invariant physique, un script. Jamais avec l'assurance du modèle.
4. **Une tâche par prompt, de petites étapes, un commit par étape.**
5. **Donnez le contexte qui compte, pas le contexte qui est gros** : les bons fichiers, versions, messages d'erreur, conventions.
6. **Planifiez avant de coder** dès que plusieurs fichiers sont touchés. Relisez le plan, puis implémentez.
7. **Protégez ce qui définit le « correct »** : tests, fichiers golden, conventions. Ne laissez pas l'agent les modifier pour faire passer un test.
8. **Donnez à l'agent le minimum de permissions dont il a besoin**, travaillez sur une branche, lisez chaque diff.
9. **Pas de secrets, pas de données confidentielles, pas de résultats non publiés dans les prompts**, sauf si votre entreprise a approuvé l'outil pour cela.
10. **Écrivez ce qui marche** (fichier d'instructions, modèles de prompts) et gardez-le dans le dépôt, relu comme du code.

---

## 1. Avant de rédiger un prompt

- Créez une branche et **commitez d'abord**. Chaque changement de l'IA doit pouvoir être relu et annulé.
- Décidez du **périmètre** : quels fichiers peuvent changer, lesquels ne le doivent pas.
- Sachez ce que le modèle **ne peut pas savoir** : les versions installées sur *votre* machine, les conventions de votre équipe, tout ce qui a été publié après son entraînement.
  Vérifiez les noms dans votre environnement (`hasattr(np, "trapezoid")`) au lieu de vous fier à la mémoire.
- Mettez les connaissances stables dans un **fichier d'instructions** (`AGENTS.md`) une fois pour toutes, au lieu de les répéter dans chaque prompt.

## 2. Anatomie d'un bon prompt (six blocs)

| Bloc | Question à laquelle il répond | Exemple pour du code numérique |
|---|---|---|
| **Objectif** | Que veux-je, et pourquoi ? | « Ajoute `pulse_widths_fwhm(x, fs, idx)` : la FWHM de chaque impulsion en secondes. » |
| **Contexte** | Que doit-il savoir ? | Projet, fichier, entrées avec leurs **unités**, une fonction existante à imiter. |
| **Contraintes** | Que doit-il (ne pas) se passer ? | NumPy uniquement, pas de modification en place des entrées, NaN si le franchissement n'est pas atteint. |
| **Exemples** | À quoi ressemble un bon résultat ? | « Une gaussienne d'écart-type σ a une FWHM = 2√(2 ln 2)·σ. » |
| **Format** | Quelle forme doit prendre la réponse ? | La fonction, puis les tests, puis une liste d'hypothèses. |
| **Vérification** | Comment saurons-nous que c'est juste ? | « Liste tes hypothèses et pose-moi des questions d'abord. Les tests doivent couvrir… » |

Les habitudes qui paient :
- **Les vérifications physiques sont les meilleurs tests d'acceptation** (valeur analytique, conservation, symétrie, limite connue).
- Terminez par **« Liste tes hypothèses et pose-moi des questions avant d'écrire du code »** quand la tâche est ambiguë.
- Pour un bug, demandez **des hypothèses classées et une expérience pour chacune, avant tout correctif.** Demandez la cause avant le correctif.
- Collez les **messages d'erreur exacts**, pas leur description.
- Après 2 ou 3 tentatives ratées, **repartez avec un meilleur prompt** dans une session neuve : une longue chaîne d'échecs pollue le contexte.

## 3. Un workflow qui marche : explorer, planifier, implémenter, vérifier, commiter

| Phase | Vous | IA | Kilo Code |
|---|---|---|---|
| **Explorer** | Posez une question précise | Lit et cartographie le code, cite les fichiers | Agent *Ask* (lecture seule) |
| **Planifier** | Relisez et corrigez le plan | Propose fichiers, étapes, risques | Agent *Plan* |
| **Implémenter** | Gardez des étapes petites, nommez le périmètre | Écrit le code et les tests | Agent *Code* |
| **Vérifier** | Lancez tout, lisez le diff | Lance les tests, corrige les échecs | tests + votre relecture |
| **Commiter** | Assumez le changement | Rédige le message et la doc | git |

Pour un bug : **reproduisez d'abord avec un test qui échoue**, puis des hypothèses, puis un correctif minimal à la cause racine, puis un test de non-régression.
Pour un refactoring : **d'abord des tests de caractérisation** (ils figent le comportement actuel), puis de petites étapes.

## 4. Vérifier comme un scientifique

**Cinq contrôles avant d'accepter du code généré**
1. Est-ce que je comprends chaque ligne ?
2. Est-ce que ça tourne, et est-ce que des tests *significatifs* passent ?
3. Les fonctions, paquets et versions utilisés existent-ils vraiment **dans mon environnement** ?
4. Respecte-t-il nos conventions (unités, dB, structure) ?
5. Est-il sûr : entrées, secrets, permissions, licences ?

**Code numérique : pièges typiques à chercher**
- **Tableaux modifiés en place** (`x -= x.mean()` modifie le tableau de l'appelant) : renvoyez un nouveau tableau.
- **Conventions dB** : un rapport d'amplitudes utilise `20·log10`, un rapport de puissances utilise `10·log10`. L'assistant peut proposer l'une ou l'autre ; c'est vous qui décidez.
- **Unités** dans les noms (`_V`, `_s`, `_hz`), comportement sur **NaN et entrée vide**, **graines** pour les données aléatoires, **tolérances** que vous savez justifier.
- **API obsolètes ou renommées** (par exemple `np.trapz` n'existe plus dans les versions récentes de NumPy : `np.trapezoid`).
- Un **nombre que le modèle n'a pas calculé avec un outil** est une supposition. Compter des caractères ou multiplier de grands nombres « de tête » n'est pas fiable.
- Remplacer votre propre boucle par un appel de bibliothèque (par exemple `scipy.signal.find_peaks`) peut **changer silencieusement les résultats** : prouvez d'abord l'équivalence avec des tests.

**Un test au vert n'est pas forcément un bon test**
- Cassez le code volontairement et vérifiez qu'un test échoue. Recommencez avec le script de mutation de l'atelier 2.2.
- Méfiez-vous des tests qui recalculent la même expression que le code, qui n'assertent que `> 0` ou `is not None`, ou qui mockent tout.
- La couverture dit quelles lignes ont été exécutées, pas si un comportement a été vérifié.
- Les tests par propriétés (`hypothesis`) et les **fichiers golden** protègent les refactorings.

## 5. Travailler avec un agent en sécurité

- **Moindre privilège.** Configurez les permissions explicitement (`templates/kilo-project-kit/kilo.jsonc`). Demandez confirmation avant les commandes shell, avant les modifications difficiles à annuler, avant l'accès web.
- **N'activez pas l'auto-approbation à la légère.** La documentation de Kilo Code elle-même avertit qu'elle contourne les demandes de confirmation et donne à l'agent un accès direct à votre système, et que l'accès à la ligne de commande est particulièrement dangereux.
- **Protégez les fichiers qui définissent la justesse** (`tests/golden/`, secrets) : interdisez leur modification par une règle de permission, et dites-le dans le prompt.
- **Travaillez par incréments** : un incrément, lancez les tests, commitez. Si l'agent dérive ou boucle, arrêtez, annulez (`git restore .`) et reformulez l'objectif avec ce que vous avez appris.
- **Lisez d'abord le diff des tests** : une *valeur attendue* a-t-elle changé, ou seulement la façon de construire les objets ? Une assertion affaiblie est un signal d'alerte.
- **Traitez le contenu que l'agent lit comme non fiable** (pages web, tickets, fichiers venus d'ailleurs) : il peut contenir des instructions destinées à l'agent (injection de prompt).
- **Ne mettez jamais de secrets dans les prompts ni dans les fichiers que l'agent peut lire.** Kilo Code traite la lecture des fichiers `.env` comme sensible et demande d'abord ; gardez ce comportement.
- **Demandez des preuves** : chemins de fichiers et numéros de ligne que vous pouvez ouvrir. Si l'agent affirme « tous les tests passent », faites-lui montrer la sortie.

## 6. Plusieurs agents : seulement quand un seul atteint une limite

Commencez avec **un** agent. Envisagez-en plusieurs seulement pour : surcharge de contexte, sous-tâches parallèles réellement indépendantes (fichiers différents), rôles ou permissions différents (un relecteur en lecture seule), vérification indépendante.
Évitez-les pour des changements petits ou fortement couplés, ou quand vous ne pouvez pas encore vérifier la sortie d'un seul agent.
Coûts : plus de tokens et de temps, information perdue lors des passations, modifications conflictuelles, erreurs qui se cumulent.
Rédigez un **brief précis** pour chaque sous-agent (objectif, fichiers autorisés, hors périmètre, livrable, vérification). C'est vous qui intégrez et relisez.
Voir `templates/multi-agent/`.

## 7. Pratiques d'équipe

- **Ressources partagées dans le dépôt** : fichier d'instructions, modèles de prompts, agents, skills, commandes, checklist de revue, charte. Relisez-les comme du code.
- **Transparence et responsabilité** : convenez en équipe de quand l'usage de l'IA est mentionné dans une pull request ; l'auteur reste responsable.
- **La revue IA est consultative** : une première passe qui complète une revue humaine. Donnez-lui des critères écrits (`templates/automation/REVIEW_CRITERIA.md`).
- **Les contrôles déterministes font barrière** (tests, lint, scan de secrets) ; les étapes IA conseillent et ne doivent jamais bloquer à elles seules.
- **Pilotez avant de standardiser** : une petite tâche réelle, une métrique, des critères d'arrêt.

## 8. Quand ne pas utiliser l'IA

- Données confidentielles dans un outil non approuvé.
- Vous ne pouvez pas évaluer le résultat (pas d'expertise, pas de test).
- Un changement trivial plus rapide à la main.
- Une logique critique pour la sécurité ou la sûreté sans revue d'expert.
- Des exigences floues : clarifiez d'abord avec les personnes.
- Quand maîtriser la compétence est le but : galérez un peu d'abord.

---

## 9. Kilo Code : ce que dit la documentation

Vérifié dans la documentation officielle (kilo.ai/docs) en **septembre 2026**. Kilo Code évolue vite : **vérifiez votre version installée**.
Les anciennes versions utilisaient d'autres noms et chemins (par exemple un agent *Architect*, `.kilocodemodes`, un dossier `.kilocode/`) ; la documentation actuelle indique que les fichiers hérités sont lus ou migrés automatiquement.

| Besoin | Où / comment |
|---|---|
| Instructions du projet | `AGENTS.md` à la racine du projet (en majuscules ; `AGENT.md` en repli). Un `AGENTS.md` dans un sous-dossier est chargé quand l'agent lit des fichiers de ce dossier. `/init` (CLI) le crée ou le met à jour. |
| Règles supplémentaires | Fichiers Markdown (par exemple `.kilo/rules/*.md`) listés dans la clé `instructions` de `kilo.jsonc` (globs autorisés). |
| Configuration | `kilo.jsonc` à la racine du projet ou `.kilo/kilo.jsonc` (ce dernier l'emporte si les deux existent) ; global : `~/.config/kilo/kilo.jsonc`. Rechargez la fenêtre ou démarrez une nouvelle session CLI après avoir changé les permissions du projet. |
| Permissions | Clé `permission` : `allow`, `ask` ou `deny`, par outil (`read`, `edit`, `bash`, `task`, `webfetch`…), avec des motifs glob. **La dernière règle qui correspond l'emporte** : mettez la règle générale d'abord, les exceptions après. |
| Agents (anciens modes personnalisés) | `.kilo/agents/<nom>.md` : frontmatter YAML (`description`, `mode: primary` ou `subagent`, `permission`…) puis le prompt. Changez avec `/agents`. |
| Sous-agents | `mode: subagent`. Appelés par l'agent via son outil `task`, ou par vous avec `@nom-de-l-agent`. Seul le résumé remonte à l'agent parent. `permission.task` contrôle quels sous-agents peuvent être appelés. |
| Skills | `.kilo/skills/<nom>/SKILL.md` avec `name` (doit être égal au nom du dossier, minuscules et tirets) et `description`. `/reload` prend en compte les changements. |
| Commandes | `.kilo/commands/<nom>.md` devient `/<nom>`. Frontmatter facultatif : `description`, `agent`, `model`, `variant`, `subtask`. |
| Contexte | `@/chemin/fichier`, `@terminal`, `@git-changes`. L'agent peut aussi trouver les fichiers lui-même. |
| Travail en parallèle | *Agent Manager* (VS Code) : plusieurs sessions, éventuellement dans des git worktrees séparés. L'ancien agent *Orchestrator* est marqué obsolète : Code, Plan et Debug délèguent eux-mêmes aux sous-agents. |
| Sessions (CLI) | `/new`, `/sessions`, `/compact` (résumer une longue session), `/undo`, `/redo`, `/fork`, `/review`, `/diff`. Liste complète dans l'aide-mémoire. |
| Fichiers à tenir hors de portée | Utilisez les **permissions** `read`/`edit` dans `kilo.jsonc` (`.kilocodeignore` est l'ancienne méthode et est migré). |

**Deux points sur lesquels la documentation n'est pas cohérente, donc ne vous y fiez pas :**
- la permission **par défaut** des outils sans règle (une page dit *ask*, une autre dit que la plupart des outils sont en *allow*) : écrivez toujours les règles que vous voulez ;
- l'**ordre** dans les exemples de permissions (une page met la règle spécifique en premier) : suivez la règle « la dernière règle qui correspond l'emporte » et testez que vos règles font ce que vous croyez.

## Sources

- Règles personnalisées : https://kilo.ai/docs/customize/custom-rules
- Instructions personnalisées : https://kilo.ai/docs/customize/custom-instructions
- AGENTS.md : https://kilo.ai/docs/customize/agents-md
- Modes personnalisés (agents) : https://kilo.ai/docs/customize/custom-modes
- Sous-agents personnalisés : https://kilo.ai/docs/customize/custom-subagents
- Permissions des agents : https://kilo.ai/docs/customize/agent-permissions
- Skills : https://kilo.ai/docs/customize/skills
- Workflows (commandes) : https://kilo.ai/docs/customize/workflows
- Utiliser les agents : https://kilo.ai/docs/code-with-ai/agents/using-agents
- Mentions de contexte : https://kilo.ai/docs/code-with-ai/agents/context-mentions
- Approbation automatique des actions : https://kilo.ai/docs/getting-started/settings/auto-approving-actions
- Agent Manager : https://kilo.ai/docs/automate/agent-manager
- MCP : https://kilo.ai/docs/automate/mcp/using-in-kilo-code
- CLI : https://kilo.ai/docs/code-with-ai/platforms/cli
