#!/usr/bin/python3
for i, num  in enumerate(range(100)):
    if i < 99:
        if i < 10:
            print("0{}".format(num), end=", ")
        else:
            print("{}".format(num), end=", ")
    else:
        print("{}".format(num))
