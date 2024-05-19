# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

def zero(calc=None):
    if calc is None:
        return  0
    elif calc[0] == "+":
        return 0 + calc[1]
    elif calc[0] == "-":
        return 0 - calc[1]
    elif calc[0] == "*":
        return 0 * calc[1]
    elif calc[0] == "/":
        return int(0 / calc[1])
def one(calc=None):
    if calc is None:
        return 1
    elif calc[0] == "+":
        return 1 + calc[1]
    elif calc[0] == "-":
        return 1 - calc[1]
    elif calc[0] == "*":
        return 1 * calc[1]
    elif calc[0] == "/":
        return int(1 / calc[1])
def two(calc=None):
    if calc is None:
        return 2
    elif calc[0] == "+":
        return 2 + calc[1]
    elif calc[0] == "-":
        return 2 - calc[1]
    elif calc[0] == "*":
        return 2 * calc[1]
    elif calc[0] == "/":
        return int(2 / calc[1])
def three(calc=None):
    if calc is None:
        return 3
    elif calc[0] == "+":
        return 3 + calc[1]
    elif calc[0] == "-":
        return 3 - calc[1]
    elif calc[0] == "*":
        return 3 * calc[1]
    elif calc[0] == "/":
        return int(3 / calc[1])
def four(calc=None):
    if calc is None:
        return 4
    elif calc[0] == "+":
        return 4 + calc[1]
    elif calc[0] == "-":
        return 4 - calc[1]
    elif calc[0] == "*":
        return 4 * calc[1]
    elif calc[0] == "/":
        return int(4 / calc[1])
def five(calc=None):
    if calc is None:
        return 5
    elif calc[0] == "+":
        return 5 + calc[1]
    elif calc[0] == "-":
        return 5 - calc[1]
    elif calc[0] == "*":
        return 5 * calc[1]
    elif calc[0] == "/":
        return int(5 / calc[1])

def six(calc=None):
    if calc is None:
        return 6
    elif calc[0] == "+":
        return 6 + calc[1]
    elif calc[0] == "-":
        return 6 - calc[1]
    elif calc[0] == "*":
        return 6 * calc[1]
    elif calc[0] == "/":
        return int(6 / calc[1])
def seven(calc=None):
    if calc is None:
        return 7
    elif calc[0] == "+":
        return 7 + calc[1]
    elif calc[0] == "-":
        return 7 - calc[1]
    elif calc[0] == "*":
        return 7 * calc[1]
    elif calc[0] == "/":
        return int(7 / calc[1])
def eight(calc=None):
    if calc is None:
        return 8
    elif calc[0] == "+":
        return 8 + calc[1]
    elif calc[0] == "-":
        return 8 - calc[1]
    elif calc[0] == "*":
        return 8 * calc[1]
    elif calc[0] == "/":
        return int(8 / calc[1])
def nine(calc=None):
    if calc is None:
        return 9
    elif calc[0] == "+":
        return 9 + calc[1]
    elif calc[0] == "-":
        return 9 - calc[1]
    elif calc[0] == "*":
        return 9 * calc[1]
    elif calc[0] == "/":
        return int(9 / calc[1])

def plus(num):
    return ["+", num]
def minus(num):
    return ["-", num]

def times(num):
    return ["*", num]
def divided_by(num):
    return ["/", num]



# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
def domain_name(url):
    url_start = ['http://', 'https://', 'www.']
    url_no_start = url.replace(''.join([x for x in url_start if x in url]), '')
    url_no_start = url_no_start.replace(''.join([x for x in url_start if x in url]), '')
    print(url_no_start)
    return ''.join(list(url_no_start)[0:url_no_start.index(".")])


# domain_name("http://www.codewars.com/kata/")

# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python
def product_fib(_prod):
    prev = 0
    cur = 1
    next = 0
    while cur * prev < _prod:
        next = prev + cur
        prev = cur
        cur = next
    if prev*cur >=_prod:
        return [prev, cur, prev*cur ==_prod]
    next = prev + cur
    prev = cur
    cur = next
    return [prev, cur, prev*cur ==_prod]

product_fib(4895)

# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(lst):
    return [x for x in lst if x!=0] + [0]*lst.count(0)


move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
import re
def pig_it(text):
    print(' '.join(x[1::]+x[0] +'ay' if re.findall(r'[a-zA-Z]', x) else x for x in text.split()))
    return ' '.join(x[1::]+x[0] +'ay' if re.findall(r'a-zA-Z', x) else x for x in text.split())

# pig_it('Pig latin is cool !')

# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
def make_readable(seconds):
    HH = seconds//3600 if seconds//3600>9 else '0'+str(seconds//3600)
    MM = seconds//60%60 if seconds//60%60>9 else '0'+str(seconds//60%60)
    SS = seconds%60 if seconds%60>9 else '0'+str(seconds%60)
    # print(f'{HH}:{MM}:{SS}')

    hours, seconds = divmod(seconds, 60**2)
    minutes, seconds = divmod(seconds, 60)
    print(hours, minutes, seconds)
    print('{:02}:{:02}:{:02}'.format(hours, minutes, seconds))
    print('%02d:%02d:%02d' % (hours, minutes, seconds))

    return f'{HH}:{MM}:{SS}'

# make_readable(159055)
# make_readable(86399)
# make_readable(359999)


# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
def rgb(r, g, b):
    if r < 0:
        r = 0
    elif r > 255:
        r = 255
    if g < 0:
        g = 0
    elif g > 255:
        g = 255
    if b < 0:
        b = 0
    elif b > 255:
        b = 255

    if r < 16:
        r = '0' + str(hex(r)[2:].upper())
    else:
        r= str(hex(r)[2:].upper())

    if g < 16:
        g = '0' + str(hex(g)[2:].upper())
    else:
        g= str(hex(g)[2:].upper())

    if b < 16:
        b = '0' + str(hex(b)[2:].upper())
    else:
        b = str(hex(b)[2:].upper())

    return ''.join([r, g, b])

rgb(-20, 275, 125)


rgb(254, 253, 252)
# "FEFDFC"

# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
def dir_reduc(arr):
    text = '_'.join(arr)
    while 'NORTH_SOUTH' in text or 'SOUTH_NORTH' in text or 'EAST_WEST' in text or 'WEST_EAST' in text:
        text = text.replace('NORTH_SOUTH', '')
        text = text.replace('SOUTH_NORTH', '')
        text = text.replace('EAST_WEST', '')
        text = text.replace('WEST_EAST', '')
        text = text.split("_")
        text = '_'.join(x for x in text if x!='')
    return text.split('_') if text!='' else []



# dir_reduc(["NORTH", "SOUTH"])
 # ['WEST']

# https://www.codewars.com/kata/530e15517bc88ac656000716
def rot13(message):
    print(ord('s'))
    print(ord('a'))
    print(ord('z'))
    print(ord('f'))
    arr = []
    for x in message:
        if x.isalpha():
            if 65 <= ord(x) < 78 or 97 <= ord(x) < 110:
                arr.append(ord(x)+13)
            elif 110 <= ord(x) <= 122:
                arr.append(97-122+ord(x)+12)
            elif 78 <= ord(x) <= 90:
                arr.append(65-90+ord(x)+12)
        else:
            arr.append(ord(x))
    print(''.join([chr(x) for x in arr]))
    return ''.join([chr(x) for x in arr])


# test.assert_equals(rot13('test'), 'grfg', 'Returned solution incorrect for fixed string = test')
# test.assert_equals(rot13('Test'), 'Grfg', 'Returned solution incorrect for fixed string = Test')
# test.assert_equals(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%'

# rot13('AaTtSs')

# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python
def generate_hashtag(s=''):
    s.capitalize()
    result = '#'+''.join([x.capitalize() for x in s.split()])
    return result if s != '' and len(result) <= 140 else False

# generate_hashtag('CoDeWaRs   is niCe')

# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c
def max_sequence(arr):
    if arr == []: return 0
    cur_sum = 0
    max_sum = 0
    for x in arr:
        cur_sum += x
        if cur_sum < 0:
            cur_sum = 0
        elif max_sum < cur_sum:
            max_sum = cur_sum
    return max_sum



    #работает но долго
    # if arr == []: return 0
    # max_arr = []
    # max_sum = 0
    # for x in arr:
    #     max_arr.append(x)
    #     if sum(max_arr) < 0:
    #         max_arr = []
    #     elif max_sum < sum(max_arr):
    #         max_sum = sum(max_arr)
    # return max_sum


test = [1,2,3,4,5]
# print(test[:-2])
# print(round(10/2, 2))


# max_sequence([-2, 14, -4, -10, 2, 19, -18, -18, -20, -15, -2, 13, -6, -15, 5, -3, -1])

# max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43])

# max_sequence([5, -11, 3, -20, -15, -18, 17, 3, 7, -19, 6, 11])

# max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43])
    # , 155
# max_sequence([-1, 20, -2, 18, 1, -10, 0, -17, -5, 20, 5, 5, -18, -18, -14, 12, 5, 19, -4])

# should be 37

# https://www.codewars.com/kata/525c65e51bf619685c000059/train/python
def cakes(recipe, available):
    # print(recipe['flour'])
    # print('flour' in recipe)
    # print('test' not in recipe)
    # print([x for x in recipe])
    num = []
    for x in recipe:
        if x not in available:
            return 0
        num.append(available[x]//recipe[x])
    return min(num)

# must return 2
# cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})
# must return 0
# cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000})

# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python
def first_non_repeating_letter(s):
    # print(s.lower())
    # print(set(s.lower(//)))
    # print(s.index("t"))
    # print([s.lower().count(x) for x in set(s.lower())])
    un = [x for x in s if s.lower().count(x.lower()) == 1]
    return un[0] if len(un)>0 else ''



first_non_repeating_letter('at')
# , 'a')
first_non_repeating_letter('1<Tre1s<s')
# , 't')
first_non_repeating_letter('moonmen')
# , 'e')
