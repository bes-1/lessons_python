from itertools import cycle

c = 0

for el in cycle("1234567890"):
    if c > 20:
        break
    else:
        print(el)
        c +=1
