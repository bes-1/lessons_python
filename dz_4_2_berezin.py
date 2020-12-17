"""Решение со статически заполненным списком"""

# begin_list = [23, 5, 2, 4, 2, 1, 20, 75, 12, 32]
# finish_list = [begin_list[i] for i in range(1, len(begin_list)) if begin_list[i] > begin_list[i - 1]]
# print(finish_list)


"""Решение с динамически заполненным списком"""

numbers_list = int(input('Введите количество чисел в списке: '))
list_begin = [int(input(f'Введите {i+1} число : ')) for i in range(numbers_list)]
print(f'Вы ввели список чисел: {list_begin}')
list_finish = [list_begin[i] for i in range(1, len(list_begin)) if list_begin[i] > list_begin[i - 1]]
print(f'Необходимый список: {list_finish}')

