class CheckInListOnNumbers(Exception):
    list_numbers = []

    def __init__(self, value):
        self.value = value
        if self.value.isdigit():
            CheckInListOnNumbers.list_numbers.append(int(self.value))
        else:
            print('Вы ввели строку, а нужно число!')


while True:
    try:
        value_of_user = input('Введите число: ')
        raise CheckInListOnNumbers(value_of_user)
    except:
        pass
    exit = input('Введите "stop", чтобы пррекратить заполнять список числами или любой символ для продолжения: ')
    if exit == 'stop':
        break
    else:
        continue

print(CheckInListOnNumbers.list_numbers)
