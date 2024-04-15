dic = {
 "HFH":"A",
 "FFH":"B",
 "SHS":"C",
 "SHH":"D",
 "SSH":"E",
 "FHF":"F",
 "FSS":"G",
 "HFF":"H",
 "HHH":"I",#J
 "SFS":"K",
 "FFS":"L",
 "FHS":"M",
 "SSF":"N",
 "FHH":"O",
 "HHF":"P",
 "SFF":"Q",
 "FSF":"R",
 "FSH":"S",
 "HHS":"T",
 "FFF":"U",#V
 "SSS":"W",
 "HFS":"X",
 "SHF":"Y",
 "SFH":"Z",
}

with open('input.txt', 'r') as f:
    msg = f.read()


def resolution(phrase: str, dictionnaire: dict):
    """
    Fonction qui regarde les 3 premiers caractère d'une phrase :
    - si ils correspondent à une syllabe fourchelangue : elle traduit la syllabe puis elle supprime les 3 caratères et retourne la nouvelle phrase amputée des 3 caractères + la lettre traduite

    - si ils ne correspondent pas à une syllabe fourchelangue : cela signifie que la syllabe commence par "HS". Elle supprime donc uniquement les deux premiers caractère de la syllabe (le "HS") puis retourne la nouvelle phrase amputée des deux premières lettres + un espace    

    Args:
        phrase (str): la phrase à traduire 
        dictionnaire (dict): dictionnaire des correspondances fourchelague/alphabet

    Outputs:
        lettre (str) : la lettre ou l'espace correspondant à la traduction de la syllabe
        phrase (str) : la nouvelle phrase amputée de sa syllabe traduite
    """

    # On créer la liste des syllabes fourchelangu existantes à partir des clés du dictionnaire
    keys = [key for key in dictionnaire.keys()]

    # On récupère la première syllabe de la phrase fourchelangue
    syllabe = phrase[0] + phrase[1] + phrase[2]

    # On vérifie si cette syllabe fourchelangue existe
    if syllabe in keys:
        # Si la syllabe existe on la traduit
        lettre = dictionnaire[syllabe]
        
        # On supprime cette syllabe de la phrase
        phrase = phrase.removeprefix(syllabe)

    elif syllabe not in keys:
        # Si la syllabe n'existe pas, c'est que c'est un espace
        lettre = " "

        # On supprime uniquement les deux premières lettres de la phrase qui sont forcément des "HS"
        phrase = phrase.removeprefix("HS")

    # On retourne la lettre traduite et la nouvelle phrase
    return lettre, phrase 

"""
L'idée est d'utiliser récursivement cette fonction ci-dessus pour traduire le message au fur et à mesure.    
"""

# Liste dans laquelle on va faire apparaitre à chaque itération la lettre traduite
traduction = []

# On fait une boucle while tant que le msg n'est pas entièrement traduit
while msg != "":
    # On récupère la lettre traduite à chaque itération et msg devient la phrase amputée de la première syllabe à chaque nouveau tour de boucle
    lettre, msg = resolution(phrase=msg, dictionnaire=dic)
    traduction.append(lettre)

# On affiche le résultat
print(''.join(traduction))
