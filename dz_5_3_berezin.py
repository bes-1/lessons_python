with open("dz_5_3.txt", encoding="utf-8") as f:
    surname_less_salary = []
    sum = 0
    count_employee = 0
    for line in f:
        list_str = line.split(' ')
        if list_str[1] < "20000.00":
            surname_less_salary.append(list_str[:-1])
        sum += float(list_str[1])
        count_employee += 1
print(f'Фамилии сотрудников у которых ЗП меньше 20000.00 руб.: {surname_less_salary}\n'
      f'Средняя ЗП сотрудника: {sum/count_employee:.02f}')
