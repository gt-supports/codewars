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


# https://www.codewars.com/kata/557af4c6169ac832300000ba/solutions/python?filter=me&sort=best_practice&invalids=false
def remove_rotten(bag_of_fruits):
    if bag_of_fruits:
        return [el[6:].lower() if el[:6] == 'rotten' else el for el in bag_of_fruits]
    return []


# https://www.codewars.com/kata/57d532d2164a67cded0001c7/solutions/python?filter=me&sort=best_practice&invalids=false

def histogram(results):
    histogram = ""
    for value in range(6, 0, -1):
        count = results[value - 1]
        line = f"{value}|{'#' * count}"
        if count > 0:
            line += f" {count}"
        line += "\n"
        histogram += line
    return histogram
