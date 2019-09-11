#!/usr/bin/python3
def uppercase(str):
    for a in str:
        c = ord(a)
        if c >= ord('a') and c <= ord('z'):
            c -= 32
        print("{:c}".format(c), end="")
    print("")
