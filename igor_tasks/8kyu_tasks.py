# test comments
# https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/train/python

def switch_it_up(number):
    words = {
        0: "Zero",
        1: "One",
        2: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    return words.get(number)


# https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python

def double_char(s):
    return "".join([i * 2 for i in s])


# https://www.codewars.com/kata/5625618b1fe21ab49f00001f/train/python

def say_hello(name):
    return f"Hello, {name}"
