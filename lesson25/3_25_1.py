from typing import Optional
from typing import Union


def to_power(x: Optional[Union[int, float]], exp: int) -> Optional[Union[int, float]]:
    if exp == 1:
        return x
    elif exp <= 0:
        raise ValueError('Function cant work with 0')
    else:
        return x * to_power(x, exp - 1)


print(to_power(2, 3) == 8)
print(to_power(3.5, 2) == 12.25)
try:
    print(to_power(2, -1))
except ValueError as msg:
    print(msg)

# print(to_power(2, 0))