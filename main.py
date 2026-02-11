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

ages = np.array([[28,19,19,10],
                 [12,45,57,28]])
teens = ages[ages <= 19]
adults = ages[(ages > 19) & (ages <= 50)]
print(adults)

