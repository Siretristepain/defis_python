import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utile.alphabet import alphabet

# On ajoute les caractères _ et . au dictionnaire de l'alphabet de mon package utile
alphabet['_'] = 27
alphabet['.'] = 28


def move_rotor(configuration: list):
    """Fonction qui permet de faire tourner d'un cran un rotor.
    Cela consiste seulement à décaler la liste d'un cran vers la gauche.

    Args:
        configuration (list): la configuration du rotor au temps T.

    Returns:
        configuration (list): la configuration du rotor au temps T+1.
    """

    configuration.append(configuration[0])
    configuration.remove(configuration[0])
    return configuration


# print(move_rotor(configuration=['a','b','c','d']))

def resolution(msg_crypted: str):
    order = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','.']
    rotor_1 = ['U','S','K','F','E','V','I','Y','W','Z','T','X','A','G','C','Q','N','B','M','O','D','H','L','R','_','P','J','.']
    rotor_2 = ['X','H','V','N','D','C','R','Z','Q','P','S','B','_','O','K','T','.','L','U','W','G','J','M','E','F','A','I','Y']
    rotor_3 = ['A','W','Y','J','L','F','O','V','_','T','I','Q','M','Z','E','R','X','U','S','D','K','B','P','N','G','C','.','H']
    reflecteur = ['.','X','F','_','J','C','Y','I','H','E','L','K','N','M','P','O','Z','T','W','R','V','U','S','B','G','Q','D','A']
    msg_decrypted = []

    i = 0

    for car in msg_crypted:

        i += 1

        # Je dois d'abord retrouver l'indice de la lettre à traduire dans l'alphabet
        car_index = alphabet[car.lower()]

        # Grâce à l'indice précédent, je peux retrouver en quelle lettre elle a été transformer dans le rotor 1
        car_rotor_1 = rotor_1[car_index - 1]

        # Maintenant je dois retrouver l'indice de la nouvelle lettre dans l'alphabet
        car_rotor_1_index = alphabet[car_rotor_1.lower()]

        # Grâce à l'indice précédent, je peux retrouver en quelle lettre elle a été transformer dans le rotor 2
        car_rotor_2 = rotor_2[car_rotor_1_index - 1]

        # Maintenant je dois retrouver l'indice de la nouvelle lettre
        car_rotor_2_index = alphabet[car_rotor_2.lower()]

        # Grâce à l'indice précédent, je peux retrouver en quelle lettre elle à été transformer dans le rotor 3
        car_rotor_3 = rotor_3[car_rotor_2_index - 1]

        # Maintenant qu'on connait la lettre qui entre dans le réflecteur, on va pouvoir retrouver la lettre qui va en sortir, mais d'abord il nous faut son index
        car_rotor_3_index = alphabet[car_rotor_3.lower()]
        car_reflecteur = reflecteur[car_rotor_3_index - 1]

        # À partir de là on amorce le retour de la gauche vers la droite (réflecteur --> rotor 1)
        # L'opération est maintenant différente : maintenant on regarde dans le rotor dans lequel on rentre
        # l'index de la lettre qui entre et on regarde à quel index cela corresponds dans l'ordre de l'alphabet.

        # Traitement du rotor 3
        car_rotor_3_return_index = rotor_3.index(car_reflecteur)
        car_rotor_3_return = order[car_rotor_3_return_index]

        # Traitement du rotor 2
        car_rotor_2_return_index = rotor_2.index(car_rotor_3_return)
        car_rotor_2_return = order[car_rotor_2_return_index]

        # Traitement du rotor 1
        car_rotor_1_return_index = rotor_1.index(car_rotor_2_return)
        car_rotor_1_return = order[car_rotor_1_return_index]

        msg_decrypted.append(car_rotor_1_return)

        # Rotation des rotors
        #====================

        # On tourne le rotor 1 à chaque itération
        rotor_1 = move_rotor(configuration=rotor_1)

        # On tourne le rotor 2 toutes les 5 itérations
        if i % 6 == 0:
            rotor_2 = move_rotor(configuration=rotor_2)

        # On tourne le rotor 3 toutes les 25 itérations
        if i % 26 == 0:
            rotor_3 = move_rotor(configuration=rotor_3)

    return ''.join(msg_decrypted)

print(resolution(msg_crypted="_ZP_KMSOXEPOKXWZGBWWDNLAGJYQUI.HUHNGVQKOJNGJ.URCEXJQIPADGMW.VQDVBLNHWV.VPVRWGTTPI_UJACKLSFWBUUQZYTNOLEP.JHYLXFTBNYGKOBKK_UGOT_PXVVSULWWAMKBDWHZNZUNX_UICRW.YLMLGDPARIFKJAQYQL.SHUFWJTTZPLPQLBUDFZQVVRCWXQEWPPSDX"))