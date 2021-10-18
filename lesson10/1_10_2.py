def task2(a, b):
    return int(a) ** 2 / int(b)


try:
    a = input('enter number:')
    b = input('enter number:')

    print(task2(a, b))
except (ValueError, ZeroDivisionError):
    print('Use numbers only')
