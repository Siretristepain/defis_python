with open("donnees.txt", 'r') as f:
    content = [line.rstrip('\n') for line in f.readlines()]

col_gauche = []
col_droite = []

for line in content:
    col_gauche.append(line[8:12])
    col_droite.append(line[19:23])

# ===========
# Date unique
# ===========

dates_uniques = []

for date in col_gauche:
    if not date in dates_uniques:
        dates_uniques.append(date)

for date in col_droite:
    if not date in dates_uniques:
        dates_uniques.append(date)

print(f"Nombre de date unique : {len(dates_uniques)}")

# ==========
# Résolution
# ==========

""" 
Ma nouvelle idée c'est de prendre un ordre temporel aléatoire qui sera donc très probablement faux.
Ensuite, je vais lire ligne à ligne les conditions pour voir si elles sont vérifiées.
Un grand nombre d'entres elles ne le seront probablement pas.
Mon idée c'est que puisque ces conditions sont faciles à corriger, je vais les corriger pas à pas jusqu'à ce qu'il n'y en ai plus.
"""

# Mon ordre temporel aléatoire
ordre_temporel = dates_uniques
# print(ordre_temporel)

# =============
# Vérifications
# =============

def validation(ordre: list):
    for i in range(len(col_gauche)):
        date_before = col_gauche[i]
        date_after = col_droite[i]
        print(f"Date before = {date_before}")
        print(f"Date after = {date_after}")

        index_date_before = ordre.index(date_before)
        index_date_after = ordre.index(date_after)
        print(f"Index date before = {index_date_before}")
        print(f"Index date after = {index_date_after}")

        if index_date_before >= index_date_after:
            print(f"Il y a une erreur avec les date {date_before} et {date_after}")
            # ça vaut dire que date_before et date_after sont inversées
            return [date_before, date_after]
        
    # Si aucun problème, return True
    return True

# ===============================
# Fonction de correction d'erreur
# ===============================

def correction(ordre: list, date_1, date_2):
    """Corrige l'ordre des 2 dates. Place date_2 à l'incide n-1 où n est l'indice de date_1.

    Args:
        date_1 (_type_): La première date (mais qui devrait être la deuxième)
        date_2 (_type_): La seconde date (mais qui devrait être la première)
    """
    index_date_1 = ordre.index(date_1)
    index_date_2 = ordre.index(date_2)

    ordre.remove(date_2)

    new_index_date_2 = index_date_1 - 1
    if new_index_date_2 == -1:
        new_index_date_2 = 0

    ordre.insert(new_index_date_2, date_2)

    return ordre

# ==========
# Assemblage
# ==========

status = False
while status != True:
    # On vérifie si on a une erreur 
    status = validation(ordre=ordre_temporel)

    if status != True:
        # On applique une correction
        date_1 = status[0]
        date_2 = status[1]

        ordre_temporel = correction(ordre=ordre_temporel, date_1=date_2, date_2=date_1)

# print(status)
print(ordre_temporel)

""" 
Ma réponse :

2233,2366,2099,3009,2526,2014,3264,3268,2828,3789,4887,3373,1743,3014,2639,3959,3095,3498,3195,3219,3977,3990,3997,4342,3515,4399,1079,1289,1454,1558,1686,1911,2428,3523,3652,1735,1371,1974,2143,2174,2182,1322,1510,1534,3080,1267,1492,3084,1706,1146,1789,4059,1886,3943,3967,4333,4640,2247,4602,1083,1586,2527,2900,3241,3630,1508,1272,2272,4587,1109,2321,2740,4165,4571,4641,3500,2235,3832,1229,2511,3729,3135,3708,3752,3989,4819,4077,2104,4864,4283,1158,1324,2504,3224,2244,3309,1331,3860,1520,1125,2698,3818,3975,4030,4572,2025,1037,1053,2892,3063,3820,4740,4464,1598,1266,3745,2620,2731,3218,2759,4534,4544,4766,1689,1182,1251,3182,3190,3957,4127,4325,1627,2120,4417,1315,1320,1329,1840,2130,3691,4118,3316,4481,1479,1362,1389,2334,4285,1745,1773,3974,4494,1944,2160,2257,4483,3017,2282,4293,3497,4694,2391,2454,2523,2697,2765,2894,3297,3529,3563,3594,3673,3714,3944,4051,4414,4532,4542,4607,4664,4692,4820,4901,4918,2834,4634,1016,1742,1921,2259,2778,3249,3440,3448,4012,4071,1231,2878,3709,3887,4560,1498,2039,2495,3116,3352,3410,3516,4080,4091,4346,4777,4253,2037,2792,2913,3610,3851,3912,4573,4190,3237,2222,2552,1173,1816,2094,3889,4596,4969

"""