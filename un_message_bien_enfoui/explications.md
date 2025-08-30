# Un message bien enfoui

Nous avons un fichier d'entrée : [fichier](./src/input.txt) qui contient des coordonnées GPS sur chaque ligne.

On soupçonne qu'une message (plus précisément un horaire) soit caché au travers de ces coordonnées.

Pour cela, on doit conserver uniquement les coordonnées pour lesquelles la somme des digits de la latitude est divisible par 13 et idem pour la longitude.

Ensuite, on doit regarder sur Google Maps si une lettre ou un chiffre n'est pas caché dans le paysage.

## Résolution

J'ai créer une fonction **check_div_by_13** qui prends en entrée une chaîne de caractère et qui fait la somme des digits qui la compose. La fonction retourne True si le total est divisible par 13, False sinon.

Ensuite, j'ouvre le fichier, récupère le contenu de chaque ligne et boucle dessus.

Pour chaque ligne, je dissocie la latitude et la longitude et j'appelle **check_div_by_13** sur chaque. Si les 2 retournent True, j'ajoute la ligne de coordonnées à ma liste **keep_lines**.
