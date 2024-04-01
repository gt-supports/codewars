# https://www.codewars.com/kata/56786a687e9a88d1cf00005d/solutions/python?filter=me&sort=best_practice&invalids=false
def validate_word(word):
    # your code here
    word = word.lower()

    dict = {}
    for i in word:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    counts = list(dict.values())
    return all(count == counts[0] for count in counts)

