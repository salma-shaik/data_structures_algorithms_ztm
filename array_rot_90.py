"""
Rotating a 2D Array by 90 Degrees (Python)
A 2-dimensional array is an array of arrays.

Implement a function that takes a square 2D array (# columns = # rows) and rotates it by 90 degrees.

Example:
[[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

[[          1],
[4, 5, 6    2],
[7, 8, 9    3]]


[[        4 1],
[         5  2],
[7, 8, 9  6 3]]

->

[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]

When you are done, try implementing this function so that you can solve this problem in place. Solving it in place
means that your function won't create a new array to solve this problem.  Instead, modify the content of the given
array with O(1) extra space.

NOTE: For simplicity, we're going to represent a 2 dimensional array as a list of lists in Python.
"""
import numpy as np


def rotate_array_new(test_arr):
    np_arr = np.array(test_arr)

    nrows = np_arr.shape[0]
    ncols = np_arr.shape[1]

    rotated_array = np.zeros((ncols, nrows))

    i = nrows-1
    j = 0

    p = 0
    q = 0

    while j < ncols:
        while i >=0:
            rotated_array[p, q] = np_arr[i, j]

            i -= 1
            q += 1
        j += 1
        p += 1
        i = nrows-1
        q = 0

    return rotated_array

""" 
def rotate_array_curr(test_arr):
    np_arr = np.array(test_arr)

    nrows = np_arr.shape[0]
    ncols = np_arr.shape[1]

    i = nrows - 1
    j = 0

    p = 0
    q = 0

    while j < ncols:
        while i >= 0:
            rotated_array[p, q] = np_arr[i, j]

            i -= 1
            q += 1
        j += 1
        p += 1
        i = nrows - 1
        q = 0

# print(rotate_array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]]))

"""
a1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
# print(rotate_array_new(a1)) # should return:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]

a2 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]
print(rotate_array_new(a2)) # should return:
# [[13, 9, 5, 1],
#  [14, 10, 6, 2],
#  [15, 11, 7, 3],
#  [16, 12, 8, 4]]