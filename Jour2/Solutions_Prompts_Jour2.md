# Jour 2 : solutions de prompts

Ce sont des **réponses modèles**, pas les seules bonnes. Essayez d'abord chaque étape avec votre propre prompt, puis comparez :
quels blocs (objectif, contexte, contraintes, exemples, format, vérification) aviez-vous que le prompt modèle n'a pas, et inversement ?

Chaque entrée donne l'étape du TP, le mode suggéré et le prompt. Le TP 2.4 (ressources d'équipe) et le TP 2.5 (automatisation) utilisent les fichiers de `templates/`.

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

---

## TP 2.1 : Refactoring à grande échelle avec un agent

*Module 5 · Utiliser des agents IA pour des tâches complexes (1/3)*

### 2.1.1 Écrivez le contrat de refactoring (humain) : un exemple rempli

**Mode :** HUMAN

```text
CONTRAT DE REFACTORING
Objectif :      remplacer le dict global CONFIG et les dicts run par des dataclasses explicites Config et Run (plus pathlib, logging, annotations de type) sans changer aucun résultat.
Invariants :    tests/golden/summary_expected.csv et tests/golden/pulses.json sont intacts et les tests passent ; les options CLI de scripts/run_analysis.py sont inchangées ; aucune nouvelle dépendance.
Interdit :      modifier tests/golden/*, affaiblir ou supprimer une assertion, ajouter une dépendance, toucher des fichiers hors du plan.
Terminé quand : python -m pytest -q passe ; `git diff main -- tests/golden` n'affiche rien ; `git grep -nE "CONFIG|os\.path|glob\.glob" -- pulselab scripts` n'affiche rien ; python scripts/benchmark.py affiche la même somme de contrôle qu'avant.
Retour arrière : un commit par incrément sur la branche refactor-config ; `git restore .` ou `git revert` pour revenir en arrière.
```

*Prompt de référence rédigé pour ce support (la fiche de TP ne donne qu'un scaffold pour cette étape).*

### 2.1.2 Demandez un plan et challengez-le

**Mode :** PLAN

```text
Plan uniquement, ne modifiez aucun fichier.
Refactorez ce projet : (1) remplacer le dict global CONFIG de pulselab/config.py par une dataclass figée Config (threshold_v, min_gap_s, band) passée explicitement ; (2) remplacer le dict run renvoyé par load_run par une dataclass Run (name, t, signal, temp, fs, meta) ; (3) utiliser pathlib au lieu de os.path et glob ; (4) utiliser logging au lieu de print pour les messages (garder le tableau de résultats affiché par print_table) ; (5) ajouter des annotations de type aux fonctions publiques.
Invariants : tests/golden/* intacts ; le CSV de synthèse et les impulsions ne changent pas ; options CLI inchangées ; aucune nouvelle dépendance ; n'affaiblissez aucune assertion.
Donnez un plan ordonné en incréments pour que les tests puissent tourner après chaque incrément : fichiers touchés, risques, et commandes qui prouvent chaque incrément.
```

### 2.1.4 Incrément par incrément (tests après chacun, un commit chacun)

**Mode :** AGENT, EDIT

```text
Exécutez uniquement l'incrément A du plan : créez la dataclass figée Config dans pulselab/config.py (threshold_v=0.25, min_gap_s=0.05, band=None), la dataclass Run dans pulselab/io.py, faites que load_run renvoie un Run construit à partir de pathlib.Path, et utilisez logging (logger = logging.getLogger(__name__)) au lieu de print dans io.py.
Règles : ne touchez pas tests/golden/ ; aucune nouvelle dépendance ; n'affaiblissez aucune assertion ; si un test doit changer, dites-le-moi d'abord. Après le changement, lancez python -m pytest -q et montrez le résultat. Arrêtez-vous après cet incrément.
```

---

## TP 2.2 : Tests avancés : score de mutation, cas limites, propriétés

*Module 5 · Utiliser des agents IA pour des tâches complexes (2/3)*

### 2.2.2 Demandez un plan de test visant les survivants

**Mode :** PLAN, CHAT

```text
Ces mutants ont survécu à ma suite de tests (python scripts/mini_mutation.py) :
M2 pulselab/spectrum.py: freqs[1] - freqs[0] -> freqs[1] + freqs[0]
M3 pulselab/spectrum.py: (freqs >= fmin) & (freqs <= fmax) -> (freqs > fmin) & (freqs <= fmax)
M4 pulselab/spectrum.py: if not fmin < fmax -> if not fmin <= fmax
M9 pulselab/peaks.py: (mid > thr) -> (mid >= thr)
M11 pulselab/fit.py: (t_peaks[-1] - t_peaks[0]) or 1.0 -> ... or 2.0
Plan uniquement. Pour chaque mutant, donnez SOIT un test concret (entrée, valeur attendue, pourquoi il échoue sur le mutant) SOIT une preuve qu'il est équivalent. Tests uniquement : ne modifiez pas le source. Données aléatoires avec graine fixée uniquement.
```

### 2.2.4 Tests basés sur les propriétés

**Mode :** EDIT, AGENT

```text
Écrivez des tests par propriétés dans tests/test_properties.py avec hypothesis (max_examples=50, deadline=None). Ignorez tout le module avec pytest.importorskip si hypothesis n'est pas installé.
Propriété 1 (remove_offset) : pour tout tableau de flottants finis de longueur >= 2 avec des valeurs dans [-1e3, 1e3], l'entrée n'est pas modifiée, la moyenne du résultat est ~0 (tolérance relative à l'échelle des données) et l'appliquer deux fois donne le même résultat.
Propriété 2 (dominant_frequency) : pour toute fréquence entière f dans [2, 200] Hz, fs = 1000 Hz, durée 4 s, toute amplitude dans [0.1, 5] sur un offset constant, le résultat est égal à f à 0.3 Hz près.
Propriété 3 (find_pulses) : pour tout tableau de flottants de longueur 3 à 400 avec des valeurs dans [-2, 2], les indices sont croissants, des indices consécutifs diffèrent d'au moins int(min_gap_s * fs), chaque échantillon renvoyé est au-dessus du seuil, et les premier et dernier échantillons ne sont jamais renvoyés.
Tests uniquement : ne changez pas le source. Lancez python -m pytest -q et montrez le résultat.
```

*Prompt de référence rédigé pour ce support (la fiche de TP ne donne qu'un scaffold pour cette étape).*

---

## TP 2.3 : Mini-atelier d'orchestration multi-agents

*Module 5 · Utiliser des agents IA pour des tâches complexes (3/3)*

### 2.3.1 Écrivez trois briefs : briefs A et C (le brief B figure à l'étape 2.3.2)

**Mode :** HUMAN

```text
BRIEF A (explorateur, lecture seule)
Objectif :          écrire docs/ARCHITECTURE.md (60 lignes maximum) : modules, flux de données d'un fichier CSV jusqu'au tableau de synthèse, points d'entrée, et 3 risques, avec références de fichiers.
Contexte :          projet Python pulselab (NumPy/SciPy/pandas). Lisez le code ; ne l'exécutez pas et ne le modifiez pas.
Fichiers autorisés : docs/ARCHITECTURE.md (à créer) uniquement.
Hors périmètre :    tous les autres fichiers.
Livrable :          le fichier.
Vérification :      chaque module et chaque fonction que vous citez existe (ouvrez le fichier). Rapportez en 10 lignes maximum : ce que vous avez écrit et quels risques vous avez choisis.

BRIEF C (implémenteur)
Objectif :          ajouter write_json(rows, path) dans un nouveau module pulselab/export.py.
Contexte :          rows est la liste de dicts produite par pulselab.report.analyze_folder. Les valeurs peuvent être str, int, float, NaN ou des scalaires numpy.
Contraintes :       bibliothèque standard uniquement ; NaN s'écrit null ; les scalaires numpy sont pris en charge (conversion avec .item()) ; JSON strict (pas de jeton NaN) ; indent=2 ; le fichier se termine par un retour à la ligne.
Fichiers autorisés : pulselab/export.py et tests/test_export.py (nouveau). Hors périmètre : report.py, la CLI, les fichiers golden.
Tests :             NaN devient null ; les scalaires numpy sont pris en charge ; la sortie est du JSON strict valide qui se termine par un retour à la ligne ; liste vide.
Vérification :      python -m pytest -q. Rapportez en 10 lignes maximum.
```

*Prompt de référence rédigé pour ce support (la fiche de TP ne donne qu'un scaffold pour cette étape).*

### 2.3.2 Lancez les trois sous-agents isolément

**Mode :** AGENT, CHAT

```text
BRIEF B
Objectif : ajouter fit_decay_with_error(t_peaks, heights) -> (tau, tau_err) à pulselab/fit.py.
Contexte : projet Python/SciPy pulselab. fit_decay ne renvoie actuellement que tau en ajustant a*exp(-t/tau) avec scipy.optimize.curve_fit. tau_err doit être l'incertitude à 1 sigma sqrt(pcov[1,1]). Renvoyer (nan, nan) quand l'ajustement est impossible (aucune impulsion, trop peu de points). fit_decay doit conserver son comportement (elle peut appeler la nouvelle fonction). Les temps sont en secondes.
Fichiers autorisés : pulselab/fit.py et tests/test_fit_uncertainty.py (nouveau). Hors périmètre : tout le reste, en particulier report.py et les fichiers golden.
Tests : sur des données bruitées avec un tau connu, le vrai tau est à moins de 3 sigma ; un bruit plus fort donne un tau_err plus grand ; une entrée vide donne (nan, nan) ; fit_decay est égal à la première valeur.
Vérification : python -m pytest -q. Rapportez en 10 lignes maximum.
```

---

## TP 2.4 : Conventions d'équipe : fichier d'instructions, modèles de prompts, charte, checklist de revue

*Module 6 · Intégrer l'IA dans le workflow de votre équipe*

### 2.4.1 Fichier d'instructions pour le projet

**Mode :** CHAT, AGENT, HUMAN

```text
Rédigez un fichier d'instructions de projet pour ce dépôt (40 lignes maximum) destiné aux assistants IA et aux nouveaux collègues. Incluez : les commandes (installation, tests, lancer l'analyse, contrôle par mutation), l'organisation de pulselab/, les conventions scientifiques (unités dans les noms, le SNR en dB est un rapport d'amplitudes donc 20*log10, ne jamais modifier les tableaux d'entrée en place, préférer NumPy vectorisé), et les règles de changement (tests pour les changements numériques, tests/golden mis à jour uniquement de façon délibérée, ne jamais affaiblir un test existant, aucune nouvelle dépendance sans demander). N'incluez que ce qui ne peut pas être deviné à partir du code.
```

---

## TP 2.5 : Automatiser le cycle de développement : hook, brouillon de CI, bot de revue

*Module 7 · Automatiser le cycle de développement avec l'IA*

### 2.5.2 Implémentez `tools/precommit.py` (un script, testable)

**Mode :** AGENT, EDIT

```text
Écrivez tools/precommit.py, un hook pre-commit sans dépendance tierce (bibliothèque standard Python uniquement).
Contrôles bloquants, dans l'ordre : (1) scan de secrets sur le diff indexé (lignes ajoutées uniquement) avec des regex pour les affectations api_key/secret/token/password à de longues chaînes littérales et pour les en-têtes de clés privées ; (2) python -m compileall -q pulselab scripts tests ; (3) python -m pytest -x -q.
Étape consultative, uniquement si tous les contrôles bloquants ont réussi et si la variable d'environnement PULSELAB_AI_REVIEW_CMD est définie : lancer cette commande (shlex.split) avec le diff indexé sur stdin (tronqué à 20000 caractères), afficher sa sortie standard comme conseil. Elle ne doit JAMAIS bloquer le commit : en cas de code de sortie non nul, de timeout (variable d'environnement PULSELAB_AI_TIMEOUT, 60 s par défaut) ou si la commande ne peut pas démarrer, afficher un avertissement d'une ligne et continuer.
Ajoutez --install qui écrit .git/hooks/pre-commit (un script shell lançant python tools/precommit.py).
Testez ensuite ces six scénarios dans un dépôt git temporaire et montrez la sortie de chacun : commit propre ; test cassé ; secret dans un fichier indexé ; conseil IA affiché ; commande IA qui se termine avec le code 3 ; commande IA plus lente que le timeout.
```

---

## Aussi dans ce dépôt

- `templates/` : versions réutilisables de ces prompts (`templates/prompts/`), fichiers d'instructions, permissions, agents, skills et commandes pour Kilo Code.
- `Bonnes_Pratiques_Codage_IA.md` : le mémo de bonnes pratiques.
