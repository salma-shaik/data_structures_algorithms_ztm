'''
Implementation of binary search algorithm

Assume the list is sorted.
If not, O(nlogn) to sort it first

1. Take 2 idx variables --> low and high
2. low --> 1st index; high --> last index
3. mid = (low+high)/2
4. If elem at mid idx == target
    Could be that we have duplicate entries for target
    If elem at mid == elem at mid-1 (when mid-1 >=0)
    high = mid-1
    else return mid

5. Else if elem at mid > target ==> target is in the half below elem at mid
    Change high idx to mid-1, low would still be at 1st index
6. Else if elem at mid < target ==> target is in the half above elem at mid
    Change low idx to mid+1, high would still be at last index

7. Keep repeating until low == high
If this is the case, then either elem at low idx == elem at high idx == target or elem not found

'''


def get_elem_idx(num_list, target_num):
    left_idx = 0
    right_idx = len(num_list)-1

    while left_idx <= right_idx:
        mid_idx = (left_idx+right_idx)//2
        mid_elem = num_list[mid_idx]
        if target_num == mid_elem:
            if mid_idx - 1 >= 0 and num_list[mid_idx] == num_list[mid_idx - 1]:
                right_idx = mid_idx - 1
            else:
                return mid_idx
        elif target_num > mid_elem:
            left_idx = mid_idx + 1
        elif target_num < mid_elem:
            right_idx = mid_idx - 1
    return 'Not Found'

# res = get_elem_idx([1,2,3,4,5,6,7], target_num=6)
# print(res)

# res = get_elem_idx([1,2,3,4,5,6,7], target_num=3)
# print(res)

# res = get_elem_idx([1,2,3,3,3,4,5,6,7], target_num=3)
# print(res)

# res = get_elem_idx([1,2,3,3,3,4,5,6,7], target_num=1)
# print(res)

# res = get_elem_idx([1,1,2,3,3,3,4,5,6,7], target_num=1)
# print(res)

# res = get_elem_idx([1,1,2,3,3,3,4,5,6,7], target_num=7)
# print(res)

res = get_elem_idx([1,1,2,3,3,3,4,5,6,7], target_num=8)
print(res)