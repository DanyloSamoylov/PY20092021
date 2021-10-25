class Mathematician:

    @staticmethod
    def remove_positives(li):
        result_li = []
        for num in li:
            if num < 0:
                result_li.append(num)
        return result_li

    @staticmethod
    def filter_leaps(li):
        result_li = []
        for year in li:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                result_li.append(year)
        return result_li

    @staticmethod
    def square_nums(li):
        result_li = []
        for num in li:
            result_li.append(num**2)
        return result_li


m = Mathematician()

print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020, 2100]))

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
