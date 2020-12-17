""" Первый вариант решения"""

# from sys import argv
#
# name_script, hours, rate, bonus = argv
#
# print(f'Заработная плата = {int(hours)*int(rate) + int(bonus)}')

""" Второй вариант решения"""

from sys import argv

argv[0] = input('Введите выработка в часа: ')
a = argv[0]
argv[0] = input('Ставку в часах: ')
b = argv[0]
argv[0] = input('Введите премию: ')
c = argv[0]

print(f'Заработная плата = {int(a) * int(b) + int(c)} рублей')
