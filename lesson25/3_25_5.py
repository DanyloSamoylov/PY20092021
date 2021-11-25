

def sum_of_digits(digit_string: str) -> int:
    if len(digit_string) == 1:
        return int(digit_string)
    return int(digit_string[0]) + sum_of_digits(digit_string[1:])


print(sum_of_digits('26') == 8)
