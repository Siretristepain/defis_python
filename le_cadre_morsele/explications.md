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

## 1ère erreur : symboles 0 et 1

Ma fonction **filtre_all_pixel** n'était pas raccord avec la façon dont fonctionne le dictionnaire de traduction des lettres en morse dans mon module utile.

En effet, dans mon dictionnaire, les codes morse sont écris avec des 0 et des 1 où 0 resprésente les espaces et 1 représente les points et les traits.

Or, lorsque l'on affiche une matrice avec plt.imshow, les pixels 1 sont blancs et les pixels 0 sont noirs.

Or, dans ma "compréhension", je partais du principe que c'était les pixels noirs qui représentaient les lettres. C'était donc l'inverse.

### Rappel sur le morse

Le morse est basé sur une unité que je vais appelé 'un point'. Avec ces points, le morse dispose de 2 symbole : 
- le simple point (composé de 1 unité)
- le trait (composé de 3 unité, donc 3 points)

 À chaque lettre de l'alphabet est associé un code composé de point et de trait.

Entre chaque lettre d'un même mot, il y a 3 points vides.

Entre chaque mot il y a 7 points vides.

## Résolution étape par étape

J'ouvre l'image avec matplotlib.image --> **img**.

Je créer plusieurs fonctions :

- filtre_all_pixel : fonction qui convertis tous les pixels d'une image en 100 % s'ils n'étaient pas 100% à l'origine et laissent les pixels 100% blancs lorsqu'ils étaient 100% blancs à l'origine.

- convert_sequence_to_str_bis : convertis une sequence np.array en string, en enlevant les crochets au début et à la fin + en suppriment les espaces et les points.

- split_by_words : transforme une str en liste, en séparant les éléments par le pattern '0000000'.

- split_by_letter : transforme une str en liste, en séparant les éléments par le pattern '000'.

- translate_sequence : permet de traduire une séquence np.array composée de 0 et 1 cachant un message en morse en écriture normale. Pour cela, cette méthode fait appel aux méthodes précédentes.

Etapes :

- appliquer la méthode filtre_all_pixel sur **img** pour obtenir **img_black_white**. Cette dernière est donc une image noire et blanche. **Attention** : les pixels blancs sont ceux qui indique un trait plein et les noirs les traits vides (c'est donc contre intuitif). Cette étape permet donc notamment de visualiser le morse dans le cadre de l'image.

- récupérer les bandes qui compose le cadre grâce au slicing : il s'agit des variables line_1, line_2, ...

- appliquer la méthode translate_sequence sur chaque bandes du cadre pour voir le message apparaitre.

Voici le message :

```
 bravo manifestement vous avez reussi a trouver le message cache qui va vous permettre de vous documenter grace

  wikipedia sur cet animal qu est le morse le morse odobenus rosmarus est s

 ne espece de grands mammiferes marins unique representant actuel de son genre odobenus ainsi que de sa famille cel

  des odobenidae le morse est parfaitement reconnaissable a ses defenses ses mo

 astaches drues et son allure massive les males adultes du pacifique peuvent peser jusqu a deux tonnes et parmi le

 i membres du clade des pinnipedes l espece n est depassee en taille que par l ele

 phant de mer le morse vit principalement dans les eaux peu profondes des plateaux continentaux passant une pa

  importante de son existence sur les blocs de glace ou les icebergs deriv

 tnts de ces platesformes il part a la recherche de sa nourriture de predilection les mollusques bivalves du be

 ethos c est un animal sociable a l esperance de vie d environ 40 ans et cone

 idere comme une espece cle des ecosystemes marins de l arctique le morse occupe une place importante dans la

 lture de nombreux peuples autochtones de l arctique qui le chasserent

 rour sa viande sa graisse sa peau ses defenses et ses os bon si vous etes arrives la c est que vous avez pu tourner

 elusieurs fois dans le cadre et ceci vaut bien un indice car malheureusement t

 e n est pas ce texte qui vous donnera le nom de la personne solution de l enigme pour le trouver il vous faud

  regarder dans l image et plus precisement dans les composantes vertes de

 eertains pixels de la ligne 35 ce sont ceux qui debutent a la colonne 769 et qui vont de 4 en 4 avec un peu

 e code ascii vous devriez trouver la personne en rapport avec l image




 n tout cas bravo d etre arrive jusque la et j espere que ce petit documentaire sur le morse vous aura plu

 n tout cas bravo d etre arrive jusque la et j espere que ce petit documentaire sur le morse vous aura plu
```

On constate que la plupart du texte ne sert à rien mais que l'on a une indication : le nom que l'on cherche est caché dans l'image, plus précisément dans les composantes vertes des pixels allant de 4 en 4 commençant à la ligne 351 et à la colonne 769.

**Attention** : dans le message, la ligne indiquée est 35 et non 351 mais cela est dû à une "erreur" dans mon code. En effet, je parcours tous les pattern d'une sequence et je cherche la lettre correspondante dans le dictionnaire **morse_str** de mon package **utile**.

En effet, voici mon code :

```
for letter in letters:
    # hide_letter = [key for key, value in morse_str.items() if value == letter]
    try:
        hide_letter = [key for key, value in morse_str.items() if value == letter]
        result.append(hide_letter[0])
    except:
        pass
```

Donc lorsqu'aucune traduction n'est trouvée, mon code ne fais qu'une simple 'pass' et il est donc impossible de voir lorsqu'il y a une erreur (j'ai donc mis longtemps à comprendre d'où venait mon problème).

Or, j'avais mal encodé le caractère '1' dans le dictionnaire morse_str :

```
    '1': '101110111011101111',
```

On voit que j'ai ajouté un 1 en trop à la fin.
Le bon encodage est :     '1': '10111011101110111'. Je l'ai corrigé par la suite.

## Réponse

Si on convertis en ASCII les composantes vertes des pixels de 4 en 4 à partir des coordonnées 351/769, on trouve : **Alfred Vail**.
