import matplotlib.image as mpimg
import numpy as np

# Charger l'image
img = mpimg.imread("./le_cadre_morsele/src/cadre_morsele.png")

# Si float 0-1 → convertir en 0-255
if img.dtype != np.uint8:
    img = (img * 255).astype(np.uint8)

# Plage de lignes à tester
for row in range(35,36):  # 41 car en Python le dernier index est exclu
    ligne = img[row]  # (largeur, 3)
    pixels = ligne[769::]  # (n, 3)
    verts = pixels[:, 1]  # composante verte
    print(verts)
    # message = ''.join(chr(v) for v in verts)
    # print(f"Ligne {row}: {message}")
