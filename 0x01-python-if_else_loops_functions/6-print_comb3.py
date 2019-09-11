#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i == 0 and j == 1:
            print("{:d}{:d}".format(i, j), end="")
        elif (i != j):
            print(", {:d}{:d}".format(i, j), end="")
print("")
