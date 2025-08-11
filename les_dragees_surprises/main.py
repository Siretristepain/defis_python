def inverse_with_previous(a: list, b: int):
    """Fonction permettant d'inverser l'élément d'indice b dans une liste a avec l'élément à l'indice b-1 (celui
    qui le précède).

    Ex : 
    inverse_with_previous(a=[1,2,3], b=2)
    ---> [1,3,2]

    Args:
        a (list): liste contenant tous les éléments.
        b (int): indice de l'élément à inverser avec le précédent.

    Raises:
        IndexError: Erreur si l'indice b fournis en entrée est supérieur au nombre d'éléments dans la liste a.

    Returns:
        a (list): La liste après la permutation des de l'élément d'indice b avec l'élément d'indice b-1.
    """

    # Cas où l'élement à inverser avec le précédent est le 1er de la liste (dans ce cas on l'inverse avec le dernier).
    if b == 0:
        previous_value = a[-1]
        a[len(a)-1] = a[0]
        a[0] = previous_value
        return a

    # Cas où l'indice de l'élément à inverser est plus grand que le nombre d'éléments dans la liste.
    elif b > len(a) - 1:
        raise IndexError("L'index fournis est trop grand. La liste n'a pas assez d'éléments.")

    # Cas normal
    previous_value = a[b-1]
    a[b-1] = a[b]
    a[b] = previous_value
    return a


# Liste des dragées surprises
dragees = ['A','B','E','C','G','F','M','O','H','P','S','V']

# nb_tour est le compteur du nombre de tour et i est l'indice de l'élément à inverser dans la liste.
nb_tour = 1
i = -1

# Pour éviter une boucle infinie, je mets une une sécurité pour arrêter la boucle si on dépasse les 100 tours.
while True and nb_tour < 100:
    i += 5
    i = i % 12
    inverse_with_previous(a=dragees, b=i)

    # On vérifie si les 4 dragées voulus sont les 4 premières de la liste, si c'est le cas on stop la boucle.
    if 'A' in dragees[:4] and 'E' in dragees[:4] and 'G' in dragees[:4] and 'H' in dragees[:4]:
        break

    nb_tour += 1

print(f"Nombre de tour : {nb_tour}\nDragées : {dragees}")
# Nombre de tour : 85
# Dragées : ['A', 'H', 'E', 'G', 'V', 'F', 'B', 'O', 'C', 'P', 'S', 'M']
