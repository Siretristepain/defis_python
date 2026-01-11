import re

# =============================
# Ouverture du fichier d'entrée
# =============================

with open("les_victimes_de_tooms_part1/src/input.txt", "r") as f:
    # Récupération de chaque ligne dans une grande liste de liste -> [ [ligne1], [ligne2], ...]
    lines = [line.split('\n')[0] for line in f.readlines()]

# num = re.findall(pattern=r'\d{1,2}\.\d{1,2}', string=content)
# print(lines)

# Empreinte de Tooms
TOOMS = [10, 12, 6, 9, 18.5, 22, 7, 4, 9, 10]

def extract_data_from_line(line: str) -> list[float]:
    """
    Fonction qui extrait l'empreinte d'une ``line`` donnée en entrée.
    
    :param line: la ligne d'entrée du fichier dont on veut extraire les données.
    :type line: str
    :return data (list[float]): les données d'empreinte extraite, sous forme de liste. 
    """
    data = line.split('-')[1]
    data = data.split(',')
    data = [float(elem) for elem in data]
    return data

def check_differences(data: list[float]) -> bool:
    """
    Fonction qui compare l'empreinte ``data`` d'entrée avec l'empreinte de TOOMS pour voir si elles correspondent.
    Les empreintes correspondent si le delta entre chaque élément est le même.
    
    :param data: l'empreinte dont on souhaite savoir si elle provient de TOOMS.
    :type data: list[float]
    :return: True si empreinte de TOOMS, False sinon.
    :rtype: bool
    """
    # On initialise un delta à 0.
    delta = 0
    # On parcours tous les éléments de l'empreinte.
    for i in range(len(data)):
        # On calcul le detla en l'élément i de l'empreinte d'entrée et l'élément i de l'empreinte de TOOMS.
        current_delta = TOOMS[i] - data[i]
        # Si on est au premier élément, on met delta à jour avec cette valeur.
        if i == 0:
            delta = current_delta

        # A partir du deuxième élément, on vérifie que le delta soit bien toujours égal.
        else:
            if current_delta != delta:
                return False
    return True

datas = []

for line in lines:
    datas.append(extract_data_from_line(line=line))


tot = 0

for i in range(len(datas)):
    data = datas[i]
    if check_differences(data=data):
        tot += i+1


print(tot)
# --> 4843
