import numpy as np

array1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(array1 % 2 == 0)
# Output : [False  True False  True False  True False  True False  True]
# If we specify condition with an numpy array, it returns
# an array which contains boolean values which represents each element
# with either True or False based on whether that element satisfies
# the given condition