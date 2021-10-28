from functools import wraps


def arg_rules(type_: type, max_length: int, contains: list):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if type(*args, **kwargs) != type_:
                print('Wrong type of data.')
            if len(*args, **kwargs) > max_length:
                print('Wrong length')
            for symbol in contains:
                if symbol not in contains:
                    print('Wrong symbols')
            return func(*args, **kwargs)
        return wrapper
    return inner


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f'{name} drinks pepsi in his brand new BMW !'


print(create_slogan('johndoe05gmail.com'))
print(create_slogan('S@SH05'))
