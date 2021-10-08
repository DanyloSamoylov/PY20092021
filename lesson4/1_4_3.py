list_1 = list(range(1, 101))
list_2 = []
i = 0
while i < list_1.index(100):
    if i % 7 == 0 and i % 5 != 0:
        list_2.append(i)
    i += 1
print(list_2)
