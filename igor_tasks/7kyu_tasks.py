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


# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

def filter_list(l):
    result = []
    for i in l:
        if isinstance(i, int):
            result.append(i)
    return result


# https://www.codewars.com/kata/5417423f9e2e6c2f040002ae/train/python

def digitize(n):
    return [int(i) for i in str(n)]


# https://www.codewars.com/kata/588a3c3ef0fbc9c8e1000095/train/python

def max_diff(lst):
    return sorted(lst, reverse=True)[0] - sorted(lst)[0] if len(lst) > 1 else 0


# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

def printer_error(s):
    count = 0
    for char in s:
        if ord(char) > ord('m'):
            count += 1
    return f"{count}/{len(s)}"


# https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python

def binary_array_to_number(arr):
    string_number = ''.join([str(num) for num in arr])
    return int(string_number, 2)


# https://www.codewars.com/kata/53d2697b7152a5e13d000b82/train/python

def copy_list(l):
    return l.copy()


# https://www.codewars.com/kata/57a04da9e298a7ee43000111/train/python

def reverse_list(lst):
    return lst[::-1]


# https://www.codewars.com/kata/586ec0b8d098206cce001141/train/python

def inverse_slice(items, a, b):
    return items[:a] + items[b:]


# https://www.codewars.com/kata/57d86d3d3c3f961278000005/train/python

def last(lst):
    if isinstance(lst, list) and len(lst) > 0:
        return lst[-1]
    else:
        return None


# https://www.codewars.com/kata/57ae18c6e298a7a6d5000c7a/train/python

def replace_all(obj, find, replace):
    return [elem if elem != find else replace for elem in obj] if isinstance(obj, list) else obj.replace(find, replace)


# https://www.codewars.com/kata/56b1eb19247c01493a000065/train/python

def unique_sum(lst):
    return sum(set(lst)) if len(lst) > 0 else None


# https://www.codewars.com/kata/54162d1333c02486a700011d/train/python

def penultimate(a):
    return a[-2]


# https://www.codewars.com/kata/59557b2a6e595316ab000046/train/python

def convert_hash_to_array(dct):
    return [[k, v] for k, v in dct.items()]


# https://www.codewars.com/kata/54466996990c921f90000d61/train/python

def is_monotone(heights):
    for i in range(len(heights) - 1):
        if heights[i] > heights[i + 1]:
            return False
    return True


# https://www.codewars.com/kata/580a4001d6df740d61000301/train/python

def complete_series(seq):
    highest = max(seq)
    if len(seq) != len(set(seq)):
        return [0]
    return list(range(highest + 1))
