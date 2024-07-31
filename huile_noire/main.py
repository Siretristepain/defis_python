# =====================================
# Dictionnaire d'évolution des cellules
# =====================================

dic_evolution = {
    '111' : '0',
    '110' : '1',
    '101' : '1',
    '100' : '0',
    '011' : '1',
    '010' : '1',
    '001' : '1',
    '000' : '0',
}

# ======================================================
# Fonction d'évolution d'une cellule à partir du triplet
# ======================================================

def cell_evolution(triplet: list):
    triplet_str = ''.join(triplet)
    evolution = dic_evolution[triplet_str]
    return evolution

if __name__ == '__main__':
    print(cell_evolution(triplet=['0','0','1']))