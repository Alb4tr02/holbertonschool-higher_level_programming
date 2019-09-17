#!/usr/bin/python3
def multiple_returns(sentence):
    a = 0
    b = 0
    if sentence is None:
        a = None
    else:
        b = sentence[0]
        a = len(sentence)
    tup = (a, b)
    return (tup)
