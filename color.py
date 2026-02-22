import numpy as np
from PIL import Image

image = Image.open("./images/nature.jpg")

def brighten_image():
    # create array with dtype=int32 bcuz 
    # bydefault np.array convert image into array whose dtype is uint8
    # uint8 can only hold value from 0 - 255
    # So when we increase value & if it exceed 255, it starts from 0 again
    image_array = np.array(image,dtype=np.int32)
    result_array = image_array + 50
    np.clip(result_array,0,255,out=result_array)
    result_image = Image.fromarray(result_array.astype(np.uint8))
    result_image.show()

def darken_image():
    image_array = np.array(image,dtype=np.int32)
    result_array = image_array - 50
    np.clip(result_array,0,255,out=result_array)
    result_image = Image.fromarray(result_array.astype(np.uint8))
    result_image.show()
darken_image()