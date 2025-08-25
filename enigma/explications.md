# Enigma

La machine énigma était une machine à chiffrer des messages durant la seconde guerre mondiale.

Dans ce problème, le fonctionnement de la machine est simplifiée mais l'idée reste la même.

La machine est composée de plusieurs rotors et d'un réflecteur.

Dans l'exercice, on prends une machine composée de 3 rotors et d'un réflecteur.

Pour simplifier les explications, on ne prendre pas des lettres mais des chiffres de 0 à 3.

Voici le schéma de fonctionnement de la machine :

![enigma_schema](/enigma/src/enigma.png)

L'information à coder rentre par le rotor le plus à droite et parcours le chemin vers la gauche jusqu'au réflecteur et repart vers la droite pour ressortir par le rotor de droite. 
Par exemple, si un 0 rentre à droite, on voit en suivant le chemin qu'il ressort sous forme de 1.

Chaque rotor modifie un chiffre en un autre et le réflecteur échange les chiffres par paires.

Par exemple, le rotor 1 envoie le 0 sur 1, le 1 sur 3, le 2 sur 0 et le 3 sur 2.

On peut symboliser ceci comme cela :

```
0 -> 1
1 -> 3
2 -> 0
3 -> 2
```

Pour simplifier, on peut dire que le rotor 1 est sur la configuration 1302.

Sur le même principe, le rotor 2 est sur la configuration 2301, le rotor 3 est sur la configuration 0312 et le réflecteur est sur la configuration 1032.

À chaque codage d'une lettre, le rotor de droite (rotor 1) tourne d'un cran, ce qui modifie sa configuration. Ainsi, après avoir codé une lettre, le rotor 1 passe en configuration 3021 (puis en 0213 puis en 2130,...).

À chaque révolution (tour complet) du rotor 1, le rotor 2 tourne d'un cran.

À chaque révolution du rotor 2, le rotor 3 tourne d'un cran.

Seul le réflecteur ne tourne **jamais**.

**Important** : Le réflecteur ne tourne jamais. Ainsi, sa configuration reste la même du début à la fin du processus de cryptage du message. C'est grâce à lui que pour décrypter un message, il suffit de replacer les rotors dans la position initiale et de refaire le processus de cryptage sur le message crypté pour le décrypter.

## Objectifs

En entrées du problème, on a un message crypté et les positions initiales des rotors 1, 2 et 3 ainsi que celle du réflecteur.

L'objectif est de déchiffrer le message.

Voici les données d'entrée :

- rotor 1 : USKFEVIYWZTXAGCQNBMODHLR_PJ.
- rotor 2 : XHVNDCRZQPSB_OKT.LUWGJMEFAIY
- rotor 3 : AWYJLFOV_TIQMZERXUSDKBPNGC.H
- réflecteur : .XF_JCYIHELKNMPOZTWRVUSBGQDA
- message crypté : _ZP_KMSOXEPOKXWZGBWWDNLAGJYQUI.HUHNGVQKOJNGJ.URCEXJQIPADGMW.VQDVBLNHWV.VPVRWGTTPI_UJACKLSFWBUUQZYTNOLEP.JHYLXFTBNYGKOBKK_UGOT_PXVVSULWWAMKBDWHZNZUNX_UICRW.YLMLGDPARIFKJAQYQL.SHUFWJTTZPLPQLBUDFZQVVRCWXQEWPPSDX

Il semble que ce code ait été obtenu avec une énigma comportant 28 symboles : les 26 lettres de l'alphabet, le tiret du bas et le point, dans cet ordre : ABCDEFGHIJKLMNOPQRSTUVWXYZ_. .

## Idées de résolution

Je pense représenter le système de la machine par une liste de listes :

```
[ [reflecteur], [rotor3], [rotor2], [rotor1] ]
```

Je vais ensuite créer une fonction qui permet de faire tourner d'un cran un rotor. La fonction prendra la position du rotor au temps T en entrée et retournera la position du rotor au temps T+1.

Ensuite je placerais tous les rotors sur les bonnes positions (celles données en entrées).

Ensuite, je bouclerais sur chaque caractères du message crypté en faisant tourner les rotors quand ils le faudra, sachant que :

- rotor 1 : tourne à chaque itérations (à chaque i).
- rotor 2 : tourne toutes les 5 itérations (c'est à dire à chaque révolution du rotor 1) --> quand i % 5 == 0 .
- rotor 3 : tourne toutes les 25 itérations (c'est à dire à chaque révolution du rotor 2 ou encore toutes les 5 révolutions du rotor 1). --> quand i % 25 == 0 .
