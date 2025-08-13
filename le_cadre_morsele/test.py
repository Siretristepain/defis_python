import matplotlib.image as mpimg
import numpy as np

# Charger l'image
img = mpimg.imread("./le_cadre_morsele/src/cadre_morsele.png")

# Si float 0-1 → convertir en 0-255
if img.dtype != np.uint8:
    img = (img * 255).astype(np.uint8)

# Extraire la ligne 35
ligne = img[36]  # (largeur, 3)

# Prendre pixels de la colonne 769 à la fin, avec un pas de 4
pixels = ligne[770::4]  # (n, 3)

# Récupérer la composante verte
verts = pixels[:, 1]  # colonne index 1 = G

# Convertir en texte ASCII
message = ''.join(chr(v) for v in verts)

print(message)
