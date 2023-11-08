#!/usr/bin/python3
for i, num  in enumerate(range(100)):
    if i < 99:
        print("{:02d}".format(num), end=", ")
    else:
        print("{}".format(num))
