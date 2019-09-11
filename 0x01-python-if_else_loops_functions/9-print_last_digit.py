#!/usr/bin/python3
def print_last_digit(number):
    lst_dig = int(str(number)[-1])
    print("{:d}".format(lst_dig), end="")
    return lst_dig
