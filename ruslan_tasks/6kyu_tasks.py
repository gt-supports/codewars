# Old tasks
import string


# https://www.codewars.com/kata/556deca17c58da83c00002db
def tribonacci(signature, n):
    last_three = signature[0:n:]
    for i in range(n-3):
        last_three.append(sum(last_three[-3::]))
    return last_three

# https://www.codewars.com/kata/546f922b54af40e1e90001da
def alphabet_position(text):
    d = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26
    }
    return " ".join(str(d[letter]) for letter in list(text.lower()) if letter in d)

# https://www.codewars.com/kata/523f5d21c841566fde000009
def array_diff(a, b):
    new_arr = []
    for num in a:
        if num not in b:
            new_arr.append(num)
    return new_arr

# https://www.codewars.com/kata/576757b1df89ecf5bd00073b
def tower_builder(n_floors):
    return [" " * ((n_floors-i-1)) + "*" * (1 + 2*i) + " " * ((n_floors-i-1)) for i in range(n_floors)]

# https://www.codewars.com/kata/5266876b8f4bf2da9b000362
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return names[0] + " likes this"
    elif len(names) == 2:
        return names[0] + " and " + names[1] + " like this"
    elif len(names) == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    elif len(names) >=4:
        return names[0] + ", " + names[1] + " and " + str(len(names)-2) + " others like this"

# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python
# 2024-04-04
def is_valid_walk(walk):
    return walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e') and len(walk) == 10


# https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python
def bouncing_ball(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and window < h:
        i = 0
        while h * bounce ** i > window:
            i += 1
        return 2*i-1
    else:
        return -1

# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python
def find_nb(m):
    n = 0
    sum = 0
    while sum < m:
        sum += (n+1)**3
        n += 1
    return n if sum == m else -1

# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python
def high(x):
    arr = []
    for word in x.split():
        weight = 0
        for letter in word:
            weight += ord(letter)-96
        arr.append(weight)
    max_weight_index = [x for x in range(len(arr)) if arr[x] == max(arr)][0]
    return x.split()[max_weight_index]


# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python
def queue_time(customers, n):
    if n == 1:
        return sum(customers)
    elif n >= len(customers):
        return max(customers)
    else:
        queue_arr = []
        new_arr = customers[::-1]
        for i in range(n):
            queue_arr.append(new_arr.pop())
        cust_len = len(new_arr)
        queue_arr_len = len(queue_arr)
        queue = 0
        while cust_len > 0 or queue_arr_len > 0:
            min_arr = min(queue_arr)
            queue_arr = [x-min_arr for x in queue_arr]
            queue += min_arr
            queue_arr.remove(0)
            queue_arr_len -= 1
            for i in range(n - len(queue_arr)):
                if len(new_arr) > 0:
                    queue_arr.append(new_arr.pop())
                    queue_arr_len += 1
                    cust_len -= 1
        return queue



# https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
def solution(s):
    return ''.join([" " + letter  if letter.isupper() else letter for letter in list(s) ])

# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
def order(sentence):
    # print(sorted(sentence.split(), key = lambda word: sorted(word))) не понял
    keys = []
    for word in sentence.split(" "):
        for symbol in word:
            if symbol.isdigit():
                keys.append(symbol)
    my_dict = dict(zip(keys, sentence.split(" ")))
    arr = []
    for idx in sorted(keys):
        arr.append(my_dict[idx])
    return ' '.join(arr)



order("is2 Thi1s T4est 3a")

# https://www.codewars.com/kata/5626b561280a42ecc50000d1/python
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    my_arr = []
    for i in range(a, b+1):
        check = 0
        for j in range(len(str(i))):
            check += int(str(i)[j])**(j+1)
        if check == i:
            my_arr.append(i)
    return my_arr

sum_dig_pow(1,200 )

# https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python
def expanded_form(num):
    return ' + '.join([str(int(x)*10**y) for y, x in enumerate(list(str(num))[::-1]) if int(x) != 0][::-1])

expanded_form(70304)

# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python
def two_sum(numbers, target):
    for i, num_i in enumerate(numbers):
        for j, num_j in enumerate(numbers):
            if i!=j and num_i+num_j == target:
                return i,j

two_sum([1, 2 , 3], 4)

# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
def count(s):
    unique_letters = [ letter for letter in set(list(s))]
    idx= [list(s).count(letter) for letter in unique_letters ]
    return {keys:values for keys, values in zip(unique_letters, idx)}

def count_test(s):
    print({i: s.count(i) for i in s})


# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
def dig_pow(n, p):
    suma = sum([int(x)**(p+i) for i, x in enumerate(list(str(n)))])
    return suma / n if suma % n == 0 else -1

dig_pow(46288, 3)


# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2 == 1][0]



find_it([1,1,2,-2,5,2,4,4,-1,-2,5])

# https://www.codewars.com/kata/57814d79a56c88e3e0000786/python

def decrypt(encrypted_text, n):
    if encrypted_text == None:
        return None
    elif encrypted_text == '':
        return ''
    for x in range(n):
        divide = len(encrypted_text) // 2
        if x % 2 == 0:
            if len(encrypted_text) % 2 != 0:
                even = encrypted_text[:divide:]
                odd = encrypted_text[divide::]
            else:
                even = encrypted_text[:divide:]
                odd = encrypted_text[divide::]
        else:
            if len(encrypted_text) % 2 != 0:
                even = encrypted_text[:divide:]
                odd = encrypted_text[divide::]
            else:
                even = encrypted_text[:divide:]
                odd = encrypted_text[divide::]
        my_arr = []
        for i in range(max(len(odd), len(even))):
            my_arr.append(odd[i])
            if i < len(even):
                my_arr.append(even[i])
        encrypted_text = ''.join(my_arr)
    return encrypted_text
    for i in range(n):
        odd= ''.join([odd for idx, odd in enumerate(encrypted_text) if idx%2 != 0])
        even= ''.join([even for idx, even in enumerate(encrypted_text) if idx % 2 == 0])
        encrypted_text = odd + even
    return encrypted_text

def encrypt(text, n):
    if text == None:
        return None
    elif text == '':
        return ''
    for i in range(n):
        odd = ''.join([odd for idx, odd in enumerate(text) if idx%2 != 0])
        even = ''.join([even for idx, even in enumerate(text) if idx % 2 == 0])
        text = odd + even
    return text

# decrypt(decrypt("hskt svr neetn!Ti aai eyitrsig", 1))
# encrypt("012345", 3)

# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
def duplicate_count(text):
    return sum([1 for x in set(text.lower()) if list(text.lower()).count(x) > 1])
# Your code goes here

duplicate_count("abcdeaB")

# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
def is_pangram(s):
    print(string.ascii_lowercase)
    print()
    return len([x for x in set(s.lower()) if x.isalpha()]) == 26



# is_pangram("1bcdefghijklmnopqrstuvwxyz")
# is_pangram("The quick, brown fox jumps over the lazy dog!")

# https://www.codewars.com/kata/550498447451fbbd7600041c/train/python
def comp(array1, array2):
    if array1 == None or array2 == None or array1 =={} or array2 =={} or array1 == null or array2 == null:
        return False
    if len(array1) != len(array2):
        return False
    array1 = [abs(x) for x in array1]
    array2 = [abs(y) for y in array2]
    check = 0
    for idx, x in enumerate(sorted(array1)):
        for idy, y in enumerate(sorted(array2)):
            if idx == idy and x**2 == y:
                check += 1
    return True if check == len(array1) else False

    # your code

# comp([121,144,19,161,19,144,19,11], [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19])

# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python
def delete_nth(order,max_e):
    new_arr = []
    for x in order:
        idx_arr = [i for i, y in enumerate(order) if y == x]
        new_arr += idx_arr[:max_e]
    arr = list(set(sorted(new_arr)))
    return [num for idx, num in enumerate(order) if idx in arr]



delete_nth(["a", 2, 3, "a", "a", 2, "a", 2, 3, 3, "a", 4, 5, 3, 1], 3)
# delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3)

# https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python
def count_smileys(arr):
    eyes = [':', ';']
    noses = ['-', '~']
    mouths = [')','D']
    print(sum([1 for x in arr if x[0] in eyes and x[-1] in mouths and x[1] in noses if len(x) == 3]))
    count = 0
    for x in arr:
        if x[0] in eyes and x[-1] in mouths:
            if len(x) == 3 and x[1] in noses or len(x) == 2:
                count += 1
    print(count)
    return  count


    # return sum([1 for x in arr if x[0] in eyes and x[-1] in mouths])

# count_smileys([':)', ':(', ':D', ':O', ':;'])


# https://www.codewars.com/kata/514b92a657cdc65150000006
def solution(number):
    # print(sum(x for x in range(number) if x % 3 == 0  or x % 5 == 0))
    return sum([x for x in range(number) if x % 3 == 0  or x % 5 == 0])


# solution(6)

# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
def spin_words(sentence):
    print(' '.join([w[::-1] if len(w)>4 else w for w in sentence.split()]))
    # Your code goes here
    return ' '.join([w[::-1] if len(w)>4 else w for w in sentence.split()])


# spin_words("This is another test")

# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
def digital_root(n):
    # print( n%9 or n and 9)
    while len(str(n)) > 1:
        n = sum([int(x) for x in list(str(n))])
    return n

digital_root(942)

# https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
def create_phone_number(n):
    # чужие решения разбор
    # print("({}{}{}) {}{}{}-{}{}{}{}".format(*n))
    x = ''.join(map(str, n))
    # print(x)
    # print('(%s) %s-%s'%(x[:3], x[3:6], x[6:]))
    # print('(%s) %a-%s' % (x[:3], x[3:6], x[6:]))


    a =''.join([str(x) for idx, x in enumerate(n) if idx <3])
    b =''.join([str(x) for idx, x in enumerate(n) if idx >= 3 and idx <6])
    c = ''.join([str(x) for idx, x in enumerate(n) if idx >= 6 and idx < 10])
    return "("+a+") "+b + "-"+c

    # print("("+''.join(str(n[0:3]))+") "+str(n[3:6])+"-" +str(n[6:]))

    # "(123) 456-7890"
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python
def find_outlier(integers):
    # arr = [ 1 if x%2 else 0 for x in integers ]
    arr = [x % 2 for x in integers]
    # print(arr.index(1))
    # print(arr.index(0))
    # print(integers.index(1719))
    id = [idx for idx, y in enumerate(arr) if arr.count(y) == 1 ][0]
    # print(integers[id])
    return integers[id]

# find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])
# find_outlier([160, 3, 1719, 19, 11, 13, -21])


# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python
def count_bits(n):
    return sum(int(x) for x in bin(n)[2:])

# count_bits(1234)

# https://www.codewars.com/kata/517abf86da9663f1d2000003
import math
def persistence(n):
    i = 0
    arr = list(str(n))
    while len(arr) > 1:
        n = math.prod([int(x) for x in arr])
        arr = list(str(n))
        i += 1
    return i


    # your code

# persistence(39)

# https://www.codewars.com/kata/517abf86da9663f1d2000003
import re
def to_camel_case(text):
    # print(re.sub('_|-|-[a-z]{}1|_[a-z]{1}','',text))
    print(text.title())
    text = re.sub('_|-', ' ', text)
    text = ''.join([x[0].upper()+x[1::] if idx > 0 else x for (idx, x) in enumerate(text.split())])
    text2 = ''.join([x.capitalize() if idx > 0 else x for (idx, x) in enumerate(text.split())])
    # print(text2)
    return text



# to_camel_case("the_stealth_warrior")
# to_camel_case("The-Stealth-Warrior")

# https://www.codewars.com/kata/5287e858c6b5a9678200083c
def narcissistic( value ):
    return sum(int(x)**len(str(value)) for x in str(value)) == value

narcissistic(153)

# https://www.codewars.com/kata/54e6533c92449cc251001667
def unique_in_order(sequence):
    if len(sequence) == 0: return []
    arr = []
    arr.append(sequence[0])
    for x in sequence:
        if x !=arr[-1]:
            arr.append(x)
    return arr

unique_in_order('AAAABBBCCDAABBB')  # ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')          #['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])    #[1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   #[1, 2, 3]

# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python
def find_even_index(arr):
    id_arr = [id for id, x in enumerate(arr) if sum(arr[:id:]) == sum(arr[id+1::])]
    return id_arr[0] if id_arr!=[] else -1


# find_even_index([8,8])

# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
def solution(s):
    arr_1 = list(s)[0::2]
    arr_2 = list(s)[1::2]
    arr = [x+y for idx, x in enumerate(arr_1) for idy, y in enumerate(arr_2) if idx == idy]
    if len(s)%2:
        arr.append(s[-1]+'_')
    return arr

# solution('dfdgdgwge')

# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

def find_uniq(arr):
    return min(arr) if arr.count(min(arr)) == 1 else max(arr)

find_uniq([ 1, 1, 1, 2, 1, 1 ])

# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python
def find_missing_letter(chars):
    arr = [ord(i) for i in chars]
    for id, x in enumerate(arr):
        if arr[id:id+2][-1]-arr[id:id+2][0] == 2:
            return chr(arr[id:id+2][0]+1)


# find_missing_letter(['a','b','c','d','f'])

# https://www.codewars.com/kata/5277c8a221e209d3f6000b56
def valid_braces(string):
    while '{}' in string:
        string = string.replace('{}', '')
    while '[]' in string:
        string = string.replace('[]', '')
    while '()' in string:
        string = string.replace('()', '')
    while '{}' in string:
        string = string.replace('{}', '')
    while '[]' in string:
        string = string.replace('[]', '')
    while '{}' in string:
        string = string.replace('{}', '')
    while '()' in string:
        string = string.replace('()', '')
    print(string == '')
    return string == ''

# valid_braces("([{}])")


# https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python
import math
def is_prime(num):
    if num < 2:
        return False
    sqrt = int(math.sqrt(num)+1)
    for i in range(2, sqrt):
        if num % i == 0:
            return False
    return True


# is_prime(2)

# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python
def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""
    print([''.join([strarr[i+k] for k in range(k)]) for i in range(len(strarr)-k+1)])
    arr = [''.join([strarr[i+k] for k in range(k)]) for i in range(len(strarr)-k+1)]
    arr_len = [len(x) for x in arr]
    print(arr[arr_len.index(max(arr_len))])
    return arr[arr_len.index(max(arr_len))]


# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)

# longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3)

# "abigailtheta"

# https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python
def in_array(array1, array2):
    arr = []
    for x in array1:
        for y in array2:
            if x in y and x not in arr:
                arr.append(x)
    return sorted(arr)


a1 = ["arp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp']

in_array(a1, a2)

# https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python
def roman_solution(n):
    thousand = n//1000
    hundreds  = (n%1000)//100
    decimals = (n%100)//10
    dig = n%10
    num = ('M'*thousand + ('CM' if hundreds == 9 else "D"+"C"*(hundreds-5) if hundreds>=5
                            else "CD" if hundreds == 4 else "C"*hundreds)+
                        ('XC' if decimals == 9 else "L"+"X"*(decimals-5) if decimals>=5
                            else "XL" if decimals == 4 else "X"*decimals) +
                        ('IX' if dig == 9 else "V" + "I" * (dig - 5) if dig >= 5
                        else "IV" if dig == 4 else "I" * dig))
    return num

roman_solution(2589)

# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

# https://www.codewars.com/kata/51b6249c4612257ac0000005/train/python
def roman_to_dec_solution(str):
    d = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }
    num = 0
    i = 0
    while i < len (str):
        if str[i:i+2] in d:
            num += d[str[i:i+2]]
            i += 2
        else:
            num += d[str[i]]
            i += 1
    return num


# roman_to_dec_solution("MDCLXVI")

# https://www.codewars.com/kata/59daf400beec9780a9000045/train/python
def name_in_str(strng : str, name : str) -> bool:
    letters = [x for x in name.lower() if x in strng.lower() ]
    print(letters)
    if len(letters) != len(name):
        print("1 False")
        return False
    count_letters_set = [name.lower().count(x) for x in set(letters)]
    count_letters_strn = [strng.lower().count(x) for x in set(letters)]
    check_amount = [1 if count_letters_set[i]<=count_letters_strn[i] else 0 for i, x in enumerate(count_letters_set)]
    if sum(check_amount) != len(check_amount):
        return False



    order_lst = [ x for x in strng.lower()  if x in letters]
    check_order = [1 if letters[i] == order_lst[i] else 0 for i, x in enumerate(letters) ]
    if sum(check_order) != len(check_order):
        return False
    return True




# name_in_str("Across the rivers", "chris")  #True)
# name_in_str("Next to a lake", "chris") # False)
# name_in_str("Under a sea", "chris") # False)
# name_in_str("A crew that boards the ship", "chris") # False)
# name_in_str("A live son l ", "Allison") # False)
# name_in_str("Just enough nice friends", "Jennifer") # False)
# name_in_str("thomas", "Thomas") # True)
# name_in_str("pippippi", "Pippi") # True)
# name_in_str("pipipp", "Pippi") # False)
# name_in_str("ppipip", "Pippi") # False)

# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python
def wave(people):
    my_wave = []
    for i in range(len(people)):
        if people[i] != ' ':
            my_wave += [people[:i] + people[i].upper() + people[i+1:]]
    return my_wave

# https://www.codewars.com/kata/587731fda577b3d1b0001196

def camel_case(s):
    return ''.join(s.title().split())

# camel_case('hello world')

# https://www.codewars.com/kata/52b757663a95b11b3d00062d

def to_weird_case(words):
    arr_f = []
    for w in words.split():
        arr_w = []
        for i, letter in enumerate(w):
            if i%2:
                arr_w += letter.lower()
            else:
                arr_w += letter.upper()
        arr_f.append(''.join(arr_w))
    return ' '.join(arr_f)
# def word_test(words):
    # ''.join(letter.lower() if i%2 else letter for i, letter in enumerate(word.upper())
# def to_weird_case_2(words):
    # ' '.join(word_test(x) for x in words.split)

    # print(' '.join(''.join(letter.lower() if w[i]%2 else letter.upper() for i, letter in enumerate(w)) for w in words.split()))


to_weird_case("Weird string case")

# https://www.codewars.com/kata/5503013e34137eeeaa001648/train/python
def diamond(n):
    if n%2==0 or n <0:
        return None
    str = ""
    row = 0
    while n > 0:
        if row+1 < n:
            str += " "*((n-1-row)//2) + "*"*(1+2*row) + "\n"
        elif row+1 == n:
            str += "*" * (1 + 2 * row) + "\n"
        if row+1 > n:
            str += " "*((row+1-n)//2) + "*"*(1+2*(n-1)) + "\n"
        n -= 1
        row += 1
    return str

# diamond(9)


# https://www.codewars.com/kata/55466989aeecab5aac00003e/train/python
def sq_in_rect(lng, wdth):
    if lng != wdth:
        arr = []
        while min(lng, wdth) > 0:
            arr.append(min(lng, wdth))
            lng, wdth = max(lng, wdth) - min(lng, wdth), min(lng, wdth)
        return arr
    return None

sq_in_rect(5, 3)
# [3, 2, 1, 1]

# https://www.codewars.com/kata/515decfd9dcfc23bb6000006
import re
def is_valid_IP(strng):
    pattern = re.compile(r"^\d+$")
    if all(bool(pattern.match(x)) for x in strng.split('.')) == False:
        return False
    if strng == '' or len(strng.split('.')) != 4 or any(x.isalpha() for x in strng.split(".")):
        return False
    if re.search(" ", strng):
        return False
    if any(int(x) < 100 and len(x) > 2 for x in strng.split('.')):
        return False
    if any(int(x) < 10 and len(x) > 1 for x in strng.split('.')):
        return False
    return all(0 <= int(x) <= 255 for x in strng.split('.'))


is_valid_IP('12.255.56.1')
# , True)
is_valid_IP('')
# , False)
is_valid_IP('abc.def.ghi.jkl')
# , False)


# https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python

def title_case(title, minor_words=''):
    print(minor_words.lower())
    print([x.lower() for x in title.split() if x.lower() in minor_words.lower()])
    return ' '.join(x.title() if x.lower() not in minor_words.lower() or i == 0 else x.lower() for i, x in enumerate(title.split()))
    pass


# title_case('')
# , '')
# title_case('a clash of KINGS', 'a an the of')
# , 'A Clash of Ki/ngs')
# title_case('THE WIND IN THE WILLOWS', 'The In')
# , 'The Wind in the Willows')
# title_case('the quick brown fox')
# , 'The Quick Brown Fox')

# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python
def multiplication_table(size):
    arr = []
    arr_1 = list(range(1, size+1))
    for i in range(1, size+1):
        arr_temp = [x*i for x in arr_1]
        arr.append(arr_temp)
    return arr

multiplication_table(3)

# https://www.codewars.com/kata/51e0007c1f9378fa810002a9
def parse(data):
    print(list(data))
    arr = []
    y = 0
    for x in list(data):
        if x == 'i': y += 1
        elif x == 'd': y -= 1
        elif x == 's': y *= y
        elif x == 'o': arr.append(y)
    return arr

# parse("ooo")
# , [0, 0, 0])
# parse("ioioio")
# , [1, 2, 3])
# parse("idoiido")
# , [0, 1])
# parse("isoisoiso")
# , [1, 4, 25])
# parse("codewars")
# , [0])

# https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python
def stock_list(list_of_art, list_of_cat):
    if list_of_art == [] or list_of_cat == []:
        return ''
    arr = [(x[0], int(x.split()[1])) for x in list_of_art]
    return ' - '.join([f'({x} : {sum(y[-1] for y in arr if y[0]==x )})' for x in list_of_cat])



    pass


b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B", "C", "D"]
stock_list(b, c)
# , "(A : 0) - (B : 1290) - (C : 515) - (D : 600)")

a = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
d = ["A", "B"]
stock_list(a, d)
# , "(A : 200) - (B : 1140)")