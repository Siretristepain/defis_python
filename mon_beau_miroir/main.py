# =========
# Fonctions
# =========

def check_palindrome(number: int) -> bool:
    """
    Fonction qui check si un nombre ``number`` donné en entrée est un palindrome,
    c'est à dire qu'il est égal à lui-même retourné.

    Args:
        number (int): le nombre à vérifier.

    Returns:
        bool: True si palindrome, False autrement.
    """
    number_str = str(number)
    return number_str == number_str[::-1]

def rotate_number(number: int) -> int:
    """
    Fonction qui permet de retourner un nombre ``number`` donné en entrée.

    Example:
        rotate_number(number=123)
        >>> 321

    Args:
        number (int): le nombre qu'on souhaite inverser.

    Returns:
        int: le nombre rotationné.
    """
    return int(str(number)[::-1])

def search_palindrome(number: int) -> list[int]:
    """
    Fonction qui recherche le palindrome d'un nombre par incrémentation du nombre avec son image renversée.

    Example:
        search_palindrome(number=475)
        >>> [15851, 3]

    Car:
        475 + 574 = 1049
        1049 + 9401 = 10450
        10450 + 5401 = 15851

    Args:
        number (int): le nombre dont on souhaite connaitre le palindrome par incrémentation.

    Returns:
        list[int]: le résultat sous forme [palindrome, nb_itération]
    """
    running = True
    iteration = 0

    while running:
        rotated_number = rotate_number(number=number)
        composition = number + rotated_number
        number = composition
        iteration += 1

        if check_palindrome(composition):
            running = False

    return [number, iteration]

print(f"Le résultat est : {[search_palindrome(number=number) for number in (396, 294, 290, 861, 481, 194, 570, 463, 265, 935)]}.")
# --> Le résultat est : [[79497, 5], [9339, 4], [2552, 4], [13431, 3], [2552, 3], [2992, 3], [5115, 4], [45254, 5], [45254, 5], [25652, 4]].
