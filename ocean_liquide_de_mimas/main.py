import requests

"""
Ce problème utilise le système de consultation d'URL pour récupérer les données d'entrée et pour retourner la réponse.
Pour que ça fonctionne, il faut utiliser le module requests, voici la méthode à suivre :

r = requests.get("https://pydefis.callicode.fr/defis/URLDEFI/get/votrelogin/code", verify=True)
print(r) # Pour contrôle
data = r.json()
print(data) # Pour contrôle
reponse = {'signature': data['signature'], 'c': data['a'] + data['b']}
r = requests.post("https://pydefis.callicode.fr/defis/URLDEFI/post/votrelogin/code", json=reponse, verify=True)
print(r) # Pour contrôle
data = r.json()
print(data) # Pour contrôle
"""

# On récupère les données d'entrée
r = requests.get("https://pydefis.callicode.fr/defis/C24_Mimas/get/JonSnow/db750", verify=True)
data = r.json()

def compute_min_local(map: list[list]) -> list[list]:
    """
    Fonction pour générer la carte des profondeurs locales.
    Pour rappel, la profondeur locale d'un point corresponds à la moyenne des profondeurs du point courant et de ses 8 voisins.
    (=> On ne calcule pas les profondeurs locales pour les bordures).
    
    :param map: carte montrant l'épaisseur de glace en chaque point.
    :type map: list[list]
    :return : final
    :rtype: list[list]
    """
    LENGTH = len(map[0])
    WIDTH = len(map)

    final = []

    # Each line (except first and last)
    for x in range(1, LENGTH-1):
        new_line = []
        # Each column (except first and last)
        for y in range(1, WIDTH-1):
            local_depth = (1/9) * (map[x-1][y-1] + map[x-1][y] + map[x-1][y+1] + map[x][y-1] + map[x][y] + map[x][y+1] + map[x+1][y-1] + map[x+1][y] + map[x+1][y+1])
            new_line.append(local_depth)
        
        final.append(new_line)
    
    return final

def find_min(map: list[list]):
    min_found = {'x' : 0,
                 'y' : 0,
                 'value' : 999}

    for i in range(len(map)):
        current_list = map[i]
        for j in range(len(current_list)):
            current_elem = current_list[j]

            if current_elem < min_found['value']:
                min_found['x'] = i + 1
                min_found['y'] = j + 1
                min_found['value'] = current_elem

    return min_found

# ====
# LOOP
# ====

reponse = {}
x = 1
for elem in data:
    if elem not in ['signature', 'status']:
        ocean = data[elem]

        # Compute map of min for ocean
        maped_ocean = compute_min_local(map=ocean)

        # Search min
        min_found = find_min(map=maped_ocean)

        if x < 10:
            reponse[f'trou0{str(x)}'] = [min_found['x'], min_found['y']]
        elif x == 10:
            reponse[f'trou10'] = [min_found['x'], min_found['y']]
            reponse['signature'] = data['signature']

        x += 1

        
        
# print(reponse)
# --> {'trou01': [3, 25], 'trou02': [7, 18], 'trou03': [6, 8], 'trou04': [27, 12], 'trou05': [12, 16], 'trou06': [11, 15], 'trou07': [17, 16], 'trou08': [3, 15], 'trou09': [20, 8], 'trou10': [2, 7], 'signature': '-- JonSnow 1768148145 fa2314a34e 91615e0dbb1acd0cfd0897212619a922 --'}

r = requests.post("https://pydefis.callicode.fr/defis/C24_Mimas/post/JonSnow/db750", json=reponse, verify=True)
print(r)
data = r.json()
print(data)

# <Response [200]>
# {'message': 'Bravo, défi résolu !!!', 'status': 'OK'}
