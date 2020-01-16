#!/usr/bin/python3

""" Look for the peak """


def find_peak(list_of_integers):
    """ Find the peak """
    if len(list_of_integers) == 0:
        return None
    else:
        peak = list_of_integers[0]
        for n in list_of_integers:
            if n > peak:
                peak = n
        return peak
