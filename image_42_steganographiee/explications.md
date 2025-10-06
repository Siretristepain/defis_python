# Image 42 stéganographiée

Dans cette exercice, on doit retrouver un message dissimulé dans une image.

En effet, certains pixels sont "spéciaux". Il s'agit des pixels qui vérifie la règle suivante :

```
16 x R + 4 * V + B = X où X est divisible par 42
```

Normalement, si l'on révèle tous ces pixels, un message indiquant un lieu doit apparaître.

## Résolution

La première idée qui me vient en tête en lisant cet exercice est de créer un masque à appliquer ensuite sur l'image pour révéler tous les pixels vérifiant la règle ci-dessus.

Un masque est un "tableau conditionnel" a appliqué sur un tableau et qui retourne True ou False.

L'idée c'est de faire un masque qui vérifie si un pixel respecte la règle ou non.

On obtiendra donc un tableau de booléen dans lequel tous les True seront les pixels suivant la règle et False les pixels ne suivant pas la règle.

On aura juste a afficher notre masque pour voir le message.

Voici le message obtenu :

```
Conseils aux extraterrestres à New York :
Posez-vous n'importe où, à Central Park, où vous voudrez.
Personne ne s'en souciera, si tant est qu'on vous remarque.

Un tuyau pour survivre :
....
```
