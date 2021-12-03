from random import randint

"""
A bubble sort can be modified to “bubble” in both directions.
The first pass moves “up” the list and the second pass moves “down.”
This alternating pattern continues until no more passes are necessary.
Implement this variation and describe under what circumstances it might be appropriate.

"""

num = [randint(0, 100) for _ in range(10)]
# num = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]

def bubble_sort(li):
    for iter_num in range(len(li)-1, 0, -1):  # стартует с длинны списка на позицию -1, до 0 с шагом -1
        for iter_num2 in range(0, len(li), 1):  # стартует с 0-й позиции до длинны списка с шагом в 1
            for ind in range(iter_num):
                for indx in range(iter_num2):
                    if li[ind] > li[ind+1]:
                        temp = li[ind]
                        li[ind] = li[ind + 1]
                        li[ind + 1] = temp
                        print(li)
                        if li[indx] > li[indx + 1]:
                            temp2 = li[indx]
                            li[indx] = li[indx+1]
                            li[indx+1] = temp2
                            print(li)
    return li


print(num)
print(bubble_sort(num))
"""
если 9-я позиция больше чем 10-я то идет свап и так далее с шагом -1,
и если 0-я позиция больше чем 1-я то идет свап и так далее с шагом +1
"""