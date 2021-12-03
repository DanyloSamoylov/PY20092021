from random import randint
from time import time
"""
One way to improve the quicksort is to use an insertion sort on lists that are small in length
(call it the “partition limit”).
Why does this make sense?
Re-implement the quicksort and use it to sort a random list of integers.
Perform analysis using different list sizes for the partition limit.
"""

num = [randint(0, 100) for _ in range(100)]
num2 = [randint(0, 1000) for _ in range(1000)]


def insertion_sort(li):
    for i in range(1, len(li)):
        ival = li[i]
        ii = i
        while ii > 0 and li[ii - 1] > ival:
            li[ii] = li[ii - 1]
            ii -= 1
        li[ii] = ival
    return li


def quick_sort(li):
    length = len(li)
    if length <= 1:
        return li
    items_greater = []
    items_lower = []
    pivot = li.pop()
    for item in li:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


start_time = time()
print(insertion_sort(num2))
print(f'we take {start_time - time()} time')
start_time2 = time()
print(quick_sort(num2))
print(f'we take {start_time2 - time()} time')

