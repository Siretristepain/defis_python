# Dictionnaire qui contient le nombre de possibilités par lettre
letters = {
    'a': 1,
    'c': 1,
    'g': 1,
    'u': 1,
    'r': 2,
    'y': 2,
    'k': 2,
    'm': 2,
    's': 2,
    'w': 2,
    'b': 3,
    'd': 3,
    'h': 3,
    'v': 3,
    'n': 4,
}

# La séquence d'entrée
sequence = "NDNKCNVNUGYWRGCNABGSNCRACGSHWNNCYBCSNVUAAGDCMNKNYNNBNCGUBHUNRANDGDMDRSYMGSNWHNDNCVCMAMCANWKYRKVMWMKC"

# On initialise les compteurs
nb_2 = 0
nb_3 = 0
nb_4 = 0

for lettre in sequence:
    if letters[lettre.lower()] == 2:
        nb_2 += 1
    elif letters[lettre.lower()] == 3:
        nb_3 += 1
    elif letters[lettre.lower()] == 4:
        nb_4 += 1

# On fait le calcul
result = (2**nb_2) * (3**nb_3) * (4**nb_4)

print(result)
# --> 609847177343522690648871272448
