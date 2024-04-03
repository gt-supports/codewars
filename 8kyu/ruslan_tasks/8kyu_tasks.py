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

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump