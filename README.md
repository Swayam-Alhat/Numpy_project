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

`size`,`shape`,`ndim`, & `dtype` are important properties of numpy array. Read examples.

### Indexing & Slicing

For 1D arrays, basic indexing & slicing works the same as Python `lists`

#### 2d array

```python
import numpy as np

array_2d = np.array([[1,2,3],[4,5,6]])
print(array_2d)
print(array_2d.ndim) # It has 2 dimension. So Its a 2D array
print(array_2d.shape)
# (2,3) 2 = rows & 3 = columns
# This means array has 2 rows & each row has 3 columns or values
# This 2D array has 2 dimensions
# 1st is Row & 2nd is Column

```

```
[[1 2 3]
 [4 5 6]]
2
(2, 3)
```

#### 3d array

```python
import numpy as np

array_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(array_3d)
print(array_3d.ndim) # Its 3 dimension array i.e 3d array
print(array_3d.shape)
# (2,2,3) This means, array have total 3 dimensions.
# 1st dim is layer. i.e 2 = layers
# 2nd dim is rows (Rows in each layer). This array have 2 rows in each layer
# 3rd dim is columns (each row has 3 columns / values). This array have 2 rows, each contains 3 columns.

# Thus (2,2,3) refers to 2 layers each contains 2 rows and each row contains 3 columns
```

```
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
3
(2, 2, 3)
```

> **Note:** Terms like _layers_, _rows_, and _columns_ are informal and just for intuition.
> In NumPy, dimensions are called **axes**. The 1st dimension is **axis 0**, 2nd is **axis 1**, and 3rd is **axis 2** and so on.

> In Numpy arrays, we only use **1 square brackets** to perform indexing and slicing

#### Indexing with 2d array.

```python
import numpy as np

array_2d = np.array([[1,2,3],[4,5,6]])
print(array_2d[0,1]) # 2
# So, In [], we specify index positions of dimensions.
# That is, as we know, 2d arrays have 2 dimensions. 1st is row & 2nd is column.
# So while indexing 2d array, we specify index positions of rows and columns
# i.e array_2d[0,1] This means row at 0th index position & column at 1st index position. So we get 2
# So basically we specify index position of dimensions in square brackets and each dimension is separated by ",".
# i.e [0,1] means 0th row (1st dimension) & column at 1st index (2nd dimension)
```

```python
import numpy as np

array_2d = np.array([[1,2,3],[4,5,6]])
print(array_2d[1,0:2]) # [4,5]
# We want 4,5 which is in 2nd row,
# So we specify index position of that row i.e [1,]
# Then we want 2 elements from that row,
# So we specify columns index positions from start to end of that row
# using ":". i.e [1,0:2]
# 0:2 means we want columns from 0th index position to 1st index position.
# python excludes the end value.
# So, 0:2 means start from 0th index & stop before 2nd index (i.e 0th and 1st index)
```

```python
import numpy as np

array_2d = np.array([[1,2,3],[4,5,6]])
print(array_2d)
# access whole 2nd column
print(array_2d[:,1]) # [2,5]
# As we want to access all elements of 2nd column, so specify all rows.
# i.e ":". This means from start to end. And this is at row position,
# So from 0th row till last row. And then we specify 1 which means column
# at 1st index position. So we get elements which are in 1st index column
# and from all rows
```

```python
import numpy as np

array_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array_2d)
print(array_2d[1:,:2])
"""[[4,5]
    [7,8]]"""
# [1:,:2] This means considering row, we want rows from 1st index position till last
# And In those rows, we want columns from start (i.e 0th index)
# up to (but not including) 2nd index, i.e columns at 0th and 1st index.
# So we get a submatrix of rows from 1st index till last & columns from 0th till 1st index.
```

#### Indexing with 3d array

Indexing with 3d arrays will be a bit similar as we done for 2d array. Just instead of 2 dimensions, we have 3 dimensions, so we need to specify index positions of 3 dimensions. i.e array[ index_of_d1, index_of_d2, index_of_d3 ]  
Example

```python
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

```
