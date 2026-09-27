# Formation OpenAI Codex — Kit participant

Dépôt de distribution : le guide interactif et le code de départ de chaque jour, prêts à cloner.

```text
Jour1/                          TP 1 à 3 — Prise en main de Codex & génération assistée
  Guide_Participant_Jour1.html   guide interactif : ouvrez-le simplement dans votre navigateur
  Starters/                     tp1_initialiser, tp2_api, base_facturation
Jour2/                          TP 4 à 7 — Fonctions avancées, Tools & Agents spécialisés
  Guide_Participant_Jour2.html
  Starters/                     base_facturation, tp4_action, tp5_tool, tp6_agents, tp7_refactor
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
