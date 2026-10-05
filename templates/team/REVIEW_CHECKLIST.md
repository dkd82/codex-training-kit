# Checklist de revue pour les changements assistés par IA

- [ ] Je comprends chaque ligne modifiée.
- [ ] Les tests passent ET au moins un test échoue si je casse le nouveau code (vérifié).
- [ ] Aucun tableau d'entrée n'est modifié en place ; les unités et la convention dB sont correctes.
- [ ] Pas de nouvelle dépendance, de chemin absolu, de secret ni de gros fichier.
- [ ] Les changements de comportement sont décrits dans la pull request ; les fichiers golden ne changent que volontairement.
- [ ] Le diff ne touche pas de fichiers hors du périmètre de la tâche.
- [ ] J'ai lu le diff des tests en premier : aucune valeur attendue n'a été changée juste pour faire passer un test.
