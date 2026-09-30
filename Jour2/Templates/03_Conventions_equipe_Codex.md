# Conventions d'équipe pour OpenAI Codex

Modèle de conventions à adopter (et adapter) pour qu'une équipe utilise Codex de façon cohérente sur un même
dépôt. Les points marqués **[Codex]** rappellent un emplacement ou un mécanisme documenté officiellement ; le
reste, ce sont des choix d'équipe à trancher et à écrire noir sur blanc.

## 1. Où vivent les fichiers (rappel)

| Élément | Emplacement | Partagé avec l'équipe ? |
|---|---|---|
| Instructions de projet | `AGENTS.md` à la racine du dépôt (et sous-dossiers si besoin) | **Oui** — versionné avec le code |
| Agents personnalisés | `.codex/agents/<nom>.toml` | **Oui** si utile à l'équipe — versionné |
| Agents personnels | `~/.codex/agents/` | Non — reste sur le poste de chacun⋅e |
| Skills | `.agents/skills/<nom>/SKILL.md` | **Oui** — versionné, recommandé pour les méthodes réutilisables |
| Hooks | `.codex/hooks.json` + scripts dans `.codex/hooks/` | **Oui** — versionné, garde-fous automatiques de l'équipe |
| Commandes personnalisées | `~/.codex/prompts/<nom>.md` | Non — personnel uniquement, et **mécanisme déprécié** (préférer une skill) |
| Configuration | `.codex/config.toml` (projet) / `~/.codex/config.toml` (personnel) | Le fichier projet peut être versionné |

**Règle d'équipe recommandée** : tout ce qui doit être partagé (AGENTS.md, agents projet, skills, hooks) est
**dans le dépôt**, versionné et revu en pull request comme le reste du code. Tout ce qui est personnel
(préférences, raccourcis individuels) reste dans le profil `~/.codex/` de chacun⋅e et n'est jamais poussé sur
le dépôt partagé.

## 2. Qui peut modifier quoi

- Un agent, une skill ou un hook versionné **s'exécute pour toute l'équipe** : il se propose, se revoit et se
  fusionne comme n'importe quelle modification de code — pas de fichier `.toml`/`.json` ajouté « en douce »
  sans revue.
- Un hook exécute du code à chaque déclenchement (avant/après un outil, démarrage de session…) : traitez tout
  changement de `.codex/hooks/` comme du code sensible (revue obligatoire, tests — voir le TP 8 pour un exemple
  de hook testé avec `pytest`).
- Convention de nommage suggérée : un nom d'agent/skill en minuscules avec tirets ou underscores, qui décrit le
  **rôle** plutôt que la personne qui l'a créé (`architecte`, `revue_securite`, pas `agent_de_jean`).

## 3. Permissions par défaut de l'équipe

| Situation | Niveau recommandé |
|---|---|
| Exploration, audit, question sur le code | Read-only |
| Génération/modification de code dans le dossier de travail | Auto (workspace-write) |
| Accès à toute la machine / réseau non restreint | À proscrire par défaut ; exception documentée et temporaire uniquement |

**[Codex]** Ces trois niveaux correspondent aux présets `/permissions` (Read-only, Auto, Full Access) et aux
options `--sandbox` de la CLI (`read-only`, `workspace-write`, `danger-full-access`). Un agent personnalisé peut
fixer son propre `sandbox_mode` dans son fichier `.toml` (par exemple, forcer `read-only` pour un agent
d'exploration) — utilisez-le pour que le garde-fou survive même si quelqu'un oublie de le préciser dans le prompt.

## 4. Gestion des secrets

- Jamais de clé d'API, mot de passe ou jeton en clair dans : le code, un prompt, `AGENTS.md`, un fichier
  `.codex/agents/*.toml`, un hook, ou un commit.
- Utilisez une variable d'environnement (`OPENAI_API_KEY`, etc.) ou un gestionnaire de secrets de l'équipe.
- Un hook `PreToolUse` peut détecter et bloquer automatiquement une fuite évidente avant exécution d'une
  commande (voir `Starters/tp8_hooks` / `Solutions/tp8_hooks`) — un filet de sécurité utile, mais qui ne
  dispense pas de la vigilance de chacun⋅e.

## 5. Processus de revue avant fusion

1. `git status` / `git diff` : le périmètre modifié correspond-il à la demande ?
2. Tests au vert.
3. **[Codex]** `/review` (application) ou `codex review --uncommitted` (CLI) sur les changements non commités.
4. Validation humaine avant fusion — y compris pour un changement produit par un agent « exécutant ».

Vous pouvez reprendre la fiche de suivi utilisée pendant la formation (case à cocher : Plan validé avant code /
Tests verts / Diff relu / Commit) comme modèle de check-list de pull request.

## 6. Cycle de vie des agents, skills et hooks partagés

- **Décrire clairement** le rôle (`description`) : c'est ce que Codex utilise pour savoir **quand** proposer ou
  utiliser cet agent/cette skill.
- **Tester** ce qui peut l'être (un hook se teste comme un script normal, en lui envoyant l'entrée JSON attendue
  sur son entrée standard).
- **Revoir périodiquement** : un agent ou une skill qui ne sert plus, ou dont les instructions sont devenues
  incohérentes avec le code actuel, doit être mis à jour ou retiré — comme une dépendance qu'on ne met jamais à
  jour devient un risque.
- **Documenter le remplacement** des commandes personnalisées dépréciées (`~/.codex/prompts/`) par des skills
  quand une équipe veut partager une méthode personnelle qui a fait ses preuves.

## 7. Mesurer le coût, en équipe

- **[Codex]** Un workflow avec plusieurs sous-agents consomme plus de tokens qu'une session unique, puisque
  chaque agent fait son propre travail. Réservez le parallélisme aux tâches qui en profitent réellement
  (relecture sous plusieurs angles, exploration d'un gros périmètre) plutôt qu'à une habitude systématique.
- Suivez, au niveau de l'équipe, un indicateur simple : temps gagné perçu vs. consommation — et ajustez les
  conventions (quand utiliser un agent, quand rester en session simple) en fonction de ce retour.

## À faire avant de partager ce document

- [ ] Remplacer les recommandations génériques par les choix réels de votre équipe (niveau de permissions par
  défaut, outil de gestion des secrets, processus de revue existant).
- [ ] Ajouter un lien vers votre `AGENTS.md` de référence et vos agents/skills/hooks déjà partagés, s'il y en a.
- [ ] Nommer une personne ou une petite équipe responsable de la revue périodique des agents/skills/hooks
  versionnés (section 6).
