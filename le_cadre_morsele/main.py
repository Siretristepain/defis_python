import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utile.alphabet import morse_str

img = mpimg.imread("./le_cadre_morsele/src/cadre_morsele.png")

def filtre_all_pixel(img_origin):
    """Fonction qui permet de convertir tous les pixels d'une image en blanc s'ils n'étaient pas 100% blancs à l'origine
    et en noir s'ils étaient blancs à l'origine.

    Du coup, les pixels du cadre cachant des points en morse seront blancs et tous les espaces en noirs (et pas l'inverse).
    En effet, il faut comprendre que quand on affiche une matrice via imshow :
    - les pixels 1 apparaissent en blanc.
    - les pixels 0 apparaissen en noir.

    Or, dans mon dictionnaire de transcription alphabet/morse, les points et les traits de morse sont symboliser par
    des 1 et les espacements par des 0. On voit donc le problème apparaitre. C'est pour ça que cette fonction est un peu
    contre intuitive en créant les pixels "pleins" en blanc (--> donc valeur 1) et les pixels "vides" en noir (--> donc valeur 0).

    Args:
        img_origin (ndarray): l'image à traiter.

    Returns:
        im (ndarray): copie de l'image d'origine modifiée.
    """

    im = np.copy(img_origin)
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            r, v, b = im[i, j]

            # On convertis les pixels non 100% noirs en noir
            if (r, v, b) != (0, 0, 0):
                im[i, j] = (0, 0, 0)
            
            # On convertis les pixels 100% en 100% blancs
            else:
                im[i, j] = (1, 1, 1)

    return im

# white_black = filtre_all_pixel(img_origin=img)
# print(type(white_black))
# plt.imshow(white_black)
# plt.show()

# first_band = white_black[0,:,0]
# print(type(first_band[0]))

def convert_sequence_to_str(sequence):
    return np.array2string(sequence).removeprefix('[').removesuffix(']').replace(' ', '').replace('.', '').replace('\n', '')

def split_by_words(sequence: str):
    return sequence.split('0000000')

def split_by_letter(word: str):
    return word.split('000')

def translate_sequence(sequence):

    result = []

    # On convertis notre sequence en str
    sequence = convert_sequence_to_str(sequence)

    # On sépare les mots de notre sequence
    sequence = split_by_words(sequence)

    for word in sequence:
        letters = split_by_letter(word)
        result.append(' ') # Ajout d'un espace entre chaque mot

        for letter in letters:
            # hide_letter = [key for key, value in morse_str.items() if value == letter]
            try:
                hide_letter = [key for key, value in morse_str.items() if value == letter]
                result.append(hide_letter[0])
            except:
                pass
            

    return ''.join(result)

# convert_one_sequence(first_band)
# print(convert_sequence_to_str(first_band))
# print(translate_sequence(first_band))

first_row = img[0,:,:]
last_column = img[1:,-1,:]
cadre = np.concatenate([first_row, last_column])
# print(cadre.shape)
cadre = cadre.reshape(cadre.shape[0], 1, cadre.shape[1])
# print(cadre)

sequence = filtre_all_pixel(cadre)
print(sequence[:,0,0])
print(sequence.shape)
print(translate_sequence(sequence[:,0,0]))
print(convert_sequence_to_str(sequence[:,0,0]))
