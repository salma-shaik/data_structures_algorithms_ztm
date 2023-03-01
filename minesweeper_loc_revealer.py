"""
Find Where to Expand in Minesweeper (Python)
Implement a function that turns revealed cells into -2 given a location the user wants to click.

For simplicity, only reveal cells that have 0 in them.
If the user clicks on any other type of cell (for example, -1 / bomb or 1, 2, or 3),
just ignore the click and return the original field.  If a user clicks 0, reveal all other 0's that are connected to it.

Your function should take:

field: The given field as a 2D array
num_rows / numRows: The number of rows in the given field
num_cols / numCols: The number of columns in the given field
given_i / givenI: The row index of the cell the user wants to click
given_j / givenJ: The column index of the cell the user wants to click


NOTE: For simplicity, arrays are represented as lists in Python

"""
import numpy as np


def assign_neg_two(test_arr, x, y):
    adj_pos = [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y - 1], [x, y + 1], [x + 1, y - 1], [x + 1, y],
               [x + 1, y + 1]]

    for pos in adj_pos:
        # python allows negative indices. So even if -1, 2 --> still trying to assign some value whereas isn't helpful
        # here because logic based on positive indices
        if pos[0] >= 0 and pos[1] >= 0:
            try:
                # Change all other 0's that are connected to it to -2
                if test_arr[pos[0], pos[1]] == 0:
                    test_arr[pos[0], pos[1]] = -2
                    assign_neg_two(test_arr, pos[0], pos[1])
            except:
                pass
    return test_arr


def reveal_cells(field, given_i, given_j):
    given_arr = np.array(field)

    # If a user clicks 0, reveal all other 0's that are connected to it
    if given_arr[given_i, given_j] == 0:
        given_arr[given_i, given_j] = -2
        return assign_neg_two(given_arr, given_i, given_j)
    else:
        return given_arr


field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

# print(reveal_cells(field1, 2, 2))
# print()
# print(reveal_cells(field1, 1, 4))

field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

# print(reveal_cells(field2, 0, 1))

# print(reveal_cells(field2, 1, 3))

field3 = [[0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, -1, 1, 0]]

# print(reveal_cells(field3, 2, 2))

field4 = [[-1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, -1]]
print(reveal_cells(field4, 1, 3))

"""
# NOTE: The following input values will be used for testing your solution.
field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

# click(field1, 3, 5, 2, 2) should return:
# [[0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0],
#  [0, 1, -1, 1, 0]]

# click(field1, 3, 5, 1, 4) should return:
# [[-2, -2, -2, -2, -2],
#  [-2, 1, 1, 1, -2],
#  [-2, 1, -1, 1, -2]]


field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]
          
# click(field2, 4, 4, 0, 1) should return:
# [[-1, 1, 0, 0],
#  [1, 1, 0, 0],
#  [0, 0, 1, 1],
#  [0, 0, 1, -1]]

# click(field2, 4, 4, 1, 3) should return:
# [[-1, 1, -2, -2],
#  [1, 1, -2, -2],
#  [-2, -2, 1, 1],
#  [-2, -2, 1, -1]]

Example 1:

Given field:
field3 = [[0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, -1, 1, 0]]

Click location: (2, 2: row index = 2, column index = 2)

Resulting field:
[[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[0, 1, -1, 1, 0]] (same as the given field)


Example 2:

field4=
[[-1, 1, 0, 0],
[1, 1, 0, 0],
[0, 0, 1, 1],
[0, 0, 1, -1]]

Click location: (1, 3: row index = 1, column index = 3)

Resulting field:
[[-1, 1, -2, -2],
[1, 1, -2, -2],
[-2, -2, 1, 1],
[-2, -2, 1, -1]]
"""
