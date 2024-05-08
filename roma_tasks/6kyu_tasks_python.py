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


# https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/python
def arithmetic(a, b, operator):
    if operator == 'add':
        return a + b
    if operator == 'subtract':
        return a - b
    if operator == 'multiply':
        return a * b
    if operator == 'divide':
        return a / b


# https://www.codewars.com/kata/5b180e9fedaa564a7000009a/solutions/python?filter=me&sort=best_practice&invalids=false
def solve(s):
    length = len([i for i in s if i.lower() == i])
    return s.lower() if length >= len(s) / 2 else s.upper()


# https://www.codewars.com/kata/58b8c94b7df3f116eb00005b/solutions/python
import re


def reverse_letter(s):
    letters = re.findall(r'[a-zA-Z]', s)
    return ''.join(letters[::-1])


# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/solutions/python

def row_sum_odd_numbers(n):
    if type(n) == int and n > 0:
        return n ** 3
    else:
        return "Input a positive integer"


# https://www.codewars.com/kata/5aba780a6a176b029800041c/solutions/python
def max_multiple(divisor, bound):
    return bound // divisor * divisor


# https://www.codewars.com/kata/5ac6932b2f317b96980000ca/solutions/python?filter=me&sort=best_practice&invalids=false
def min_value(digits):
    uniq_digits = sorted(list(set(digits)))
    return int(''.join(map(str, uniq_digits)))


# https://www.codewars.com/kata/59cfc000aeb2844d16000075/solutions/python
def capitalize(s):
    evenCap = ''.join([char.upper() if i % 2 == 0 else char for i, char in enumerate(s)])
    oddCap = ''.join([char.upper() if i % 2 != 0 else char for i, char in enumerate(s)])

    return [evenCap, oddCap]


# https://www.codewars.com/kata/556196a6091a7e7f58000018/solutions/python
def largest_pair_sum(numbers):
    new_muns = numbers.sort()
    return numbers[-1] + numbers[-2]


# https://www.codewars.com/kata/57ed30dde7728215300005fa/train/python
def bumps(road):
    return 'Woohoo!' if road.count('n') <= 15 else 'Car Dead'


# https://www.codewars.com/kata/5a4138acf28b82aa43000117/train/python
def adjacent_element_product(array):
    new_arr = []
    for i, num in enumerate(array[:-1]):
        new_arr.append(num * array[i + 1])
    return max(new_arr)


# https://www.codewars.com/kata/535474308bb336c9980006f2/train/python
def greet(name):
    return f"Hello {name[0].upper() + name[1:].lower()}!"


# https://www.codewars.com/kata/59a8570b570190d313000037/train/python
def sum_cubes(n):
    return sum(num ** 3 for num in range(1, n + 1))


# https://www.codewars.com/kata/58daa7617332e59593000006/train/python
def find_longest(numbers):
    largest = numbers[0]

    for number in numbers:
        if len(str(number)) > len(str(largest)):
            largest = number

    return largest


# https://www.codewars.com/kata/57f759bb664021a30300007d/train/python

def switcheroo(x):
    replacement = {'a': 'b', 'b': 'a'}
    return ''.join(replacement.get(letter, letter) for letter in x)


# https://www.codewars.com/kata/57eaec5608fed543d6000021/train/python

def div_con(x):
    sum_int = sum(i for i in x if type(i) == int)
    sum_none_int = sum(int(i) for i in x if type(i) == str)
    return sum_int - sum_none_int


# https://www.codewars.com/kata/5aa1bcda373c2eb596000112/solutions/python
def max_tri_sum(numbers):
    sorted_numbers = sorted(set(numbers), reverse=True)
    return sum(sorted_numbers[:3])


# https://www.codewars.com/kata/52aeb2f3ad0e952f560005d3/train/python
def sort_gift_code(code):
    return ''.join(sorted(code))


# https://www.codewars.com/kata/59377c53e66267c8f6000027/train/python
def alphabet_war(fight):
    left_side_letters = {
        'w': 4,
        'p': 3,
        'b': 2,
        's': 1
    }
    right_side_letters = {
        'm': 4,
        'q': 3,
        'd': 2,
        'z': 1
    }
    left_side_scores = 0
    right_side_scores = 0

    for char in fight:
        if char in left_side_letters:
            left_side_scores += left_side_letters[char]
        elif char in right_side_letters:
            right_side_scores += right_side_letters[char]

    if left_side_scores > right_side_scores:
        return 'Left side wins!'
    elif left_side_scores < right_side_scores:
        return 'Right side wins!'
    return "Let's fight again!"


# https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c/solutions/python
def even_numbers(arr, n):
    return [i for i in arr if i % 2 == 0][-n:]


# https://www.codewars.com/kata/55b051fac50a3292a9000025/train/python
def filter_string(st):
    return int(''.join([i for i in st if i.isdigit()]))


# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

def solution(number):
    sum = 0;
    if number < 0:
        return 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


# best practise(rewriting)
def solution_second(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)
