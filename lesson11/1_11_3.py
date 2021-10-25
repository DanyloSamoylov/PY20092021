nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def choose_func(x, *args):

    def square_nums(a):
        return [a ** 2 for a in a]

    def remove_negatives(b):
        remove_ = list(filter(lambda x: x > 0, b))
        return remove_

    if all(el > 0 for el in x):
        return square_nums(x)
    else:
        return remove_negatives(x)


choose_func(nums1, square_nums, remove_negatives)




