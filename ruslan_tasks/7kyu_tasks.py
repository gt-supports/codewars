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
    return ''.join(list(url)[:index[0]]) if index !=[] else url
    # TODO: complete

remove_url_anchor("www.codewars.comabout")

# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python
def maskify(cc):
    print('#'*2)
    print('#' * -2)
    return ''.join(['#' if idx < len(cc)-4 else x for idx, x in enumerate(list(cc))])

# maskify('SF$SDfgsd2eA')
# maskify('2eA')

# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
import re
def disemvowel(string_):
    print(''.join(re.findall(r'[^aeiouAEIOU]', string_)))
    return ''.join(re.findall(r'[^aeiouAEIOU]', string_))


# disemvowel("This website is for losers LOL!")

# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
import math
def is_square(n):
    return n > 0 and int(math.sqrt(n)) == math.sqrt(n)

is_square(-25)


# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
def to_jaden_case(string):
    arr = []
    for w in string.split():
        arr_1 = w[0].upper() + w[1:len(w):].lower()
        arr.append(arr_1)
    return ' '.join(arr)



# to_jaden_case("How can mirrors be real if our eyes aren't real")


# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python
def open_or_senior(data):
    return ['Senior' if w[0] > 54 and w[1] > 7 else 'Open' for w in data]



# open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])

# https://www.codewars.com/kata/544aed4c4a30184e960010f4
def divisors(integer):
    div = [ x for x in range(2, integer) if integer % x == 0]
    return div if div else f'{integer} is prime'

# divisors(37)


# https://www.codewars.com/kata/52f3149496de55aded000410/train/python
def sum_digits(number):
    return sum(int(x) for x in str(abs(number)))

# sum_digits(-32)

# https://www.codewars.com/kata/58b8c94b7df3f116eb00005b
def reverse_letter(st):
    return ''.join([x for x in st if x.isalpha()][::-1])


reverse_letter("ultr53o?n")

# For str = "ultr53o?n", the output should be "nortlu".

# https://www.codewars.com/kata/5a3dd29055519e23ec000074
def check_exam(arr1,arr2):
    summa = sum(0 if arr2[i] == '' else 4 if arr1[i] == arr2[i] else -1 for i,x in enumerate(arr1))
    return summa if summa > 0 else 0



# https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python
def solve_1(s):
    return s.lower() if sum(1 for x in s if x.islower()) >= len(s) / 2 else s.upper()


# https://www.codewars.com/kata/5ac6932b2f317b96980000ca/train/python
def min_value(digits):
    return int(''.join([str(x) for x in sorted(set(digits))]))


# min_value([4, 8, 1, 4])

# https://www.codewars.com/kata/59cfc000aeb2844d16000075/train/python
def capitalize(s):
    even = ''.join(x.upper() if i%2==0 else x for i, x in enumerate(s)  )
    odds = ''.join(x.upper() if i % 2 == 1 else x for i, x in enumerate(s))
    return [even, odds]

# capitalize("abcdef")
# ,['AbCdEf', 'aBcDeF'])

# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/python
def factorial(n):
    x = 1
    for y in range(1, n+1):
        x *= y
    return 'ValueError ' if n < 0 or n > 12 else 1 if n == 0 else x

# factorial(5)
# factorial(1)

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)

    __repr__ = __str__

# https://www.codewars.com/kata/577bd8d4ae2807c64b00045b/train/python
def declare_winner(fighter1, fighter2, first_attacker):
    while fighter1.health>0 and fighter2.health>0:
        if fighter1.name == first_attacker:
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health>0:
                fighter1.health -= fighter2.damage_per_attack
        else:
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health>0:
                fighter2.health -= fighter1.damage_per_attack
    return fighter1.name if fighter1.health > 0 else fighter2.name

declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew")
# , "Lew")


# https://www.codewars.com/kata/51675d17e0c1bed195000001/train/python
def solution_d(digits):
    print(digits[:len(digits)-4])
    # print(max(int(x) for i, x in enumerate(digits[:len(digits)])))
    t = 0
    for i, x in enumerate(digits[:len(digits)-4]):
        if int(digits[i:i+5]) > t:
            t = int(digits[i:i+5])
    return t



# solution_d('123456777')
# solution_d('1283214321328871321312312321123123445547879884')

# https://www.codewars.com/kata/539de388a540db7fec000642
from dateutil import parser
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    # print(entered_code == correct_code and parser.parse(current_date) <= parser.parse(expiration_date))
    return entered_code == correct_code!=False and parser.parse(current_date) <= parser.parse(expiration_date)



check_coupon('123','123','September 5, 2014','October 1, 2014')
# , True);
check_coupon("123", "123", "July 9, 2015", "July 2, 2015")
# == False
check_coupon('123a','123','September 5, 2014','October 1, 2014')
# , False);

check_coupon(0, False, 'September 5, 2014', 'September 25, 2014')

# https://www.codewars.com/kata/664b9dd610985cc3b6784111/train/python

def all_nines(x):
    return 0

# https://www.codewars.com/kata/57a06b07cf1fa58b2b000252/train/python
def is_it_letter(s):
    return s.isalpha()

# https://www.codewars.com/kata/5436f26c4e3d6c40e5000282/train/python
def sum_of_n(n):
    # print( [sum(range(x+1)) for x in range(n+1)])
    # print(range(-n))
    # print([sum(range(x+1))*(-1 if n<0 else 1) for x in range(abs(n)+1)])

    # print([sum(range(x for x in range(n+1)] if n>=0 else [sum(range(x+1)) for x in range(abs(n)+1)]*(-1))
    return []

# sum_of_n(3)
sum_of_n(-3)


# https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


# https://www.codewars.com/kata/526c7363236867513f0005ca/train/python

def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year %100 != 0)

# https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/python
def remove_duplicate_words(s):
    arr_inx = sorted([s.split().index(x) for x in set(s.split())])
    return " ".join([s.split()[int(x)] for x in arr_inx])



remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta")
# , "alpha beta gamma delta")
remove_duplicate_words("my cat is my cat fat")
# , "my cat is fat")