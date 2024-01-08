#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    else:
        dec = [1, 5, 10, 50, 100, 500, 1000]
        rm = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        int_num = 0
        parser = 0
        numer_size = len(roman_string)
        while parser < numer_size:
            if parser == 0:
                int_num += dec[rm.index(roman_string[parser])]
            else:
                if dec[rm.index(roman_string[parser])] > dec[rm.index(roman_string[parser - 1])]:
                    int_num += (dec[rm.index(roman_string[parser])] - (dec[rm.index(roman_string[parser - 1])] * 2))
                else:
                    int_num += dec[rm.index(roman_string[parser])]
            parser += 1
    return int_num
