from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} called with {args}')
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4, 5)
square_all(4, 5, 6, 7)
print(square_all.__name__)
