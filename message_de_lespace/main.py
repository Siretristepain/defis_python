import os

def check_sequence(a: str):
    """Fonction qui vérifie si dans une chaine de caractère donné il existe des groupes de 4 lettres
    successives présentant des doublons.

    Args:
        a (str): la chaîne de caractère à vérifier.

    Returns:
        bool: True si la str est valide (aucun groupe de 4 lettres avec doublons), False sinon.
    """

    b = list(a)
    for i in range(len(a)-3):
        if len(set(b[i:i+4])) != 4:
            return False
    return True

def process_a_file(file_path: str):

    no_doublon = 0

    with open(file_path, 'r') as f:
        content = [line.rstrip('\n') for line in f.readlines()]
    
    for line in content:
        if check_sequence(line):
            no_doublon += 1

    if no_doublon < 172 or no_doublon > 235:
        return file_path[-7:-4]

    return False

# print(process_a_file(file_path='./message_de_lespace/input/enreg180.txt'))



def resolution():
    path_to_all_file = './message_de_lespace/input'
    files = os.listdir(path_to_all_file)

    suspect_files = []

    for file in files:
        check = process_a_file(file_path=f"./message_de_lespace/input/{file}")

        if check != False:
            suspect_files.append(check)
    
    return suspect_files


print(resolution())
#['010', '084', '093', '135', '334', '336', '386', '411', '493']
#10, 84, 93, 135, 334, 336, 386, 411, 493
