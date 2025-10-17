# Huile noire

Dans ce problème, nous étudions le comportement d'une suite de cellules. Il existe des cellules blanches (représentées par un 0) et des cellules noires (représentées pas un 1). Ces cellules évolues dans le temps suivant des règles bien définies.

**Les règles d'évolution**:

* 1 1 1 -> 0
* 1 1 0 -> 1
* 1 0 1 -> 1
* 1 0 0 -> 0
* 0 1 1 -> 1
* 0 1 0 -> 1
* 0 0 1 -> 1
* 0 0 0 -> 0

Ces règles indique pour chaque triplet de cellules comment évolue la cellule du milieu. La première règle énonce : pour un triplet de cellules noires, la cellule du milieu devient blanche au pas de temps suivant. La seconde règle énonce : pour un triplet de cellules noire, noire, blanche, la celulle du milieu reste noire au pas de temps suivant.

Les règles donnent en français :

- Une cellule noire entourée de noires devient blanche
- une cellule noire avec une voisine gauche noire et une voisine droite blanche reste noire
- une cellule blanche entourée de cellule noires devient noire
- une cellule blanche avec une voisine noire à gauche et une blanche à droite reste blanche
- une cellule noire avec une voisine de gauche blanche et une voisine de droite noire reste noire
- une cellule noire entourée de blanche reste noire
- une cellule blanche avec une voisine gauche blanche et une voisine noire à droite devient noire
- une cellule blanche entourée de blanches reste blanche

**Important** : on imagine que l'échantillon se referme, c'est à dire que la cellule de gauche de la première cellule est la dernière cellule et que la cellule de droite de la dernière cellule est la première.

Si un échantillon est décrit par la suite de chiffre : 0 1 1 0 1 0 0 on dit que son état est de 52 (c'est sa correspondance en binaire).

La description de l'échantillon en entrée du problème contient 3 valeurs :

- départ : 25794542787624960 -> il s'agit du binaire correspondant à l'état de l'échantillon
- taille : 100 -> nombre de cellule composant l'échantillon
- étapes : 178 -> le nombre de pas de temps à réaliser

## Résolution

Je vais inscrire les règles d'évolution dans un dictionnaire.

Je vais ensuite créer une fonction qui prendra un triplet de cellule en entrée. En sortie, elle donnera la nouvelle valeur de la cellule via le dictionnaire d'évolution.

Ensuite je vais créer une fonction qui simule 1 pas de temps pour la séquence complète. Concrètement, elle prendra une séquence au temps T et elle retournera la séquence au temps T+1.
C'est cette fonction qui sera appelée dans les 178 pas de temps requis dans l'exercice.
Cette fonction fera appelle à la fonction précédent qui donne l'évolution d'une cellule.

Pour le reste, je n'aurais qu'à convertir le nombre donné en entrée représentant la séqence au début en binaire, puis travailler avec, puis la convertir en entier à la fin.

### Step by step

Lorsque je convertis 25794542787624960 en binaire, j'obtiens un nombre binaire de 55 digits. Or je dois avoir 100 cellules. J'en déduis que je dois rajouter 45 fois "0" devant.

Pour reconvertir le binaire final après les 178 pas de temps en entier décimal, il faut rajouter '0b' devant la séquence binaire.
