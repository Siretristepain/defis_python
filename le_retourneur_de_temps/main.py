def check_seven(nb_min: int):
    """Fonction qui vérifie si la somme des digits du nombre de minutes passé en argument est divisible par 7.

    Args:
        nb_min (int): le nombre de minute à vérifier.

    Returns:
        (bool) : True si la somme est divisible par 7, else sinon.
    """

    # On commence par calculer la somme des digits
    nb_min_list = list(str(nb_min))
    digits_sum = sum([int(i) for i in nb_min_list])

    # On vérifie ensuite si la somme est divisible par 7
    if digits_sum % 7 == 0:
        return True
    return False

def turn_necklace(nb_min: int, particular: bool, increment: int):
    """Fonction récursive qui simule l'action de tourner d'un cran le remonteur de temps.
    À chaque tour, la fonction regarde l'argument particular. S'il est sur True, c'est que l'itération précédente été divisible par 7 est
    que par conséquent, ce tour ci on doit retirer 7 minutes au lieu d'en ajouter 2.
    Ensuite, sur le nouveau total de minute, on appel la fonction check_seven et on rappelle turn_necklace avec les bons arguments.

    Args:
        nb_min (int): le nombre de minute remontées dans la passé jusqu'ici (juste avant la nouvelle itération).
        particular (bool): True si l'itération précédente été divisible par 7 (auquel cas on doit retirer 7 min), False sinon (auquel cas on ajoute 2 min).
        increment (int): compteur qui permet d'ajouter une condition de fin à notre fonction récursive (Régler manuellement dans la fonction le nombre d'incrément choisis).

    Returns:
        _type_: _description_
    """

    # On incrémente notre incrément
    increment += 1

    # Condition d'arrêt, sans quoi on fait une boucle inifie
    while increment < 200:

        print(f"Le nombre de minute remonté est : {nb_min}")

        # On gère le cas particulier
        if particular:
            nb_min -= 7
        else:
            nb_min += 2
        
        # On fait appel à check_seven pour vérifier le cas particulier
        particular = check_seven(nb_min)

        # On rappel turn_necklace avec les bons arguments pour le prochain tour
        return turn_necklace(nb_min=nb_min, particular=particular, increment=increment)



turn_necklace(nb_min=0, particular=False, increment=0)