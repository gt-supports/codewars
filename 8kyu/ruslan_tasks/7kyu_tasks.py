# https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python
# 2024-04-02

def remove_smallest(numbers):

    return [numbers[i] for i in range(len(numbers)) if i != numbers.index(min(numbers))]
