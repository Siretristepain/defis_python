with open("./journee_de_troc_de_baguettes/src/input_for_example.txt", "r") as f:
    content = [line.rstrip('\n') for line in f.readlines()]

print(content)

def find_all_trades(first_student: str, second_student: str):
    """Fonction qui prends le noms de 2 élèves d'un échange et qui retourne la liste de tous les AUTRES échanges où l'un des 2 élèves apprait.
    Attention : la fonction ne retourne pas l'échange où les 2 éléves apparaissent ensemble en même temps !

    Args:
        first_student (str): le prénom du premier élève de l'échange.
        second_student (str): le prénom du second élève de l'échange.

    Returns:
        keep_trades (list) : liste des échanges où first_student OU second_student apparaissent (mais pas en même temps).
    """

    keep_trades = []
    for trade in content:
        if first_student in trade and not second_student in trade:
            keep_trades.append(trade)
        elif second_student in trade and not first_student in trade:
            keep_trades.append(trade)
    
    return keep_trades

# print(find_all_trades(first_student='Harry', second_student='Pansy'))
