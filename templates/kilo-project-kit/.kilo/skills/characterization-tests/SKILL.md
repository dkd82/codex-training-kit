---
name: characterization-tests
description: Comment figer le comportement actuel d'une fonction avant de la refactorer, avec un fichier golden calculé par le code actuel et une copie oracle de l'implémentation actuelle. À utiliser avant d'optimiser, de vectoriser ou de restructurer du code numérique.
---

# Tests de caractérisation avant un refactoring

1. **Ne touchez pas encore au source.** Lisez la fonction et listez ses appelants ainsi que le prétraitement qui a lieu avant son appel.
2. **Fichier golden.** Lancez le code ACTUEL sur les vrais fichiers de données et stockez les sorties (par exemple les indices détectés) dans `tests/golden/<name>.json`. Un test compare le code à ce fichier.
3. **Oracle.** Copiez l'implémentation actuelle dans le fichier de test (`legacy_<name>`). Un second test compare le nouveau code à l'oracle sur de nombreuses entrées générées.
4. **Entrées générées.** Des données aléatoires avec égalités et plateaux, plusieurs valeurs de chaque paramètre y compris 0, et des entrées de longueur 0 à 3.
5. **Elles doivent passer sur le code inchangé.** Sinon, les tests sont faux : corrigez-les avant de refactorer.
6. **Refactorez par petites étapes**, en lançant ces tests après chacune. Une fonction de bibliothèque qui paraît équivalente (par exemple `scipy.signal.find_peaks`) n'est acceptée que si ces tests passent.
7. Commitez les tests et le fichier golden **avant** le commit de refactoring.
