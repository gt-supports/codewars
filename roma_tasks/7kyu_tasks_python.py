# https://www.codewars.com/kata/5949481f86420f59480000e7/solutions/python
def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'


# https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/solutions/python?filter=me&sort=best_practice&invalids=false
def row_weights(array):
    team1 = sum(array[::2])
    team2 = sum(array[1::2])
    return (team1, team2)


# https://www.codewars.com/kata/5982619d2671576e90000017/solutions/python?filter=me&sort=best_practice&invalids=false
def sponge_meme(s):
    result = ""

    for index, character in enumerate(s):
        if index % 2 == 0:
            result += character.upper()
        else:
            result += character.lower()

    return result
