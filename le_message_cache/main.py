from PIL import Image 
import numpy as np

# On ouvre et on récupère la matrice de l'image d'entrée
img = Image.open('cocotiers.png')
# img = img.convert("L") # Pour convertir en nuances de gris
img_np = np.array(img) 

# On récupère les dimensions de l'image
longueur = img_np.shape[0]
largeur = img_np.shape[1]
print(f"Dimensions de l'image : {longueur} pixels de long et {largeur} pixels de large")

# Je vais récupérer le message dans cette liste
car = []

# Pour chaque pixels, on vas récupérer les valeurs RVB
for i in range(largeur):
    for j in range(longueur):
        (rouge, vert, bleu) = img.getpixel((i, j))
        
        # Je dois convertir ces valeur sde RVB en binaire
        rouge_bin = format(rouge, '08b')
        vert_bin = format(vert, '08b')
        bleu_bin = format(bleu, '08b')

        car.append(rouge_bin[-1])
        car.append(vert_bin[-1])
        car.append(bleu_bin[-1])

        # pixel = img.getpixel((i, j))
        # pixel_bin = format(pixel, '08b')
        # car.append(pixel_bin)


# Maintenant je dois boucle sur la liste car sur tous les huits éléments pour en déduire le caractère ascii
message = []
for i in range(0,len(car),7):
    binaire = car[i:i+8]
    binaire = ''.join(binaire)
    nb_entier = int(binaire, 2) # On convertit le binaire en entier

    # On convertit l'entier en ASCII
    car_ascii = chr(nb_entier)

    # On fait apparaitre ce caractère ascii dans la liste message
    message.append(car_ascii)

# On affiche le résultat
print(''.join(message))

if __name__ == '__main__':
    # print(to_bin(111))
    pass
