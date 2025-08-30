def check_div_by_13(coord: str):
    """Fonction qui détermine si la somme des digits qui compose coord est divisible par 13.

    Args:
        coord (str): la chaine de caractère à vérifier.

    Returns:
        (bool) : True si la somme des digits est divisible par 13, sinon False.
    """

    total = 0
    for car in coord:
        if car.isdigit():
            total += int(car)

    if total % 13 == 0:
        return True
    
    return False

# print(check_div_by_13("04621;;;"))

# ==========
# Résolution
# ==========

# Ouverture du fichier et récupération des lignes
with open("./un_message_bien_enfoui/src/input.txt", "r") as f:
    content = [line.rstrip('\n') for line in f.readlines()]

# Liste des coordonnées à conserver
keep_lines = []

# Boucle sur chaque ligne de coordonnée
for line in content:
    # On dissocie latitude et longitude
    lat = line.split(' ')[0]
    long = line.split(' ')[1]

    if check_div_by_13(lat) and check_div_by_13(long):
        keep_lines.append(line)

print(f"Voici les coordonnées à retenir : {keep_lines}")
# --> Voici les coordonnées à retenir : ['53.524929 -2.217329', '41.31791 2.10019', '43.12466 12.888219', '40.415129 -3.695529', '41.31791 2.10019', '33.826629 -84.36288', '25.68918 -80.31842', '43.26987 5.39621', '55.68456 12.51629', '51.70193 5.25761', '40.86206 -74.12804', '33.68402 -84.87156', '40.38911 -80.07551', '33.68402 -84.87156', '53.53451 -2.08646']