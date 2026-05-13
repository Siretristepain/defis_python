M=[[17, 3, 4, 14, 5, 17], [8, 16, 3, 17, 14, 12], [13, 5, 15, 4, 16, 3], [14, 7, 3, 16, 3, 2], [6, 1, 16, 10, 5, 13], [11, 1, 9, 11, 18, 8]]
ITERATION = 39

def one_step_line(line: list) -> list:
    """
    Fonction qui applique la transformation à une ligne de la matrice uniquement (--> donc à une simple liste).

    Args:
        line (list): la liste à transformer.

    Returns:
        list: la liste transformée.
    """
    return [((9*k)+3)%19 for k in line]

def one_step_matrice(matrice: list[list]) -> list[list]:
    """
    Fonction qui applique la transformation à la matrice entière.

    Args:
        matrice (list[list]): la matrice à transformer.

    Returns:
        list[list]: la matrice transformée.
    """
    return [one_step_line(line) for line in matrice]

def sum_matrice(matrice: list[list]) -> int:
    """
    Fonctinon qui retourne la somme de tous les éléments d'une matrice.

    Args:
        matrice (list[list]): la matrice dont on souhaite additionner tous les éléments.

    Returns:
        int: le total.
    """
    return sum([sum(line) for line in matrice])

for i in range(ITERATION):
    M = one_step_matrice(matrice=M)

print(f"Le résultat final est : {sum_matrice(matrice=M)}.")
