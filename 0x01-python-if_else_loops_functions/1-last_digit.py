#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
if int(number) >= 0:
    if int(number[-1]) > 5:
        print("The last digit of", number, "is", number[-1], "and is greater than 5")
    elif int(number[-1]) < 6: 
        print("The last digit of", number, "is", number[-1], "and is less than 6 and not zero")
    elif int(number[-1]) == 0:
        print("The last digit of", number, "is", number[-1], "and is zero")
else:
    print("The last digit of", number, "is -" + number[-1], "and is less than 6 and not zero")
