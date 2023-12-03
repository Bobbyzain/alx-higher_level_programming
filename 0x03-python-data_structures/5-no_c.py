#!/usr/bin/python3
def no_c(my_string):
    i = 0
    cleaned_str = ""
    while i < len(my_string):
        if my_string[i] == "c" or my_string[i] == "C":
            pass
        else:
            cleaned_str += my_string[i]
        i += 1

    return cleaned_str
