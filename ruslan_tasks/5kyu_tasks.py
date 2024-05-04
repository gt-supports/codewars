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
    print(lst.count(0))
    print([0]*2)
    print([x for x in lst if x!=0] + [0]*lst.count(0))
    return [x for x in lst if x!=0] + [0]*lst.count(0)


move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]