
def with_index(iterable, start=0):
    for el in range(len(iterable)):
        yield start, iterable[el]
        start += 1


li = [1, 2, 4, 4, 5, 6, 7]

# help(enumerate)
print(type(with_index))

for el in with_index(li, 1):
    print(el)
