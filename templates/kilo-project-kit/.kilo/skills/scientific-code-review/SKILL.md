---
name: scientific-code-review
description: Critères pour relire un diff de code Python scientifique (exactitude numérique, modification en place, unités, convention dB, tests manquants ou faibles, chemins, dépendances, périmètre). À utiliser quand on demande de relire des changements, une pull request ou du code généré.
---

# Revue de code scientifique

Relisez dans cet ordre et rapportez 7 commentaires au maximum, du plus grave au moins grave (fichier:ligne, gravité, problème, correctif en une phrase).

1. **Exactitude numérique** : unités, convention dB, erreurs de décalage d'index, dtype, gestion des NaN et des entrées vides, division par zéro.
2. **Aliasing** : un argument modifié en place (`-=`, `/=`, affectation par tranche) auquel l'appelant ne s'attend pas.
3. **Tests** : changements de comportement sans test ; tests qui ne pourraient pas échouer ; valeurs attendues recalculées avec le code testé ; tolérances trop larges.
4. **Hygiène** : constantes codées en dur, chemins absolus, secrets, dépendances nouvelles ou inutilisées, gros fichiers.
5. **Périmètre** : fichiers modifiés que la tâche ne nécessitait pas ; fichiers golden modifiés sans raison indiquée.

Ne commentez pas le formatage. Dites « aucun problème trouvé » s'il n'y en a pas, et dites quelles parties vous n'avez pas pu juger.
