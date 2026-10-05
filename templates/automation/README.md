# Modèles d'automatisation

| Fichier | Ce que c'est | Statut |
|---|---|---|
| `precommit.py` | Hook pre-commit : contrôles déterministes **bloquants** (scan de secrets, syntaxe, tests rapides) + une revue IA **consultative** qui ne peut jamais bloquer | Testé dans un dépôt git temporaire avec six scénarios (ci-dessous) |
| `REVIEW_CRITERIA.md` | Critères donnés à un relecteur IA ou à un bot de pull request : quoi vérifier, quoi ignorer, format de sortie | Fichier texte |
| `ci-example.yml` | Un brouillon de CI avec un job `tests` qui fait barrière et un job `ai-review` consultatif, désactivé (syntaxe GitHub Actions) | Syntaxe YAML vérifiée ; **jamais exécuté**. À adapter à votre système de CI |

## Principe

**Les contrôles déterministes font barrière ; l'IA conseille.** Une étape IA ne doit jamais décider du code de sortie d'un commit ou d'un build, doit être sans danger en cas d'échec (erreurs et timeouts n'affichent qu'un avertissement), et ne doit pas recevoir plus de données que nécessaire.

## Installer le hook

1. Copiez `precommit.py` vers `tools/precommit.py` dans votre dépôt (le script retrouve la racine du dépôt à partir de son propre emplacement).
2. Modifiez les constantes en haut du fichier : `SOURCE_DIRS` (dossiers dont la syntaxe est vérifiée) et, si besoin, la commande de test.
3. Lancez `python tools/precommit.py --install` : cela écrit `.git/hooks/pre-commit`.
4. Conseil facultatif d'un outil IA : définissez `AI_REVIEW_CMD` avec une commande qui lit le diff indexé sur **stdin** et affiche des commentaires sur **stdout** (utilisez un outil approuvé par l'entreprise), et éventuellement `AI_REVIEW_TIMEOUT` (secondes, 60 par défaut).

## Les six scénarios à rejouer dans un dépôt temporaire

| # | Situation | Attendu |
|---|---|---|
| S1 | commit propre | passe |
| S2 | un test est cassé | commit **bloqué**, test en échec affiché |
| S3 | un fichier indexé contient `API_KEY = "abcd1234efgh5678"` | commit **bloqué**, la ligne est affichée |
| S4 | la commande IA affiche un conseil | conseil affiché, le commit passe |
| S5 | la commande IA se termine en erreur | avertissement affiché, le commit passe |
| S6 | la commande IA est plus lente que le timeout | avertissement affiché, le commit passe |

## Avant de l'utiliser

- Que **reçoit** la commande IA ? (le diff indexé, tronqué à 20 000 caractères.) Pourrait-il contenir des secrets, des résultats non publiés, des données personnelles ou confidentielles ? Où la commande s'exécute-t-elle et où vont les données ? Qui a approuvé l'outil pour ces données ?
- Le scan de secrets se résume à deux expressions régulières simples : il est prévisible mais **n'est pas** un scanner de secrets complet.
