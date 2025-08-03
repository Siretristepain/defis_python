# Le message du Vortex Zephyr

L'exercice consiste à décoder un message chiffré à l'aide d'un chiffrement de César variable.

Pour rappel, un chiffrement de César variable consiste à prendre 2 nombres entiers :
- décalage initial.
- incrément.

Pour chiffrer la première lettre de notre phrase, on prends son indice dans l'alphabet et on lui ajoute le décalage initial.
Ensuite, pour la deuxième lettre, on prends le décalage total de la lettre précédente auquel on ajoute l'incrément.
Et ainsi de suite.

Ainsi, pour n'importe quelle lettre de rang n, son décalage total corresponds au décalage de la lettre de rang n-1 auquel on ajoute l'incrément.

On peut donc poser le problème sous forme d'équation :

```
À chaque lettre A est associé une "image" A'.

Le décalage entre A et A' vaut X.

On peut alors poser :

X = D + n x I

Avec :

- X : décalage total
- D : décalage initial
- n : l'indice de la lettre en question
- I : l'incrément
```

Ainsi, pour la première lettre, n vaut 0, ce qui simplifie X en X = D.
Pour la seconde lettre, n vaut 1 donc X = D + I.
Pour la troisième lettre, X = D + 2 x I.
Etc...

## Résolution

Malheureusement, on ne peut pas résoudre mathématiquement notre équation car nous avons un système à 1 équation et 2 inconnues. En effet, on cherche la valeur de X et on ne connais ni D (le décalage initial) ni I (l'incrément). Or, lorsqu'un système à d'avantage d'inconnues que d'équations, on ne peut pas le résoudre simplement.

La solution qui m'est venue est une solution **brut force**.

L'idée est de se dire qu'il n'y a finalement que 26 possibilités de valeur de décalage initial. En effet, si on dépasse 26 (qui corresponds à la lettre Z), on recommence l'alphabet par le début : A, B, C, ... .

Ainsi, même si on choisi un décalage initial de 1425, ça revient au même que de prendre un décalage initial de 21 car 1425 % 26 = 21.

Ensuite, sur le même principe exactement, il y a 26 possibilités de valeur d'incrément (pour les mêmes raisons que le décalage initial).

Ainsi donc, pour chaque valeur de décalage initial, il faudrait tester les 26 possibilités d'incrément.

Cela fait un total de 26 x 26 = 676 combinaisons possibles, ce qui semble bien raisonnable pour une résolution brut force.

J'ai donc créer une fonction **decryptage** qui permet de décrypter un texte qui prends en argument le texte à traduire (str), un décalage initial (int) et un incrément (int).

Ensuite, j'ai créer une fonction **resolution** qui fait les boucles sur les 676 possibilités de combinaisons décalage inital / incrément et qui fait appel à **decryptage** à chaque fois. À chaque itération, la fonction écrit dans le fichier **output.txt** le message traduit. On peut chercher dedans ensuite en faisant des recherche de mot existant.

**Resultat** : On voit dans le fichier output.txt que lorsque le décalage initial vaut 7 et que l'incrément vaut 5, la phrase traduite donne : "ATTENTION AU FUTUR REDACTEUR EN CHEF DU GUIDE GALACTIQUE NOMME STAGYAR CEST UN DANGEREUX DESEQUILIBRE".

## Point d'attention

Lorsque j'ai lancé mon script la 1ère fois, j'ai eu une erreur :

```
TypeError: sequence item 8: expected str instance, bool found
```

En cherchant l'erreur avec le mode debug, j'ai compris que cela avait lieu dans ma fonction **decryptage** lorsque **true_position** valait 0. En effet, **true_position** est calculée comme la soustraction entre l'indice de la lettre cryptée - le décalage. Il est donc possible que la soustraction retourne 0.
C'est pour ça que dans le code j'ai ajouté la structure :

```
if true_position == 0:
    true_position = 26
```

**NB** : Le code que j'ai fournis n'est évidemment pas optimal, on constate pas mal de répétition etc mais il fonctionne et me semble assez lisible.
