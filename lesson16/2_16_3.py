from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def convert_to_int(*args, **kwargs):
            print('Converted to int')
            try:
                result = func(*args, **kwargs)
                return int(result)
            except TypeError:
                print('Something wrong')
        return convert_to_int

    @staticmethod
    def to_str(func):
        @wraps(func)
        def convert_to_str(*args, **kwargs):
            print('Converted to str')
            try:
                result = func(*args, **kwargs)
                return str(result)
            except TypeError:
                print('Something wrong')
        return convert_to_str

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def convert_to_bool(*args, **kwargs):
            print('Converted to bool')
            try:
                result = func(*args, **kwargs)
                return bool(result)
            except TypeError:
                print('Something wrong')
        return convert_to_bool

    @staticmethod
    def to_float(func):
        @wraps(func)
        def convert_to_float(*args, **kwargs):
            print('Converted to float')
            try:
                result = func(*args, *kwargs)
                return float(result)
            except TypeError:
                print('Something wrong')
        return convert_to_float


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


print(do_nothing('25'))
assert do_nothing('25') == 25
assert do_something('True') is True
