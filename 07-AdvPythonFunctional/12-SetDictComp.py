# set/dict comprehensions

# set
mylist_1 = {char for char in "hello"}
# print(mylist_1)

my_list2 = {num for num in range(0, 100)}
# print(my_list2)

# Dict Comp

simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key: value ** 2 for key, value in simple_dict.items()}
print(my_dict)

# only add values which are even
my_dict2 = {key: value ** 2 for key, value in simple_dict.items() if value % 2 == 0}
print(my_dict2)

# create dict with single list
my_dict3 = {num: num * 2 for num in [1, 2, 3]}
print(my_dict3)
