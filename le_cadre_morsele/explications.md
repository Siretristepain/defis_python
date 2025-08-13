# Le cadre morselé

L'énoncé du problème est très simple : on sait qu'il y a un message caché dans l'image fournie mais on ne sait pas sous quelle forme. Le but est de retrouvé un prénom.

## Résolution

Etant donné que le problème s'appelle "Le cadre morselé", que l'image représente un Morse et que l'image possède des bandes noires "suspectes", il y a fort à parier que le message soit codé en morse dans les bandes noires.

En chargeant l'image et en faisant apparaitre la matrice 10x10 des premiers pixels qui sont tous censés être noirs (0,0,0), on se rends compte que certains ne sont pas tout à fait noirs (bien que ce soit invisible à l'oeil nu).

J'ai donc crée une fonction **filtre_all_pixel** qui permet de convertir une image en noir et blanc selon cette méthode : si le pixel est (0,0,0) il reste à (0,0,0) sinon il passe sur (255,255,255). C'est à dire que seuls les pixels 100% noirs restent noirs, les autres passent tous 100% blancs.

En affichant l'image obtenue, je vois le message en morse apparaitre :

![image_bordure_morse](/le_cadre_morsele/src/pixel.png)

L'image ci-dessus corresponds au coin inférieur droit de l'image.

On voit que le message est écrit sur 5 lignes.

**Attention** : au niveau des coins, je ne sais pas comment faire. Ex: sur la ligne la plus extérieure : court - court - long - long - court ?

### Rappel sur le morse

Le morse est basé sur une unité que je vais appelé 'un point'. Avec ces points, le morse dispose de 2 symbole : 
- le simple point (composé de 1 unité)
- le trait (composé de 3 unité, donc 3 points)

 À chaque lettre de l'alphabet est associé un code composé de point et de trait.

Entre chaque lettre d'un même mot, il y a 3 points vides.

Entre chaque mot il y a 7 points vides.