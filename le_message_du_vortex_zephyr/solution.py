import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utile.alphabet import alphabet

def search_by_index(index: int):
    for k, v in alphabet.items():
        if v == index:
            return k
    return False

def decryptage(text: str, initial_move: int, increment: int):

    # Retire les espaces
    text = text.replace(" ","")
    text = text.lower()

    decrypted_text = []

    for i in range(len(text)):
        
        # Gestion du premier car
        if i == 0:
            true_position = abs(alphabet[text[i]] - initial_move)
            true_position = true_position % 26
            if true_position == 0:
                true_position = 26
            decrypted_text.append(search_by_index(true_position))
            continue

        # Traitement normal
        true_position = alphabet[text[i]] - (initial_move + i * increment)
        true_position = true_position % 26
        if true_position == 0:
            true_position = 26
        decrypted_text.append(search_by_index(true_position))

    return ''.join(decrypted_text).upper()

# print(decryptage(text="snpkvqlinftn", initial_move=3, increment=10))

def resolution(text: int):
    for d in range(1,27):
        for i in range(1,27):
            text_to_show = decryptage(text=text, initial_move=d, increment=i)
            with open("./le_message_du_vortex_zephyr/output.txt", 'a') as f:
                f.write(f"""
_____________________________________________
D = {d}, i = {i}
{text_to_show}
_____________________________________________
""")

    return True

resolution(text="HFKAO ZTEIA ZPJNT VASWY FBRMO GUOYA GJFWP IIOVU KELHBOXMAG JOLEK WHELH XEXDJ HCEWU XPHCK VBULC LEMOM HZ")
