def compute_empreinte(address: str):
    """
    Fonction qui permet de calculer l'empreinte d'une adresse donnée en entrée.
    Pour rappel :

    l'empreinte d'une adresse corresponds à une chaine de caractères composée de chiffres et de lettre.
    Les lettres sont triées par ordre alphabétique et sont précédées de leur nombre d'occurrence.

    Ex : 
    address = 'bonjour'
    empreinte = '1b1j1n2o1r1u'

    Args :
        - address (str) : l'adresse dont on souhaite calculer l'empreinte.

    Returns :
        - empreinte (str) : l'empreinte correspondant à l'adresse.
    """
    # On commence par retirer les espaces dans l'adresse et les tirets
    address = address.replace(' ', '')
    address = address.replace('-', '')

    # On créer ensuite un set pour obtenir chaque lettre qui compose l'adresse (de façon unique)
    address_set = set(list(address))

    # On créer un dictionnaire qui affiche l'occurrence de chaque lettre dans l'adresse ( Ex : {'h': 2, 'b': 4, ...} )
    occurrences = {letter: address.count(letter) for letter in address_set}

    # Le dictionnaire précédent n'est pas trié par ordre alphabétique, on le fait donc ici de façon un peu cool
    sorted_occurrences = {letter: value for letter, value in sorted(occurrences.items(), key=lambda item: item[0])}

    # On génère l'empreinte à partir du dictionnaire trié des occurrences (on pourrait faire mieux c'est sûr, mais c'es simple et ça marche)
    empreinte = [(str(value), letter) for letter, value in sorted_occurrences.items()]

    empreinte = str(empreinte)

    empreinte = empreinte.replace("'", '')
    empreinte = empreinte.replace(",", '')
    empreinte = empreinte.replace("(", '')
    empreinte = empreinte.replace(")", '')
    empreinte = empreinte.replace("[", '')
    empreinte = empreinte.replace("]", '')
    empreinte = empreinte.replace(" ", '')

    return empreinte


# print(compute_empreinte('boulevard jean jaures'))


# On ouvre le fichier pour récupérer chaque adresse
with open('meli_melo_dadresses/src/input.txt', 'r') as f:
    content = [line.rsplit('\n')[0] for line in f.readlines()]

TARGET = "1a6e1g1i1l1m1n1o2r2s2u1y"

for address in content:
    if compute_empreinte(address) == TARGET:
        print(f"L'adresse correspondante est : {address} .")
        break

# L'adresse correspondante est : rue goya le mee-sur-seine .
