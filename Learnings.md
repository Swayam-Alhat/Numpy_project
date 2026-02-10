# Learnings

### Broadcasting

Broadcasting is the process where NumPy automatically makes arrays with different shapes compatible to perform operations on them.

Before we perform arithmetic operations between arrays, we should ensure they are compatible. NumPy compares array shapes **element-wise from right to left** (starting from the trailing dimensions). Two dimensions are compatible when:

1. They are equal, **OR**
2. One of them is 1

If arrays have different numbers of dimensions, the smaller array is treated as having dimensions of size 1 prepended to its shape.

**Examples:**

```python
arr1 = np.array([[1, 2, 3]])
arr2 = np.array([
  [1, 2, 3],
  [4, 5, 6],
])

print(arr1.shape) # (1, 3)
print(arr2.shape) # (2, 3)
```

Checking compatibility (right to left):

- **Last dimension**: 3 == 3 ✓ (equal)
- **Second-to-last**: 1 vs 2 ✓ (one is 1)

**So both arrays are compatible.** arr1 will be broadcast to shape (2, 3) by repeating its row.

**More Examples:**

```python
# Compatible cases
(3, 1) and (3, 4)  # ✓ Compatible → broadcasts to (3, 4)
(3, 4) and (4,)    # ✓ Compatible → (4,) becomes (1, 4), broadcasts to (3, 4)
(5, 1, 3) and (1, 4, 3)  # ✓ Compatible → broadcasts to (5, 4, 3)

# Incompatible cases
(3, 4) and (3,)    # ✗ NOT compatible (4 ≠ 3, and neither is 1)
(2, 3) and (3, 2)  # ✗ NOT compatible (dimensions don't align)
```
