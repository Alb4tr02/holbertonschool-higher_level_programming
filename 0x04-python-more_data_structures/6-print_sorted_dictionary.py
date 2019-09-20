#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    list = (sorted(a_dictionary.items()))
    for i in list:
        print("{}{} {}".format(i[0], ":", i[1]))
