z = 'Danylo'
x = 'Samoylov'
c = z + ' ' + x

print('Good morning, ' + c, end='.\n')  # just greeting
print(c, type(c), len(c))               # lets see what type we have

# trying to manipulate strings
print('Replace "space" with "-":', c.replace(' ', '-'))
print('How we see this in lowercase:', c.lower())
print('How we see this in uppercase:', c.upper())
print('Lets count how many "lo" we have:', c.count('lo'))

c = c.split(' ')
print(c, type(c), len(c))
c2 = " ".join(c)
print(c2, type(c2))
c3 = c[1] + ' ' + c[0]
print(c3, type(c3), len(c3))

# lets make only initials from variables "z" and "x"
print(z[0] + '.' + x[0] + '.')
