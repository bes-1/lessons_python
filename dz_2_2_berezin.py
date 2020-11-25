number_enter = int(input('Введите количество элементов списка: '))
list = []
for i in range(number_enter):
    list.append(int(input(f'введите {i + 1} элемент списка: ')))
print(list)
for i in range(1, len(list), 2):
    list[i-1], list[i] = list[i], list[i-1]
print(list)
