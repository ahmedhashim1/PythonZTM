def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = make_list(100)  # it will take memory to hold list items of 100 numbers
print(my_list)
