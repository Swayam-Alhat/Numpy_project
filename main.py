import numpy as np
from PIL import Image

 # open() loads given image as PIL image object.
image = Image.open("./images/leena.jpg")

# function to brighten Image
def brighten_image():
    image_array = np.array(image, dtype=np.int32)
    # add 30 in each pixels
    result_image_array = image_array + 30

    # we convert values which are less than 0 or more than 255 into 0 (min) & 255 (max)
    np.clip(result_image_array,0,255,out=result_image_array)

    # convert array into image
    result_image = Image.fromarray(result_image_array.astype(np.uint8))
    result_image.show(result_image)

def darken_image():
    # convert image into array & change dtype=int32
    image_array = np.array(image, dtype=np.int32)

    # perform actual operation to darken an image
    result_image_array = image_array - 30

    # keep values in array within 0 to 255
    np.clip(result_image_array,0,255,out=result_image_array)

    # convert back into PIL image object. but before that, change dtype = uint8
    result_image = Image.fromarray(result_image_array.astype(np.uint8))

    result_image.show()
    
def increase_contrast():
    image_array = np.array(image,dtype=np.int32)

    print(image_array)

    print('  ')

    conditions = [image_array > 128, image_array < 128]
    choices = [image_array + 30, image_array - 30]

    result_array = np.select(conditions,choices,default=128)
    
    np.clip(result_array, 0, 255, out=result_array)
    result_image = Image.fromarray(result_array)

    result_image.show()
increase_contrast()