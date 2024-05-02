# https://www.codewars.com/kata/559590633066759614000063/train/python

def min_max(lst):
    return [min(lst), max(lst)]


# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python

def xo(s):
    return True if s.lower().count("x") == s.lower().count("o") else False
