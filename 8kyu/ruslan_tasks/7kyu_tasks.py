# https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python
# 2024-04-02

def remove_smallest(numbers):

    return [numbers[i] for i in range(len(numbers)) if i != numbers.index(min(numbers))]


# https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python
# 2024-04-04
def number(bus_stops):
    in_bus = sum([num[0]-num[1] for num in bus_stops])