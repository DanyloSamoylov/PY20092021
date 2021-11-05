
def in_range(start: int, end: int, step=1):
    if step > 0:
        while start < end:
            yield start
            start += step
    elif step < 0:
        while start > end:
            yield start
            start += step
    else:
        raise ValueError('Step cant be 0')


x = in_range(20, 1, -1)

print(type(x))
# help(range)

for el in x:
    print(el)
