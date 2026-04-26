import re

# =======================
# Ouvrir le fichier input
# =======================

with open("les_hybrides_s1e09/src/input.txt", "r") as f:
    lines = [line.split('\n')[0] for line in f.readlines()]

# On extrait les séquences de chaque ligne
sequences = [re.search(pattern=r"\d{4,}", string=line).group() for line in lines]
print(len(sequences))

# ========
# Fonction
# ========

PATTERN = {
    '0001': 'A',
    '1010': 'T',
    '1100': 'G',
    '0011': 'C',
}

def check_valid_sequence(sequence: str):
    # Early return dans le cas où la séquence n'a pas une longueur multiple de 4.
    if len(sequence) % 4 != 0:
        return False
    
    for i in range(0, len(sequence)-3, 4):
        base = sequence[i:i+4]
        if not base in PATTERN.keys():
            print(f"{base} not in pattern")
            return False
    # Si toutes les bases observées de la séquence sont correctes, alors la séquence complète est correcte.
    return True

# ==========
# Résolution
# ==========

invalid = []

for i in range(len(sequences)):
    if not check_valid_sequence(sequence=sequences[i]):
        invalid.append(i+1)

print(f"Les index des séquences invalides sont : {invalid}.")
# --> Les index des séquences invalides sont : [4, 9, 14, 20, 22, 24, 30, 31, 40, 41, 43, 46, 50, 51, 57, 60, 61, 62, 65, 66, 74, 77, 82, 83, 85, 86, 89, 90, 98].
