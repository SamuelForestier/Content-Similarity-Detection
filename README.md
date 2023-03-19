# Content-Similarity-Detection

## **L'indice de Jaccard :**

L'indice de Jaccard est une mesure de la similarité entre deux ensembles de données. Plus précisément, il mesure la similarité entre deux ensembles en comparant la proportion d'éléments communs aux deux ensembles par rapport au nombre total d'éléments.

L'indice de Jaccard est calculé en divisant le nombre d'éléments communs aux deux ensembles par le nombre total d'éléments dans les deux ensembles. Mathématiquement, cela peut être représenté comme ceci :

J(A,B) = |A ∩ B| / |A ∪ B|

où A et B sont deux ensembles, ∩ représente l'intersection entre les ensembles et ∪ représente l'union entre les ensembles.

Par exemple, si A = {1, 2, 3} et B = {2, 3, 4}, alors l'intersection entre les ensembles est {2, 3} et l'union entre les ensembles est {1, 2, 3, 4}. Par conséquent, l'indice de Jaccard entre les deux ensembles est de :

J(A,B) = |{2,3}| / |{1,2,3,4}| = 2 / 4 = 0.5

## **La distance de Levenshtein :**

La distance de Levenshtein est une mesure de la similarité entre deux chaînes de caractères. Cette mesure est basée sur le nombre minimum d'opérations d'édition nécessaires pour transformer une chaîne en une autre. Les opérations d'édition possibles sont l'insertion, la suppression et la substitution d'un caractère.

Le calcul de la distance de Levenshtein se fait en utilisant une matrice de distances. Cette matrice est remplie en comparant chaque caractère des deux chaînes de départ et d'arrivée. Pour chaque paire de caractères, la matrice contient la distance entre les sous-chaînes correspondantes de la chaîne de départ et de la chaîne d'arrivée.

**Le calcul de la matrice de distances se fait en trois étapes :**

**Initialisation :** La première ligne et la première colonne de la matrice sont initialisées avec des valeurs croissantes, représentant le coût de chaque opération d'édition nécessaire pour transformer une chaîne vide en une sous-chaîne de la chaîne de départ. Par exemple, pour calculer la distance de Levenshtein entre "chat" et "chapeau", les premières lignes de la matrice pour serait :

|   |   | c | h | a | p | e | a | u |
|---|---|---|---|---|---|---|---|---|
|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| c | 1 |   |   |   |   |   |   |   |
| h | 2 |   |   |   |   |   |   |   |
| a | 3 |   |   |   |   |   |   |   |
| t | 4 |   |   |   |   |   |   |   |

Cela signifie qu'il faut un coût de 1 pour insérer le premier caractère "c" dans une chaîne vide, un coût de 2 pour insérer les deux premiers caractères "c" et "h", et ainsi de suite.

**Remplissage de la matrice :** Les cases restantes de la matrice sont remplies en calculant la distance de Levenshtein pour chaque sous-chaîne de la chaîne de départ et de la chaîne d'arrivée.

**Retourner la distance :** La distance de Levenshtein entre les deux chaînes est la valeur située dans la dernière case de la matrice.

|   | c | h | a | p | e | a | u | u |
|---|---|---|---|---|---|---|---|---|
|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| c | 1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| h | 2 | 1 | 0 | 1 | 2 | 3 | 4 | 5 |
| a | 3 | 2 | 1 | 0 | 1 | 2 | 3 | 4 |
| t | 4 | 3 | 2 | 1 | 1 | 2 | 3 | 4 |

La distance de Levenshtein entre "chat" et "chapeau" est donnée par la valeur de la cellule en bas à droite de la matrice, qui est égale à 4. Cela signifie qu'il faut effectuer au minimum 4 opérations d'édition (substitution et insertion) pour transformer "chat" en "chapeau".

## **La plus longue sous-séquence :**

Le calcul de la plus longue sous-séquence (LCS pour "Longest Common Subsequence") entre deux chaînes de caractères se fait en cherchant la plus longue séquence de caractères qui est commune aux deux chaînes, sans nécessairement être consécutive.

Le calcul se fait en utilisant une matrice. Chaque case de la matrice représente la longueur de la plus longue sous-séquence commune pour une partie des deux chaînes considérées. La matrice est remplie de haut en bas et de gauche à droite, en utilisant une relation de récurrence qui utilise les valeurs des cases précédentes.

**Le remplissage de la matrice se fait de la manière suivante :**

On initialise la première ligne et la première colonne de la matrice à 0.

**On remplit le reste de la matrice en utilisant la relation de récurrence suivante :**

Si les caractères à l'indice i-1 de la première chaîne et j-1 de la deuxième chaîne sont identiques, alors la valeur de la case (i, j) est égale à la valeur de la case (i-1, j-1) + 1.

Sinon, la valeur de la case (i, j) est le maximum entre la valeur de la case (i, j-1) et la valeur de la case (i-1, j).

La valeur de la case en bas à droite de la matrice est la longueur de la plus longue sous-séquence commune.

Par exemple, pour calculer la LCS entre les chaînes de caractères "ABCD" et "ABED", on remplit la matrice de la manière suivante :

|   |   | A | B | E | D |
|---|---|---|---|---|---|
|   | 0 | 0 | 0 | 0 | 0 |
| A | 0 | 1 | 1 | 1 | 1 |
| B | 0 | 1 | 2 | 2 | 2 |
| C | 0 | 1 | 2 | 2 | 2 |
| D | 0 | 1 | 2 | 2 | 3 |

La LCS entre "ABCD" et "ABED" est de longueur 3 et correspond à la sous-séquence "ABD".

## **Le TF-IDF :**

Le TF-IDF (term frequency-inverse document frequency) est une mesure de l'importance d'un terme dans un ensemble de documents. Cette mesure est utilisée en recherche d'information pour classer les documents en fonction de leur pertinence par rapport à une requête.

**Le TF-IDF est calculé en trois étapes :**

1. Le calcul du TF (term frequency) : cette étape consiste à calculer le nombre de fois qu'un terme donné apparaît dans un document. Le TF est généralement normalisé par la longueur du document pour éviter que les documents plus longs aient un avantage sur les documents plus courts. La formule la plus couramment utilisée pour calculer le TF est :
TF(t,d) = (nombre de fois que le terme t apparaît dans le document d) / (nombre total de termes dans le document d)

2. Le calcul de l'IDF (inverse document frequency) : cette étape consiste à calculer l'inverse de la fréquence d'apparition d'un terme dans l'ensemble des documents. Cette mesure permet de donner plus de poids aux termes qui sont rares dans l'ensemble des documents, et donc plus discriminants. La formule la plus couramment utilisée pour calculer l'IDF est : IDF(t) = log(N / n_t) (N est le nombre total de documents dans l'ensemble) / (n_t est le nombre de documents qui contiennent le terme t)

3. Le calcul du TF-IDF : cette étape consiste à multiplier le TF par l'IDF pour obtenir une mesure de l'importance d'un terme dans un document donné et dans l'ensemble des documents. 

Les termes ayant un TF-IDF élevé pour un document donné sont considérés comme plus importants et pertinents pour ce document. Les termes ayant un TF-IDF faible pour l'ensemble des documents sont considérés comme plus rares et discriminants pour l'ensemble des documents. Le TF-IDF est donc une mesure utile pour l'indexation et la recherche de documents.

## **Word Mover's Distance :**

TODO :