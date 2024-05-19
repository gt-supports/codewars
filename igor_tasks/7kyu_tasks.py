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


# https://www.codewars.com/kata/5949481f86420f59480000e7/train/python

def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"


# https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/python

def remove_url_anchor(url):
    return url.split("#")[0]


# https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/python

def gimme(input_array):
    return input_array.index(sorted(input_array)[1])


# https://www.codewars.com/kata/55b42574ff091733d900002f/train/python

def friend(x):
    massive_friend = []
    for i in x:
        if len(i) == 4:
            massive_friend.append(i)
        else:
            continue
    return massive_friend


# https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python

def number(lines):
    return ["{}: {}".format(i + 1, v) for i, v in enumerate(lines)]


# https://www.codewars.com/kata/57cc981a58da9e302a000214/train/python

def small_enough(array, limit):
    for num in array:
        if num > limit:
            return False
    return True


# https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/python

def is_anagram(test, original):
    return True if sorted(test.lower()) == sorted(original.lower()) else False


# https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python

def capitals(word):
    indexes = []

    for index, char in enumerate(word):
        if char.isupper():
            indexes.append(index)

    return indexes


# https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python

def sum_two_smallest_numbers(numbers):
    return sorted(numbers)[0] + sorted(numbers)[1]


# https://www.codewars.com/kata/58b8c94b7df3f116eb00005b/train/python

def reverse_letter(st):
    result = ""
    for i in st:
        if i.isalpha():
            result += i
    return result[::-1]


# https://www.codewars.com/kata/56747fd5cb988479af000028/train/python

def get_middle(s):
    length = len(s)
    if length % 2 == 0:
        return s[length // 2 - 1] + s[length // 2]
    else:
        return s[length // 2]


# https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python

def sum_two_smallest_numbers(numbers):
    return sorted(numbers)[0] + sorted(numbers)[1]


# https://www.codewars.com/kata/52f3149496de55aded000410/train/python

def sum_digits(number):
    sum = 0
    number = abs(number)
    while number > 0:
        sum += number % 10
        number //= 10

    return sum


# https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c/train/python

def sort_by_length(arr):
    return sorted(arr, key=len)


# https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/train/python

def solution(nums):
    return sorted(nums) if isinstance(nums, list) else []


# https://www.codewars.com/kata/5a3dd29055519e23ec000074/train/python

def check_exam(arr1, arr2):
    score = 0

    for i in range(0, 4):
        if arr1[i] == arr2[i]:
            score += 4
        elif arr2[i] == "":
            continue
        else:
            score -= 1

    return score if score >= 0 else 0


# https://www.codewars.com/kata/5ac6932b2f317b96980000ca/train/python


def min_value(digits):
    str_digits = ''.join(str(i) for i in sorted(set(digits)))
    nums = ""

    for i in str_digits:
        nums += i
    return int(nums)


# https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/train/python


def flatten_and_sort(array):
    return sorted([element for row in array for element in row])


# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

def get_sum(a, b):
    if a == b:
        return a
    elif a < b:
        return sum(range(a, b + 1))
    else:
        return sum(range(b, a + 1))


# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

def maskify(cc):
    if len(cc) > 4:
        return "#" * (len(cc) - 4) + cc[-4:]
    else:
        return cc


# https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python

def add_binary(a, b):
    sum_bin = bin(a + b)
    return ''.join(i for i in sum_bin if i.isdigit())[1::]


# https://www.codewars.com/kata/586f6741c66d18c22800010a/train/python

def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number + 1, step))
