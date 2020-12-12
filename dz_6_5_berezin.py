class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')


t = Stationery('Отрисовка')
t.draw()
p_1 = Pen('Ручка')
p_1.draw()
p_2 = Pencil('Карандаш')
p_2.draw()
h = Handle('Маркер')
h.draw()