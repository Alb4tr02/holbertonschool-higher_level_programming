#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0 or i % 5 == 0):
            if i % 3 == 0:
                print("{:s}".format("Fizz"), end="")
            if (i % 5 == 0):
                print("{:s} ".format("Buzz"), end="")
            else:
                print("{:s}".format(" "), end="")
        else:
            print("{:d} ".format(i), end="")
