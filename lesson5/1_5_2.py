user_data = input('Please enter your phone number:')
tele_num = user_data
user_number = []

if len(tele_num) == 10 and tele_num.isdigit():
    user_number.append(tele_num)
    print('Thank you, we got your phone number.')
elif len(tele_num) < 10 or len(tele_num) > 10:
    print('Number must be 10 symbols only.')
else:
    print('You need to use only numbers - not letters.')

print('Result:', user_number, type(user_number))
