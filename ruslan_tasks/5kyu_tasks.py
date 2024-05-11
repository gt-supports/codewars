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



dir_reduc(["NORTH", "SOUTH"])
 # ['WEST']