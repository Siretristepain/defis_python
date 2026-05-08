# ====================
# Ouverture du fichier
# ====================

with open("robots_tueurs_de_krikkets_pt1/src/input.txt", "r") as f:
    content = [line.split('\n')[0] for line in f.readlines()]

# ============
# Phase de tri
# ============

"""
logs = {
    'mac1': [l1, l2],
    'mac2': [l2, l4],
    ...
}

"""
logs = {}

def extract_mac_and_position(line: str) -> list:
    mac = line[19:36]
    position = line[52:-1]
    return [mac, position]

for line in content:
    info = extract_mac_and_position(line)

    # Si l'adresse mac de la ligne est déjà dans le dictionnaire logs, alors on ajoute simplement le lieu dans la liste déjà existante pour ce mac.
    is_in_dict = logs.get(info[0], False)
    if is_in_dict:
        logs[info[0]].append(info[1])

    # Si l'adresse mac de la ligne n'est pas déjà dans le dictionnaire logs, on l'ajoute, avec le lieu.
    else:
        logs[info[0]] = [info[1]]

# =========
# Fonctions
# =========

def compare_two_list(l1: list, l2: list) -> float:
    """
    Fonction qui permet de retourner la ressemblance entre 2 listes en comparant les éléments qu'elles contiennent.
    (valeur entre 0 et 1, 1 signifiant que les 2 listes contiennent les mêmes données, mais pas forcément dans le même ordre).
    Attention : se base sur la liste la plus petite.

    Exemple :

    l1=[1,2,3,4]
    l2=[1,2]

    compare_two_list(l1,l2) --> 1.0

    Args:
        l1 (list): la première liste.
        l2 (list): le deuxième liste.

    Returns:
        float: ressemblance (entre 0 et 1).
    """
    lists = [l1, l2]
    lists.sort(key= lambda l: len(l))

    smaller_list = lists[0]
    longest_list = lists[1]

    find_counter = 0
    for elem in smaller_list:
        if elem in longest_list:
            find_counter += 1

    return find_counter / len(smaller_list)

# ==============================================================================
# Recherche des 4 robots avec la plus grande ressemblance dans les lieux visités
# ==============================================================================

# On initialise les 4 valeurs de ressemblance les plus élevées à 0.
max_1 = [0, 0]
max_2 = [0, 0]
max_3 = [0, 0]
max_4 = [0, 0]

robots = list(logs.keys())

for i in range(len(robots)):
    current_robot = robots[i]

    # On veut comparer le robot avec tous les autres après lui (pas la peine de faire ceux avant lui puisqu'ils l'on déjà comparés avec eux).
    # Cas du dernier robot
    if i == len(robots)-1:
        break

    for j in range(i+1, len(robots)):
        same = compare_two_list(
            l1=logs.get(current_robot),
            l2=logs.get(robots[j])
        )

        comparision = [f"{current_robot} - {robots[j]}", same]

        # Pas très propre mais ça marche
        if comparision[1] > max_1[1]:
            max_4 = max_3
            max_3 = max_2
            max_2 = max_1
            max_1 = comparision
        
        elif comparision[1] > max_2[1]:
            max_4 = max_3
            max_3 = max_2
            max_2 = comparision

        elif comparision[1] > max_3[1]:
            max_4 = max_3
            max_3 = comparision

        elif comparision[1] > max_4[1]:
            max_4 = comparision

if __name__ == "__main__":
    # print(compare_two_list(l1=[1,2,3,4], l2=[1,5]))
    print(max_1)
    print(max_2)
    print(max_3)
    print(max_4)

"""
['b7:52:7a:02:42:04 - 14:ba:6b:aa:94:55', 1.0]
['b7:52:7a:02:42:04 - c5:3e:d8:2c:07:cd', 1.0]
['b7:52:7a:02:42:04 - f8:cb:82:e2:e6:62', 1.0]
['14:ba:6b:aa:94:55 - f8:cb:82:e2:e6:62', 1.0]

Donc --> b7:52:7a:02:42:04 14:ba:6b:aa:94:55 c5:3e:d8:2c:07:cd f8:cb:82:e2:e6:62
"""
