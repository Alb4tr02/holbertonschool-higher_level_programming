#!/usr/bin/python3
msg = "0"
for i in range(0, 100):
    if i > 9:
        msg = ""
    if i < 99:
        print("{:s}{:d}, ".format(msg, i), end="")
    else:
        print("{:d}".format(i))
