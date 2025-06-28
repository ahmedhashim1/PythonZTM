# enumerate add index 'COLUMN' to a iterable

# for chat in enumerate('hellooooooooooooooo'):
#     print(chat)
#
# for i in enumerate([1, 2, 3, 3, 4, 5]):
#     print(i)  # this will print list with default index

# Excercise
for i, num in enumerate(list(range(100))):
    if num == 50:
        print(f"the index of {num} is {i}")
