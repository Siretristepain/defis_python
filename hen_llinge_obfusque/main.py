def suppr_doublon(msg: str, running: bool = True):
    """
    Fonction récursive permettant de supprimer tous les motifs 'xX' d'une chaîne de caractères.
    La condition d'arrêt de la fonction est donnée via la booléen 'running' en argument.

    Args:
        - msg (str) : la chaîne de caractère dont on souhaite supprimer les motifs 'xX'.
        - running (bool) (default : True) : utile dans la fonction pour savoir si le traitement est terminé ou non.

    Returns:
        msg (str) : la chaîne de caractère vidée de ses motifs 'xX'.

    Example :
        suppr_doublon(msg="boOnjoOur")
        --> "bnjur"
    """

    # Condition d'arrêt
    if not running:
        return msg

    # On récupère l'index du premier doublon de la chaîne
    index = find_index_doublon(msg)
    if index == -1:
        running = False
        return suppr_doublon(msg, running=False)

    # On supprime 2 fois d'affilée à cet index car la première fois, ça va "décaler" toute la partie droite de la chaîne vers la gauche d'un cran, or on souhaite supprimer les 2 lettres du motif
    msg_list = list(msg)
    msg_list.pop(index)
    msg_list.pop(index)

    msg = ''.join(msg_list)
    return suppr_doublon(msg, running=True)


def find_index_doublon(msg):
    """
    Fonction qui permet de trouver l'index du premier motif 'xX' dans une chaîne de caractère.

    Args:
        - msg (str) : la chaîne de caractère dans laquelle on souhaite trouver l'index d'un doublon 'xX'.

    Returns:
        - i (int) : l'index du doublon 'xX', ou -1 si aucun doublon 'xX' n'est trouvé.

    Example:
        find_index_doublon("boOnjoOur")
        --> 1
    """

    # Tips : pour identifier un doublon 'xX', il faut que x et X soient différent (casse), que x soit bien en minuscule et que si on consertis X en minuscule, alors x et X soient égaux.
    for i in range(len(msg)-1):
        if (msg[i] != msg[i+1]) and (msg[i] == msg[i].lower()) and (msg[i].lower() == msg[i+1].lower()) :
            return i
    return -1


# print(find_index_doublon("boOnjour"))
# print(suppr_doublon("boOnjoOur"))

print(suppr_doublon(
    msg="""MzZfiIFmMpPizwWZkbByYKfFjJkKusSbBUplLqisSlLdDIQPnrRnuUuUsgkKfFdDGSxhHmMmMXgGjaAJpzZpeEPPnNpncmMinNIwpPWfFcCCNPnqQxXNeqQhHraefFEdkKDpmMPARaqQqQikjJKmMoOIrRpPoOnNmyYMfFxXkoOsSKzZwefFEWvV yYyYjJpPEviIzeExXZxgGwWjkKJXmMxXVvVkqQoOagxXGeEAoOpPtTntTNnNKjtTxXwWgGJunjJdDoONUspPSutTtgGTUhHqlLrRQmuUjJnwfFWNxXpzZPyYlLzZMoOnweEfFWkwpPjJWnNxXKyYjJyYfFuUicbBCcCpuUoOPoeEoOsgwWsaAsSSjJGkKeEnNSpPvVsmyYMoOsSSOxXdyqQzZmMmMYnNDd"""
))

# --> Minnea Enid
# Ce qui signifie en Hen Llinge "Aimer les paquerettes".
