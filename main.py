import numpy as np
from PIL import Image

# open() loads given image as PIL image object.
image = Image.open("./images/leena.jpg")


image_array = np.array(image, dtype=np.int32)

result_image_array = image_array + 20

# we convert values which are less than 0 or more than 255 into 0 (min) & 255 (max)
np.clip(result_image_array,0,255,out=result_image_array)

result_image = Image.fromarray(result_image_array)
result_image.show()