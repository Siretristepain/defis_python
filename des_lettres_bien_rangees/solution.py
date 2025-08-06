import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utile.alphabet import alphabet, accent_car

def check_word(word: str):
    """Fonction qui vérifie si un mot est bien rangé ou pas.
    Un mot est bien rangé si toutes les lettres qui le compose sont dans l'ordre alphabétique.

    Args:
        word (str): le mot a vérifié.

    Returns:
        _bool_: True si le mot est bien rangé, False sinon.
    """

    for i in range(1, len(word)):
        current_letter = word[i]
        previous_letter = word[i-1]

        # Gestion des caractères accentués
        if current_letter in accent_car.keys():
            current_letter = accent_car[current_letter]

        if previous_letter in accent_car.keys():
            previous_letter = accent_car[previous_letter]
        
        if alphabet[current_letter] < alphabet[previous_letter]:
            return False
    return True

# print(check_word('äbc'))

def resolve():
    """Fonction qui résouds le problème donné, à savoir : trouver le nombre de mot d'au moins 3 lettres bien rangés
    dans le fichier input.txt .

    Returns:
        nb_words (int): le nombre de mots d'au moins 3 lettres bien rangés trouvés.
    """

    nb_words = 0

    with open("des_lettres_bien_rangees/input.txt", 'r', encoding='utf-8') as f:
        content = [word.rstrip('\n') for word in f.readlines()]
    
    for word in content:
        if len(word) >= 3 and check_word(word=word.lower()):
            nb_words += 1

    return nb_words

print(f"Il y a : {resolve()} mots bien rangés d'au moins 3 lettres.")
# ---> 131
