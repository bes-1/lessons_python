from itertools import count
from math import factorial


def gen_count():
    for el in count(1):
        yield factorial(el)


list_gen_count = gen_count()
i = 0
for el in list_gen_count:
    if i < 4:
        print(el)
        i += 1
    else:
        break
