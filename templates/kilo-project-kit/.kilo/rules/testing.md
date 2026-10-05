# Règles de test

- Chaque test vérifie une vraie valeur. Pas de `assert x is not None`, pas de `assert x > 0` seul.
- Ne calculez jamais la valeur attendue avec le code testé.
- Utilisez `pytest.approx` avec une tolérance que vous pouvez justifier dans un commentaire.
- Privilégiez les vérifications analytiques (une exponentielle connue doit redonner sa constante de temps, une gaussienne de largeur sigma a une FWHM de 2*sqrt(2*ln 2)*sigma).
- Avant un refactoring, écrivez des tests de caractérisation (fichier golden + une copie oracle du code actuel).
- Ne modifiez jamais `tests/golden/*` et n'affaiblissez jamais une assertion pour faire passer un test. Si une valeur golden doit changer, arrêtez-vous et demandez.
- Après avoir écrit des tests, cassez le code volontairement (changez un opérateur ou une constante) : au moins un test doit échouer.
