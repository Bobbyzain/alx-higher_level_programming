#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()
    new_list = []
    for i in set_1:
        if i in set_2:
            new_list.append(i)
        else:
            continue
    new_set.update(new_list)
    return new_set
