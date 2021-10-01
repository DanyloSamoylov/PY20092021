user_data = input('Please enter your name:')
work_name = user_data
name_data = []

if user_data.isalpha():
    name_data.append(work_name.lower())
elif user_data.isdigit():
    print('You need to use only letters.')
else:
    print('Something went wrong.')

question_user = input('Lets check if your name in the list?\n')

if question_user.lower() in name_data and True:
    print('True. Your name in the list.')
else:
    print('Incorrect name')
