def test(a):
    def add(b):
        return a + b
    return add


print(test(1)(10))
