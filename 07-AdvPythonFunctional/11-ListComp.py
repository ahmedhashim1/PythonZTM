# List/set/dict comprehensions

my_list = []

for char in "hello":
    my_list.append(char)

print(my_list)

# faster way, List comprehension
ch = "hello"
my_list_lc = [char for char in ch]
print(my_list_lc)

my_list2 = [num for num in range(0, 100)]
print(my_list2)

# only even numbers
my_list3 = [num * 2 for num in range(0, 100)]
print(my_list3)

#
my_list4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]
print(my_list4)
