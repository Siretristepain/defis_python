def check_sum_compatible(number: int, n: int):
    """Fonction qui vérifie si la somme des chiffres qui composent number est divisible par n.
    De plus, la fonction vérifie si number contient un zéro, auquel cas elle retourne False.

    Args:
        number (int): le nombre a vérifier.
        n (int): le diviseur.

    Returns:
        (bool) : True si number ne contient aucun zéro et que la somme de ses chiffres est divisible par n.
    """

    # On créer la liste des chiffres composant number
    number_to_list = [int(i) for i in str(number)]

    # On retourne False si un zéro fait parti des chiffres de number
    if 0 in number_to_list:
        return False

    # On vérifie la division par n
    return sum(number_to_list) % n == 0

def check_times_compatible(number: int, n: int):
    """Fonction qui permet de vérifier si la multiplication des chiffres qui composent number est divisible par n.

    Args:
        number (int): le nombre à tester.
        n (int): le diviseur.

    Returns:
        (bool) : True si la multiplication des chiffres qui composent number est divisible par n.
    """

    # On créer la liste des chiffres composant number
    number_to_list = [int(i) for i in str(number)]

    # On initialise le résultat de la multiplication à 1
    times = 1

    for num in number_to_list:
        times = times * num

    # 0%n retourne True, or on ne veut pas que les résultats de zéro retourne True, on les gère donc à part
    if times == 0:
        return False
    
    # On vérifie la division
    return times % n == 0

# print(check_sum_compatible(77))
# print(check_times_compatible(0))

# Liste qui va stocker tous les nombre n-compatibles
result = []

# On veut la taille de la liste des nombres à 6 chiffres ne contenant aucun 0 n-compatibles
for i in range(100000, 999999):
    if check_sum_compatible(i, n=42) and check_times_compatible(i, n=42):
        result.append(i)

print(len(result))
# 3390
