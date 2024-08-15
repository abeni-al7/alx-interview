# Rotate 2D Matrix

This directory contains Python code that implements a function to rotate a 2D matrix.

## Description

The `0-rotate_2d_matrix.py` file in this directory contains a Python function `rotate_2d_matrix(matrix: List[List[int]]) -> None` that takes a 2D matrix as input and rotates it 90 degrees clockwise.

## Usage

To use the `rotate_2d_matrix` function, follow these steps:

1. Import the function into your Python script:

```python
from rotate_2d_matrix import rotate_2d_matrix
```

2. Create a 2D matrix:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

3. Call the `rotate_2d_matrix` function with the matrix as input:

```python
rotate_2d_matrix(matrix)
```

4. The original matrix will be rotated 90 degrees clockwise.

## Example

Input:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Output:
```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This code is released under the [MIT License](LICENSE).
