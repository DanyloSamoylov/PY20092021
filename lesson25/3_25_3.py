from typing import Optional


def mult(a: int, n: int) -> int:
    if n == 0:
        return 0
    elif n < 0:
        raise ValueError('This func works only with positive integers')
    elif n == 1:
        return a
    return a + mult(a, n - 1)


print(mult(2, 4) == 8)
print(mult(2, 0) == 0)
try:
    print(mult(2, -4))
except ValueError as msg:
    print(msg)

