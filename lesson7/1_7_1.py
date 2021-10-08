import random


while True:
    rand_number = random.randint(1, 10)
    answer_ = int(input('Type number from 1 to 10:'))
    if answer_ == rand_number or answer_ != rand_number:
        if answer_ < rand_number:
            print(f'The number {answer_} is less than mine.', 'my number:', rand_number)
        elif answer_ > rand_number:
            print(f'The number {answer_} is bigger than mine.', 'my number:', rand_number)
        else:
            print(f'Congrats! You won. Number {answer_} is {rand_number}.')
            break
