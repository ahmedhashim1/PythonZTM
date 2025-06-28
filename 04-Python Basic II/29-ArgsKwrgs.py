def super_func(*args, **kwargs):  # this *args will aceept any num of aurguments
    print(args, kwargs)
    return sum(args)


print(super_func(1, 2, 3, 4, 5, num1=5, num2=6))

# Rule of order: params,*args, default param, **kwargs
