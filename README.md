# Formation OpenAI Codex — Kit participant

Dépôt de distribution : le guide interactif et le code de départ de chaque jour, prêts à cloner.

```text
Jour1/                          TP 1 à 3 — Prise en main de Codex & génération assistée
  Guide_Participant_Jour1.html   guide interactif : ouvrez-le simplement dans votre navigateur
  Starters/                     tp1_initialiser, tp2_api, base_facturation
Jour2/                          TP 4 à 7 (+ TP 8 bonus) — Fonctions avancées, Tools & Agents, orchestration multi-agents, hooks & commandes perso
  Guide_Participant_Jour2.html
  Starters/                     base_facturation, tp4_action, tp5_tool, tp6_agents, tp7_refactor, tp8_hooks
  Templates/                    à réutiliser en équipe après la formation (bonnes pratiques, prompts, conventions)
```

## Utilisation

1. Clonez ce dépôt (ou téléchargez-le en zip).
2. Ouvrez `JourN/Guide_Participant_JourN.html` dans votre navigateur — aucune installation requise. Le guide fonctionne hors ligne ;
   votre progression, vos cases cochées et les prompts que vous rédigez sont enregistrés automatiquement dans ce navigateur.
3. Suivez les instructions du guide en travaillant dans `JourN/Starters/`.

Chaque bloc « Squelette de prompt (à compléter) » est un champ de texte libre : écrivez votre prompt directement dedans
(bouton **Copier** pour le copier vers Codex, **↺ Réinitialiser** pour revenir au squelette de départ).

## Prérequis

Python 3.11 ou plus, Git, un IDE, et Codex installé (CLI et/ou extension). Pour certains TP : une clé d'API OpenAI
(fournie par votre formateur) — à placer uniquement dans une variable d'environnement, jamais dans un fichier.

## À partir du Jour 3 ou en cas de doute

Le Jour 2 embarque sa propre copie de `base_facturation` : si vous n'avez pas fait le Jour 1, ou si vous préférez repartir
d'une base neuve, utilisez celle fournie dans `Jour2/Starters/`.

## TP 8 — bonus (hooks & commande personnalisée)

`Jour2/Starters/tp8_hooks/` contient un hook `PreToolUse` et une commande personnalisée (`/prompts:`) à compléter, avec leurs
tests. Facultatif : à faire en fin de Jour 2 si le temps le permet, sinon en autonomie après la formation — voir le guide du
participant Jour 2 pour les instructions.

## Templates à partager avec votre équipe

`Jour2/Templates/` contient trois documents prêts à diffuser après la formation, à toute l'équipe qui utilise Codex sur vos
dépôts (pas seulement les participants) : bonnes pratiques de code avec Codex en équipe, des squelettes de prompts
réutilisables, et des conventions d'équipe (où ranger quoi, permissions par défaut, gestion des secrets, processus de
revue). Voir `Jour2/Templates/README.md`.
