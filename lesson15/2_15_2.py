from functools import wraps


def stop_words(words: list):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            str_ = func(*args, **kwargs)
            for word in words:
                if word in str_:
                    str_ = str_.replace(word, '*')
            return str_
        return wrapper
    return inner


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f'{name} drinks pepsi in his brand new BMW !'


print(create_slogan('Steve'))
assert create_slogan('Steve') == 'Steve drinks * in his brand new * !'
