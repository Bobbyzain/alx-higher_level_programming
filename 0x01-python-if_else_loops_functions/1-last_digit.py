#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
n = number[-1]
if int(number) >= 0:
    if int(n) > 5:
        print("Last digit of", number, "is", n, "and is greater than 5")
    elif int(n) < 6 and int(n) != 0:
        print("Last digit of", number, "is", n, "and is less than 6 and not 0")
    elif int(n) == 0:
        print("Last digit of", number, "is", n, "and is 0")
else:
    print("Last digit of", number, "is -" + n, "and is less than 6 and not 0")
