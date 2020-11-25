my_list = [7, 5, 3, 3, 2]
print(f'Список значений в начальном рейтинге: {my_list}')
while True:
    answer = int(input('Введите 1 если хотите добавить в рейтинг значение или 0, если не хотите: '))
    if answer == 0:
        break
    else:
        new_value = int(input('Введите новое значение для рейтинга:'))
        my_list.append(new_value)
        sort_list = sorted(my_list, reverse=True)
        print(sort_list)
