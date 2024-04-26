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

# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python
def wave(people):
    my_list = people.partition(" ")
    print(my_list)
    my_wave = []
    for word in my_list:
        new_word = [word[:j:] + word[j].upper() + word[j+1::] for j in range(len(word))]
        my_wave += new_word

    print(my_wave)
    return my_wave

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

count_smileys([':)', ':(', ':D', ':O', ':;'])


