

# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
# def snail(snail_map):
#     amount = len(snail_map) * len(snail_map[0])
#     arr = []
#     g = 0
#     while g < amount:
#         if snail_map != []:
#             for j in range(len(snail_map[0])):
#                 arr.append(snail_map[0][j])
#                 g += 1
#             snail_map.remove(snail_map[0])
#         if snail_map != []:
#             for i in range(len(snail_map)):
#                 arr.append(snail_map[i][-1])
#              g += 1
#                 snail_map[i].remove(snail_map[i][-1])
#         if snail_map != []:
#             for h in range(len(snail_map[0])):
#                 arr.append(snail_map[-1][-1])
#                 g += 1
#                 snail_map[-1].remove(snail_map[-1][-1])
#                 if snail_map[-1] == []:
#                     snail_map.remove(snail_map[-1])
#         if snail_map != []:
#             for k in range(-1, -len(snail_map), -1):
#                 arr.append(snail_map[k][0])
#                 g += 1
#                 snail_map[k].remove(snail_map[k][0])
#     return arr

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


    # print(arr)

# def snail2(array):
#     out = []
#
#     while len(array):
#         out += array.pop(0)
#         print(array)
#         print(out)
#         print(list(zip(*array)))
#         array = list(zip(*array))[::-1] # Rotate
#         print(array)
#         print("here")
#     return out

# 11 12 13 23 33 32 31
# snail2([ [1,2,3],
#          [8,9,4],
#          [7,6,5]])
# snail2(    [[1,   2,   3,  4,  5],
            # [6,   7,  8,  9, 10],
            # [11, 12, 13, 14, 15],
            # [16, 17, 18, 19, 20],
            # [21, 22, 23, 24, 25]])


# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

def format_duration(s):
    years = f'{s//(60*60*24*365)} year{"s" if s//(60*60*24*365) > 1 else ""}' if s//(60*60*24*365) > 0 else ""
    days = f'{(s//(60*60*24))%365} day{"s" if (s//(60*60*24))%365 > 1 else ""}' if (s//(60*60*24))%365 > 0 else ""
    hours = f'{(s//(60*60))%24} hour{"s" if (s//(60*60))%24 > 1 else ""}' if (s//(60*60))%24 > 0 else ""
    minutes = f'{(s//60)%60} minute{"s" if (s//60)%60 > 1 else ""}' if (s//60)%60 > 0 else ""
    second = f'{s%60} second{"s" if s%60 > 1 else ""}' if s%60 > 0 else ""
    arr = [years, days, hours, minutes, second]
    arr_1 = [x for x in arr if x != ""]
    return 'now' if s == 0 else ', '.join(x for x in arr_1[:len(arr_1)-1])+f' and {arr_1[-1]}' if len(arr_1) > 1 else arr_1[0]



# format_duration(253374061)#, "8 years, 12 days, 13 hours, 41 minutes and 1 second")
# format_duration(242062374)#, "7 years, 246 days, 15 hours, 32 minutes and 54 seconds")
# format_duration(101956166)#, "3 years, 85 days, 1 hour, 9 minutes and 26 seconds")
# format_duration(33243586)#, "1 year, 19 days, 18 hours, 19 minutes and 46 seconds")

# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
def snail(snail_map):
    result = []
    while len(snail_map)>0:
        popped = snail_map.pop(0)
        result += popped
        # print(list(zip(*snail_map))[::-1])
        new_arr =[[snail_map[x][-y] for y in range(1, len(snail_map[0])+1)] for x in range(len(snail_map))]
        snail_map = list(zip(*new_arr))
    return result







array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
snail(array)  # => [1,2,3,6,9,8,7,4,5]