import numpy as np

# arr1 = np.array([[1,2,3,4,5],
#                  [6,7,8,9,10]])
# print(np.sum(arr1))
# print(np.mean(arr1))
# print(np.max(arr1))
# print(np.argmin(arr1))
# print(np.argmax(arr1))
# print(arr1)
# print(np.sum(arr1,axis=1))

rng = np.random.default_rng()

print(rng.integers(1,11,size=(2,2)))

