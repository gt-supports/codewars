# https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python
# 2024-04-03
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1*value2
    elif operator == "/":
        return value1 / value2


def remove_exclamation_marks(s):
    return s.replace('!', '')

# https://www.codewars.com/kata/5861d28f124b35723e00005e/solutions/python
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python
def reverse_words(text):
    print( ' '.join([''.join(list(words)[::-1]) for words in text.split()]))
    print(''.join([words for words in list(text) if words.isalpha()]))
    print(' '.join([''.join(list(words)[::-1]) for words in text.split()]))
    print(' '.join([''.join(list(words)[::-1]) for words in text.split()]))
    return ' '.join([''.join(list(words)[::-1]) for words in text.split()])
# haven't finished yet
reverse_words("double  spaced")

# https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python
def count_by(x, n):
    return [ x*(i+1) for i in range(n)]