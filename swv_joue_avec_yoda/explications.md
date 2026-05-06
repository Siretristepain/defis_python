# SW V : joue avec Yoda

Yoda nous fournis une liste de mots qui ne sont pas "organisés".

Notre objectif consiste simplement à trier cette liste de mot.

La règle a suivre est la suivante : les trois premières lettres du mot N doivent correspondre au 3 dernières lettres du mot N-1.
Autrement dis, les 3 dernières lettres du mot N doivent correspondre au 3 premières lettres du mot N+1.

**Donnée d'entrée**:
```
sassai eaux-de-vie cessaient acerbité eaux sceau tiendra hasard acéphale auxiliairement vesce eurafricaine hâtai saignant entachassent alentie césar vieillerie messéant taillable ives testacé dracéna ardentes ensablant blessas entachasses ioniens antarctique sessiles ineffaçables quercitrine besace lessivasses acerbes descellaient entachas lessive gestation lessivâtes antécédentes énamourâmes antécédent entachât inefficace testacelles sarabandes entachant rieur itérâmes antécédences messages sesquioxydes testacés
```

## Résolution

Mon idée est de créer une fonction qui prends en entrée 2 arguments :
- un mot
- une liste de mot
La fonction doit retourner le premier trouvé dans la liste qui commence par les 3 dernières lettres du mot d'entrée.

Ensuite, on créer une liste avec tous les mots.
On créer une liste vide dans laquelle va apparaitre les mots dans l'ordre.

On prends le 1er mot de la liste de tous les mot et on fait appel à notre fonction pour trouver le mot suivant.
On supprime le mot trouvé de la liste des mots et on réappelle la fonction etc...
