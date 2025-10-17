import math

# Dictionnaire du type <n°agent> -> [coordonnées_agent]
dic = {}

# Lecture du fichier de données
with open("./je_vous_surveille/donnees.txt", 'r') as f:
    content = [line.rstrip('\n') for line in f.readlines()]

# On vas remplir le dictionnaire
i = 0
for coord in content:
    # On converti les coordonnées en entiers
    x = int(coord.split(',')[0])
    y = int(coord.split(',')[1])
    # print(f"x : {x}")
    # print(f"y : {y}")
    dic[i] = [x, y]
    i += 1

# On crée la liste des entiers de 0 à 254 pour représenter chaque agent
agents = [i for i in range(255)]

# Fonction de calcul de distance entre 2 points dans un repère cartésien
def distance(coordonnees_a: list, coordonnees_b: list):
    x_a = coordonnees_a[0]
    y_a = coordonnees_a[1]
    x_b = coordonnees_b[0]
    y_b = coordonnees_b[1]
    
    distance = math.sqrt((x_b - x_a)**2 + (y_b - y_a)**2)

    return distance


# On vas boucler sur chaque clés du dictionnaire (chaque agent) puis calculer la distance à chaque autre agent pour identifier le plus proche
for agent in dic:
    # Liste dans laquelle on vas stocker la distance à tous les autres agents
    all_distances = []
    for other_agent in dic:
        if agent == other_agent:
            distance_between = 9999
        else:
            distance_between = distance(dic[agent], dic[other_agent])
        all_distances.append(distance_between)
    
    # On recherche la distance minimale
    minimale_distance = min(all_distances)

    # On recherhce l'index de cette distance minimale
    index_minimale_distance = all_distances.index(minimale_distance)

    # On supprime l'agent correspondant à cet index de distance minimale de la liste des agents
    # En fait ce que je fais c'est que je les convertis tous en -1. Ensuite je supprimerais tous les -1 de la liste des agents.
    # del agents[index_minimale_distance]
    agents[index_minimale_distance] = -1
    print(f"Agent n°{index_minimale_distance} supprimé")


agents_non_surveilles = [x for x in agents if x != -1]

"""
Liste des agents non surveillés :
[23, 24, 25, 27, 30, 32, 39, 40, 49, 55, 67, 74, 76, 78, 85, 87, 93, 96, 100, 101, 102, 103, 105, 106, 109, 111, 112, 114, 137, 139, 140, 142, 155, 156, 159, 167, 175, 178, 182, 184, 194, 208, 210, 212, 218, 220, 221, 224, 229, 231, 232, 239, 243, 247, 253]
"""

print(f"Liste des agents non surveillés :")
print(agents_non_surveilles)

if __name__ == '__main__':
    # print(type(distance([-8,-6], [-6,-8])))
    pass