# https://www.codewars.com/kata/559590633066759614000063/train/python

def min_max(lst):
    return [min(lst), max(lst)]


# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python

def xo(s):
    return True if s.lower().count("x") == s.lower().count("o") else False


# https://www.codewars.com/kata/56606694ec01347ce800001b/train/python

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


# https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/python

def arithmetic(a, b, operator):
    match operator:
        case "add":
            return a + b
        case "subtract":
            return a - b
        case "multiply":
            return a * b
        case _:
            return a / b
