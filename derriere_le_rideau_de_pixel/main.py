import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


# ==============
# Ouvrir l'image
# ==============

img = mpimg.imread("derriere_le_rideau_de_pixel/src/message.png")

# ========
# Fonction
# ========

def decrypt_sequence(sequence: list) -> str:
    """
    Fonction qui prends en entrée une séquence (list), somme le nombre de pixel noir de cette séquence (valeur == 0) puis retourne le code ASCII correspondant à ce total.

    Args:
        sequence (list): la séquence dont on souhaite déterminé le code ASCII caché.

    Returns:
        str: le caractère caché dans la séquence.
    """
    tot = 0
    for pixel in sequence:
        if pixel == 0:
            tot += 1
    return chr(tot)

# On va faire apparaitre chaque caractère les uns à la suite des autres dans la liste result
result = []

for sequence in img:
    result.append(decrypt_sequence(sequence=sequence))

print(''.join(result))
# --> Agent 1337, l'échange aura lieu à Piccadilly Circus. Soyez à l'heure. Détruisez ce message.
