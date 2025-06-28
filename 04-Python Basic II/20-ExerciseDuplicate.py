some_list = ['a', 'b', 'c', 'd', 'b', 'd', 'm', 'n', 'j']

duplicate = []
for char in some_list:
    if some_list.count(char) > 1:
        if char not in duplicate:
            duplicate.append(char)
        # print(char, end=' ')

print(duplicate)
