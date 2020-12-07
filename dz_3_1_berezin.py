num = float(input('Введите числитель: '))
den = float(input('Введите знаменатель: '))

'''Функция, которая производит деление и обрабатывает искючение "Деление на ноль"'''

def div(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print('Вы ввели знаменатель равный 0, необходимо вспомнить высшую математику и самому решить этот пример)))')

# Включил исключение, так как при деление на ноль и использование round выскакивает исключение TypeError
try:
    res = round(div(num, den), 2)
    print(f'Результат деления: {res}')
except TypeError:
    pass
