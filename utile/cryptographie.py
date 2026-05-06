from .alphabet import alphabet_from_zero
import math

# =====
# CESAR
# =====

def cesar_crypt_letter(a: str, decalage: int) -> str:
    """
    Fonction qui chiffre une lettre ``a`` en une autre via la méthode de César, c'est à dire via un décalage dans l'alphabet ``decalage``.

    Args:
        a (str): la lettre a chiffrer.
        decalage (int): le décalage à faire dans l'alphabet.

    Returns:
        str: la lettre chiffrée.
    """
    pos_a = alphabet_from_zero[a]

    return [key for key, value in alphabet_from_zero.items() if value == (pos_a + decalage)%26][0]

def cesar_crypt_text(text_to_crypt: str, decalage: int, keep_spaces: bool=True):
    """
    Fonction qui permet de chiffrer un text via la méthode de César.

    Args:
        text_to_crypt (str): le texte a chiffrer.
        decalage (int): le décalage a faire dans l'alphabet.
        keep_spaces (bool, optional): Défini si on conserve les espaces du texte d'entrée dans le texte de sortie. Defaults to True.

    Returns:
        _type_: le texte chiffré.
    """
    result = []

    if not keep_spaces:
        text_to_crypt = text_to_crypt.replace(' ', '')

    for car in text_to_crypt:
        if keep_spaces and car == ' ':
            result.append(' ')
            continue
        result.append(cesar_crypt_letter(car, decalage))

    return ''.join(result)

# ========
# VIGENERE
# ========

def vigenere_crypt_letter(a: str, b: str) -> str:
    """Fonction pour chiffrer une lettre via la méthode de Vigenère.

    Args:
        a (str): lettre à chiffrer.
        b (str): lettre de la clé correspondante.

    Returns:
        str: la lettre chiffrée.
    """
    pos_a = alphabet_from_zero[a]
    pos_b = alphabet_from_zero[b]

    return [key for key, value in alphabet_from_zero.items() if value == (pos_a + pos_b) % 26][0]

def vigenere_crypt_text(text: str, key: str, keep_spaces: bool = False) -> str:
    """Fonction pour chiffre un ``text`` via la méthode de Vigenère.

    Args:
        text (str): texte à chiffrer.
        key (str): clé utilisée.
        keep_spaces (bool, optional): Défini si les espaces du ``text`` d'entrée doivent être conservé dans l'outpout. Defaults to False.

    Returns:
        str: le texte chiffré.
    """
    if not keep_spaces:
        text = text.replace(' ', '')
    coef = math.ceil(len(text) / len(key))
    repeated_key = key * coef
    output = []

    spaces_counter = 0
    for i in range(len(text)):
        if text[i] == ' ' and keep_spaces:
            output.append(' ')
            spaces_counter += 1
            continue
        output.append(vigenere_crypt_letter(a=text[i], b=repeated_key[i - spaces_counter]))

    return ''.join(output)

def vigenere_decrypt_letter(a: str, b: str) -> str:
    """Fonction pour déchiffrer une lettre chiffrée ``a`` via la méthode de Vigenère en utilisant la lettre ``b`` de la clé.

    Args:
        a (str): lettre à déchiffrer.
        b (str): lettre correspondante de la clé.

    Returns:
        str: la lettre déchiffrée.
    """
    pos_a = alphabet_from_zero[a]
    pos_b = alphabet_from_zero[b]

    return [key for key, value in alphabet_from_zero.items() if value == (pos_a + (26 - pos_b)) % 26][0]

def vigenere_decrypt_text(text: str, key: str, keep_spaces: bool = True) -> str:
    """Fonction pour déchiffrer un ``text`` via la méthode de Vigenère avec la clé ``key``.

    Args:
        text (str): le texte à déchiffrer.
        key (str): la clé.
        keep_spaces (bool, optional): Défini si les espaces du texte chiffré doivent être conservés dans le texte déchiffré. Defaults to True.

    Returns:
        str: le texte déchiffré.
    """
    coef = math.ceil(len(text) / len(key))
    repeated_key = key * coef
    output = []
    spaces_counter = 0

    for i in range(len(text)):
        if text[i] == ' ':
            output.append(' ')
            spaces_counter += 1
            continue

        output.append(vigenere_decrypt_letter(a=text[i], b=repeated_key[i-spaces_counter]))

    return ''.join(output)

def vigenere_find_letter(a: str, b: str) -> str:
    """Fonction pour retrouver la lettre de la clé nécessaire pour chiffrer ``b`` pour obtenir ``a``.

    Args:
        a (str): lettre chiffrée.
        b (str): lettre de base souhaitée.

    Returns:
        str: la lettre pour chiffrer ``b`` en ``a``.
    """
    pos_a = alphabet_from_zero[a]
    pos_b = alphabet_from_zero[b]

    if pos_a > pos_b:
        return [key for key, value in alphabet_from_zero.items() if value == pos_a - pos_b][0]
    
    if pos_a == pos_b:
        return 'a'
    
    if pos_a < pos_b:
        return [key for key, value in alphabet_from_zero.items() if value == 26 + (pos_a - pos_b)][0]

def vigenere_find_key(text_crypt: str, text_wish: str) -> str:
    """Fonction pour trouver la clé nécessaire pour chiffrer le ``text_wish`` en ``text_crypt`` selon la méthode de Vigenère.

    Args:
        text_crypt (str): le message chiffré.
        text_wish (str): le message souhaité initial.

    Returns:
        str: la clé de chiffrement nécessaire.
    """
    output = []

    for i in range(len(text_crypt)):
        output.append(vigenere_find_letter(a=text_crypt[i], b=text_wish[i]))

    return ''.join(output)

def vigenere_all_potential_keys(text_crypt: str, existing_word: str, indexed_keys: bool=False) -> list:
    """
    Fonction utilisée lorsque l'on a un texte chiffré ``text_crypt`` avec la méthode de Vigenère mais que l'on sait qu'il existe
    le mot ``existing_word`` quelque part dans le text.
    La fonction retourne toutes les clés possibles (car la clé dépends forcément de l'endroit où se trouve ``existing_word``).

    TODO: Gérer les espaces. Pour l'instant je supprime tous les espaces du texte chiffré entrant.

    Args:
        text_crypt (str): le texte chiffré dont on sait qu'il contient ``existing_word``.
        existing_word (str) : le mot dont on sait qu'il est présent quelque part dans ``text_crypt``.

    Returns:
        all_potentials_keys (list): liste de toutes les clés potentielles.
    """

    all_potentials_keys = []

    text_crypt = text_crypt.replace(' ', '')

    for i in range(len(text_crypt) - (len(existing_word)-1)):
        crypt_word = text_crypt[i: i+len(existing_word)]

        if indexed_keys:
            all_potentials_keys.append((i, vigenere_find_key(text_crypt=crypt_word, text_wish=existing_word)))
        else:
            all_potentials_keys.append(vigenere_find_key(text_crypt=crypt_word, text_wish=existing_word))

    return all_potentials_keys

if __name__ == '__main__':
    # print(vigenere_crypt_letter('b', 'p'))
    # print(vigenere_crypt_text(text="bonjour je m appelle russel et vous", key="pizza"))
    # print(vigenere_crypt_text(text="qwmiojzidmpxodlamqtshmkdtkwtr", key="pizza"))
    # print(vigenere_decrypt_letter(a='h', b='p'))
    # print(vigenere_decrypt_text(text="qwmiojz id m pxodlam qtshmk dt kwtr", key="pizza"))
    # print(vigenere_find_letter(a='h', b='s'))
    # print(vigenere_find_key(text_crypt="hiktt", text_wish="salut"))
    
    print(vigenere_crypt_text(text="caca", key="pipi", keep_spaces=True))
    # print(vigenere_decrypt_text(text="lakmg lg cccc", key="caca"))

    # print(vigenere_decrypt_text(text="CJKDPQZZZLSULOEXFPNMXOSVLJSVRHRMFFOABIKBZFJM".lower(), key="proxima"))

    print(vigenere_find_key(text_crypt="riri", text_wish="caca"))