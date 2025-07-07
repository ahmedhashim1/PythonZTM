# filter
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def multiplyby2forMap(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


# print(list(map(multiplyby2forMap, [1, 2, 3])))
# print(list(map(multiplyby2forMap, my_list)))
# print(my_list)  # does not change actual list
print(list(filter(only_odd, my_list)))
