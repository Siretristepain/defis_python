# Analyse de séquences 1/2

Dans ce problème, on étudie des séquences d'ARN décrit par 4 bases nucléiques : A, C, G ou U.

Les séquences d'acides nucléiques sont parfois décrites à l'aide d'autres symboles comme R qui signifie A ou G, Y qui signifie C ou U, ...

Voici la liste complète des symboles :

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

La séquence ACDMR signifie donc :

- Le premier acide nucléique est forcément A
- Le second acide nucléique est forcément C
- Le troisième acide nucléique est A, G ou U
- Le quatrième acide nucléique est A ou C
- Le cinquième est A ou G

Il y a donc 12 séquences possibles qui correspondent à la description ACDMR : ACAAA, ACAAG, ACACA, ACACG, ACGAA, ACGAG, ACGCA, ACGCG, ACUAA, ACUAG, ACUCA, ACUCG .

Le but du problème est de retrouver le nombre de combinaisons possible de séquences d'ARN à partir d'une séquence d'entrée. Plus exactement il faut donner les 5 derniers digits du nombre total de combinaisons.

**La séquence d'entrée** : NDNKCNVNUGYWRGCNABGSNCRACGSHWNNCYBCSNVUAAGDCMNKNYNNBNCGUBHUNRANDGDMDRSYMGSNWHNDNCVCMAMCANWKYRKVMWMKC .

## Idées

Mon idée de résolution consiste à trouver le nombre total de combinaison via une formule, comme pour le nombre de combinaisons avce un cadenas à 4 chiffres.

Avec un cadenas à 4 chiffres, chaque "roue" à 10 possibilités : 0, 1, 2, 3, 4, 5, 6, 7, 8 et 9.

La formule du nombre de possibilités est : n^k avec n le nombre de possibilités par roue et k le nombre de roue.

Ainsi le nombre de possibilités est : 10^4 = 10 x 10 x 10 x 10 = 10 000.

Dans notre cas, je vais faire la même chose :

- Les lettres A, C, G et U n'ont qu'une seule possibilité.
- Les lettres R, Y, K, M, S, W ont 2 possibilités.
- Les lettres B, D, H, V ont 3 possibilités.
- La lettres N a 4 possibilités.

La formule pour trouver le nombre de séquences possibles est donc :

```
2^nb_2 x 3^nb_3 x 4^nb_4

Avec :

- nb_2 : le nombre de lettres ayant 2 possibilités.
- nb_3 : le nombre de lettres ayant 3 possibilités.
- nb_4 : le nombre de lettres ayant 4 possibilités.
```

## Résolution

J'ai fais exactement ce qui est décrit au dessus.
Le nombre de possibilités est : 609847177343522690648871272448 donc la solution est : 72448 .
