#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        strcpy = str
    else:
        strcpy = str[0:n]
        strcpy += str[n+1:]
    return strcpy
