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