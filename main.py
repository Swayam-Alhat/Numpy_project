import numpy as np

array_1d = np.array([1,2,3,4,5]) # 1d array
print(array_1d)
print(f"Dimensions of array_1d : {array_1d.ndim}") # 1


array_2d = np.array([[1,2,3],[4,5,6]])
print(array_2d)
print(f"Dimensions of array_2d : {array_2d.ndim}") # 2

array_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(array_3d)
print(f"Dimensions of array_3d : {array_3d.ndim}") # 3
