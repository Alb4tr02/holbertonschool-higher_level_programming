#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = len(tuple_a)
    j = len(tuple_b)
    a = 0
    b = 0
    if i > 0:
        a = tuple_a[0]
    if j > 0:
        a = a + tuple_b[0]
    if i > 1:
        b = tuple_a[1]
    if j > 1:
        b = b + tuple_b[1]
    tup = (a, b)
    return (tup)
