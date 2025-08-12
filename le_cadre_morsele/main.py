import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

img = mpimg.imread("./le_cadre_morsele/src/cadre_morsele.png")

def filtre_all_pixel(img_origin):
    im = np.copy(img_origin)
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            r, v, b = im[i, j]
            if (r, v, b) != (0, 0, 0):
                im[i, j] = (1, 1, 1)
    return im

white_black = filtre_all_pixel(img_origin=img)
# print(type(white_black))
# plt.imshow(white_black)
# plt.show()

print(white_black[:,0,0])
