# Le seul et unique

Nous avons en entrée une [liste de pokémon](./src/liste.txt) avec leurs coordonnées dans le plan.

Le but de l'exercice est simplement de retourner les coordonnées du pokémon qui n'apparait qu'une seule fois dans la liste.

Par exemple, si les coordonnées du pokémon unique sont -30, 67, la réponse sera : **-30, 67**.

## Résolution

Voici le fil directeur des idées pour la résolution de ce problème :

1) Ouvrir le fichier d'entrée et récupérer le contenu de chaque ligne (l'idée est d'obtenir une liste où chaque élément corresponds au contenu d'une ligne).
2) Créer une liste de tous les noms des pokémons (pas une liste de chaque noms unique mais une liste reprenant chaque lignes).
3) Créer une fonction qui permet de retrouver l'élément unique dans une liste donnée en entrée.
4) Via la fonction précédente, trouver le pokémon unique.
5) Parcourir les lignes du fichier à la recherche de la ligne mentionnant le pokémon unique et afficher les coordonnées correspondantes.

**Point d'intérêt** : Pour le point 3, j'ai choisi de créer une méthode récursive car je trouvais que l'exercice s'y prêtait bien, et cela me permet de me familiariser d'avantage avec ce type de fonction que j'ai toujours un peu de mal a appréhender.
