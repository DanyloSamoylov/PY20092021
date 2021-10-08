import random


user_data = input('Write "Hello":')
list_1 = list(user_data)
i = 0
for i in range(5):
    print(''.join(random.choice(list_1) for _ in range(len(list_1))))
    i += 1
