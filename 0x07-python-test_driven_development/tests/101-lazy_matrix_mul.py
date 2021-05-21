# run test with python3 -m doctest -v ./tests/101-lazy_matrix_mul.txt

First import method to test
>>> lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

SUCCESS CASES:

Test ints and floats in same size lists in list matrix:
>>> print(lazy_matrix_mul([[1, 2], [3, 4]], [[2, 0], [1, 2]]))
[[ 4  4]
[10  8]]

>>> print(lazy_matrix_mul([[-2.0, -3.0]], [[-2.0], [-4.0]]))
[[16.]]
