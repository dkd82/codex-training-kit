# Bonnes pratiques de code avec OpenAI Codex, en équipe

Ce document reprend les principes vus pendant la formation et les organise pour un usage quotidien en équipe.
Les éléments marqués **[Codex]** décrivent un mécanisme documenté officiellement ; les autres sont des **recommandations
de méthode** (à adapter aux règles déjà en place dans votre organisation).

## 1. Les quatre principes de base

1. **Vous gardez la maîtrise.** Plus l'outil est autonome (skills, tools, agents), plus vous devez l'encadrer : permissions
   minimales, validation humaine aux points clés, tests et relecture du diff avant de continuer.
2. **Permissions minimales** (principe du moindre privilège). **[Codex]** Les présets `/permissions` sont Read-only,
   Auto (lecture/écriture/exécution dans le dossier de travail, avec accord requis pour en sortir) et Full Access
   (toute la machine, réseau inclus). N'utilisez Full Access qu'en dernier recours, jamais par défaut.
3. **Porte humaine avant toute action irréversible** : fusion d'une branche, déploiement, suppression de données,
   envoi d'un e-mail ou d'un message réel. Un agent « exécutant » agit dans le cadre de ses permissions ; ce n'est
   pas une garantie de jugement.
4. **Petits pas, vérifiés.** Une tâche = un périmètre clair, un diff que vous pouvez relire en entier, des tests qui
   passent avant de continuer. Un prompt « fais tout » sur un gros périmètre est plus dur à vérifier et à corriger.

## 2. Avant de démarrer une tâche

- [ ] Le dossier a un `AGENTS.md` à jour (contexte, conventions, commandes de test). **[Codex]** Il est chargé
  automatiquement avant chaque tâche ; au-delà d'environ 32 Kio, il peut être tronqué — gardez-le concis et à jour.
- [ ] Aucun secret (clé d'API, mot de passe, jeton) n'est écrit en clair dans le code, un prompt, un fichier
  `AGENTS.md` ou un hook committé. Utilisez une variable d'environnement ou un gestionnaire de secrets.
- [ ] Le niveau de permissions choisi correspond au risque de la tâche : Read-only pour explorer/auditer, Auto pour
  générer/modifier du code dans le dossier de travail.
- [ ] Pour une tâche ambiguë ou à fort impact, on demande d'abord un **plan** (`/plan`) avant de laisser Codex agir.

## 3. Pendant la tâche

- **Structurez le prompt** : objectif, contraintes, style attendu, format de sortie. Voir le fichier
  `02_Templates_de_prompts_reutilisables.md` de ce dossier pour des squelettes prêts à l'emploi.
- **Donnez le contexte minimal mais suffisant** : fichiers concernés, spécification, exemples attendus. Un contexte
  trop large dilue l'attention du modèle ; un contexte trop pauvre l'oblige à deviner.
- **Relisez au fil de l'eau**, surtout pour les tâches longues : un écart détecté tôt coûte moins cher à corriger
  qu'un écart découvert après une implémentation complète.
- **Préférez plusieurs prompts ciblés** à un seul prompt qui couvre tout : c'est plus facile à vérifier, à corriger
  et à reprendre si une étape échoue.

## 4. Agents spécialisés et orchestration, en équipe

- Un agent **assistant** propose (vous décidez) ; un agent **exécutant** agit dans ses permissions. Commencez par
  des agents assistants sur les tâches nouvelles, élargissez l'autonomie quand la confiance s'installe.
- **[Codex]** Les agents personnalisés d'équipe se déclarent dans `.codex/agents/<nom>.toml` (versionnés avec le
  code, donc visibles et revus comme du code) avec `name`, `description` et `developer_instructions`. Les agents
  strictement personnels vont dans `~/.codex/agents/` et ne doivent pas porter de règle propre à un projet partagé.
- **[Codex]** Il n'existe pas d'agent « orchestrateur » prédéfini (les agents intégrés sont `default`, `worker`,
  `explorer`) : c'est **la session Codex elle-même** qui orchestre, dès qu'on le lui demande explicitement
  (« utilise l'agent X pour… », « lance plusieurs agents en parallèle, un par sujet »). Elle démarre les sous-agents,
  attend leurs résultats si on le précise, puis renvoie une réponse consolidée.
- Un rôle décrit uniquement en texte (« tu n'écris que dans `docs/` ») n'est **pas** un verrou technique : vérifiez
  systématiquement avec `git status` / `git diff` ce qu'un agent a réellement modifié.
- **[Codex]** Les workflows avec sous-agents consomment davantage de tokens (chaque agent fait son propre travail) ;
  réservez le parallélisme aux tâches qui en profitent vraiment (relecture d'un même changement sous plusieurs
  angles, exploration d'un gros dépôt), et restez prudent quand plusieurs agents écrivent en même temps
  (conflits possibles).

## 5. Sécurité et confidentialité

- Aucune donnée client réelle, aucun secret, aucune donnée personnelle sensible dans un prompt envoyé à un modèle
  hébergé à l'extérieur, sauf accord explicite de votre organisation.
- **[Codex]** Pour bloquer automatiquement certaines commandes dangereuses côté outillage (suppression massive,
  fuite de clé…), utilisez un hook `PreToolUse` versionné dans `.codex/hooks.json` + `.codex/hooks/`, validé une
  fois avec `/hooks` (mécanisme basé sur une empreinte du script). Voir le TP 8 (bonus) pour un exemple complet et
  testé.
- Gardez les agents d'exploration en **Read-only** (`sandbox_mode = "read-only"` dans le fichier `.toml`) tant
  qu'ils n'ont pas besoin d'écrire.

## 6. Revue de code, avant de fusionner

1. `git status` et `git diff` : vérifier le périmètre réel des modifications, y compris hors du fichier attendu.
2. **[Codex]** `/review` (dans l'application) ou `codex review --uncommitted` (en ligne de commande) pour une revue
   non interactive des changements non commités.
3. Les tests passent (`pytest`, ou l'équivalent du projet) avant tout commit.
4. Un humain valide avant fusion — Codex accélère la production, pas la décision de mise en production.

## 7. Limites à rappeler à l'équipe

- **Coût en tokens** : plus d'agents, plus de tours, plus de consommation. Mesurez le gain réel (temps gagné)
  face au coût.
- **Conflits d'écriture** : plusieurs agents qui modifient les mêmes fichiers en parallèle peuvent se marcher
  dessus ; préférez le parallélisme pour les tâches de lecture (exploration, tests, revue).
- **Propagation d'erreurs** : une erreur non détectée dans un agent (ex. l'architecte) peut se retrouver dans le
  travail de l'agent suivant (le développeur) si personne ne la relit.
- **Supervision humaine toujours nécessaire** : ces outils progressent vite mais ne remplacent pas le jugement
  d'un⋅e relecteur⋅rice.

## Pour aller plus loin

Adaptez ce document à vos propres règles (revue de code, gestion des secrets, conventions de commit) et
partagez-le avec toute personne de l'équipe qui utilise Codex sur vos dépôts. Voir aussi
`03_Conventions_equipe_Codex.md` pour les conventions concrètes de rangement des fichiers.
