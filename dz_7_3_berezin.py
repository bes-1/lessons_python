class Cell:
    def __init__(self, quantity_cell):
        self.quantity_cell = int(quantity_cell)

    def __add__(self, other):
        return f'Результат суммирования клеток: {Cell(self.quantity_cell + other.quantity_cell)}'

    def __sub__(self, other):
        if self.quantity_cell - other.quantity_cell > 0:
            return f'Результат вычитания клеток: {Cell(self.quantity_cell - other.quantity_cell)}'
        else:
            return 'Разность клеток отрицательна!'

    def __mul__(self, other):
        return f'Результат умножения клеток: {Cell(self.quantity_cell * other.quantity_cell)}'

    def __truediv__(self, other):
        return f'Результат целочисленного деления клеток: {Cell(self.quantity_cell // other.quantity_cell)}'

    def __str__(self):
        return f'{self.quantity_cell}'

    def make_order(self, quantity_slots):
        self.quantity_slots = quantity_slots
        self.int_num = int(self.quantity_cell / quantity_slots)
        self.diff_num = self.quantity_cell - self.int_num * quantity_slots
        self.row = ''
        for i in range(self.int_num):
            self.row += f'{"*" * self.quantity_slots}\\n'
        if self.quantity_cell % quantity_slots != 0:
            print(self.row + f'{self.diff_num * "*"}')
        else:
            print(self.row[:-2] + f'{self.diff_num * "*"}')


cell_1 = Cell(19)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
cell_1.make_order(5)
cell_2.make_order(3)
