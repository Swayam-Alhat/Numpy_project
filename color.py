import numpy as np
from PIL import Image

image = Image.open("./images/lion.jpg")

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

# factor > 1 = contrast increases ex. 1.5
# 0 < factor < 1 = contrast decrease ex. 0.5
# read about contrast in learning.md file
def adjust_contrast(factor):
    image_array = np.array(image,dtype=np.float32)
    result_array = 128 + (image_array - 128) * factor
    np.clip(result_array,0,255,out=result_array)
    result_image = Image.fromarray(result_array.astype(np.uint8))
    result_image.show()

def blur_image(intensity=1):
    image_array = np.array(image, dtype=np.float32)
    
    padded_array = np.pad(image_array, pad_width=((intensity, intensity), (intensity, intensity), (0, 0)))
    
    rows, cols, channels = image_array.shape
    kernel_size = (2 * intensity + 1) ** 2
    
    result_array = np.zeros_like(image_array)
    
    # Instead of looping over every pixel, we loop only over kernel positions
    # That's just (2*intensity+1)^2 iterations, e.g. 9 for intensity=1
    for di in range(2 * intensity + 1):
        for dj in range(2 * intensity + 1):
            result_array += padded_array[di:di+rows, dj:dj+cols, :]
    
    result_array /= kernel_size
    
    np.clip(result_array, 0, 255, out=result_array)
    result_image = Image.fromarray(result_array.astype(np.uint8))
    result_image.show()
blur_image(20)