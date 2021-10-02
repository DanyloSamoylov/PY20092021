user_data = input('Please enter your phone number:')
user_number = []

if len(user_data) == 10 and user_data.isdigit():
    user_number.append(user_data)
    print('Thank you, we got your phone number.')
elif not user_data.isdigit():
    print('You need to use only numbers - not letters.')
else:
    print('Number must be 10 symbols only.')
print('Result:', user_number, type(user_number))
