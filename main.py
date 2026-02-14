from PIL import Image
import numpy as np

img = Image.open("./images/black.jpg")
arrImg = np.array(img)
print(arrImg)
print(arrImg.ndim)

arrImg[:, :, :] = 250


img2 = Image.fromarray(arrImg)
img2.show()