# Old tasks

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




wave("two words")