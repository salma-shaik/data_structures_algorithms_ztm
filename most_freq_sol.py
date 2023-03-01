def most_frequent(given_list):
    max_count = 0
    max_item = None
    count = {}

    for i in given_list:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
        if count[i] > max_count:
            max_count = count[i]
            max_item = i

    print(max_item)

# most_frequent(list1) should return 1.
list1 = [1, 3, 1, 3, 2, 1]
most_frequent(list1)

# most_frequent(list2) should return 3.
list2 = [3, 3, 1, 3, 2, 1]
most_frequent(list2)

# most_frequent(list3) should return None.
list3 = []
most_frequent(list3)

# most_frequent(list4) should return 0.
list4 = [0]
most_frequent(list4)

# most_frequent(list5) should return -1.
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
most_frequent(list5)