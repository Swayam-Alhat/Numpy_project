from PIL import Image
import numpy as np

image = Image.open("./images/nature.jpg")

image_array = np.array(image,dtype=np.int32)

print(image_array.ndim)
print(image_array.shape)