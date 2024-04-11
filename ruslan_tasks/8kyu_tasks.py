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



# https://www.codewars.com/kata/568dcc3c7f12767a62000038/train/python
def set_alarm(employed, vacation):
    return employed and not vacation

# https://www.codewars.com/kata/5772da22b89313a4d50012f7/train/python
def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"



# https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python
def count_by(x, n):
    return [ x*(i+1) for i in range(n)]


# https://www.codewars.com/kata/55cbc3586671f6aa070000fb/train/python?
def check_for_factor(base, factor):
    return True if base % factor == 0 else False


# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python
def row_sum_odd_numbers(n):
    start = 1+sum([2*x for x in range(n)])
    finish = 1+sum([2 * x+2 for x in range(n)][1:])
    arr_sum = sum([x for x in range(finish+1)][start:finish+1:2])
    return arr_sum


def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if  arr != None else 0

def correct(s):
    return s.replace("5", "S").replace("0", "O").replace("1", "I")


# https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python
def get_grade(s1, s2, s3):
    average  = (s1 + s2 + s3)/3
    if 90 <= average <= 100:
        return "A"
    elif 80 <= average < 90:
        return "B"
    elif 70 <= average < 80:
        return "C"
    elif 60 <= average < 70:
        return "D"
    elif 0 <= average < 60:
        return "F"

# https://www.codewars.com/kata/55f73be6e12baaa5900000d4/train/python
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

# https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/train/python
def switch_it_up(number):
    d = {
        0: 'Zero',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }
    return d[number]

switch_it_up(2)

# https://www.codewars.com/kata/555086d53eac039a2a000083/train/python
def lovefunc( flower1, flower2 ):
    return (flower1 + flower2) % 2 == 1