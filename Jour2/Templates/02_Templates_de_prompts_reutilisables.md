# Templates de prompts réutilisables en équipe

Tous les squelettes ci-dessous suivent la même structure que celle utilisée pendant la formation :
**Objectif / Contraintes / Style / Format attendu**. Copiez-collez un squelette, remplissez les « … »,
et adaptez-le à votre contexte. Gardez les champs même quand ils semblent évidents : c'est ce qui rend
le prompt reproductible par n'importe qui dans l'équipe.

## 1. Nouvelle fonctionnalité

```prompt
Objectif : implémente … (décrire la fonctionnalité en une phrase) dans … (module/fichier concerné).
Contraintes : respecter AGENTS.md ; réutiliser … (fonctions/modèles existants à ne pas dupliquer) ;
  écrire les tests d'abord ; ne pas modifier … (périmètre interdit).
Style : suivre les conventions du projet (nommage, structure des modules).
Format attendu : code + tests, suite de tests au vert, résumé des fichiers créés ou modifiés.
```

## 2. Correction de bug

```prompt
Objectif : corrige le bug suivant : … (symptôme observé, comment le reproduire).
Contraintes : ajoute d'abord un test qui reproduit le bug (test rouge), puis corrige le code (test vert) ;
  ne pas modifier de comportement non lié au bug.
Style : minimiser le diff ; pas de refactor « au passage ».
Format attendu : le test de reproduction, le correctif, la suite de tests complète au vert, une explication
  courte de la cause racine.
```

## 3. Refactor sur du code existant (avec filet de sécurité)

```prompt
Objectif : analyse … (module/fichier) en lecture seule et propose un plan de refactor : découpage en étapes,
  risques, tests de caractérisation manquants. N'écris aucun code à ce stade.
Contraintes : comportement observable inchangé ; signaler toute zone sans test avant de la toucher.
Style : plan numéroté, une étape = un commit possible.
Format attendu : liste des étapes avec risque (faible/moyen/élevé) et tests à ajouter avant chacune.
```

```prompt
Objectif : applique l'étape … du plan validé sur … (module/fichier).
Contraintes : les tests de caractérisation existants restent au vert à chaque étape ; un seul sujet par étape.
Style : petits commits, diff minimal.
Format attendu : le code modifié, la suite de tests au vert, un résumé de ce qui a changé et pourquoi.
```

## 4. Revue de code / sécurité (en solo)

```prompt
Objectif : relis … (fichier(s) ou diff) et signale les problèmes de correction, de sécurité et de tests manquants.
Contraintes : lecture seule, aucune modification ; citer le fichier et la ligne pour chaque remarque.
Style : classer les remarques par gravité (bloquant / à corriger / suggestion).
Format attendu : une liste de constats avec fichier, ligne, gravité, et la correction proposée (sans l'appliquer).
```

## 5. Revue de code en parallèle (orchestration multi-agents)

À utiliser quand une relecture gagne à être menée sous plusieurs angles en même temps (voir TP 6, étape 5).
Rappel : c'est la session Codex elle-même qui orchestre — il n'y a pas d'agent « orchestrateur » à définir.

```prompt
Objectif : relis … (fichier(s) ou diff) avec des sous-agents en parallèle : un agent pour …
  (ex. sécurité — entrées utilisateur, injections), un agent pour … (ex. tests manquants — cas limites),
  un agent pour … (ex. lisibilité et maintenabilité).
Contraintes : attendre les résultats des … agents avant de continuer ; lecture seule pour tous les agents.
Format attendu : un résumé par thème, avec fichier et ligne concernés pour chaque remarque.
```

## 6. Génération de tests sur du code existant

```prompt
Objectif : écris des tests pour … (fonction/module), y compris les cas limites : … (lister les frontières
  connues : valeurs nulles, bornes, erreurs attendues).
Contraintes : ne modifie pas le code testé ; un test doit échouer clairement s'il détecte une régression.
Style : suivre le framework de test déjà utilisé dans le projet.
Format attendu : les tests, le résultat de leur exécution, la liste des cas couverts.
```

## 7. Documentation (README, docstrings, guide d'utilisation)

```prompt
Objectif : rédige … (README / docstrings / guide) pour … (module/projet), destiné à … (public visé :
  nouvel arrivant, utilisateur final, équipe voisine).
Contraintes : rester synchronisé avec le code actuel ; ne pas documenter un comportement qui n'existe pas
  encore ; exemples exécutables si possible.
Style : concis, exemples concrets, pas de jargon non expliqué.
Format attendu : le fichier de documentation, prêt à relire.
```

## 8. Exploration / audit en lecture seule

```prompt
Objectif : explore … (dépôt/module) pour répondre à : … (question précise : où est géré X ? comment
  fonctionne Y ?). N'effectue aucune modification.
Contraintes : citer les fichiers et symboles exacts ; signaler les zones ambiguës plutôt que de deviner.
Style : synthèse d'abord, détails ensuite.
Format attendu : une réponse directe à la question, suivie des références (fichier, ligne) qui la justifient.
```

## 9. Plan avant action (tâche ambiguë ou à fort impact)

```prompt
Objectif : propose un plan pour … (tâche), sans rien exécuter ni modifier.
Contraintes : lister les hypothèses faites ; signaler les points qui nécessitent une décision humaine
  avant de continuer.
Style : plan numéroté et vérifiable.
Format attendu : les étapes, les risques identifiés, les questions ouvertes.
```

## Comment adapter ces templates

- Gardez la structure (Objectif / Contraintes / Style / Format attendu) même pour un prompt rapide : elle évite
  les oublis les plus fréquents (contraintes de périmètre, format de sortie).
- Ajoutez un template à ce fichier dès qu'un même type de demande revient plus de deux fois dans l'équipe —
  c'est le signe qu'il mérite d'être partagé plutôt que réinventé à chaque fois.
- Versionnez ce fichier avec le code (par exemple à la racine du dépôt ou dans `.codex/`) pour qu'il évolue avec
  le projet et reste accessible à toute l'équipe.
