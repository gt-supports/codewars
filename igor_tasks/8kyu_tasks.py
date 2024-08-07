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


# https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python

def summation(num):
    return sum(range(num + 1))


# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

def abbrev_name(name):
    first, last = name.upper().split()
    return f"{first[0]}.{last[0]}"


# https://www.codewars.com/kata/555086d53eac039a2a000083/train/python

def lovefunc(flower1, flower2):
    return (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 % 2 != 0 and flower2 % 2 == 0)


# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python

def find_needle(haystack):
    for i, item in enumerate(haystack):
        if item == "needle":
            return f"found the needle at position {i}"
    return "needle not found"


# https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/train/python

def past(h, m, s):
    return (h * 3600 * 1000) + (m * 60 * 1000) + (s * 1000)


# https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python

def invert(lst):
    return [-x for x in lst]


# https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python

def bmi(weight, height):
    bmi_value = weight / (height ** 2)

    bmi_categories = {
        (None, 18.5): "Underweight",
        (18.5, 25.0): "Normal",
        (25.0, 30.0): "Overweight",
        (30.0, None): "Obese"
    }

    for (lower, upper), category in bmi_categories.items():
        if (lower is None or bmi_value > lower) and (upper is None or bmi_value <= upper):
            return category

    # https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python

    def count_positives_sum_negatives(arr):
        if not arr:
            return []

        positive_count = 0
        negative_sum = 0

        for num in arr:
            if num > 0:
                positive_count += 1
            elif num < 0:
                negative_sum += num

        return [positive_count, negative_sum]


# https://www.codewars.com/kata/53dc23c68a0c93699800041d/train/python

def smash(words):
    return ' '.join(words)


# https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/python

def reverse_seq(n):
    return list(range(n, 0, -1))


# https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python

def count_by(x, n):
    return list(range(x, (x * n) + 1, x))


# https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python

def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = mpg * fuel_left
    return max_distance >= distance_to_pump


# https://www.codewars.com/kata/577a98a6ae28071780000989/train/python

def minimum(arr):
    return min(arr)


def maximum(arr):
    return max(arr)


# https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python

def reverse_words(s):
    return " ".join(reversed(list(s.split())))


# https://www.codewars.com/kata/5a2be17aee1aaefe2a000151/train/python

def array_plus_array(arr1, arr2):
    return (sum(arr1)) + (sum(arr2))


# https://www.codewars.com/kata/563e320cee5dddcf77000158/train/python

def get_average(marks):
    return int(sum(marks) / len(marks))


# https://www.codewars.com/kata/59342039eb450e39970000a6/train/python

def odd_count(n):
    return (n - 1) // 2 if n % 2 != 0 else (n - 1) // 2 + 1


# https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python

def sum_str(a, b):
    if a == "":
        a = "0"
    if b == "":
        b = "0"

    return str(int(a) + int(b))


# https://www.codewars.com/kata/5ad0d8356165e63c140014d4/train/python

def final_grade(exam, projects):
    grade = 0

    if exam > 90 or projects > 10:
        grade = 100
    elif exam > 75 and projects >= 5:
        grade = 90
    elif exam > 50 and projects >= 2:
        grade = 75

    return grade


# https://www.codewars.com/kata/55edaba99da3a9c84000003b/train/python

def divisible_by(numbers, divisor):
    return [num for num in numbers if num % divisor == 0]


# https://www.codewars.com/kata/57f6ad55cca6e045d2000627/train/python

def square_or_square_root(arr):
    result = []

    for num in arr:
        sqrt_num = int(num ** 0.5)
        if sqrt_num * sqrt_num == num:
            result.append(sqrt_num)
        else:
            result.append(num * num)

    return result


# https://www.codewars.com/kata/523b623152af8a30c6000027/train/python

def square(n):
    return n * n


# https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/python

def two_sort(array):
    return "***".join(sorted(array)[0])


# https://www.codewars.com/kata/563a631f7cbbc236cf0000c2/train/python

def move(position, roll):
    return position + roll * 2


# https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/train/python

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]


# https://www.codewars.com/kata/563b74ddd19a3ad462000054/train/python

def stringy(size):
    return ''.join('1' if i % 2 == 0 else '0' for i in range(size))


# https://www.codewars.com/kata/57089707fe2d01529f00024a/train/python

def check_alive(health):
    if health <= 0:
        return False
    else:
        return True


# https://www.codewars.com/kata/5ae62fcf252e66d44d00008e/train/python

def expression_matter(a, b, c):
    return max(a + b + c, a * b * c, a * (b + c), (a + b) * c)
