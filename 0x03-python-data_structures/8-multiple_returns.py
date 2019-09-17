#!/usr/bin/python3
def multiple_returns(sentence):
    a = 0
    b = 0
    if len(sentence) == 0:
        b = None
    else:
        b = sentence[0]
        a = len(sentence)
    tup = (a, b)
    return (tup)
