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
    """
    Fonction d'évolution d'une cellule centrale du temps T au temps T+1 en fonction du triplet composé de la cellule, la cellule précédent et la cellule suivante.

    Args :
        - triplet (list[str]) : triplet composé de la cellule, la précédente et la suivante.
    
    Returns :
        - evolution (str) : l'état de la cellule au temps T+1 (0 ou 1).

    Example :
        cell_evolution(triplet=['0','1','0'])
        -> '1'
    """
    triplet_str = ''.join(triplet)
    evolution = dic_evolution[triplet_str]
    return evolution

# ================================================================
# Fonction d'évolution d'une séquence complète pour 1 pas de temps
# ================================================================

def sequence_one_step_evolution(sequence):
    """
    Fonction qui prends une séquence au temps T en entrée et qui retourne la séquence au temps T+1 suivant les lois d'évolution des cellules.

    Args :
        - sequence (str) : la séquence a évoluée au temps T, composée de '0' et '1'.

    Returns :
        - (str) : la séquence au temps T+1.

    Example :
        sequence_one_step_evolution(sequence='101001')
        -> '111011'
    """
    sequence_list = list(sequence)
    sequence_next_step = []

    for i in range(len(sequence_list)):
        # Cas particulier de la première cellule
        if i == 0:
            triplet = [sequence_list[-1], sequence_list[i], sequence_list[i+1]]

        # Cas particulier de la dernière cellule
        elif i == len(sequence_list) - 1:
            triplet = [sequence_list[i-1], sequence_list[i], sequence_list[0]]

        # Cas standard
        else:
            triplet = [sequence_list[i-1], sequence_list[i], sequence_list[i+1]]

        cell_next_step = cell_evolution(triplet=triplet)
        sequence_next_step.append(cell_next_step)

    return ''.join(sequence_next_step)


# ==================
# Traitement complet
# ==================


sequence = "0"*45 + str(bin(25794542787624960)).replace('0b', '') # Puisque le binaire de 25794542787624960 fait 55 digits, je rajoute 45 zéros devant.

for i in range(178):
    sequence = sequence_one_step_evolution(sequence=sequence)


print(sequence)
"""
1110001001101111100011100011101110000100000001101000111111100100000011111011010111110001110011101011
"""

# Pour convertir en entier, il faut rajouter 0b devant le nombre binaire. Le problème c'est qu'on ne peut pas faire nb = '0b' + sequence, du coup j'ai rien trouvé de mieux.
print(int(0b1110001001101111100011100011101110000100000001101000111111100100000011111011010111110001110011101011))
"""
1121255594552210026899559095531
"""



if __name__ == '__main__':
    # print(cell_evolution(triplet=['0','0','1']))
    # print(sequence_one_step_evolution(sequence="111010"))
    # print(sequence_one_step_evolution(sequence="101001"))
    # print(sequence_one_step_evolution(sequence=sequence))
    pass