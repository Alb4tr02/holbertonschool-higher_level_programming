#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    msg = "arguments:"
    a = len(sys.argv) - 1
    if (a == 0):
        msg = "arguments."
    elif (a == 1):
        msg = "argument:"
    print("{:d} {:s}".format(a, msg))
    for argument in sys.argv:
        if (sys.argv.index(argument) != 0):
            print("{:d}: {:s}".format(sys.argv.index(argument), argument))
