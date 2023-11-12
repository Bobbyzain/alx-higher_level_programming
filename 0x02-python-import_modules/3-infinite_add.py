#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arg = sys.argv[1:]
    qty = len(arg)
    if qty == 0:
        print("{}".format(qty))
    else:
        count = 0
        sum_num = 0
        while count < qty:
            sum_num += int(arg[count])
            count += 1
        print("{}".format(sum_num))
