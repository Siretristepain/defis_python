import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

plt.style.use('_mpl-gallery-nogrid')

# # make data
# X, Y = np.meshgrid(np.linspace(-3, 3, 256), np.linspace(-3, 3, 256))
# Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)
# levels = np.linspace(np.min(Z), np.max(Z), 7)

# print(X)

img = mpimg.imread("un_treck_sur_krikket/src/map_krikket.png")

# print(img)

# # plot
# fig, ax = plt.subplots()
# ax.contour(img, levels=100)
# plt.show()

print(img.shape)
print((img*255)[0][0])
print((img*255)[-1][-1])


# fix, ax = plt.subplots(nrows=1, ncols=5)


# for idx, i in enumerate(range(54, 59)):
#     delta = i

#     mask = (img*255 < 93 + delta) & (img*255 > 93 - delta)
#     # ax[idx].imshow(img)
#     ax[idx].imshow(mask)
#     ax[idx].set_title(f"delta {delta}")


# plt.show()


fig, ax = plt.subplots(nrows=1, ncols=5, figsize=(15, 3))

for idx, i in enumerate(range(54, 59)):
# for idx, i in enumerate(range(80, 88)):

    delta = i
    mask = (img*255 < 93 + delta) & (img*255 > 93 - delta)

    # Garder les valeurs originales où le masque est True, NaN ailleurs
    masked_values = np.where(mask, img, np.nan)

    ax[idx].imshow(img, cmap='gray')  # image de fond en gris
    image = ax[idx].imshow(masked_values, cmap='RdYlBu_r', alpha=0.8)  # rouge=haut, bleu=bas
    ax[idx].set_title(f"delta = {delta}")
# plt.colorbar(image, ax=ax)

plt.tight_layout()
plt.show()

# Test Antoine

