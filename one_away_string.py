# either add, update or delete

def is_one_away(str1, str2):
    if abs(len(str1) - len(str2)) > 1 or (len(str1) == 0 and len(str2) == 0):
        return False

    if len(str1) == len(str2):
        req_min_match = len(str1) - 1
    else:
        req_min_match = min(len(str1), len(str2))

    match_counter = 0
    str1_idx = 0
    str2_idx = 0

    while match_counter <= req_min_match - 1 and str1_idx != len(str1) and str2_idx != len(str2):
       if str1[str1_idx] == str2[str2_idx]:
           match_counter += 1

       else:
           if len(str1) > len(str2):
               str1_idx += 1
               continue
           elif len(str1) < len(str2):
               str2_idx += 1
               continue

       str1_idx += 1
       str2_idx += 1

    if match_counter == req_min_match:
        return(True)
    else:
        return(False)


print(is_one_away("abcde", "abcd"))  # should return True
print(is_one_away("abde", "abcde")) # should return True
print(is_one_away("a", "a")) # should return True
print(is_one_away("abcdef", "abqdef"))  # should return True
print(is_one_away("abcdef", "abccef"))  # should return True
print(is_one_away("abcdef", "abcde"))  # should return True
print(is_one_away("aaa", "abc"))  # should return False
print(is_one_away("abcde", "abc"))  # should return False
print(is_one_away("abc", "abcde"))  # should return False
print(is_one_away("abc", "bcc"))  # should return False