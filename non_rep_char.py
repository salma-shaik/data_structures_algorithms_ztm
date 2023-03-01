# "aabcbcdff"
# "xxyz"
# "aabb"

def non_repeating(str):
    str_list = list(str)
    non_rep = None
    rep = []

    while len(str_list) != 0:
        char = str_list[0]
        str_list.remove(char)
        if char not in str_list:
            if char in rep:
                continue
            else:
                non_rep = char
                break
        else:
            rep.append(char)
            str_list.remove(char)
    print(non_rep)

      # not sure how to have
    # for i in str_list_temp:
    #     str_list.remove(i)
    #     if i not in str_list:
    #         non_rep = i
    #         break
    #     else:
    #         str_list.remove(i)
    #     str_list_temp = str_list

    #### Another implementation with dictionary. I think 1st solution is better coz don't have to go everything to create a dictionary ####

    """
    # Implement your function below.
    def non_repeating(given_string):
        char_count = {}
        for c in given_string:
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1
        for c in given_string:
            if char_count[c] == 1:
                return c
        return None
    """

non_repeating("abcab") # should return 'c'
non_repeating("abab") # should return None
non_repeating("aabbbc") # should return 'c'
non_repeating("aabbdbc") # should return 'd'