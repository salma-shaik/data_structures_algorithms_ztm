"""
The size of the field is 3x4, and there are bombs at the positions [0, 0] (row index = 0, column index = 0) and [0, 1]
(row index = 0, column index = 1).

Then, the resulting field should be:

[[-1, -1, 1, 0],
 [ 2, 2, 1, 0],
 [ 0, 0, 0, 0]]


 # NOTE: The following input values will be used for testing your solution.
# mine_sweeper([[0, 2], [2, 0]], 3, 3) should return:
# [[0, 1, -1],
#  [1, 2, 1],
#  [-1, 1, 0]]

"""

import numpy as np


# There can be any number of bombs
def identify_bombs(num_bombs, num_rows, num_cols):
    ms_arr = np.zeros((num_rows, num_cols))

    for b in num_bombs:
        x = b[0]
        y = b[1]
        ms_arr[x, y] = -1

        adj_pos = [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y - 1], [x, y + 1], [x + 1, y - 1], [x + 1, y],
                   [x + 1, y + 1]]

        for pos in adj_pos:
            # python allows negative indices. So even if -1, 2 --> still trying to assign some value whereas isn't helpful
            # here because logic based on positive indices
            if pos[0] >= 0 and pos[1] >= 0:
                try:
                    # -1 check to avoid changing elements in matrix which are already assigned -1 to represent bomb
                    # location inside try to catch index error
                    if ms_arr[pos[0], pos[1]] != -1:
                        ms_arr[pos[0], pos[1]] += 1
                except:
                    pass
    print(ms_arr)


identify_bombs([[0, 2], [2, 0]], 3, 3)  # should return:
# [[0, 1, -1],
#  [1, 2, 1],
#  [-1, 1, 0]]

identify_bombs([[0, 0], [0, 1], [1, 2]], 3, 4)  # should return:
# [[-1, -1, 2, 1],
#  [2, 3, -1, 1],
#  [0, 1, 1, 1]]

identify_bombs([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5)  # should return:
# [[1, 2, 2, 1, 0],
#  [1, -1, -1, 2, 0],
#  [1, 3, -1, 2, 0],
#  [0, 1, 2, 2, 1],
#  [0, 0, 1, -1, 1]]
