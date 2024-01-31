# IA41

IQ Puzzler Pro est un projet réalisé en cours d'intelligence artificielle à l'automne 2022.

Le défi : réaliser un algorithme capable de compléter une grille avec des pièces proposées, de sorte à ce que la grille soit complètement pleine. 
Nous avons voulu rajouter au projet la possibilité de générer aléatoirement la grille et les pièces pour la compléter.

Le programme permettant de résoudre la grille est un <strong>algorithme de backtracking</strong>.
L'algorithme prend une pièce disponible et la place dans le premier endroit où celle-ci rentre en fonction des pièces déjà placé.
Lorsqu'une pièce ne peut rentrer à aucun endroit, l'algorithme retourne à la pièce précédente et teste une nouvelle configuration. 
