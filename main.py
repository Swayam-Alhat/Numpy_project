import numpy as np

arr1 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])

arr3d = np.array([[[1,2,3],[4,5,6]],
                  [[7,8,9],[10,11,12]],
                  [[13,14,15],[16,17,18]]
                  ])


date = f"{arr3d[0,0,1]}{arr3d[1,0,2]} - {arr3d[1,0,0]} - {arr3d[0,0,1]}00{arr3d[0,1,0]}"
print(date)