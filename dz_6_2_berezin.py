'''
Программа для нахождения массы асфальта, при известной длинне и ширине.
'''


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def wt(self):
        weight = self._width * self._length * 25 * 5
        print(f'Масса асфальта,необходимая для покрытия всего дорожного полотна:{weight} тонн ')


'''
Для нахождения массы асфальта, необходимо передать объекту длинну и ширину плпнируемого покрытия
'''
found_wt = Road(10, 100)
found_wt.wt()
