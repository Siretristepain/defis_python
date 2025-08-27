letters = {
    'A': ['A'],
    'C': ['C'],
    'G': ['G'],
    'U': ['U'],
    'R': ['A','G'],
    'Y': ['C','U'],
    'K': ['G','U'],
    'M': ['A','C'],
    'S': ['C','G'],
    'W': ['A','U'],
    'B': ['C','G','U'],
    'D': ['A','G','U'],
    'H': ['A','C','U'],
    'V': ['A','C','G'],
    'N': ['A','C','G','U'],
}

def check_sequence(description: str, sequence: str):
    """Fonction qui permet de vérifier si la description donnée en entrée corresponds bien à la séquence donnée en entrée.

    Args:
        description (str): la description de séquence d'ARN.
        sequence (str): la séquence d'ARN à vérifier.

    Returns:
        (bool) : True si la description est conforme avec la séquence, False sinon.
    """

    # Déjà, si la séquence ne fait pas le même longueur que la description, on peut directement retourner False
    if not len(sequence) == len(description):
        return False

    # On parcours toutes les lettres de la séquence et on regarde si la lettre au même index dans la description peut correspondre à cette lettre
    for i in range(len(sequence)):
        if sequence[i] in letters[description[i]]:
            continue
        else:
            return False

    return True

# print(check_sequence('NGKWAR', 'AGAAAA'))
# print(check_sequence('NGKWAR', 'AGUAAG'))

# ====================================
# Récupération des éléments du fichier
# ====================================

with open("./analyse_de_sequences_part2/src/input.txt", "r") as f:
    content = [elem.rstrip('\n') for elem in f.readlines() if elem != '\n' ]

# ==========
# Résolution
# ==========

# Initialisation du compteur
valid_sequences = 0

# Boucle
for sequence in content[1:]:
    if check_sequence(description=content[0], sequence=sequence):
        valid_sequences += 1

print(valid_sequences)
# --> 235
