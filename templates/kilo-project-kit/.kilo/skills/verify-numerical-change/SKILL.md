---
name: verify-numerical-change
description: Checklist pour vérifier un changement de code Python numérique ou scientifique avant de le déclarer terminé (unités, convention dB, modification en place, NaN et entrées vides, tolérances, fichiers golden, casser le code volontairement). À utiliser après tout changement pouvant modifier un nombre calculé.
---

# Vérifier un changement numérique

1. **Énoncez l'invariant.** Qu'est-ce qui ne doit pas changer (sorties, ligne de commande, fichiers golden) ? Qu'est-ce qui peut changer, et pourquoi ?
2. **Les entrées ne sont pas modifiées.** Cherchez dans le diff des opérateurs en place (`-=`, `+=`, `/=`, `[:] =`) appliqués à des arguments. Les fonctions renvoient de nouveaux tableaux.
3. **Unités et conventions.** Unités dans les noms et les docstrings. dB : rapport d'amplitudes `20*log10`, rapport de puissances `10*log10`. Si une convention est ambiguë, demandez au lieu de choisir.
4. **Cas limites.** Entrée vide, un seul échantillon, NaN, que des zéros, signal constant : le comportement est défini et testé.
5. **Tolérances.** Chaque tolérance `approx` peut être justifiée (niveau de bruit, discrétisation). Aucune tolérance large choisie pour faire passer un test.
6. **Une vérification physique existe.** Une valeur analytique, une loi de conservation ou une limite connue est testée.
7. **Les tests peuvent échouer.** Changez volontairement un opérateur ou une constante : au moins un test doit échouer. Rétablissez-le.
8. **Les fichiers golden** ne changent que volontairement, dans un commit séparé dont le message dit pourquoi.
9. **Rapport.** Listez ce qui a été vérifié, ce qui ne l'a pas été, et chaque hypothèse.
