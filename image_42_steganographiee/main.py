import matplotlib.image as mpimp
import matplotlib.pyplot as plt

# Ouvrir l'image avec matplotlib
img = mpimp.imread("image_42_steganographiee/src/C25_Image_42_encoded.png")

R = img[:,:,0]*255
V = img[:,:,1]*255
B = img[:,:,2]*255

# On créer un mask pour identifier les pixels correspondants
# mask = img[(16*img[0]* + 4*img[1] + img[2]) % 42 == 0]
mask = (16 * R + 4 * V + B) % 42 == 0
# print(mask.shape)

plt.imshow(mask)
plt.show()
