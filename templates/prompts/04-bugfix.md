# Modèle de prompt : correction de bug (v1.0)

À utiliser avec : un agent de code (Kilo Code : *Code*), une fois la cause connue.

## Objectif
Corrigez : {{bug_summary}}. Cause racine (trouvée et confirmée par moi) : {{root_cause}}.

## Contexte
- Stack : {{language_and_version}}, {{framework}}. Fichiers concernés : {{files}}.
- Reproduction (commande ou test) : {{repro}}. Attendu vs obtenu : {{expected}} / {{actual}}.

## Contraintes
- Écrivez un test en échec qui reproduit le bug AVANT de changer le code.
- Le plus petit changement possible, à la cause (pas un contournement chez l'appelant). Ne touchez pas aux fichiers sans rapport. Ne modifiez pas les tests existants.
- Si la cause est une convention scientifique (unités, dB, fenêtrage), demandez-moi au lieu de choisir.

## Format
1. Le test en échec. 2. Le correctif sous forme de diff. 3. Deux phrases expliquant pourquoi il supprime la cause.

## Vérification
- Montrez la sortie de la suite de tests. Listez les autres fonctions qui pourraient avoir le même problème, et vérifiez-les avec une recherche.
