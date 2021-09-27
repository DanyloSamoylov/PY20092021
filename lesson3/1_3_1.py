
# first string format method
name = 'Dany'
day = 'Sunday'
print(f'Good day {name}, {day.lower()} is a perfect day to learn some python.')

# second string format method
sent = 'Good day {}, {} is a perfect day to learn some python'
print(sent.format(name, day.lower()))

# third string format method
print('Good day {1}, {0} is a perfect day to learn some python'.format('sunday', 'Dany'))

# forth string format method
print('Good day %s, %s is a perfect day to learn some python' % ('Dany', 'sunday'))
