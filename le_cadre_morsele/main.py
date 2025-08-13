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

def convert_sequence_to_str(sequence):
    return np.array2string(sequence).removeprefix('[').removesuffix(']').replace(' ', '').replace('.', '').replace('\n', '')

def convert_sequence_to_str_bis(sequence):
    result = []

    for i in sequence:
        result.append(str(int(i)))

    return ''.join(result)

def split_by_words(sequence: str):
    return sequence.split('0000000')

def split_by_letter(word: str):
    return word.split('000')

def translate_sequence(sequence):
    result = []

    # On convertis notre sequence en str
    sequence = convert_sequence_to_str_bis(sequence)

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


# img_black_white = filtre_all_pixel(img)

# line_1 = img_black_white[0,:,0]
# line_2 = img_black_white[1,:,0]
# line_3 = img_black_white[2,:,0]
# line_4 = img_black_white[3,:,0]
# line_5 = img_black_white[4,:,0]

# line_minus_5 = np.flip(img_black_white[-5,:,0])
# line_minus_4 = np.flip(img_black_white[-4,:,0])
# line_minus_3 = np.flip(img_black_white[-3,:,0])
# line_minus_2 = np.flip(img_black_white[-2,:,0])
# line_minus_1 = np.flip(img_black_white[-1,:,0])

# column_1 = np.flip(img_black_white[:,0,0])
# column_2 = np.flip(img_black_white[:,1,0])
# column_3 = np.flip(img_black_white[:,2,0])
# column_4 = np.flip(img_black_white[:,3,0])
# column_5 = np.flip(img_black_white[:,4,0])

# column_minus_5 = img_black_white[:,-5,0]
# column_minus_4 = img_black_white[:,-4,0]
# column_minus_3 = img_black_white[:,-3,0]
# column_minus_2 = img_black_white[:,-2,0]
# column_minus_1 = img_black_white[1:,-1,0]

# all_sequences = [line_1, column_minus_1, line_minus_1, column_1, \
#                  line_2, column_minus_2, line_minus_2, column_2, \
#                  line_3, column_minus_3, line_minus_3, column_3, \
#                  line_4, column_minus_4, line_minus_4, column_4, \
#                  line_5, column_minus_5, line_minus_5, column_5]

# for sequence in all_sequences:
#     print(translate_sequence(sequence))
#     print()

# sequence_total = np.concatenate([first_line, second_line])

# print(sequence_total.shape)
# print(sequence_total)
# print(translate_sequence(sequence_total))

zone = img[35, 769::4, 1]
print(zone*255)
# print(img[35, 769:, 1])
plt.imshow(zone.reshape(1, zone.shape[0], zone.shape[1]))
plt.show()