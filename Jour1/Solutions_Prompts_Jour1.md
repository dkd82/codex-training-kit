# Jour 1 : solutions de prompts

Ce sont des **réponses modèles**, pas les seules bonnes. Essayez d'abord chaque étape avec votre propre prompt, puis comparez :
quels blocs (objectif, contexte, contraintes, exemples, format, vérification) aviez-vous que le prompt modèle n'a pas, et inversement ?

Chaque entrée donne l'étape du TP, le mode suggéré et le prompt. Les étapes dont le prompt figure déjà sur la fiche de TP (par exemple les quatre expériences du TP 1.1) sont reprises ici par souci d'exhaustivité.

## Correspondance rapide avec Kilo Code

| Mode utilisé dans les TP | Dans Kilo Code |
|---|---|
| CHAT | Ask agent |
| PLAN | Plan agent |
| EDIT | Code agent, avec `edit` sur *ask* pour relire chaque modification |
| AGENT | Code agent (ou Debug agent) |
| REVIEW | Ask agent, avec `@git-changes` (ou `/review` dans la CLI) |

Utile dans n'importe quel prompt (documentation de Kilo Code, vérifiée en septembre 2026) : joignez un fichier avec `@/chemin/vers/fichier` (le glisser-déposer depuis l'Explorateur fonctionne aussi),
`@terminal` ajoute la sortie du terminal, `@git-changes` ajoute votre diff non commité. L'agent peut aussi trouver des fichiers lui-même avec ses outils `read`, `grep` et `glob`.
Les noms peuvent différer dans les anciennes versions de l'extension (par exemple un agent de planification appelé *Architect*) : vérifiez ce qu'affiche votre installation.

> Les prompts ci-dessous mentionnent des chemins de fichiers comme `pulselab/fit.py` : dans Kilo Code, écrivez-les `@/pulselab/fit.py` si vous voulez joindre le fichier explicitement.

> **Numérotation.** Cette page suit l'ordre de la formation en présentiel, qui alterne cours et TP : le TP 1.3 (assistant IDE contre agent, Module 3) vient avant les cinq TP du Module 4 (1.4 à 1.8).

---

## TP 1.1 : Vérification de la réalité des LLM : voir les limites de vos propres yeux

*Module 1 · Comprendre comment l'IA code réellement*

### 1.1.1 Même prompt, deux sessions : la réponse est-elle la même ?

**Mode :** CHAT

```text
Écrivez une fonction Python dominant_frequency(x, fs) qui renvoie la fréquence dominante hors continu, en Hz, d'un signal réel x échantillonné à fs Hz, en utilisant NumPy.
```

### 1.1.2 À l'aveugle sur votre code : interrogez sur une fonction que le modèle n'a pas vue

**Mode :** CHAT

```text
Dans mon projet Python pulselab, que fait la fonction fit_decay dans pulselab/fit.py, et quelles sont ses faiblesses ? Citez les lignes auxquelles vous faites référence.
```

### 1.1.3 API obsolètes : le code fonctionne-t-il encore avec VOS versions ?

**Mode :** CHAT, HUMAN

```text
Écrivez un court extrait NumPy/SciPy qui (1) intègre sin(t) sur [0, pi] avec la règle des trapèzes en utilisant np.trapz, (2) l'intègre avec la règle de Simpson en utilisant scipy.integrate.simps, et (3) teste quels éléments d'un tableau figurent dans une liste en utilisant np.in1d. Affichez les trois résultats.
```

### 1.1.4 Tokens : comptage et arithmétique sans outils

**Mode :** CHAT, HUMAN

```text
Combien de fois la lettre « e » apparaît-elle dans : estimate_noise_from_first_differences
Et combien font 48213 * 7391 ? Répondez directement, n'utilisez aucun outil.
```

---

## TP 1.2 : Atelier de prompting : d'un prompt faible à un modèle réutilisable

*Module 2 · Le prompting efficace pour les développeurs*

### 1.2.2 Prompt faible d'abord (exprès)

**Mode :** CHAT, EDIT

```text
Écrivez une fonction pour mesurer la largeur d'une impulsion.
```

### 1.2.3 Prompt en six blocs

**Mode :** CHAT, EDIT

```text
OBJECTIF : Ajouter pulse_widths_fwhm(x, fs, idx) dans un nouveau module pulselab/pulses.py. Elle renvoie la largeur à mi-hauteur (FWHM), en secondes, de chaque impulsion.
CONTEXTE : Projet Python pulselab (NumPy/SciPy). x est un signal 1-D de flottants en volts avec une ligne de base autour de 0. fs est la fréquence d'échantillonnage en Hz. idx contient les indices d'échantillon des maxima des impulsions, tels que renvoyés par pulselab.peaks.find_pulses. Sortie : un tableau NumPy de largeurs en secondes, une par impulsion.
CONTRAINTES : NumPy uniquement. Ne pas modifier x. Le niveau de mi-hauteur d'une impulsion est x[idx]/2. Localiser les deux franchissements par interpolation linéaire (sous-échantillon). Si un franchissement n'est pas atteint avant la fin de l'enregistrement, renvoyer NaN pour cette impulsion. Un idx vide renvoie un tableau vide.
EXEMPLES : Pour une impulsion gaussienne d'écart-type sigma, la FWHM vaut 2*sqrt(2*ln(2))*sigma = 2.3548*sigma. La largeur ne dépend pas de l'amplitude.
FORMAT : D'abord la fonction avec une docstring qui précise les unités, puis les tests pytest, puis une courte liste de vos hypothèses.
VÉRIFICATION : Listez vos hypothèses et posez-moi des questions avant d'écrire du code. Les tests doivent couvrir : FWHM gaussienne à 3 % près, indépendance à l'amplitude, deux impulsions, une impulsion coupée par la fin de l'enregistrement, idx vide.
```

### 1.2.4 Hypothèses et questions : reprenez votre prompt de l'étape 1.2.3 et terminez-le par

**Mode :** CHAT

```text
Listez vos hypothèses et posez-moi des questions avant d'écrire le moindre code.
```

*Prompt de référence rédigé pour ce support (la fiche de TP ne donne qu'un scaffold pour cette étape).*

---

## TP 1.3 : Comparer un assistant IDE et un agent autonome sur la même tâche

*Module 3 · Panorama des outils IA*

### 1.3.1 Faites la tâche avec EDIT, puis avec AGENT ; chronométrez-vous

**Mode :** EDIT, AGENT

```text
Ajoutez une option --min-gap SECONDES (float) à scripts/run_analysis.py. Elle remplace min_gap_s de la config ; le comportement par défaut est inchangé. Une valeur négative doit arrêter le programme avec un message d'erreur clair (erreur argparse). Mettez à jour le README et ajoutez dans tests/ un test qui lance le script via subprocess pour une valeur valide et une valeur invalide. Lancez les tests.
```

---

## TP 1.4 : Explorer une base de code inconnue avec l'IA

*Module 4 · Workflow complet piloté par l'IA (1/5)*

### 1.4.1 Demandez une carte, avec preuves à l'appui

**Mode :** CHAT, AGENT

```text
Expliquez-moi ce projet Python. Il analyse des mesures bruitées de trains d'impulsions à partir de fichiers CSV dans data/.
Contraintes : lecture seule, ne modifiez aucun fichier. Citez le chemin de fichier et le nom de fonction pour chaque affirmation.
Donnez-moi (1) les points d'entrée, (2) une ligne par module de pulselab/, (3) le flux de données d'un fichier CSV jusqu'au tableau de synthèse en étapes numérotées, (4) où vit l'état de niveau module (global). Dites ce dont vous n'êtes pas sûr au lieu de deviner.
```

### 1.4.2 Demandez les code smells et les risques (code scientifique)

**Mode :** CHAT, AGENT

```text
Listez les risques pour la justesse scientifique dans cette base de code : état global caché, tableaux modifiés en place, nombres magiques, abandon silencieux de données, gestion d'exceptions trop large, ambiguïtés d'unités. Pour chaque risque, donnez fichier:ligne et une phrase. Ne modifiez aucun fichier.
```

---

## TP 1.5 : Implémenter une fonctionnalité multi-fichiers : puissance de bande

*Module 4 · Workflow complet piloté par l'IA (2/5)*

### 1.5.2 Demandez un PLAN, puis corrigez-le

**Mode :** PLAN

```text
Ajoutez une fonctionnalité de puissance de bande à ce projet. Plan uniquement : n'écrivez ni ne modifiez encore aucun code.
Fonctionnalité : `python scripts/run_analysis.py --band FMIN FMAX` ajoute une colonne band_power_V2 (dernière colonne) à summary.csv avec la puissance du signal en V^2 entre FMIN et FMAX Hz. Sans --band, le CSV doit rester inchangé.
Acceptation : (AC1) spectrum.band_power(x, fs, fmin, fmax, nperseg=1024) = PSD de Welch (scipy.signal.welch) intégrée sur [fmin, fmax], bornes incluses. (AC2) sinus d'amplitude A dans la bande -> A^2/2 à 5 % près, hors bande ~0, composante continue ignorée. (AC3) fmin >= fmax lève ValueError. (AC4) option CLI et colonne CSV comme décrit. (AC5) README mis à jour, tests ajoutés, tests existants au vert.
Donnez des étapes numérotées avec les fichiers touchés et la façon de vérifier chaque étape. Listez les risques et les questions.
```

### 1.5.3 Implémentez en trois petites étapes, un commit chacune

**Mode :** EDIT, AGENT

```text
Implémentez uniquement l'étape A du plan : ajoutez band_power(x, fs, fmin, fmax, nperseg=1024) à pulselab/spectrum.py et des tests dans tests/test_band_power.py.
Contraintes : utilisez scipy.signal.welch, intégrez la PSD sur la bande (bornes incluses) en sommant psd*df ; levez ValueError si fmin >= fmax ; ne modifiez pas x ; ne touchez aucun autre fichier.
Tests : sinus A=2 à 50 Hz, fs=1000 Hz, 10 s : la bande (40, 60) donne 2.0 à 5 % près ; la bande (100, 200) donne < 1e-3 ; un offset continu ne change pas le résultat ; la bande (0, fs/2) est proche de la variance ; une bande invalide lève ValueError.
Lancez les tests et montrez le résultat.
```

---

## TP 1.6 : Corriger un bug complexe : reproduire, formuler une hypothèse, vérifier, corriger

*Module 4 · Workflow complet piloté par l'IA (3/5)*

### 1.6.2 Demandez des hypothèses classées par priorité, pas un correctif

**Mode :** CHAT, PLAN

```text
Analyse de cause racine, ne proposez PAS encore de correctif.
Symptôme : analyze_run(run)["offset_V"] vaut ~0 pour tous les runs, alors que les données brutes ont des offsets (run03 ~ +0.6 V). Mon test en échec compare l'offset rapporté à la moyenne d'une copie de run["signal"] prise avant l'appel.
Fichiers pertinents : pulselab/report.py (analyze_run), pulselab/preprocess.py.
Donnez-moi des hypothèses classées dans un tableau : hypothèse | pourquoi plausible | une expérience (quelques lignes de Python) qui la confirmerait ou l'infirmerait. Dites quelle preuve changerait votre classement.
```

### 1.6.4 Corrigez à la racine, a minima

**Mode :** EDIT

```text
Corrigez la cause racine : estimate_noise (via remove_offset) modifie son tableau d'entrée en place, ce qui corrompt run["signal"] utilisé plus tard par analyze_run.
Contraintes : plus petit changement ; remove_offset doit renvoyer un nouveau tableau et ne jamais modifier son argument ; analyze_run doit calculer l'offset à partir du signal BRUT ; ne changez pas les résultats de n_pulses et tau_s ; ne modifiez pas les tests existants.
Ajoutez ensuite des tests de non-régression : remove_offset renvoie une copie ; estimate_noise laisse son entrée intacte ; analyze_run ne modifie pas run ; l'offset rapporté pour run03 est égal à la moyenne brute (environ 0.6 V).
Lancez les tests et listez les autres fonctions présentant le même risque.
```

---

## TP 1.7 : Générer et améliorer des tests (et vérifier qu'ils peuvent échouer)

*Module 4 · Workflow complet piloté par l'IA (4/5)*

### 1.7.2 Demandez un PLAN DE TEST avant tout test

**Mode :** PLAN, CHAT

```text
Proposez un plan de tests (pas encore de code de test) pour pulselab/fit.py, stats.py, io.py et report.py.
Faits connus : run04 a ~1 % d'échantillons manquants que load_run supprime ; run06 n'a aucune impulsion au-dessus du seuil donc tau_s doit être NaN ; fs est estimée à partir du pas de temps médian ; les offsets des six runs sont 0.30, -0.20, 0.60, 0.10, 0.45, 0.15 V (à 0.06 V près).
Donnez un tableau : comportement | nom du test | quel changement d'une seule ligne dans le source ce test doit détecter. Privilégiez les vérifications analytiques (une exponentielle sans bruit doit redonner son tau). Données aléatoires avec graine fixée uniquement. Ne réimplémentez pas dans le test le code testé.
```

### 1.7.3 Générez les tests à partir du plan approuvé

**Mode :** EDIT, AGENT

```text
Implémentez le plan de tests que nous avons approuvé, et uniquement les tests : créez ou complétez tests/test_fit.py, tests/test_stats.py, tests/test_io.py et tests/test_report.py.
Contraintes : ne modifiez aucun fichier en dehors de tests/. Chaque test vérifie une vraie valeur (pas de `is not None`, pas de `> 0` seul). Utilisez pytest.approx avec une tolérance que vous pouvez justifier dans un commentaire. Données aléatoires avec graine fixée uniquement (numpy default_rng). Ne recalculez jamais la valeur attendue avec le code testé.
Pour chaque test, ajoutez une docstring d'une ligne indiquant quel changement d'une seule ligne dans le source il doit détecter.
Lancez python -m pytest -q, montrez le résultat, puis listez les tests dont vous êtes le moins sûr.
```

*Prompt de référence rédigé pour ce support (la fiche de TP ne donne qu'un scaffold pour cette étape).*

---

## TP 1.8 : Refactoring guidé : accélérer `find_pulses` sans changer ses résultats

*Module 4 · Workflow complet piloté par l'IA (5/5)*

### 1.8.2 Écrivez des tests de caractérisation AVANT de changer quoi que ce soit

**Mode :** EDIT, AGENT

```text
OBJECTIF : écrire des tests de caractérisation de find_pulses avant que je le refactore.
CONTEXTE : pulselab/peaks.py, data/*.csv. Dans pulselab/report.py, l'offset du signal est retiré, puis le signal est lissé avec une moyenne glissante de max(3, int(0.008 * fs)) échantillons avant l'appel à find_pulses. La détection utilise config.CONFIG["threshold_v"] et config.CONFIG["min_gap_s"].
CONTRAINTES : ne modifiez pas pulselab/. Le fichier golden est généré par le code ACTUEL. Gardez dans le fichier de test une copie de l'implémentation actuelle à boucle comme oracle.
EXEMPLES : signaux aléatoires avec plateaux (cas d'égalité), min_gap_s dans {0, 0.01, 0.05}, signaux de longueur 0 à 3.
FORMAT : tests/test_characterization.py, plus un petit script qui écrit tests/golden/pulses.json.
VÉRIFICATION : tous les tests passent sur l'implémentation actuelle, inchangée. Montrez la sortie.
```

*Prompt de référence rédigé pour ce support (la fiche de TP ne donne qu'un scaffold pour cette étape).*

### 1.8.3 Refactorez pour supprimer la boucle par échantillon

**Mode :** EDIT

```text
Refactorez find_pulses dans pulselab/peaks.py pour supprimer la boucle Python échantillon par échantillon.
Invariant : sortie identique pour toute entrée (mêmes indices, même dtype). Règles à préserver : une impulsion est un maximum local avec x[i] > threshold, x[i] > x[i-1] et x[i] >= x[i+1] ; parmi des candidats plus proches que min_gap, le PREMIER l'emporte (glouton depuis la gauche) ; gap = int(min_gap_s * fs).
Contraintes : NumPy uniquement, pas de scipy.signal.find_peaks, aucun changement hors de peaks.py, ne modifiez pas les tests.
Lancez tests/test_characterization.py et le benchmark, et montrez les résultats.
```

---

## Aussi dans ce dépôt

- `templates/` : versions réutilisables de ces prompts (`templates/prompts/`), fichiers d'instructions, permissions, agents, skills et commandes pour Kilo Code.
- `Bonnes_Pratiques_Codage_IA.md` : le mémo de bonnes pratiques.
