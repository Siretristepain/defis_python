with open("./journee_de_troc_de_baguettes/src/input.txt", "r") as f:
    content = [line.rstrip('\n') for line in f.readlines()]

print(content)

def get_all_student(trades: list):
    students = set()
    for trade in trades:
        left_student = trade.split(' ')[0]
        right_student = trade.split(' ')[1]

        students |= {left_student}
        students |= {right_student}
    
    return students

# print(get_all_student(trades=content))

def get_all_possibles_trades_for_student(trades: list):
    # Récupère la liste de tous les prénoms
    students = get_all_student(trades=trades)

    all_trades = {stud: [] for stud in students}
    
    for student in students:
        for trade in trades:
            left_student = trade.split(' ')[0]
            right_student = trade.split(' ')[1]  
            if left_student == student:
                all_trades[student].append(right_student)
            elif right_student == student:
                all_trades[student].append(left_student)
        
    return all_trades

# print(get_all_possibles_trades_for_student(trades=content))

def check_for_obvious_trades(dict_trades: dict):
    obvious_students = set()
    for student, trades in dict_trades.items():
        if len(trades) == 1:
            obvious_students |= {student}
            obvious_students |= {trades[0]}
    
    # for student in obvious_students:
    #     for k in dict_trades:
    #         if student in dict_trades[k]:
    #             dict_trades[k].remove(student)

    for student in obvious_students:
        dict_trades.pop(student)
    
    return dict_trades



def solve(trades: list):
    dictionnary_trades = get_all_possibles_trades_for_student(trades=trades)

    all_students = get_all_student(trades=trades)

    print(check_for_obvious_trades(dict_trades=dictionnary_trades))

    # student_already_trade = set()
    # i = 0
    # while len(student_already_trade) != all_students or i <= 100:

solve(trades=content)