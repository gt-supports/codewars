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


# https://www.codewars.com/kata/57f24e6a18e9fad8eb000296/train/python

def how_much_i_love_you(nb_petals):
    petals = {
        1: "I love you",
        2: "a little",
        3: "a lot",
        4: "passionately",
        5: "madly",
        0: "not at all"
    }
    return petals[nb_petals % 6]


# https://www.codewars.com/kata/555a67db74814aa4ee0001b5/train/python

def is_even(n):
    if n % 2 == 0 or n % 2 % 2 == 0:
        return True
    else:
        return False


# https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python

def positive_sum(arr):
    arr2 = []
    for i in arr:
        if i > 0:
            arr2.append(i)
    return sum(arr2)


# https://www.codewars.com/kata/53369039d7ab3ac506000467/train/python

def bool_to_word(boolean):
    return "Yes" if boolean else "No"


# https://www.codewars.com/kata/515e271a311df0350d00000f/train/python

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)
