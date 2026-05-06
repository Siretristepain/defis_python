def solve_problem(x: int, y: int, z: int, d: int, f: int) -> int:
    """
    Fonction qui donne le nombre de jour nécessaire à l'escargot pour monter la tour à partir des infos nécessaires.

    Args:
        x (int): distance montée par jour (cm).
        y (int): distance descendue par nuit (cm).
        z (int): objectif de hauteur a atteindre (cm).
        d (int): delta de x de jour en jour (dans l'énoncé, on dit que chaque jour l'escargot monte 2cm de moins que la veille) (cm).
        f (int): fréquence des jours de pluie (en jours).

    Returns:
        int: le nombre de jours nécessaires pour atteindre ``z`` cm en montant ``x`` cm / jour et en tombant de ``y`` cm / nuit, en montant chaque jour ``d`` cm de moins que la veille et en retombant tous les ``f`` jours à l'endroit où on était 48h plus tôt.
    """

    # =====
    # START
    # =====

    day = 0
    actual_position = 0
    rain = False

    # Liste qui contient la position de l'escargot à la fin de chaque nuit (utile pour les jours de pluie).
    recap = []

    while actual_position < z:

        # ===========
        # CHECK PLUIE
        # ===========

        if day != 0 and (day+1) % f == 0:
            rain = True
            # print(f"It's raining day {day}.")

        # ====
        # JOUR
        # ====

        # Le premier jour, l'escargot grimpe de x cm, puis de x-d cm, puis x-d cm, ... (d cm en moins chaque jour. d=2 dans l'énoncé).
        actual_position += (x - day * d)

        print(f"Fin du jour {day},        hauteur = {actual_position} cm.")

        # ==============
        # CHECK OBJECTIF
        # ==============

        if actual_position >= z:
            print(f"Objectif atteint en {day} jours !")
            return day

        # ====
        # NUIT
        # ====
        # Si l'objectif n'est pas encore atteint, la nuit passe et l'escargot redescends (et s'il pleut, il redescends à l'endroit où il était 48h plus tôt, soit 2j avant).
        if rain:
            actual_position = recap[-2]
            # On repasse notre booléen de pluie à False, sinon il repleuvra la nuit suivante et ainsi de suite.
            rain = False
        else:
            actual_position -= y

        print(f"Fin de la nuit {day}, hauteur : {actual_position} cm.")

        recap.append(actual_position)

        # =======
        # NEW DAY
        # =======
        day += 1

if __name__ == '__main__':
    # L'escargot cherche à atteindre 32400cm, en montant 1170cm/j et en redescendant 290cm/j (nuit), en montant chaque jour 2cm de moins que la veille, et avec une pluie tous les 5j.
    solve_problem(x=1170, y=290, z=32400, d=2, f=5)

"""
...
Fin de la nuit 61, hauteur : 31146 cm.
Fin du jour 62,        hauteur = 32192 cm.
Fin de la nuit 62, hauteur : 31902 cm.
Fin du jour 63,        hauteur = 32946 cm.
Objectif atteint en 63 jours !
"""
