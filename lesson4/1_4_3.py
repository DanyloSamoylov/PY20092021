x = list(range(1, 101))
i = 0
new = []
while i < x.index(100):
    if i % 7 == 0 and i % 5 != 0:
        new.append(i)
    i += 1
print(new)
