import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utile.alphabet import alphabet
""" 
Même si j'ouvre VSCode dans le dossier racine defis_python et que j'execute mon script recherche.py,
alors le "répertoire courant" devient celui où se trouve le script executé. Donc il ne trouve pas
le package utile. C'est pour ça que je dois au préalable l'ajouter au PYTHONPATH via le module sys.
"""

""" 
Je vais commencer par coder un script de chiffrement pour me donner des idées afin de résoudre le problème.
"""

def search_by_index(index: int):
    for k, v in alphabet.items():
        if v == index:
            return k
    return False

def cryptage(text: str, initial_move: int, increment: int):
    crypted_text = []

    # On enlève les espaces
    text = text.replace(" ", "")

    for i in range(len(text)):
        # Gestion du premier car
        if i == 0:
            position_hide = alphabet[text[i]] + initial_move
            position_hide = position_hide % 26
            crypted_text.append(search_by_index(position_hide))
            continue

        # Traitement normal
        position_hide = alphabet[text[i]] + initial_move + i*increment
        position_hide = position_hide % 26
        crypted_text.append(search_by_index(position_hide))

    return ''.join(crypted_text).upper()

print(cryptage(text='pas de panique', initial_move=3, increment=10))