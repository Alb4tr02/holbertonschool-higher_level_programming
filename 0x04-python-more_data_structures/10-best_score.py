#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    b = list(a_dictionary.keys())[0]
    a = a_dictionary[b]
    for k, v in a_dictionary.items():
        if v > a:
            b = k
    return b
