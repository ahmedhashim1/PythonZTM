# A decorator supercharges our function


def my_decorator(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')

    return wrap_func


@my_decorator
def hello():
    print('helllloooo')


@my_decorator
def bye():
    print('see yaaaaaaa')


bye()
