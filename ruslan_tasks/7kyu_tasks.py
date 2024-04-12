# https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python
# 2024-04-02

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


stray([2,2,2,2,2,2,3])