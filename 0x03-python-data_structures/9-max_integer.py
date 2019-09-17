#!/usr/bin/python3
def max_integer(my_list=[]):
    a = 0
    if my_list is None or len(my_list) == 0:
        return (None)
    else:
        a = my_list[0]
        for i in my_list:
            if i > a:
                a = i
    return a
