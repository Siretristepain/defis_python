def compute_volume(epaisseur=0):
    """
    Méthode de calcul du volume de métal fondue.
    """
    return 8 * epaisseur

def compute_epaisseur(volume=0):
    """
    Méthode de calcul de l'épaisseur transpercée.
    """
    return 3 - 0.005 * volume

# Initialement, on transperce 0cm et le volume de métal vaut 0.
tot_epaisseur = 0
tot_volume = 0
second = 1
half = False
entire = False

while tot_epaisseur <= 70 and second < 120:
    # on calcul l'épaisseur avec le volume total jusqu'à la seconde d'avant
    epaisseur_this_second = compute_epaisseur(volume=tot_volume)
    # on calcul le volume crée par notre épaisseur sur la seconde actuelle
    volume_this_second = compute_volume(epaisseur=epaisseur_this_second)
    
    # on rajoute l'épaisseur de cette seconde au total d'épaisseur et le volume fait cette seconde au volume total
    tot_epaisseur += epaisseur_this_second
    tot_volume += volume_this_second
    

    # print(f"=== Seconde n°{second} ===\nVolume ajouté : {volume_this_second}\nEpaisseur ajoutée : {epaisseur_this_second}.")
    # print(f"Volume total : {tot_volume}\nEpaisseur totale : {tot_epaisseur}.")

    if tot_epaisseur >= 35 and not half:
        print(f"Nombre de seconde avant d'atteindre la moitié de la porte blindée : {second}")
        half = True

    if tot_epaisseur >= 70 and not entire:
        print(f"Nombre de seconde avant d'atteindre la totalité de la porte blindée : {second}")
        entire = True

    second += 1

# Nombre de seconde avant d'atteindre la moitié de la porte blindée : 16
# Nombre de seconde avant d'atteindre la totalité de la porte blindée : 67