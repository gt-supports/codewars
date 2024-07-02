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
# from date import parser
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    # print(entered_code == correct_code and parser.parse(current_date) <= parser.parse(expiration_date))
    return entered_code == correct_code!=False and parser.parse(current_date) <= parser.parse(expiration_date)



# check_coupon('123','123','September 5, 2014','October 1, 2014')
# , True);
# check_coupon("123", "123", "July 9, 2015", "July 2, 2015")
# == False
# check_coupon('123a','123','September 5, 2014','October 1, 2014')
# , False);

# check_coupon(0, False, 'September 5, 2014', 'September 25, 2014')

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

#


# https://www.codewars.com/kata/526c7363236867513f0005ca/train/python

def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year %100 != 0)

# https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/python
def remove_duplicate_words(s):
    arr_inx = sorted([s.split().index(x) for x in set(s.split())])
    return " ".join([s.split()[int(x)] for x in arr_inx])



# remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta")
# , "alpha beta gamma delta")
# remove_duplicate_words("my cat is my cat fat")
# , "my cat is fat")


 # https://www.codewars.com/kata/5663f5305102699bad000056/train/python
def mxdiflg(a1, a2):
    if a1==[] or a2==[]:
        return -1
    arr_1 = [len(x) for x in a1]
    arr_2 = [len(x) for x in a2]
    min_1 = len(a1[arr_1.index(min(arr_1))])
    min_2 = len(a2[arr_2.index(min(arr_2))])
    max_1 = len(a1[arr_1.index(max(arr_1))])
    max_2 = len(a2[arr_2.index(max(arr_2))])
    return max(abs(min_1 - max_2), abs(min_2 - max_1))



# a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
# a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]

# mxdiflg(a1, a2)

# https://www.codewars.com/kata/514a6336889283a3d2000001
def get_even_numbers(arr):
    return [x for x in arr if x%2==0]

# https://www.codewars.com/kata/582746fa14b3892727000c4f/train/python
def count_developers(lst):
    return len([i for i, x in enumerate(lst) if lst[i]['continent'] == 'Europe' and lst[i]['language'] == 'JavaScript'])



lst1 = [
  { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
  { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
  { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
  { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
]


# count_developers(lst1)

# https://www.codewars.com/kata/59706036f6e5d1e22d000016
def words_to_marks(s):
    return sum(ord(x)-96 for x in list(s))
    print(ord("a")-96)

words_to_marks('attitude')

# https://www.codewars.com/kata/5a03b3f6a1c9040084001765/train/python
def angle(n):
    return 180 * (n-2)

# https://www.codewars.com/kata/556196a6091a7e7f58000018/train/python
def largest_pair_sum(numbers):
    return sum(sorted(numbers)[-2:])


# largest_pair_sum([99, 2, 2, 23, 19])

# https://www.codewars.com/kata/580a4734d6df748060000045/train/python
def is_sorted_and_how(arr):
    return "yes, ascending" if arr == sorted(arr) else "yes, descending" if arr == sorted(arr)[::-1] else "no"

# https://www.codewars.com/kata/59377c53e66267c8f6000027/train/python
def alphabet_war(fight):
    d_l = {"w": 4, "p": 3, "b": 2, "s": 1}
    d_r = {"m": 4, "q": 3, "d": 2, "z": 1}
    r_sum = sum(d_r[x] for x in fight if x in d_r)
    l_sum = sum(d_l[x] for x in fight if x in d_l)
    return "Right side wins!" if r_sum > l_sum else "Left side wins!" if r_sum < l_sum else "Let's fight again!"

# alphabet_war("zzzzsa")


# https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce
def no_odds(values):
    return [x for x in values if x%2==0]

# https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c/train/python
def even_numbers(arr,n):
    return [x for x in arr if x % 2 == 0][-n:]

# https://www.codewars.com/kata/5aff237c578a14752d0035ae/train/python
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    return (age_1**2+age_2**2+age_3**2+age_4**2+age_5**2+age_6**2+age_7**2+age_8**2)**0.5//2
    # your code

# https://www.codewars.com/kata/57ed30dde7728215300005fa/train/python
def bumps(road):
    return "Woohoo!" if list(road).count("n") < 16 else "Car Dead"

# https://www.codewars.com/kata/5a4138acf28b82aa43000117/train/python
def adjacent_element_product(array):
    max_p = array[0] * array[1]
    for i in range(1, len(array)-2):
        max_p = max(max_p, array[i]*array[i+1])
    print(max_p)
    return max_p


# adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921])
# , -14)

# https://www.codewars.com/kata/5300901726d12b80e8000498/train/python
def fizzbuzz(n):
    return ["FizzBuzz" if x % 15 == 0 else "Fizz" if x%3 == 0 else "Buzz" if x%5 == 0 else x for x in range(1,n+1)]


# https://www.codewars.com/kata/59a8570b570190d313000037/train/python
def sum_cubes(n):
    return sum(x**3 for x in range(1, n+1))

# https://www.codewars.com/kata/58fa273ca6d84c158e000052/train/python
def digits(n):
    return len(str(n))

# https://www.codewars.com/kata/535474308bb336c9980006f2/train/python
def greet(name):
    return f'Hello {name.capitalize()}!'

# https://www.codewars.com/kata/5680781b6b7c2be860000036/train/python
def vowel_indices(word):
    return [i for i, x in enumerate(word, 1) if x.lower() in "aeioyu"]

# vowel_indices("apple")


# https://www.codewars.com/kata/5506b230a11c0aeab3000c1f
def evaporator(content, evap_per_day, threshold):
    days = 0
    left = content
    limit = content * threshold /100
    while left >= limit:
        left *= (1 - evap_per_day / 100)
        days += 1
    return days

# evaporator(10, 10, 5)

# https://www.codewars.com/kata/525e5a1cb735154b320002c8
def triangular(n):
  return n * (n + 1) // 2 if n > 0 else 0

# https://www.codewars.com/kata/534d0a229345375d520006a0/train/python
def power_of_two(n):
    return n>0 and (n & n - 1) ==0
# power_of_two(73786976294838206460)

# https://www.codewars.com/kata/58daa7617332e59593000006/train/
def find_longest(arr):
    arr_len = [len(str(x)) for x in arr]
    idx = arr_len.index(max(arr_len))
    return arr[idx]



# find_longest([1, 10, 100, 300])

# https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5/train/python
def reverse_number(n):
    return n/abs(n)*int(str(abs(n))[::-1]) if n!=0 else 0


# https://www.codewars.com/kata/5a523566b3bfa84c2e00010b/train/python
def min_sum(arr):
    sum = 0
    for x in range(len(arr)//2):
        max_arr = arr.pop(arr.index(max(arr)))
        min_arr = arr.pop(arr.index(min(arr)))
        sum += max_arr * min_arr
    return sum

# min_sum([12,6,10,26,3,24])

# https://www.codewars.com/kata/57f759bb664021a30300007d/train/python
def switcheroo(s):
    return ''.join("a" if x == "b" else "b" if x == "a" else x for x in s)


# switcheroo('aaabcccbaaa')
# , 'bbbacccabbb')

# https://www.codewars.com/kata/5783d8f3202c0e486c001d23/train/python
def to_float_array(arr):
    return [float(x) for x in arr]
