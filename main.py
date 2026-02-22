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
    result_image.show()

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

# adjust contrast 
# factor
def adjust_contrast(factor):
    image_array = np.array(image,dtype=np.float32) # for further formula

    result_array = 128 + (image_array - 128) * factor
    np.clip(result_array,0,255,out=result_array)

    result_image = Image.fromarray(result_array.astype(np.uint8))
    result_image.show()

# consider intensity = 1 and read code. It will be easy to understand
# That sub_matrix is of 3x3
# Also read Readme.md file
def blur_image(intensity):
    image_array = np.array(image,dtype=np.float32)

    # add padding of 1 width from all 4 sides
    padded_array = np.pad(image_array,pad_width=intensity,mode="constant",constant_values=0)

    rows,cols = padded_array.shape

    result_data = []

    for i in range(intensity,rows - intensity):
        result_row = []
        for j in range(intensity,cols - intensity):
            sub_matrix = padded_array[i-intensity:i+(intensity + 1),
                                      j-intensity:j+(intensity + 1)]
            avg = np.mean(sub_matrix)
            result_row.append(avg)

        result_data.append(result_row)
    
    result_array = np.array(result_data)

    result_image = Image.fromarray(result_array.astype(np.uint8))
    result_image.show()


blur_image(1)