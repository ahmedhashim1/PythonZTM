# map
# map(action, iterable

def multiplyby2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)


# with map we don't need to define blank list, only need to return actual result in function
my_list = [1, 2, 3]


def multiplyby2forMap(item):
    return item * 2


print(list(map(multiplyby2forMap, [1, 2, 3])))
print(list(map(multiplyby2forMap, my_list)))
print(my_list)  # does not change actual list
