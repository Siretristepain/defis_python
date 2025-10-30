class Voiture():
    def __init__(self, roue, couleur, conducteur=None):
        self.roue = roue
        self.couleur = couleur
        self.conducteur = conducteur


maVoiture = Voiture(roue=4, couleur="rouge")
clio3 = Voiture(4,"marron","xxx")
print(clio3.couleur)
clio3.couleur = "beige"
print(clio3.couleur)