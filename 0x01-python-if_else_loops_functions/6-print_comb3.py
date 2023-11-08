#!/usr/bin/python3
for i, num1 in enumerate(range(9)):
    if i < 8:
        for j, num2 in enumerate(range(num1 + 1, 9)):
            print("{}{}".format(num1, num2), end=", ")
    else:
        print("{}{}".format(i, i + 1))
