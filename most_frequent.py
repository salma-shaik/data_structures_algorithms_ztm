# [4,3,4,9,4]

def get_most_freq_num(test_arr):

    if len(test_arr) == 0:
        return None
    # Get the unique list of entries to use as keys
    key_list = list(set(test_arr))

    # Create a dictionary with above key list as unique keys and with default values of zero for each
    num_dict = dict(zip(key_list, [0]*len(key_list)))

    for i in test_arr:
        num_dict[i] +=1

    # Sort the dict by values in descending order
    num_dict_sorted = sorted(num_dict, key=num_dict.get, reverse=True)
    print(num_dict_sorted[0])

    # To sort the dict by key in descending order
    print(sorted(num_dict, reverse=True))

# get_most_freq_num([4,3,4,9,4])

get_most_freq_num([])
