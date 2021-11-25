

def reverse(input_str: str) -> str:
    """
    Function returns reversed input string
    """
    if len(input_str) == 1:
        return input_str
    return input_str[-1] + reverse(input_str[:-1])


print(reverse('hello') == 'olleh')
print(reverse('o') == 'o')
