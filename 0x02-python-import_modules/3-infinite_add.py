#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0
    for argument in sys.argv:
        if (sys.argv.index(argument) != 0):
            res += int(argument)
    print("{:d}".format(res))
