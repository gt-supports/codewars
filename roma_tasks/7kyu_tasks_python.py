# https://www.codewars.com/kata/5949481f86420f59480000e7/solutions/python
def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'


# https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/solutions/python?filter=me&sort=best_practice&invalids=false
def row_weights(array):
    team1 = sum(array[::2])
    team2 = sum(array[1::2])
    return (team1, team2)


# https://www.codewars.com/kata/5982619d2671576e90000017/solutions/python?filter=me&sort=best_practice&invalids=false
def sponge_meme(s):
    result = ""

    for index, character in enumerate(s):
        if index % 2 == 0:
            result += character.upper()
        else:
            result += character.lower()

    return result


# https://www.codewars.com/kata/557af4c6169ac832300000ba/solutions/python?filter=me&sort=best_practice&invalids=false
def remove_rotten(bag_of_fruits):
    if bag_of_fruits:
        return [el[6:].lower() if el[:6] == 'rotten' else el for el in bag_of_fruits]
    return []


# https://www.codewars.com/kata/57d532d2164a67cded0001c7/solutions/python?filter=me&sort=best_practice&invalids=false

def histogram(results):
    histogram = ""
    for value in range(6, 0, -1):
        count = results[value - 1]
        line = f"{value}|{'#' * count}"
        if count > 0:
            line += f" {count}"
        line += "\n"
        histogram += line
    return histogram


# https://www.codewars.com/kata/5656b6906de340bd1b0000ac/solutions/python?filter=me&sort=best_practice&invalids=false
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


# https://www.codewars.com/kata/56541980fa08ab47a0000040/solutions/python?filter=me&sort=best_practice&invalids=false
def printer_error(s):
    k = 0

    for char in s:
        if char > 'm' or char < 'a':
            k += 1

    return f"{k}/{len(s)}"


# https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python

def binary_array_to_number(arr):
    return int(''.join(str(bit) for bit in arr), 2)


# https://www.codewars.com/kata/559590633066759614000063/train/python
def min_max(lst):
    return [min(lst), max(lst)]


# https://www.codewars.com/kata/55d1d6d5955ec6365400006d/train/python
import math


def round_to_next5(n):
    return math.ceil(n / 5) * 5


# https://www.codewars.com/kata/57cc981a58da9e302a000214/solutions/python
def small_enough(array, limit):
    return max(array) <= limit
