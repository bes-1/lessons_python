def find_sum():
    total_sum = 0
    exit = False
    while exit == False:
        numbers = input('Введите числа через пробел или "/" для выхода: ').split()
        sum_now = 0
        for el in range(len(numbers)):
            if numbers[el] == '/':
                exit = True
                break
            else:
                sum_now = sum_now + int(numbers[el])
        total_sum = total_sum + sum_now
        print(f'Текущая сумма: {total_sum}')
    return total_sum


print(f'Итоговая сумма: {find_sum()}')
