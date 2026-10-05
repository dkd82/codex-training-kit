# Conventions scientifiques

- Nommez les grandeurs avec leur unité : `offset_V`, `duration_s`, `fs_hz`, `snr_db`.
- Une valeur en dB d'un rapport d'amplitudes vaut `20*log10(rapport)` ; pour un rapport de puissances, c'est `10*log10(rapport)`. Si la convention d'une grandeur n'est pas indiquée, demandez.
- Les fonctions ne modifient jamais leurs arguments en place. Utilisez `x - x.mean()`, pas `x -= x.mean()`, sauf si la fonction est explicitement documentée comme travaillant en place.
- Les données aléatoires utilisent un générateur avec graine : `numpy.random.default_rng(seed)`.
- Le comportement pour une entrée vide et pour NaN est défini dans la docstring et couvert par un test.
- Ne remplacez pas une boucle par un appel de bibliothèque (par exemple `scipy.signal.find_peaks`) sans un test prouvant que les résultats sont identiques.
- Vérifiez qu'une fonction NumPy ou SciPy existe dans la version installée avant de l'utiliser (certains anciens noms n'existent plus).
