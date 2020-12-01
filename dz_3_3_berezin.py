def my_func(num1, num2, num3):
    if num2 > num1 and num3 > num1:
        sum_nums = num2 + num3
    elif num1 > num3 and num2 > num3:
        sum_nums = (num1 + num2)
    else:
        sum_nums = num1 + num3
    return sum_nums

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))

print(f'Суммма двух наибольших чисел: {my_func(num1, num2, num3)}')
