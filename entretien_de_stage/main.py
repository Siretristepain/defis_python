import re

# ====================
# Ouverture du fichier
# ====================

with open("entretien_de_stage/src/input.txt", "r") as f:
    words = [line.split('\n')[0] for line in f.readlines()]

# =========
# Fonctions
# =========
def good_word(word: str) -> bool:
    """
    Aie aie aie, j'ai initialement mal compris l'exercice, et j'ai crus qu'il fallait trouver les mots d'au moins 12 lettres AVEC un 'e' en 3ème position
    ET avec exactement 3 'l'.

    Args:
        word (str): le mot pour lequel on souhaite vérifier les conditions.

    Returns:
        bool: True si toutes les conditions sont correctes, False autrement.
    """
    cond_1 = re.search('..e.........', word)
    cond_2 = len(re.findall(r'l', word)) == 3

    if cond_1 and cond_2:
        return True
    return False

def real_good_word(words: list[str]) -> list[int]:
    """
    Méthode qui cherche les mots qui remplissent l'une des 3 conditions suivantes dans la liste de mot ``words`` :
    - le mot a exactement 12 caractères.
    - le mot a un 'e' en troisième position.
    - le mot contient 2 'l'.

    Pour chaque condition, la méthode compte le nombre de mot qui match la condition et retourne une liste de ces 3 nombres (dans l'ordre des conditions explicitées ci-dessus).

    Args:
        words (list[str]): liste de mots dans laquelle on veut faire les recherches.

    Returns:
        list[int]: liste des 3 nombres : [nombre de mots de 12 lettres, nombre de mot avec un 'e' en 3ème, nombdre de mot contenant 2 'l']
    """
    # Initialize
    twelve_letters = 0
    third_e = 0
    three_l = 0

    # Loop
    for word in words:
        # Conditions
        cond_1 = re.search('^.{12}$', word)
        cond_2 = re.search('^..e.*', word)
        cond_3 = len(re.findall(r'l', word)) == 2

        # Vérifications
        if cond_1:
            twelve_letters += 1
        if cond_2:
            third_e += 1
        if cond_3:
            three_l += 1

    return [twelve_letters, third_e, three_l]

# ==========
# Résolution
# ==========

# result = [word for word in words if good_word(word)]
# print(f"Les mots corrects sont : {', '.join(result)}.")

print(real_good_word(words=words))
# [23, 13, 19]
