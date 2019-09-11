#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst_dig = int(str(number)[-1])
if number < 0 and lst_dig != 0:
    lst_dig *= -1
if lst_dig == 0:
    msg = "and is 0"
elif lst_dig < 6:
    msg = "and is less than 6 and not 0"
else:
    msg = "and is greater than 5"
print("Last digit of {:d} is {:d} {:s}".format(number, lst_dig, msg))
