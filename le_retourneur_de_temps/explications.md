# Le retourneur de temps

Dumbledore a donné à Hermione le remonteur de temps afin de pouvoir suivre tous ses cours.

Lorsque l'on fait un tour avec le remonteur de temps, on remonte de 2 minutes dans le passé. Donc si on fait 2 tour on remonte de 4 minutes, si on fait 3 tour 6 minutes, ...

Il existe cependant une petite particularité pour éviter de remonter trop loin dans le passé : si la somme de tous les chiffres qui composent le nombre de minutes est divisible par 7, alors au prochain tour, au lieu de remonter de 2 minute dans le passé, on **enlève** 7 minutes (donc vers le présent !).

```
 nombre    durée voyage
de tours    en minutes
    1           2 
    2           4 
    3           6 
    4           8  
    5          10  
    6          12  
    7          14  
    8          16  <-- 
    9           9  
   10          11  
   11          13  
   12          15  
   13          17  
   14          19  
   15          21  
   16          23  
   17          25  <--
   18          18  
```

Pour valider ce défis, il faut indiquer le nombre de minute maximum que l'on peut remonter dans le passé.

## Idées

Ma première idée consiste à créer une fonction qui simule le fait de tourner le remonteur de temps d'un cran et qui gère le cas particulier.

Ensuite je ferais simplement une boucle pour essayer 100 tours pour voir si le nombre de minutes se stabilise. Si ce n'est pas le cas, je referais la boucle sur 500 tours, puis 1000, etc ... Dans la limite du raisonnable.

Si ça ne suffit pas, je réfléchirais à une autre solution.

## Résolution

La solution est : 59 minutes.