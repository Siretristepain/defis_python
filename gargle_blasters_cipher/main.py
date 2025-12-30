import math

# ========================
# Lire le fichier d'entrée
# ========================

# On récupère le contenu du fichier en une grosse liste dans laquelle chaque ligne est une sous-liste.

with open("gargle_blasters_cipher/input.txt", "r") as f:
    lines = [(line.split('\n')[0]).split(',') for line in f.readlines()]

# ==============
# Trouver la clé
# ==============

# On "applati" la grosse liste pour ne plus avoir de listes imbriquées.
all_lines = [item for line in lines for item in line]

key = []

# On parcours chaque élément du fichier et on compte son nombre d'occurrence. Si c'est 1, alors il fait parti de la clé.
# L'avantage de cette technique est de conserver l'ordre d'apparition des éléments qui composent la clé.
for elem in all_lines:
    if all_lines.count(elem) == 1:
        key.append(elem)

print(f"La clé est de taille {len(key)} et est : {key}.")

# =====================
# Déchiffrer le message
# =====================

# Constantes
msg = list('1jlXmyHooOo5Sfxrq7TyinEG2bHU67R.sv 3AJICAavmdbHjeWCpHvx0CHRyACcn')
LEN_MSG = len(msg)
LEN_KEY = len(key)
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ."

def extend_key_for_matching_msg_length(key: list) -> list:
    """
    Function pour répéter la clé autant que nécessaire pour qu'elle soit aussi grande que le message à décoder.
    
    :param key: la clé a potentiellement répéter.
    :type key: list
    :return: la clé dupliquée pour matcher la longueur exact du message à décoder.
    :rtype: list
    """
    coef = math.ceil(LEN_MSG / LEN_KEY)

    return (key*coef)[:LEN_MSG]


def xor(A: str, B: str):
    """
    Fonction qui réalise l'opération XOR (--> OU EXCUSIF) sur les opérandes ``A`` et ``B``, après les avoir convertis en binaire.

    Pour rappel, voici la table du XOR :

    A  |  B  |  XOR
    ________________
    0  |  0  |   0
    0  |  1  |   1
    1  |  0  |   1
    1  |  1  |   0

    --> On constate que XOR retourne 1 uniquement si A et B sont différents, 0 sinon.

    !! Attention !! Les 'A' et 'B' qui sont en arguments de la fonction sont différents de ceux du tableau du XOR ci-dessus.
    Dans les arguments, 'A' et 'B' sont des nombres sous forme de str comme '42', tandis que dans le tableau c'est des 0 ou des 1.
    (c'est à dire les nombres en argument tranformés en binaire).
    
    :param A: L'opérande gauche.
    :type A: str
    :param B: L'opérande droite.
    :type B: str
    """
    A = '{0:08b}'.format(int(A))
    B = '{0:08b}'.format(int(B))

    result = []

    for i in range(8):
        if A[i] == B[i]:
            result.append('0')
        else:
            result.append('1')

    # Pour convertir un nombre binaire en décimal, on utilise int avec une base 2.
    return int(''.join(result), 2)

decrypted_msg = []
repeated_key = extend_key_for_matching_msg_length(key=key)

# Boucle de décryptage caractère par caractère
for i in range(LEN_MSG):
    # On récupère le caractère du message à décrypter et sa position dans l'alphabet
    car_to_decrypt = msg[i]
    index_in_alphabet = ALPHABET.index(car_to_decrypt)

    # On applique le XOR entre la position dans l'alphabet du caractère à décrypter ET le caractère de la clé correspondant
    decrypted_car = xor(A=str(index_in_alphabet), B=repeated_key[i])

    # On fait apparaitre la position dans l'alphabet du caractère décodé dans la liste decrypted_msg.
    decrypted_msg.append(ALPHABET[decrypted_car])

print(f"Le message codé dit : {''.join(decrypted_msg)}.")
# --> Le message codé dit : Rendez vous au Milliways a 16h34 exactement la semaine derniere..
