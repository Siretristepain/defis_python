# Tips git

À la création du dépôt, je n'avais pas de fichier .gitignore .

J'ai donc travaillé, fais des commit et des push sans rien masqué.

Cela fait que j'avais mes dossier __pycache__ visibles sur le dépôt distant.

Pour palier à cela, j'ai créer un .gitinore à la racine du dépôt dans lequel j'ai indiqué :

```
__pychache__/
```

Grâce à cela, tous les dossiers de ce type seront ignorés.

Le problème, c'est que les anciens dossiers __pycache__ du dépôt sont déjà suivis par git.

Il a donc fallu les retirer de la liste des fichiers suivis.

Voici une capture d'écran de la manipulation :

![image_terminal](/utile/src/pycache_folder_git.png)

Au début, on voit que mon git status affiche les modifications dans le __pycache__ de utile.

Ensuite, la commande :

```
git rm --cached -r *.pyc
```

permet de retirer tous les fichier .pyc de la liste des fichiers suivis par git.

De fait, lorsque je refais git status, les modifications du __pycache__ ne sont plus visibles car cette fois git voit dans le .gitignore que les fichiers __pycache__ ne doivent pas être suivis et qu'aucun ne l'est déjà.
