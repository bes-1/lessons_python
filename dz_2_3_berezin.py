number_month = int(input('Введите номер месяца от 1 до 12: '))
list = [[1, 'январь'], [2, 'февраль'], [3, 'март'], [4, 'апрель'], [5, 'май'], [6, 'июнь'],
        [7, 'июль'], [8, 'август'], [9, 'сентябрь'], [10, 'октябрь'], [11, 'ноябрь'], [12, 'декабрь']]
if number_month >= 1 and number_month <= 12:
    for i in range(len(list)):
        if number_month == list[i][0]:
            print(f'Месяцу под № {number_month} соответствует {list[i][1]}')
else:
    print('Вы ввели некорректно номер месяца, запустите программу заново и в следующий раз не ошибитесь!)))')

number_month = int(input('Введите номер месяца от 1 до 12: '))
dict_month = {1: 'январь',
              2: 'февраль',
              3: 'март',
              4: 'апрель',
              5: 'май',
              6: 'июнь',
              7: 'июль',
              8: 'август',
              9: 'сентябрь',
              10: 'октябрь',
              11: 'ноябрь',
              12: 'декабрь'}
if number_month >= 1 and number_month <= 12:
    for i in dict_month:
        if number_month == i:
            print(f'Месяцу под № {number_month} соответствует {dict_month[i]}')
else:
    print('Вы ввели некорректно номер месяца, запустите программу заново и в следующий раз не ошибитесь!)))')