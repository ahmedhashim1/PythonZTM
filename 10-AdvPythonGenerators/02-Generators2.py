# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i * 2)
#     return result
#
#
# my_list = make_list(100)  # it will take memory to hold list items of 100 numbers
# print(my_list)
def generator_function(num):
    for i in range(num):
        yield i


g = generator_function(1)
print(g)  # this will print object memory address
print(next(g))  # 0
print(next(g))  # 2
print(next(g))  # 4
print(next(g))  # 6
print(next(g))  # 8

# for item in generator_function(1000):
#     print(item)
