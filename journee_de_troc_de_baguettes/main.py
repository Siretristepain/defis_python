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

def find_all_names(trades: list, first_student: str, second_student: str):
    """Fonction qui retourne la liste de tous les prénoms autre que first_student ou second_student qui apparaissent dans l'ensemble des
    échanges contenu dans trades.

    Args:
        trades (list): liste des échanges où l'on veut récupérer les prénoms.
        first_student (str): le prénom du premier élève pour lequel on ne veut pas récupérer le prénom.
        second_student (str): le prénom du second élève pour lequel on ne veut pas récupérer le prénom.

    Returns:
        all_names (list) : liste des prénoms souhaités.
    """

    all_names = []
    for trade in trades:
        left_student_trade = trade.split(' ')[0]
        right_student_trade = trade.split(' ')[1]

        if left_student_trade not in [first_student, second_student] and left_student_trade not in all_names:
            all_names.append(left_student_trade)
        if right_student_trade not in [first_student, second_student] and right_student_trade not in all_names:
            all_names.append(right_student_trade)

    return all_names

# others_trades = find_all_trades(first_student='Harry', second_student='Pansy')
# print(others_trades)
# others_students = find_all_names(trades=others_trades, first_student='Harry', second_student='Pansy')
# print(others_students)

def count_occurences_student_in_collection(trades: list, student: str):
    """Fonction qui permet de compter le nombre de fois que le prénom d'un élève (student) apparait dans un ensemble d'échange (trades).

    Args:
        trades (list): l'ensemble d'échange dans lequel chercher le prénom de l'élève.
        student (str): le prénom de l'élève que l'on recherche dans les échanges.

    Returns:
        counter (int) : le nombre de fois que le prénom de l'élève apparait dans les échanges.
    """

    counter = 0
    for trade in trades:
        if student in trade:
            counter += 1

    return counter

# print(count_occurences_student_in_collection(trades=content, student='Harry'))

# ==========
# Résolution
# ==========

with open("./journee_de_troc_de_baguettes/src/input_for_example.txt", "r") as f:
    content = [line.rstrip('\n') for line in f.readlines()]

print(content)

keep_trades = []

for trade in content:
    left_student = trade.split(' ')[0]
    right_student = trade.split(' ')[1]

    epsilon = find_all_trades(first_student=left_student, second_student=right_student)

    others_students = find_all_names(trades=epsilon, first_student=left_student, second_student=right_student)

    i = 0

    for other_student in others_students:
        i += 1
        occurences_in_all_trades = count_occurences_student_in_collection(trades=content, student=other_student)
        occurences_in_epsilon = count_occurences_student_in_collection(trades=epsilon, student=other_student)

        if occurences_in_all_trades > occurences_in_epsilon:
            continue
        else:
            break

    if i == len(others_students):
        keep_trades.append(trade)

print(f"Les échanges à faire sont : {keep_trades}.")
