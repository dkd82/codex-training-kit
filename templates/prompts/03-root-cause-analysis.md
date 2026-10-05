# Modèle de prompt : analyse de cause racine (v1.0)

À utiliser avec : un agent en lecture seule (Kilo Code : *Ask*). **Ne demandez pas encore de correctif.**

## Objectif
Trouvez la cause racine de : {{symptom}}. Ne proposez pas encore de correctif.

## Contexte
- Attendu : {{expected}}. Observé : {{observed}}.
- Test en échec ou reproduction : {{repro}}. Sortie : {{paste_the_exact_output}}
- Fichiers pertinents : {{files}}.

## Contraintes
- Aucune modification de code. Classez les hypothèses de la plus à la moins probable.

## Format
Un tableau : hypothèse | pourquoi elle est plausible | une expérience (quelques lignes de Python) qui la confirmerait ou l'infirmerait.

## Vérification
Dites quelle preuve changerait votre classement.
