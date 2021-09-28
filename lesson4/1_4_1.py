import random
list_1 = []
i = 0
while i < 10:                              # lets add random numbers to list_1
    random_number = random.randint(1, 100)
    list_1.append(random_number)
    i += 1
print('List 1:', list_1)
print('The biggest number is:', max(list_1))
