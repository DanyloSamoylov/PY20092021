import random


list_1 = []
list_2 = []
i = 0
while i < 20:
    if i < 10:
        random_number = random.randint(1, 10)
        list_1.append(random_number)
        i += 1
    else:
        random_number = random.randint(1, 10)
        list_2.append(random_number)
        i += 1
print('List 1:', list_1, type(list_1))
print('List 2:', list_2, type(list_2))
list_3 = set(list_1) & set(list_2)
print('List 3:', list_3, type(list_3))
