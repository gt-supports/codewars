

# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
def snail(snail_map):
    amount = len(snail_map) * len(snail_map[0])
    arr = []
    g = 0
    while g < amount:
        if snail_map != []:
            for j in range(len(snail_map[0])):
                arr.append(snail_map[0][j])
                g += 1
            snail_map.remove(snail_map[0])
        if snail_map != []:
            for i in range(len(snail_map)):
                arr.append(snail_map[i][-1])
             g += 1
                snail_map[i].remove(snail_map[i][-1])
        if snail_map != []:
            for h in range(len(snail_map[0])):
                arr.append(snail_map[-1][-1])
                g += 1
                snail_map[-1].remove(snail_map[-1][-1])
                if snail_map[-1] == []:
                    snail_map.remove(snail_map[-1])
        if snail_map != []:
            for k in range(-1, -len(snail_map), -1):
                arr.append(snail_map[k][0])
                g += 1
                snail_map[k].remove(snail_map[k][0])
    return arr

    # [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 6, 7, 8, 9, 14, 19, 18, 17, 16, 11, 12, 13]
    # [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
    #
    # [[1, 2, 3, 4, 5],
    #  [6, 7, 8, 9, 10],
    #  [11, 12, 13, 14, 15],
    #  [16, 17, 18, 19, 20],
    #  [21, 22, 23, 24, 25]]

    # 01 02 03
    # 11 12 13
    # 21 22 23


    print(arr)

def snail2(array):
    out = []

    while len(array):
        out += array.pop(0)
        print(array)
        print(out)
        print(list(zip(*array)))
        array = list(zip(*array))[::-1] # Rotate
        print(array)
        print("here")
    return out

# 11 12 13 23 33 32 31
snail2([ [1,2,3],
         [8,9,4],
         [7,6,5]])
# snail2(    [[1,   2,   3,  4,  5],
            # [6,   7,  8,  9, 10],
            # [11, 12, 13, 14, 15],
            # [16, 17, 18, 19, 20],
            # [21, 22, 23, 24, 25]])

