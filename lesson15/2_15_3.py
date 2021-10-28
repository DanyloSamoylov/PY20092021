from functools import wraps


def arg_rules(type_: type, max_length: int, contains: list):
    def inner(func):
        @wraps(func)
        def wrapper(str_):
            if type(str_) != type_:
                print(f'Wrong type of data - {type_}.')
                return False
            if len(str_) > max_length:
                print(f'Wrong length - {max_length}')
                return False
            for symbol in contains:
                if symbol not in contains:
                    print('Wrong symbols')
                    return False
            return func(str_)
        return wrapper
    return inner


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f'{name} drinks pepsi in his brand new BMW !'


print(create_slogan('johndoe05gmail.com'))
print(create_slogan('S@SH05'))
