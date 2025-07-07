some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# find the duplicates using list comprehension
duplicates = [item for item in set(some_list) if some_list.count(item) > 1]
print(duplicates)

duplicates2 = list(set([item for item in some_list if some_list.count(item) > 1]))
print(duplicates2)
