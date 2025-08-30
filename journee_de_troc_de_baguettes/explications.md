# Journée de troc de baguette

À Pourdlard, une journée d'échange de baguette est organisée. Cependant, les élèves ne peuvent pas échanger leurs baguettes n'importe comment, en effet, n'oublions pas que c'est la baguette qui choisi son sorcier ou sa sorcière mais pas l'inverse !

Pour cela, Ollivander nous a fourni une liste de tous les échanges possibles : [liste](./src/input.txt).

Sur chaque ligne est indiqué un échange possible. Ainsi, sur la première ligne Killian et Lilian peuvent échanger **mutuellement** leurs baguettes.

Le but de l'exercice est de trouver la combinaison d'échanges à faire pour faire en sorte que chaque élève échange exactement 1 fois sa baguette.

Exemple :

Si la liste d'entrée était :

```
Harry Dean
Harry Pansy
Dean Hannah
Colin Hermione
Harry Seamus
Colin Hannah
Hannah Ron
Dean Colin
Hannah Seamus
Ron Pansy
```

Alors, les échanges à faire serait :

```
Harry Dean
Colin Hermione
Hannah Seamus
Ron Pansy
```

Le format de la solution attendu corresponds à la séquences des prénoms deux à deux, simlement séparés par des espaces. Ainsi, la solution serait :

```
Harry Dean Colin Hermione Hannah Seamus Ron Pansy
```

## Idées

Le problème semble plus complexe qu'il n'y parait. Une solution brut force est sans doute possible mais ne parait pas optimale, ça serait sans doute un peu comme chasser une mouche au lance roquettes.

Ma première idée (mais qui ne fonctionne peut être pas) :

Pour valider ou non un échange entre A et B, il faudrait récupérer l'ensemble des autres échanges où A ou B apparaissent. Appelons cet ensemble E. Dans cet ensemble E, il faudrait récupérer tous les prénoms des autres élèves (c'est à dire autre que A et B). Appelons cette liste de prénoms L. Pour chaque prénom dans L, il faudrait voir s'il existe un autre échange qui existe faisant intervenir L non compris dans E. Si c'est le cas, on pourrait valider notre échange initial, sinon non.
