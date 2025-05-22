# Projet SUPINFO - Mini-jeux de stratégie combinatoire en Python

## Contexte

- Projet individuel sans soutenance.
- Rendu sous forme d’archive `.zip` contenant tout le code source.
- Plagiat interdit, sanction : zéro.
- Qualité du code importante (pas de variables globales, structure claire).
- Documentation expliquant les algorithmes jointe pour chaque jeu.
- Structure de code imposée, respect obligatoire sous peine d’ajournement.

## Objectif

Programmer en Python deux jeux de stratégie combinatoire abstraits :

1. Snort  
2. Dodgem

---

## 1 - Snort

### Règles

- Plateau carré n×n vide au départ.
- Joueur 1 : pions blancs (1), joueur 2 : pions noirs (2).
- À tour de rôle, poser un pion sur une case vide qui n’est pas orthogonalement adjacente à un pion adverse.
- Le joueur qui ne peut plus poser de pion perd.

### Fonctions à implémenter

- `newBoard(n)` : crée un plateau vide.
- `displayBoard(board, n)` : affiche le plateau.
- `possibleSquare(board, n, player, i, j)` : vrai si placement possible en (i, j).
- `selectSquare(board, n, player)` : saisie valide des coordonnées.
- `updateBoard(board, player, i, j)` : place un pion en (i, j).
- `again(board, n, player)` : vrai si le joueur peut encore jouer.
- `snort(n)` : gère une partie complète.

---

## 2 - Dodgem

### Règles

- Plateau carré n×n.
- Joueur 1 place n−1 pions sur la dernière ligne (sauf première case).
- Joueur 2 place n−1 pions sur la première colonne (sauf dernière case).
- À tour de rôle, déplacer un pion orthogonalement vers une case vide.
- Joueur 1 peut déplacer vers haut, gauche, droite.
- Joueur 2 peut déplacer vers haut, bas, droite.
- Pion sorti du plateau est retiré définitivement.
- Un joueur gagne s’il fait sortir tous ses pions ou bloque ceux de l’adversaire.

### Fonctions à implémenter

- `newBoard(n)` : crée plateau initial avec pions positionnés.
- `displayBoard(board, n)` : affiche le plateau.
- `possiblePawn(board, n, directions, player, i, j)` : vrai si le pion en (i, j) peut être déplacé.
- `selectPawn(board, n, directions, player)` : saisie valide d’un pion.
- `possibleMove(board, n, directions, player, i, j, m)` : vrai si déplacement possible dans la direction m.
- `selectMove(board, n, directions, player, i, j)` : saisie de la direction.
- `move(board, n, directions, player, i, j, m)` : effectue le déplacement.
- `win(board, n, directions, player)` : vrai si joueur a gagné.
- `dodgem(n)` : gère une partie complète.

---

## Notes

- Contrôler toutes les saisies utilisateur.
- Pas de variables globales.
- Code clair, bien structuré.
- Joindre une documentation expliquant les algorithmes pour chaque jeu.

---

Bonne programmation.
