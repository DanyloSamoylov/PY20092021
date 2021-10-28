class Fraction():

    def __init__(self, var):
        self.var = var

    def __add__(self, other):
        return self.var + other.var

    def __sub__(self, other):
        return self.var - other.var

    def __mul__(self, other):
        return self.var * other.var

    def __truediv__(self, other):
        return self.var / other.var

    def __eq__(self, other):
        return self.var == other.var


x = Fraction(1/2)
y = Fraction(1/4)

print(x+y, x-y, x*y, x/y, sep='; ')

assert Fraction(x + y) == Fraction(3/4)
