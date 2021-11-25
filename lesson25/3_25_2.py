from typing import Optional


def is_palindrome(looking_str: str, index: int=0) -> bool:
    # если длина 1. ответ: да
    if len(looking_str) == 1:
        return True
    # если длина до 3х символов. ответ: да
    elif looking_str[0] == looking_str[-1] and len(looking_str) <= 3:
        return True
    # рекурсия
    elif looking_str[0] == looking_str[-1]:
        return is_palindrome(looking_str[1:-1])
    else:
        return False


print(is_palindrome('mom'))
print(is_palindrome('sassas'))
print(is_palindrome('o'))
