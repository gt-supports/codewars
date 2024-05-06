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


# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python

def reverse_words(text):
    return " ".join([word[::-1] for word in text.split(" ")])


# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

def find_short(s):
    return len(min(s.split(), key=len))


# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

def filter_list(l):
    new_list = []
    for i in l:
        if type(i) is int:
            new_list.append(i)
    return new_list


# https://www.codewars.com/kata/57f609022f4d534f05000024/train/python

def stray(arr):
    nums = [i for i in arr if arr.count(i) == 1]
    return nums[0]
