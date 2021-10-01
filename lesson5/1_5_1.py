# first input to make answer with 2 first and 2 last characters
user_data = input('Sample String:')
sente = user_data

if len(sente) < 10:
    print('Sentence must be at least 10 symbols.')
elif sente.isdigit():
    print('You need only letters - not numbers.')
else:
    print('Thank you, i got your info.')

res = sente[0:2] + sente[-2:]
print('Result:', res)

# second input to make double answer.
user_data_2 = input('Sample String:')
doubletime = user_data_2

if len(doubletime) < 2:
    print('Sentence must be at least 2 symbols.')
elif doubletime.isdigit():
    print('You need only letters - not numbers.')
else:
    print('Result:', doubletime + doubletime)

# third input for empty string
user_data_3 = input('Sample String:')
wrong_letter = user_data_3

if len(user_data_3) <= 1 or len(user_data_3) >= 1:
    print('Result: Empty String')
else:
    print('Something went wrong')




