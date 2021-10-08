import random


oper_ = ['+', '-']
i = 0
while True:
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    answer_ = input(f'How much is {num_1} {random.choice(oper_)} {num_2}:')
    if int(answer_) == num_2 + num_1:
        print(f'Answer correct!! {num_1} + {num_2} = {answer_}')
    else:
        print(f'Answer correct!! {num_1} - {num_2} = {answer_}')
        i += 1
