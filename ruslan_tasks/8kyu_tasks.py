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

# https://www.codewars.com/kata/55d24f55d7dd296eb9000030/python
def summation(num):
    return sum([n for n in range(num+1)])


# https://www.codewars.com/kata/5556282156230d0e5e000089/train/python

def dna_to_rna(dna):
    return dna.replace("T", "U")

# https://www.codewars.com/kata/577a98a6ae28071780000989/train/python
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

# https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# https://www.codewars.com/kata/58261acb22be6e2ed800003a/train/python
def get_volume_of_cuboid(length, width, height):
    return length * width * height

# https://www.codewars.com/kata/55cb632c1a5d7b3ad0000145/train/python
def hoop_count(n):
    return "Great, now move on to tricks" if n>=10 else "Keep at it until you get it"

# https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/python
def check(seq, elem):
     return elem in seq

# https://www.codewars.com/kata/59ca8246d751df55cc00014c/train/python
def hero(bullets, dragons):
    return True if bullets / (2 * dragons) >=1 else False

# https://www.codewars.com/kata/53dc54212259ed3d4f00071c/train/python
def sum_array(a):
    return sum(a)

# https://www.codewars.com/kata/56b1f01c247c01db92000076/python
def double_char(s):
    return ''.join([2 * letter for letter in s])

# https://www.codewars.com/kata/56efc695740d30f963000557/python
def to_alternating_case(string):
    return ''.join([letter.upper() if letter.islower() else letter.lower() for letter in string])


to_alternating_case('HeLLo WoRLD')

# https://www.codewars.com/kata/563a631f7cbbc236cf0000c2/train/python
def move(position, roll):
    return position + roll * 2

# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]



is_palindrome("aba")

# https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/python
def two_sort(array):
    return '***'.join(sorted(array)[0])

two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"])

# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python
def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [1, 15, 15]
    if human_years == 2:
        return [2, 24, 24]
    return  [human_years, 24+(human_years-2)*4, 24+(human_years-2)*5]


human_years_cat_years_dog_years(1)

# https://www.codewars.com/kata/5ae62fcf252e66d44d00008e/train/python
def expression_matter(a, b, c):
    return max([a * b * c, (a + b) * c, a * (b + c), a + b + c])

expression_matter(9,1,1)

# https://www.codewars.com/kata/55a70521798b14d4750000a4/train/python
def greet(name):
    return f"Hello, {name} how are you doing today?"


# https://www.codewars.com/kata/58ca658cc0d6401f2700045f/train/python
def find_multiples(integer, limit):
    # list(range(integer, limit + 1, integer))  разобрать решение
    return [integer*(i+1) for i in range(int(limit/integer)) ]


# https://www.codewars.com/kata/5aa736a455f906981800360d/train/python
def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]


# https://www.codewars.com/kata/5bb904724c47249b10000131/train/python
def points(games):
    total = 0
    for points in games:
        if int(points[0]) > int(points[-1]):
            total += 3
        elif int(points[0]) == int(points[-1]):
            total += 1
    return total



points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3'])

# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
def count_positives_sum_negatives(arr):
    positive = len([num for num in arr if num >0])
    negative = sum([num for num in arr if num < 0])
    return [positive, negative] if arr else []



count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])

# https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python
def area_or_perimeter(l , w):
    return l*w if l==w else 2*(l+w)


# https://www.codewars.com/kata/58649884a1659ed6cb000072/train/python
def update_light(current):
    return { 'green': 'yellow', 'yellow': 'red', 'red': 'green'}[current]

update_light('green')