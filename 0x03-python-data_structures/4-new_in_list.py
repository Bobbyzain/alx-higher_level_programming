#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    g = my_list.copy()
    if idx < 0:
        return g
    elif idx >= len(my_list):
        return g
    else:
        g[idx] = element
    return g
