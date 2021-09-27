z = 'Danylo'
x = 'Samoylov'
c = z + ' ' + x

print('Good morning, ' + c, end='.\n')  # just greeting
print(c, type(c), len(c))               # lets see what type we have

# trying to manipulate strings
print(c.replace(' ', '-'))
print(c.lower())
print(c.upper())
print(c.count('lo'))                    # we have 2 "lo" in the end of name and surname

c = c.split(' ')
print(c, type(c), len(c))
c2 = " ".join(c)
print(c2, type(c2))
c3 = c[1] + ' ' + c[0]
print(c3, type(c3), len(c3))

# lets make only initials from variables "z" and "x"
c4 = z[0:1] + ' ' + x[0:1]
print(c4.replace(' ', '.'), end='.')
