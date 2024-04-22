# https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python
# 2024-04-02
import math
def remove_smallest(numbers):

    return [numbers[i] for i in range(len(numbers)) if i != numbers.index(min(numbers))]


# https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python
# 2024-04-04
def number(bus_stops):
    in_bus = sum([num[0]-num[1] for num in bus_stops])


def reverse_words(text):
    letters_arr = [text[i] for i in range(len(text))]
    word_arr = []
    gen_arr = []
    for i in range(len(letters_arr)):
        if i == 0:
            word_arr.append((letters_arr[i]))
            if i+1 < len(letters_arr) and letters_arr[i+1].isspace():
                gen_arr.append(''.join(word_arr))
                word_arr = []
        elif not letters_arr[i-1].isspace() and not letters_arr[i].isspace():
            word_arr.append(letters_arr[i])
            if i+1 < len(letters_arr) and letters_arr[i+1].isspace():
                gen_arr.append(''.join(word_arr))
                word_arr = []
            elif i+1 == len(letters_arr):
                gen_arr.append(''.join(word_arr))
        elif not letters_arr[i-1].isspace() and letters_arr[i].isspace():
            # word_arr = []
            word_arr.append(letters_arr[i])
            if i + 1 < len(letters_arr) and not letters_arr[i + 1].isspace():
                gen_arr.append(''.join(word_arr))
                word_arr = []
            elif i+1 == len(letters_arr):
                gen_arr.append(''.join(word_arr))
        elif letters_arr[i-1].isspace() and letters_arr[i].isspace():
            word_arr.append(letters_arr[i])
            if i + 1 < len(letters_arr) and not letters_arr[i + 1].isspace():
                gen_arr.append(''.join(word_arr))
                word_arr = []
            elif i+1 == len(letters_arr):
                gen_arr.append(''.join(word_arr))
        elif letters_arr[i-1].isspace() and not letters_arr[i].isspace():
            # word_arr = []
            word_arr.append(letters_arr[i])
            if i + 1 < len(letters_arr) and letters_arr[i + 1].isspace():
                gen_arr.append(''.join(word_arr))
                word_arr = []
            elif i+1 == len(letters_arr):
                gen_arr.append(''.join(word_arr))
        print(gen_arr)
    # print(''.join([''.join(list(words)[::-1]) for words in gen_arr]))
    return ''.join([''.join(list(words)[::-1]) for words in gen_arr])

# https://www.codewars.com/kata/57f609022f4d534f05000024/train/python
def stray(arr):
    return [arr[i] for i in range(len(arr)) if arr[i] != arr[i-1] and arr[i] != arr[i-2]][0]

# https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
def square_digits(num):
    print(int(''.join([str(int(x)**2) for x in str(num)])))
    return int(''.join([str(int(x)**2) for x in str(num)]))

# https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python
def nb_year(p0, percent, aug, p):
    i = 0
    while p0 < p:
        p0 += math.floor(p0 * percent/100) + aug
        i += 1
    return i

# https://www.codewars.com/kata/542c0f198e077084c0000c2e/python
def divisors(n):
    return len([x for x in range(1, n) if n % x == 0])

divisors(30)

# https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/train/python
def solution(nums):
    return sorted(nums) if nums else []


# https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python
def number(lines):
    return [f'{idx+1}: {x}' for idx, x in enumerate(lines)]


# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python
def DNA_strand(dna):
    d = {"A": "T", "T": "A", "C": "G", "G": "C"}
    # print(dna.translate(str.maketrans("ATCG", "TAGC"))) запомнить
    return ''.join([d[i] for i in list(dna)])


# https://www.codewars.com/kata/566fc12495810954b1000030/train/python
def nb_dig(n, d):
    arr = [k**2 for k in range(n+1)]
    return list(str(arr)).count(str(d))

# https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c/train/python
def sort_by_length(arr):
    return sorted(arr, key=len)


sort_by_length(["beg", "life", "i", "to"])

# https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/python
def arithmetic(a, b, operator):
    if operator == "add":
        return a+b
    elif operator == "subtract":
        return a-b
    elif operator == "divide":
        return a / b
    return a*b

 # создай словарь!!!
    #"add", "subtract", "divide", "multiply".


# https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/python
def remove_url_anchor(url):
    index = [idx for idx, x in enumerate(url) if x == "#"]
    print(index)
    return ''.join(list(url)[:index[0]]) if index !=[] else url
    # TODO: complete

remove_url_anchor("www.codewars.comabout")