import numpy as np

array_2d = np.array([[1,2,3],[4,5,6]])
print(array_2d[0,1]) # 2 
# So, In [], we specify index positions of dimensions. 
# That is, as we know, 2d arrays have 2 dimensions. 1st is row & 2nd is column. 
# So while indexing 2d array, we specify index positions of rows and columns
# i.e array_2d[0,1] This means row at 0th index position & column at 1st index position. So we get 2
# So basically we specify index position of dimensions in square brackets and each dimension is separated by ",". i.e [0,1] means 0th row (1st dimension) & column at 1st index (2nd dimension)