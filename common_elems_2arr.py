def common_elements(arr1, arr2):
    common_arr = []
    first_arr = arr1
    sec_arr = arr2
    if len(arr1) == 0 and len(arr2) == 0:
        return common_arr
    else:
        if len(arr1) < len(arr2):
            first_arr = arr2
            sec_arr = arr1
        for i in arr1:
            if i in arr2:
                common_arr.append(i)
    print(common_arr)

list_a1 = [1, 3, 4, 6, 7, 9]
list_a2 = [1, 2, 4, 5, 9, 10]
common_elements(list_a1, list_a2) # should return [1, 4, 9] (a list).

list_b1 = [1, 2, 9, 10, 11, 12]
list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
common_elements(list_b1, list_b2) # should return [1, 2, 9, 10, 12] (a list).

list_c1 = [0, 1, 2, 3, 4, 5]
list_c2 = [6, 7, 8, 9, 10, 11]
common_elements(list_c1, list_c2) # should return [] (an empty list).