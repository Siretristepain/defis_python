# Les dragées surprises

Rappel énoncé :

Harry, Ron et Hermione veulent se partager les 12 dragées surprises qu'ils leur reste. Ils en auront donc 4 chacun.

Hermione propose de les mélanger selon une méthode particulière : les disposer en cercle puis faire le tour du cercle de 5 en 5 et à chaque fois intervertir la dragée avec la précédente.

La position de départ est la suivante : **A B E C G F M O H P S V** (chaque lettre corresponds à un parfum).

Au premier tour, on inverse donc G avec C, ce qui donne : **A B E G C F M O H P S V**.

Au second tour, on inverse donc P avec H, ce qui donne : **A B E G C F M O P H S V**.

Et ainsi de suite... Après le mélange, Hermione aura les 4 premières dragées. Elle souhaiterais avoir les dragées **A E G H** (peu importe l'ordre). Au bout de combien de permutation aura t'elle ces dragées ?

## Résolution

Avant toute chose, on voit qu'il vas falloir permuter des éléments dans une liste. J'ai donc commencé par écrire une fonction **inverse_with_previous** qui prends 2 paramètres en entrées : a (list) et b (int). a corresponds à la liste contenant tous les éléments et b l'indice de l'élément de l'on souhaite inverser avec le précédent.

Maintenant, on voit clairement que l'on va devoir faire un nombre d'itération inconnu, ce qui laisse penser que l'on va utiliser une boucle while. La boucle while étant assez risquée (boucle infini), je rajoute une condition pour mettre fin à la boucle après un certain nombre d'itération arbitraire. Si jamais le résultat n'est toujours pas correct après ce nombre d'itération, je pourrais l'augmenter manuellement et ainsi garder le controle sur le nombre d'itération maximales.

Pour la résolution à proprement parler, je définis 2 variables nb_tour et i (indice de l'élément à inverser avec le précédent) puis je fais une boucle while.
A chaque tour de boucle, je permute l'élément d'indice i avec l'élément d'indice i-1 dans la liste des dragées.
Je vérifie ensuite si les dragées **A E G H** sont les 4 premières. Si c'est le cas, je stoppe la boucle while et j'affiche le résultat.

La seule difficulté de l'exercice réside dans le fait que la liste de dragées se "répète à l'inifi". C'est à dire qu'après le dernier élément, on retombe sur le premier. Ainsi, si on a i=0, on doit inverser la première dragée avec la dernière. Pour cela, je fais i % 12 à chaque tour de boucle. L'opérateur % permet de retourner le reste de la division Euclidienne et m'assure ainsi de toujours avoir un i entre 0 et 11.
