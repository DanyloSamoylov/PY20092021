user_data = input('Enter your name and your age:')
a = user_data.split(' ')
print(f'Hello {a[0]}, on your next birthday you`ll be {int(a[1])+1} years.')
