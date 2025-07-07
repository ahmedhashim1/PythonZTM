# A decorator supercharges our function
# what if hello function get a parameter, will decorator still works?

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('**********')
        func(*args, **kwargs)
        print('**********')

    return wrap_func


@my_decorator
def hello(greeting, emoji=";("):
    print(greeting, emoji)


hello("HIIIIIIIIII")
