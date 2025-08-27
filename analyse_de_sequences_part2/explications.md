# Analyse de séquences 2/2

Cet exercice est une suite de l'exercicie "Analyse de séquences 1/2".

On retrouve des séquences d'ARN composées de 4 bases nucléiques différentes : A, C, G et U.

Pour rappel :

```
A -> A
C -> C
G -> G
U -> U
R -> A ou G
Y -> C ou U
K -> G ou U
M -> A ou C
S -> C ou G
W -> A ou U
B -> non A
D -> non C
H -> non G
V -> non U
N -> A ou C ou G ou U
```

Dans cet exercice, nous avons un [fichier](./src/input.txt) d'entrée qui contient sur la première ligne une description de séquence d'ARN et en-dessous, plusieurs centaines de séquences d'ARN composées uniquement de A, C, G et U.

Le but est de trouver parmi ces séquences, le nombre qui correspondent bel et bien à la description de la première ligne.

## Idées

Je vais ouvrir le fichier input.txt et récupérer toutes les séquences qu'il contient dans une liste.

Ensuite je vais créer une fonction qui prendra 2 séquences en argument A et B. La fonction retournera True si B corresponds bien à la description A et False sinon.

Ensuite je bouclerais sur tous les éléments de ma liste des séquences (en omettant bien la primère car ce sera la description de la 1ère ligne) et ferais appel à ma fonction sur chacune pour la comparer à la description de la 1ère ligne.

Je créerais au préalable un compteur (une simple variable) que j'incrémenterai à chaque True de ma fonction et qui me permettra donc d'obtenir le nombre de séquences valides.

## Résolution

J'ai crée un dictionnaire **letters** qui associe à que lettre une liste des potentielles lettre qu'elle symbolise.

J'ai crée une fonction **check_sequence** qui prends en entrée une description (donc toujours la séquence de la 1ère ligne du fichire) et une séquence à vérifier. La fonction retourne True si la description correponds bien à la séquence et False sinon.

J'ai ensuite ouvert et récupérer les séquences du fichier d'entrée dans une liste en faisant bien attention d'enlever les potentiels symboles de retour à la ligne **'\n'** avec la fonction rstrip().

J'ai ensuite initialiser le compteur **valid_sequences** à 0.

Enfin, j'ai boucler sur les séquences de la liste en faisant appel à **check_sequence** et en incrémentant de 1 **valid_sequences** lorsque la fonction retourne True.

Le nombre de bonne séquences est 235.