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

# =================================================================================================================
# Je voudrais faire un dictionnaire avec pour clé chaque date unique et en valeur la liste des date à visiter avant
# =================================================================================================================

dic = {}

for date in dates_uniques:
    # On récupère tous les indices où "date" apparait dans la colonne de gauche
    indices = [index for index, value in enumerate(col_gauche) if value == date]
    # On prévois le fait que les valeurs du dictionnaire soient dans une liste
    dic[date] = []
    # On boucle sur tous les indices
    for i in range(len(indices)):
        dic[date].append(col_droite[indices[i]])

# ========================
# On crée l'ordre temporel
# ========================

ordre_temporel = []

def find_first_index(lst: list, element):
    try :
        indice = lst.index(element)
    except:
        indice = None

    if indice == None:
        indice = 9999
    return indice


for date in dates_uniques:
    print(f"Date à traiter : {date}")
    # On récupère les dates à faire APRES notre date
    dates_a_faire_apres = dic[date]
    print(f"Liste des dates à visiter après : {dates_a_faire_apres}")
    # Maintenant on veut récupérer les indices de ces dates dans notre 'ordre_temporel' s'ils existent.
    # Si c'est le cas, on veut placer notre nouvelle date avant le plus petit indice.
    # Si ces dates n'existent pas, on place notre nouvelle date à la fin de notre 'ordre_temporel'.
    indices_dates_apres = []
    for date_apres in dates_a_faire_apres:
        indices_dates_apres.append(find_first_index(ordre_temporel, date_apres))

    print(f"Indices des dates à visiter après : {indices_dates_apres}")

    # Si la liste est vide on ajoute simplement notre date à l'ordre temporel
    if indices_dates_apres == []:
        ordre_temporel.append(date)
    # Si la liste n'est pas vide, on cherche le plus petit élément et on insère notre date à l'indice encore avant
    else:
        indice_min = min(indices_dates_apres)
        indice_to_place = indice_min - 1
        if indice_to_place == -1:
            indice_to_place = 0

        ordre_temporel.insert(indice_to_place, date) # insert(indice_voulu, element_voulu)
    
    print('*'*20)

# for i in range(len(ordre_temporel)):
#     ordre_temporel[i] = int(ordre_temporel[i])

print(len(ordre_temporel))
print(f"ORDRE TEMPOREL : {ordre_temporel}")

# ==========
# Validation
# ==========

""" 
Pour la validation, il suffit de regarder ligne à ligne si chaque condition est vérifiée.
"""

for i in range(len(col_gauche)):
    date_before = col_gauche[i]
    date_after = col_droite[i] 

    index_date_before = ordre_temporel.index(date_before)
    index_date_after = ordre_temporel.index(date_after)

    if index_date_after <= index_date_before:
        print(f"ERREUR! Ligne {i}. {date_before} doit être visiter avant {date_after}")