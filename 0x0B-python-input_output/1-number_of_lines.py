#!/usr/bin/python3
def number_of_lines(filename=""):
    a = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            a += 1
    return a
