# Numpy Learning

Numpy is a python library that allows us to store data in N-dimensional arrays and perform numerical/mathematical operations on them. It includes collection mathematical functions to operate on arrays.
Numpy is much more efficient and fast because it is written in C.

## Notes

Numpy arrays are more efficient and fast than python lists.

### Create numpy array

```python
import numpy as np

arr1 = np.array([1,2,3,4,5])
print(type(arr1))
```

```
<class 'numpy.ndarray'>
```

`np.array()` is used to create numpy array.

_Also, while creating numpy array, all elements should be of same type. i.e `int` or `float`._

We can also create an array using `np.arange()` which is similar to `range()`. That is, we can provide start,end & step/diff values as arguments.

```python
import numpy as np

array1 = np.arange(0,10,2)
print(array1)
```

```
[0 2 4 6 8]
```

### Perform operations on array

To perform operations on python list, we need to use for loop which is not efficient and is time consuming. Whereas, with numpy arrays, we can perform operations without writing a for loop. Numpy allows us to perform vectorized operations on arrays which means we can directly perform operation on each element in array without looping.
