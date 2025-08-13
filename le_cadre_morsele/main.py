import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utile.alphabet import morse_str

img = mpimg.imread("./le_cadre_morsele/src/cadre_morsele.png")

def filtre_all_pixel(img_origin):
    im = np.copy(img_origin)
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            r, v, b = im[i, j]
            if (r, v, b) != (0, 0, 0):
                im[i, j] = (1, 1, 1)
    return im

white_black = filtre_all_pixel(img_origin=img)
# print(type(white_black))
# plt.imshow(white_black)
# plt.show()

first_band = white_black[:,0,0]
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

        for letter in letters:
            # hide_letter = [key for key, value in morse_str.items() if value == letter]
            hide_letter = [key if value == letter else '%' for key, value in morse_str.items()]
            result.append(hide_letter[0])

    return ''.join(letter)

# convert_one_sequence(first_band)
# print(convert_sequence_to_str(first_band))
print(translate_sequence(first_band))
