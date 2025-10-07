# Fonction de décompression de la chaîne
def unzip(chaine: str):
    """
    Fonction qui décompresse la chaîne passant en entrée.
    La fonction parcours la chaîne. Si elle rencontre un chiffre x, alors elle affichera x fois le caractères suivant.

    Ex :
    chaine = +B+BNB2N2+3NBN2B
    sortie = +B+BNBNN++NNNBNBB

    Args:
        - chaine (str) : la chaîne à décompresser.

    Returns:
        - (str) : la chaîne décompressée.
    """

    # result vas stocker les caractères qui vont apparaitre au fur et à mesure du traitement.
    # occurrence indique le nombre de fois que le caractère suivant va apparaitre dans result
    result = []
    occurrence = 1

    for car in chaine:
        for i in range(occurrence):
            result.append(car)

        if car.isdigit():
            occurrence = int(car)
        else:
            occurrence = 1

    # return ''.join(result).replace(lambda x: x.isdigit() == True, '') # Ne fonctionne pas car replace attends une str en 1er argument
    # On peut utiliser filter dans join pour définir une fonction lambda. Ici on s'en sert pour n'afficher que les caractères qui ne sont pas des nombres, compris dans result
    return ''.join(filter(lambda x: x.isdigit() == False, result))


print(unzip('+B+BNB2N2+3NBN2B'))
