from pathlib import Path, PosixPath

# On défini l'entrée de notre hiérarchie de dossiers/fichiers d'entrée.
p = Path("secret_de_poesie_vogone/src/C25_MeliMeloFiles_dir")

# On récupète tous les fichier txt du zip
files = sorted(p.glob('**/*.txt'))

# Liste qui contiendra tous les fichiers utiles (-> càd ceux qui auront un n° de fragments et un ou des offset).
interested_files = []

def is_digit_on_file(text: str) -> bool:
    """
    Fonction qui permet de vérifier si le contenu d'une chaîne de caractère contient au moins un chiffre.
    Je me sers de cette fonction pour trouver les fichier utile.

    Je fais donc l'hypothèse qu'AUCUN fichier non-utile contient un chiffre, sinon ça tombe à l'eau comme fonction.
    
    :param text: la chaîne de caractère (-> contenu du fichier), dans laquelle on souhaite vérifier la présence d'un chiffre.
    :type text: str
    :return: True si la str contient au moins un chiffre, False sinon.
    :rtype: bool
    """
    for car in text:
        if car.isdigit():
            return True
    return False

# On récupère tous les fichiers intéressants dans la liste interested_files et on supprime les autres.
for file in files:
    if is_digit_on_file(file.read_text()):
        interested_files.append(file)
    # Delete all useless files
    else:
        file.unlink()

def extact_header_from_file(file: PosixPath) -> tuple:
    """
    Fonction utilisée pour extraire les données intéressante d'un fichier utile.
    Elle récupère son n° de fragment (digit de la 1ère ligne).
    Elle récupère les offset (digits de la 2ème ligne).
    Elle récupère les caractères intéressants via ces offset et un appel à la fonction get_element_by_index.
    
    :param file: objet PosixPath de pathlib.
    :type file: PosixPath
    :return: tuple contenant en premier élément le n° de fragment pour pouvoir ordoner les fragments par la suite et en second, la 'bribe' de mot formé via les offset.
    :rtype: tuple
    """
    # On ouvre le fichier txt et on en fait une liste ligne à ligne.
    with open(file, 'r') as f:
        content = [line.split('\n')[0] for line in f.readlines()]
    
    # On récupère fragment et offset.
    fragment = int(content[0])
    offset = [int(x) for x in content[1].split(' ')]

    # Liste qui va contenir tous les caractères intéressants pour former la 'bribe' de mot.
    each_car = []

    # Pour chaque offset, on fait un appel à get_element_by_index pour récupérer le caractère correspondant.
    for off in offset:
        car = get_element_by_index(list_of_line=content[2:], index=off)
        each_car.append(car)
    
    # On retourne le n° de fragment et la 'bribe' de mot formée.
    return (fragment, ''.join(each_car))

def get_element_by_index(list_of_line: list, index: int):
    # Join each element of the list by an empty space to "simulate" the \n which count to 1 car.
    concatenated_text = ' '.join(list_of_line)
    return concatenated_text[index]

# Liste qui va contenir tous les tuples d'information de chaque fichier, qu'on pourra ensuite ordonnée par n° de fragment.
data_extract_from_all_files = []

# On extrait les données de chaque fichiers utiles.
for file in interested_files:
    data = extact_header_from_file(file=file)
    data_extract_from_all_files.append(data)

# On ordonne la liste.
data_extract_from_all_files = sorted(data_extract_from_all_files, key=lambda x: x[0])

# On a plus qu'à afficher les données à la seconde place du tuple.
print(f"Le message caché Vogon est : \n{''.join([msg[1] for msg in data_extract_from_all_files])}")
# Le message caché Vogon est : 
# Après la Terre, nous devrons détruire barnard star b
