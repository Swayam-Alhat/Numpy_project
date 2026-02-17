import numpy as np

array_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(array_3d.shape)
print(array_3d[1,0,2]) #9

# access 2nd column
print(array_3d[:,:,1]) 
""""[[2 5]
     [8 11]]"""
# [:,:,1] means consider all layers 
# and consider all rows within that layers.
# And at last, within those rows, only consider 
# column at index position 1
