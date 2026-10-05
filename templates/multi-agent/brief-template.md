# Modèle de brief pour un sous-agent ou une session séparée

Un sous-agent ou une session neuve ne connaît **que ce que vous écrivez ici**. Rendez le brief autonome.

```
BRIEF <nom>
Objectif :           {{one_sentence}}
Contexte :           {{ce qu'il doit savoir : projet, conventions, unités, fichiers à lire}}
Fichiers autorisés : {{les SEULS fichiers qu'il peut créer ou modifier}}
Hors périmètre :     {{tout le reste, explicitement (report.py, la CLI, tests/golden/...)}}
Livrable :           {{signature / fichier / comportement}}
Vérification :       {{commande à lancer}}. Rendez compte en 10 lignes maximum : ce qui a été fait, fichiers touchés, résultat des tests.
```

## Règles pour l'ensemble des briefs

- Les « fichiers autorisés » de deux briefs ne se recouvrent jamais.
- Tout ce qui touche plusieurs morceaux (câblage, options de la CLI, fichiers golden) est **votre** étape d'intégration, pas celle d'un sous-agent.
- Chaque brief indique comment le résultat sera vérifié.
- Après l'intégration : lancez tous les tests, lisez les diffs fichier par fichier, et demandez un second avis à un relecteur dans un contexte neuf.

## Exemple (issu du TP 2.3)

```
BRIEF B
Objectif :           ajouter fit_decay_with_error(t_peaks, heights) -> (tau, tau_err) à pulselab/fit.py.
Contexte :           fit_decay ne renvoie actuellement que tau (scipy.optimize.curve_fit de a*exp(-t/tau)). tau_err est l'incertitude à 1 sigma sqrt(pcov[1,1]). Renvoyer (nan, nan) quand l'ajustement est impossible. fit_decay conserve son comportement. Les temps sont en secondes.
Fichiers autorisés : pulselab/fit.py et tests/test_fit_uncertainty.py (nouveau).
Hors périmètre :     tout le reste, en particulier report.py et les fichiers golden.
Livrable :           la fonction et ses tests : le vrai tau est à moins de 3 sigma sur des données bruitées ; un bruit plus fort donne un tau_err plus grand ; une entrée vide donne (nan, nan) ; fit_decay est égal à la première valeur.
Vérification :       python -m pytest -q. Rendez compte en 10 lignes maximum.
```
