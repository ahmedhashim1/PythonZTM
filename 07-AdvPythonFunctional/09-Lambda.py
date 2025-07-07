# lambda, only use for once, annonymous function
# lambda param: action(param)

from functools import reduce

my_list = [1, 2, 3]


def multiplyby2forMap(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


# print(reduce(accumulator, my_list, 0))
print(list(map(lambda item: item * 2, my_list)))  # no longer needs multiplyby2 function
print(list(filter(lambda item: item % 2 != 0, my_list)))  # no longer needs only_odd function
print(reduce(lambda acc, item: acc + item, my_list))  # no longer needs accumulator function
