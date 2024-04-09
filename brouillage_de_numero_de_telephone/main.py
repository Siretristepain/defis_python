from collections import Counter

# Ouvrir le dictionnaire puis récupérer les mots sans le caractère \n via splitlines()

with open('dictionnaire.txt', 'r') as f:
    contenu = f.read().splitlines()

# On créer un dictionnaire des correspondances avec les lettres des anciens téléphones portables

dic_cor = {
        'a' : 2, 
        'b' : 2,
        'c' : 2,
        'd' : 3,
        'e' : 3,
        'f' : 3,
        'g' : 4,
        'h' : 4,
        'i' : 4,
        'j' : 5,
        'k' : 5,
        'l' : 5,
        'm' : 6,
        'n' : 6,
        'o' : 6,
        'p' : 7,
        'q' : 7,
        'r' : 7,
        's' : 7,
        't' : 8,
        'u' : 8,
        'v' : 8,
        'w' : 9,
        'x' : 9,
        'y' : 9,
        'z' : 9,
    }

# On vas créer une liste de tuple de la façon [(mot1, numero_correspondant), (mot2, numero_correspondant), ... ]

correspondances = []

for mot in contenu:

    # On enlève toutes les majuscules des mots
    mot = mot.lower()

    # On veut spliter le mot pour obtenir une liste de toutes ses lettres
    mot_liste = [*mot] 

    # Maintenant on veut créer le numéro correspondant au mot en faisant la correspondance lettre à lettre via le dictionnaire dic_cor
    numero = []

    for lettre in mot_liste:
        numero.append(dic_cor[lettre])
   
    # Je dois convertir tous les chiffres du numéro en str pour l'étape suivante
    for i in range(len(numero)):
        numero[i] = str(numero[i])

    # Maintenant on veut recoller le numéro pour passer de ça ['1','2','3','4'] à ça 1234 (!conversion list -> str!)
    numero = ''.join(numero)

    # On enregistre le mot et son numéro correspondant dans notre liste de tuples "correspondances"
    correspondances.append((mot, numero))


"""
En fait je me rends compte que ma liste de tuple n'est pas très pratique.
Car maintenant je souhaite compter les occurences de chaque numéro pour trouver les numéros les plus fréquents.
Or c'est facile de compter l'occurences des éléments dans une liste mais plus dur sur une liste de tuples
"""

# Je créer donc une simple liste des numéros de téléphones pour pouvoir simplement compter les occurences
numero_liste = []

for item in correspondances:
    numero_liste.append(item[1])


# Habile méthode pour compter les occurences de chaques éléments dans une liste python
occurences = [[numero, numero_liste.count(numero)] for numero in set(numero_liste)]


# Maintenant je fais une liste des occurences pour trouver l'occurence la plus élévée
liste_occurences = []

for item in occurences:
    liste_occurences.append(item[1])

maximum = max(liste_occurences)


# Maintenant que l'on a le maximum on peut regarder auxquels numéros il correspond dans "occurences"
liste_bon_numero = []

for item in occurences:
    if item[1] == maximum:
        liste_bon_numero.append(item[0])


# Maintenant il faut trier les numéros dans l'ordre croissant
liste_bon_numero = sorted(liste_bon_numero)


# Prints résultats
for numero in liste_bon_numero:
    with open('result.txt', 'a') as f:
        f.write(f"{numero}, ")



