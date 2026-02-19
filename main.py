import numpy as np

array1 = np.array([1,2,3,4,5,6]) # 1d array. Its shape is 1
print(array1.reshape(2,3)) 
# [[1 2 3]
#  [4 5 6]]

# reshape() allows us to reshape an array
# we specify shapes as argument i.e for above example, we passed
# 2 and 3. So this means array will have 2 dimensions - Rows & Columns
# 2 rows & 3 columns. Make sure 
# product of shapes == no. of elements in existing array.
# for above ex, 2*3 == 6.

# Creating an 3d array from 1d array.

array2 = np.arange(1,13) # [1  2  3  4  ... 11  12]
# Its dimensions = 1 & shape = (12,)

print(array2.reshape(2,2,3)) 

# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]

# This means 3 dimension - 
# 2 layers, 2 rows & 3 columns
