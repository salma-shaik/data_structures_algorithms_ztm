def is_rotation(lst1, lst2):
    rotation_flag = True

    if len(lst1) != len(lst2):
        rotation_flag = False

    lst2_first_elem = lst2[0]
    lst1_l2_first_elem_idx = lst1.index(lst2_first_elem)
    lst1_rearngd = lst1[lst1_l2_first_elem_idx:] + lst1[:lst1_l2_first_elem_idx]

    for i,j in zip(lst1_rearngd,lst2):
        if i!=j:
            rotation_flag = False
            break
    print(rotation_flag)

list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
is_rotation(list1, list2a) # should return False.
#
list2b = [4, 5, 6, 7, 1, 2, 3]
is_rotation(list1, list2b) # should return True.
#
list2c = [4, 5, 6, 9, 1, 2, 3]
is_rotation(list1, list2c) # should return False.
#
list2d = [4, 6, 5, 7, 1, 2, 3]
is_rotation(list1, list2d) # should return False.
#
list2e = [4, 5, 6, 7, 0, 2, 3]
is_rotation(list1, list2e) # should return False.
#
list2f = [1, 2, 3, 4, 5, 6, 7]
is_rotation(list1, list2f) # should return True.
#
list2g = [7, 1, 2, 3, 4, 5, 6]
is_rotation(list1, list2g) # should return True.