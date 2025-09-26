# Ouverture du fichier d'entrée pour récupérer chaque ligne
with open("le_seul_et_unique/src/liste.txt", "r") as f:
    content = [line.rsplit('\n')[0] for line in f.readlines()]

# On créer une liste de tous les pokémons (chaque ligne du fichier mais uniquement les noms)
all_pokemon = [line.split(',')[0] for line in content]

def find_unique_element_in_list(liste: list):
    """
    Fonction récursive qui retourne le premier élément unique de la liste d'entrée.

    Args:
        - liste (list): liste dans laquelle on cherche le premier élément unique.
    """

    # Cas où l'on aurait aucun élément unique dans la liste, la fonction s'appelerait à l'infini sans cela.
    if liste == []:
        return False

    # On prends le premier élément de la liste et on compte son nombre d'occurrence total dans la liste
    element = liste[0]
    nb_element = liste.count(element)

    # Si l'élément apprait plus d'une fois, on supprime toutes ses occurrences de la liste et on rappelle la fonction avec la nouvelle liste.
    if nb_element > 1:
        for i in range(nb_element):
            liste.remove(element)
        
        return find_unique_element_in_list(liste)
    
    # Si l'élément apparait une seule fois dans la liste, c'est l'élément unique !
    if nb_element == 1:
        return element

# print(find_unique_element_in_list(all_pokemon))
# aflamanoir

# On récupère le pokemon unique via la fonction créer pour retourner le premier élément unique d'une liste
unique_pokemon = find_unique_element_in_list(all_pokemon)

# On parcours les lignes du fichier pour retrouver la ligne qui mentionne le pokémon unique et on en retire ses coordonnées.
for line in content:
    if line.split(',')[0] == unique_pokemon:
        print(f"Coordonnées de {unique_pokemon} : {line.split(',')[1]}, {line.split(',')[2]}.")
        break
# Coordonnées de aflamanoir : 47, -115.
