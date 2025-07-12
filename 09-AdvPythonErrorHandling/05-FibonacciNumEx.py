def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b


# for i in fib(21):
#     print(i)


# now using List instead of Generators
def fib2(num2):
    a = 0
    b = 1
    result = []
    for j in range(num2):
        result.append(a)

        temp = a
        a = b
        b = temp + b
    return result


print(fib2(21))
