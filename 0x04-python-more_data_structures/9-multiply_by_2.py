#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return
    new_dic = a_dictionary.copy()
    for k, v in new_dic.items():
        new_dic[k] = v * 2
    return new_dic
