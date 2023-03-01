'''
Given a rotated sorted list --> find the # times it was rotated

Function will take a list of numbers

Function \returns the # times the sorted list was rotated

'''


####### My solution #########
def num_rotations(num_list):
    if len(num_list) == 0:
        return None
    elif len(num_list) == 1:
        return 1
    return num_list.index(min(num_list))

# res = num_rotations([5,6,9,0,2,3,4])
# print(res)

# res = num_rotations([7,9,3,5,6])
# print(res)

tests = []
test = {
    'input': {
        'nums': [19,25,29,3,5,6,7,9,11,14]
    },
    'output': 3
}

test1 = {
    'input': {
        'nums': [4,5,6,7,8,1,2,3]
    },
    'output': 5
}

test2 = {
    'input': {
        'nums': [1,2,3]
    },
    'output': 0
}

test3 = {
    'input': {
        'nums': [4,1,2,3]
    },
    'output': 1
}

test4 = {
    'input': {
        'nums': [2,3,4,5,6,1]
    },
    'output': 5
}

test5 = {
    'input': {
        'nums': []
    },
    'output': 0
}

tests = [test, test1, test2, test3, test4, test5]

#
# for test in tests:
#     res = num_rotations(test['input']['nums'])
#     print(res, res==test['output'])
#     print()


####### Jovian Solution ########
'''
1. Create a variable position with value 1
2. Compare the  number at current position to the number before it
3. If the number is smaller than its prdecessor, then return position
4. Otherwise, increment position and repeat till we exhaust all the numbers 
'''


'''
Brute-Force Approach

Linear complexity -- O(n)
'''
def lin_num_rotns(num_list):
    start_pos = 0

    while start_pos < len(num_list):
        if start_pos > 0 and num_list[start_pos] < num_list[start_pos-1]:
                return start_pos

        start_pos += 1
    return 0

# tests = [test, test1, test2, test3, test4, test5]

# for test in tests:
#     res = lin_num_rotns(test['input']['nums'])
#     print(res, res == test['output'])
#     print()

'''
Efficient Approach --> Using Binary Search

1. Find the middle element
2. If the  middle element is less than immediate left element, then it is the answer
3. If the middle element is < right most, answer lies in the left half
4. If the middle element is > right most, answer lies in the right half

'''

def count_num_rotations(nums_list):
    left_idx = 0
    right_idx = len(nums_list)-1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx)//2
        mid_elem = nums_list[mid_idx]

        if mid_idx > 0:
            if mid_elem < nums_list[mid_idx-1]:
                return mid_idx
            elif mid_elem < nums_list[-1]:
                right_idx = mid_idx-1
            elif mid_elem > nums_list[-1]:
                left_idx = mid_idx+1
        else:
            return mid_idx

    return 0

for test in tests:
    res = count_num_rotations(test['input']['nums'])
    print(res, res == test['output'])
    print()