import numpy as np

array1 = np.array([[1,2,3],[4,5,6]])
array2 = np.array([[7,8,9],[10,11,12]])
print(np.vstack((array1,array2))) # adds them vertically

# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]


print(np.hstack((array1,array2))) # adds horizontally

# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]
