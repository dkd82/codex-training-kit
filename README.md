# IA pour les devs – Maîtrisez l'IA pour coder
## TP des participants (projet fil rouge « pulselab »)

Formation intra-entreprise pour CGG Services SAS · Formateur : Daouda DIOP

Ce dépôt contient tout ce dont vous avez besoin pour les TP, jour par jour, ainsi que des modèles réutilisables pour votre équipe.
Aucune donnée confidentielle n'est utilisée : le projet `pulselab` travaille sur des mesures simulées.
Les TP sont écrits pour fonctionner avec n'importe quel assistant de code IA ; les exemples et les modèles ciblent **Kilo Code**.

## Structure

```
Jour1/
  IA_Pour_Les_Devs_CGG_Services_SAS_Jour1.pdf   <- support de présentation du Jour 1
  TP_Jour1_Participant.html                     <- fiche de TP du Jour 1 (à ouvrir dans un navigateur)
  pulselab_jour1_starter.zip                    <- projet Python de départ du Jour 1
  Solutions_Prompts_Jour1.md                    <- prompts modèles pour les étapes des TP (à comparer après votre essai)

Jour2/
  IA_Pour_Les_Devs_CGG_Services_SAS_Jour2.pdf   <- support de présentation du Jour 2
  Aide-mémoire – Français.pdf                   <- aide-mémoire des commandes Kilo CLI
  TP_Jour2_Participant.html                     <- fiche de TP du Jour 2
  pulselab_jour2_starter.zip                    <- projet Python de départ du Jour 2 (état de référence propre)
  Solutions_Prompts_Jour2.md                    <- prompts modèles pour les étapes des TP

Bonnes_Pratiques_Codage_IA.md                   <- mémo : bonnes pratiques pour coder avec l'IA

templates/                                      <- fichiers réutilisables à adapter dans votre équipe
  prompts/            dix modèles de prompts (explorer, planifier, cause racine, correction de bug, nouvelle fonction, tests, ...)
  kilo-project-kit/   kilo.jsonc (instructions + permissions), AGENTS.md, règles, agents, skills, commandes slash
  multi-agent/        quand plusieurs agents valent la peine, sous-agents dans Kilo Code, modèle de brief, prompt de délégation
  team/               charte, checklist de revue, journal IA, plan de pilote, fiche de workflow
  automation/         hook pre-commit avec une étape IA consultative, critères de revue, brouillon de CI
```

## Pour commencer

1. Récupérez ce dépôt (`git clone <url>`, ou `git pull` si vous l'avez déjà).
2. Ouvrez `Jour1/TP_Jour1_Participant.html` dans votre navigateur (double-clic : la page est autonome, aucun réseau n'est nécessaire).
3. Suivez le TP 1.0 : il vous guide pour décompresser `pulselab_jour1_starter.zip` et configurer votre environnement Python.
4. Le Jour 2, faites de même avec le dossier `Jour2/` (faites d'abord un `git pull` si vous avez cloné plus tôt).

Dans les fiches de TP, vous pouvez **écrire vos prompts directement dans la page** (les encadrés jaunes, et un bloc-notes facultatif sur les étapes IA).
Vos prompts, vos étapes cochées et vos notes sont enregistrés **localement dans votre navigateur** (pas dans ce dépôt) : continuez à utiliser le même navigateur et le même emplacement de fichier.
Copiez le prompt terminé dans votre assistant avec le bouton *Copier mon prompt*.

## Règles rappelées tout au long des TP

- Pas de données confidentielles, pas de secrets dans les prompts (le jeu de données est synthétique).
- Commitez avant toute action de l'IA susceptible de modifier des fichiers, et lisez chaque diff.

## À propos des modèles

Les fichiers Kilo Code de `templates/` suivent la documentation officielle telle que lue en septembre 2026, et leur syntaxe a été validée par un script.
Ils n'ont **pas été exécutés dans Kilo Code** par leur auteur : utilisez le test de fumée de `templates/kilo-project-kit/README.md` et vérifiez votre version installée.
