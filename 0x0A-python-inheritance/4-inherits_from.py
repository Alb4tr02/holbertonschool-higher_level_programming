#!/usr/bin/python3
def inherits_from(obj, a_class):
    a = obj.__class__.__name__ not in str(a_class)
    return a and isinstance(obj, a_class)
