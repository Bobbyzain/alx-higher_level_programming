#!/usr/bin/python3
def best_score(a_dictionary):
    new_dict = a_dictionary
    score = 0
    if a_dictionary is None:
        return None
    else:
        for i in new_dict:
            if new_dict[i] > score:
                score = new_dict[i]
            else:
                continue
    b_val = list(new_dict.keys())[list(new_dict.values()).index(score)]
    return b_val
