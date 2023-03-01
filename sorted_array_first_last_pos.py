def first_pos(num_list, target_num):
    left_idx = 0
    right_idx = len(num_list) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        mid_elem = num_list[mid_idx]
        if target_num == mid_elem:
            if mid_idx - 1 >= 0 and target_num == num_list[mid_idx - 1]:
                right_idx = mid_idx - 1
            else:
                return mid_idx
        elif target_num > mid_elem:
            left_idx = mid_idx + 1
        elif target_num < mid_elem:
            right_idx = mid_idx - 1
    return -1


def last_pos(num_list, target_num):
    left_idx = 0
    right_idx = len(num_list) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        mid_elem = num_list[mid_idx]
        if target_num == mid_elem:
            if mid_idx < len(num_list)-1 and target_num == num_list[mid_idx + 1]:
                left_idx = mid_idx + 1
            else:
                return mid_idx
        elif target_num > mid_elem:
            left_idx = mid_idx + 1
        elif target_num < mid_elem:
            right_idx = mid_idx - 1
    return -1

# res = [first_pos([1,2,3,3,3,4,5,6,7], 3), last_pos([1,2,3,3,3,4,5,6,7], 3)]
# print(res)


res = [first_pos([5,7,7,8,8,10], 8), last_pos([5,7,7,8,8,10], 8)]
print(res)