import numpy as np

array_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array_2d)
print(array_2d[1:,:2]) 
"""[[4,5]
    [7,8]]"""
# [1:,:2] This means considering row, we want rows from 1st index position till last & In those rows, we want columns from start (i.e 0th index) up to (but not including) 2nd index, i.e columns at 0th and 1st index.
# So we get a submatrix of rows from 1st index till last & columns from 0th till 1st index.


