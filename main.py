import numpy as np
from PIL import Image

# open() loads given image as PIL image object.
image = Image.open("./images/leena.jpg")

# show image
image.show()

# Two methods to convert image into numpy array
# 1. np.array() - It creates new copy of image data and allows us to perform operations on that data (i.e array). So it uses memory
# 2. np.asarray() - creates a view of the original image's memory

# Thus, if we want to manipulate image, use np.array(). If we want to ONLY analyze image data, use np.asarray() which is memory efficient

image_array = np.array(image, dtype=np.int32)

# we specify dtype = int32. because bydefault it is uint8
# uint8 holds values 0-255 only. If exceeded, it wraps around (256->0, 257->1...).
# If goes below 0, it wraps to 255. So we use int32 to avoid this.
# So this can affect when we add or substract and get value beyond 0 or 255

# create new array with increased values
result_image_array = image_array + 20

# Then, we convert values which are less than 0 or more than 255 into 0 (min) & 255 (max)
np.clip(result_image_array,0,255,out=result_image_array)

result_image = Image.fromarray(result_image_array)
result_image.show()