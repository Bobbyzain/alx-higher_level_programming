#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arg = sys.argv
    arg = arg[1:]
    ap = len(arg)
    if ap == 1:
        print("{} argument:\n{}: {}".format(ap, ap, arg[0]))
    elif ap == 0:
        print("{} arguments.".format(ap))
    else:
        print("{} arguments.".format(ap))
        i = 0
        while i < ap:
            print("{}: {}".format((i + 1), arg[i]))
            i += 1
