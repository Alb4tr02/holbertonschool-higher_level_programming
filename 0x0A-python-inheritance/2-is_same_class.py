#!/usr/bin/python3
def is_same_class(obj, a_class):
    s = "<class '"+obj.__class__.__name__+"'>"
    return str(a_class).startswith(s)
