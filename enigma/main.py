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

def crypt_letter_by_rotor(letter_input: str, configuration: list):
    """Fonction qui permet de simuler le cryptage d'une lettre par un rotor en fonction de sa configuration.
    La fonction prends une lettre à crypter en entrée et retourne la lettre cryptée en sortie.

    Args:
        letter_input (str): la lettre à crypter.
        configuration (list): la configuration du rotor.

    Returns:
        (str) : la lettre cryptée.
    """

    # On cherche l'index dans l'alphabet de la lettre en entrée
    letter_index = alphabet[letter_input.lower()] - 1

    # On retourne l'élément de la configuration du rotor à l'indice correspondant à la lettre d'entrée dans l'alphabet
    return configuration[letter_index]

def decrypt_letter_by_rotor(letter_output: str, configuration: list):
    """Fonction qui permet de simuler le décryptage d'une lettre par un rotor en fonction de sa configuration.
    La fonction prends en entrée la lettre de sortie du rotor et sa configuration et retourne la lettre d'entrée du rotor.

    Args:
        letter_output (str): la lettre de sortie du rotor.
        configuration (list): la configuration du rotor.

    Returns:
        (str) : la lettre d'entrée du rotor.
    """

    # Liste des éléments de l'alphabet dans l'ordre
    order = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','.']

    # On recherche l'index dans le rotor de la lettre de sortie
    letter_index_in_rotor = configuration.index(letter_output)

    # On retourne l'élément de l'alphabet à l'indice correspondant à l'indice de la lettre de sortie dans le rotor
    return order[letter_index_in_rotor]

def resolution_bis(msg_crypted: str):
    rotor_1 = ['U','S','K','F','E','V','I','Y','W','Z','T','X','A','G','C','Q','N','B','M','O','D','H','L','R','_','P','J','.']
    rotor_2 = ['X','H','V','N','D','C','R','Z','Q','P','S','B','_','O','K','T','.','L','U','W','G','J','M','E','F','A','I','Y']
    rotor_3 = ['A','W','Y','J','L','F','O','V','_','T','I','Q','M','Z','E','R','X','U','S','D','K','B','P','N','G','C','.','H']
    reflecteur = ['.','X','F','_','J','C','Y','I','H','E','L','K','N','M','P','O','Z','T','W','R','V','U','S','B','G','Q','D','A']
    msg_decrypted = []

    i = 0

    for car in msg_crypted:

        i += 1
        
        # ========================
        # Trajet Droite --> Gauche
        # ========================

        # Rotor 1
        letter_input_rotor_1 = car
        letter_output_rotor_1 = crypt_letter_by_rotor(letter_input=letter_input_rotor_1, configuration=rotor_1)

        # Rotor 2
        letter_input_rotor_2 = letter_output_rotor_1
        letter_output_rotor_2 = crypt_letter_by_rotor(letter_input=letter_input_rotor_2, configuration=rotor_2)

        # Rotor 3
        letter_input_rotor_3 = letter_output_rotor_2
        letter_output_rotor_3 = crypt_letter_by_rotor(letter_input=letter_input_rotor_3, configuration=rotor_3)

        # ==========
        # Réflécteur
        # ==========

        letter_input_reflecteur = letter_output_rotor_3
        letter_output_reflecteur = crypt_letter_by_rotor(letter_input=letter_input_reflecteur, configuration=reflecteur)

        # ========================
        # Trajet Gauche --> Droite
        # ========================

        # Rotor 3
        letter_output_rotor_3_bis = letter_output_reflecteur
        letter_input_rotor_3_bis = decrypt_letter_by_rotor(letter_output=letter_output_rotor_3_bis, configuration=rotor_3)

        # Rotor 2
        letter_output_rotor_2_bis = letter_input_rotor_3_bis
        letter_input_rotor_2_bis = decrypt_letter_by_rotor(letter_output=letter_output_rotor_2_bis, configuration=rotor_2)

        # Rotor 1
        letter_output_rotor_1_bis = letter_input_rotor_2_bis
        letter_input_rotor_1_bis = decrypt_letter_by_rotor(letter_output=letter_output_rotor_1_bis, configuration=rotor_1)

        msg_decrypted.append(letter_input_rotor_1_bis)

        # ====================
        # Rotations des rotors
        # ====================

        # On tourne le rotor 1 à chaque itération
        rotor_1 = move_rotor(configuration=rotor_1)

        # On tourne le rotor 2 toutes les 28 itérations (c'est à dire à chaque révolution du rotor 1)
        if i % 28 == 0:
            rotor_2 = move_rotor(configuration=rotor_2)

        # On tourne le rotor 3 toutes les 784 itérations (c'est à dire à chaque révolution du rotor 2) -> On ne le tourne donc jamais puisqu'il y a moins de 784 caractères dans le message crypté
        if i % 784 == 0:
            rotor_3 = move_rotor(configuration=rotor_3)

    return ''.join(msg_decrypted)


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

# print(resolution(msg_crypted="_ZP_KMSOXEPOKXWZGBWWDNLAGJYQUI.HUHNGVQKOJNGJ.URCEXJQIPADGMW.VQDVBLNHWV.VPVRWGTTPI_UJACKLSFWBUUQZYTNOLEP.JHYLXFTBNYGKOBKK_UGOT_PXVVSULWWAMKBDWHZNZUNX_UICRW.YLMLGDPARIFKJAQYQL.SHUFWJTTZPLPQLBUDFZQVVRCWXQEWPPSDX"))


print(resolution_bis(msg_crypted="_ZP_KMSOXEPOKXWZGBWWDNLAGJYQUI.HUHNGVQKOJNGJ.URCEXJQIPADGMW.VQDVBLNHWV.VPVRWGTTPI_UJACKLSFWBUUQZYTNOLEP.JHYLXFTBNYGKOBKK_UGOT_PXVVSULWWAMKBDWHZNZUNX_UICRW.YLMLGDPARIFKJAQYQL.SHUFWJTTZPLPQLBUDFZQVVRCWXQEWPPSDX"))

# --> FELICITATIONS._VOUS_AVEZ_REUSSI_A_DECHIFFRER_CE_MESSAGE._L_INFORMATION_QUE_VOUS_DEVEZ_REMETTRE_POUR_PROUVER_QUE_VOUS_AVEZ_RELEVE_CE_DEFI_EST_LE_MOT_THOUEERIS._ATTENTION_A_NE_PAS_VOUS_TROMPER_DANS_LA_SAISIE...