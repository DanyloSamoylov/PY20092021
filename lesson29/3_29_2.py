from random import randint
"""
Implement the mergeSort function without using the slice operator.
"""

num = [randint(0, 100) for _ in range(10)]
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def merge_sort(li):
    if len(li) <= 1:
        return li
    middle = len(li)//2
    left_list = []
    right_list = []
    for el in li:
        if len(left_list) < middle:
            left_list.append(el)
        else:
            right_list.append(el)
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))


def merge(left_part, right_part):
    res = []
    while len(left_part) != 0 and len(right_part) != 0:
        if left_part[0] < right_part[0]:
            res.append(left_part[0])
            left_part.remove(left_part[0])
        else:
            res.append(right_part[0])
            right_part.remove(right_part[0])
    if len(left_part) == 0:
        res = res + right_part
    else:
        res = res + left_part
    return res


print(merge_sort(num))
