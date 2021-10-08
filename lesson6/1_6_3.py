
li = [(i, i*i) for i in range(1, 11)]
print(li)
li2 = [(i, j ** 2) for i, j in enumerate(range(1, 11), start=1)]
print(li2)
