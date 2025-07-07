# zip
my_list = [1, 2, 3, 4]
your_list = [5, 6, 7, 8]
there_list = [9, 10, 11, 12]


def multiplyby2forMap(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


# print(list(map(multiplyby2forMap, [1, 2, 3])))
# print(list(map(multiplyby2forMap, my_list)))
# print(my_list)  # does not change actual list
# print(list(filter(only_odd, my_list)))
print(list(zip(my_list, your_list, there_list)))
