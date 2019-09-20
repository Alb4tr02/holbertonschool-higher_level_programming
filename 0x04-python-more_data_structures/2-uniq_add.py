#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    a = 0
    new_list = list(set(my_list.copy()))
    for i in new_list:
        a += i
    return a
