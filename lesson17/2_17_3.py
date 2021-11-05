

class MyCustomIterable:

    def __init__(self, iterable: list, ind=0):
        self.iterable = iterable
        self.ind = ind

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind < len(self.iterable):
            result = self.iterable[self.ind]
            self.ind += 1
            return result
        else:
            print(f'Stop iteration!')
            raise StopIteration

    def __getitem__(self, item):
        return self.iterable[item]


cities = ['Kiev', 'London', 'Wuhan']
a = MyCustomIterable(cities)

print(next(a))
print(next(a))
print(next(a))
# print(next(a))
print(a[0:])
