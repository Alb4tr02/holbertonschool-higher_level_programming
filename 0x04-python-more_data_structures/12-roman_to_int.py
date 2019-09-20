#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return None
    if not roman_string:
        return 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for i in range(0, len(roman_string)):
        res += dic[roman_string[i]]
    for i in range(0, len(roman_string)):
        if i + 1 <= len(roman_string) - 1:
            if dic[roman_string[i]] < dic[roman_string[i + 1]]:
                res -= dic[roman_string[i]] * 2
    return res
