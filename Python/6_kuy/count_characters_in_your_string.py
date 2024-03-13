# https://www.codewars.com/kata/52efefcbcdf57161d4000091


def count(s):
    if not s:
        return {}
    return {i: s.count(i) for i in set(s)}


"""
from collections import Counter

def count(string):
    return Counter(string)
"""
