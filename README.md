# Numpy Learning

Numpy is a python library that allows us to store data in N-dimensional arrays and perform numerical/mathematical operations on them. It includes collection of mathematical functions to operate on arrays.
Numpy is much more efficient and fast because it is written in C.

## Notes

Numpy `arrays` are more efficient and fast than python `lists`.

### Basics of Numpy

```python
import numpy as np

arr1 = np.array([1,2,3,4,5])
print(type(arr1))
```

```
<class 'numpy.ndarray'>
```

`np.array()` is used to create numpy array.

_Also, while creating numpy array, all elements should be of same data type. i.e `int` or `float`._

We can also create an array using `np.arange()` which is similar to `range()`. That is, we can provide start,end & step/diff values as arguments.

```python
import numpy as np

array1 = np.arange(0,10,2)
print(array1)
```

```
[0 2 4 6 8]
```

There are also other ways to create arrays like `np.zeros()`, `np.ones()`, `np.linspace()` etc.

To perform operations on python list, we need to use `for` loop which is not efficient and is time consuming. Whereas, with numpy arrays, we can perform operations without writing a `for` loop. Numpy allows us to perform _vectorized operations_ on arrays which means we can directly perform operation on each element in array without looping.

_Note_ : To get data type of elements/values in an array, we use `dtype` property.
Example

```python
import numpy as np

array1 = np.array([1,2,3,4,5])
print(array1.dtype)

array2 = np.array([1.2,3.4,5.6,7.0])
print(array2.dtype)
```

```
int64
float64
```

If we have mixed values, then it returns `float` because `float` values cannot be represented as `int` but `int` values can be represented as `float`.

```python
import numpy as np

mixed_array = np.array([1,2,3,4.5,5.0])
print(mixed_array.dtype)
```

```
float64
```

We can also specify `dtype` while creating an array. lets say, you want to create an array whose `dtype` is `int32` or `float32` and not `int64` or `float64`. So in this case, we pass dtype value as second argument in `np.array()`.

Example

```python
import numpy as np

array1 = np.array([1,2,3,4,5],dtype=np.float32)
print(array1)
print(array1.dtype)
```

```
[1. 2. 3. 4. 5.]
float32
```

We can also create new array with our desired dtype using `astype(new_dtype_value)`.

```python
import numpy as np

array1 = np.array([1.5,2.8,3.4])
print(array1)

# return new array with given dtype
new_array = array1.astype(np.int32)
print(new_array)
print(new_array.dtype)
print(array1.dtype)
# array1 remains unchanged
```

```
[1.5 2.8 3.4]
[1 2 3]
int32
float64
```

#### Multidimensional arrays

Numpy allows us to create n-dimensional arrays.

```python
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
```

```
[1 2 3 4 5]
Dimensions of array_1d : 1
[[1 2 3]
 [4 5 6]]
Dimensions of array_2d : 2
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
Dimensions of array_3d : 3
```

#### Properties of Numpy array

`size`,`shape`,`ndim`, & `dtype` are important properties of numpy array
