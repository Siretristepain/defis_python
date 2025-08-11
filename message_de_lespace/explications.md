# Message de l'espace

Mulder a eu accès a des enregistrements de radiotelescope visant à découvrir une intelligence extraterrestre.

Le flux de données enregistré est composé de plusieurs séquence de 15 caractères, comme par exemple :

```
MYNBIQPMZJPLSGQ
EJEYDTZIRWZTEJD
XCVKPRDLNKTUGRP
OQIBZRACXMWZVUZ
TPKHXKWCGSHHZEZ
ROCCKQPDJRJWDRK
RGZTRSJOCTZMKSH
JFGFBTVIPCCVYEE
...
```

On s'intéresse à la propriété suivante :

```
La séquence ne contient aucun bloc de 4 lettres successives contenant une lettre en double.
```

Pour des séquences de 15 caractères comme celles ci-dessus, cette propriété est vraie environ 20.4% du temps.

Nous avons reçu 500 fichiers d'enregistrements contenant chacun 1000 séquences. Dans un tel fichier, on s'attends donc a retrouver environ 204 séquences qui vérifient la propriété.

Si un fichier a strictement moins de 172 ou strictement plus de 235 séquences qui vérifient cette propriété, on dit que l'enregistrement est suspect et laisse a suggérer l'existence d'une intelligence extraterrestre.

Il faut vérifier chaque fichier et retourner le n° de chaque fichier suspect, étant donné que la nomenclature des fichiers est **enregXXX.txt** où XXX représente le n° du fichier.

## Résolution

J'ai commencé par écrire une fonction **check_sequence** qui vérifie pour une seule séquence si la propriété est vraie. Elle retourne True si aucun doublon n'est trouvé pour chaque groupement de 4 lettres successives.

J'ai ensuite créé une fonction  **process_a_file** qui prends en argument le chemin vers un fichier à traiter. Cette méthode récupère le contenu d'un fichier (donc toutes les séquences) et boucle sur chaque séquences en faisant appel à la méthode **check_sequence**. Si le nombre de séquences vérifiant la propriété est strictement inférieure à 172 ou strictement supérieur à 235, alors la méthode retourne le n° du fichier, False sinon.

J'ai enfin créé une fonction **resolution** qui permet de récupérer une liste de tous les fichiers contenu dans le répertoire input. La fonction boucle sur chaque fichier en faisant appel à la méthode **process_a_file**. La fonction retourne ensuite la liste des n° de fichier suspects.

La **réponse** est : 10, 84, 93, 135, 334, 336, 386, 411, 493 .
