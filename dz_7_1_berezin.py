'''
Программа позволяет найти сумму любой размерности матриц, размерность передается через аргументы в класс.
Размерность второй матрицы формируется автоматически в классе,
так как матрицы должны быть идентичны по размерности, чтобы их сложить!
Стараюсь, придерживаться Вашим замечаниям, по поводу универсальности кода.
'''

class Matrix:
    matr_1 = []
    matr_2 = []
    sum_matr = []

    def __init__(self, number_line, number_column):
        # количество строк и столбцов матрицы передаем в оъект класса Matrix
        self.number_line = number_line
        self.number_column = number_column
        # заполняем первую матрицу
        for l in range(self.number_line):
            Matrix.matr_1.append([])
            for c in range(self.number_column):
                Matrix.matr_1[l].append(int(input(f'Ввод элемента {l + 1} строки и {c + 1} столбца: ')))

        # заполняем вторую матрицу
        self.number_line_2 = self.number_line
        self.number_column_2 = self.number_column
        for l in range(self.number_line_2):
            Matrix.matr_2.append([])
            for c in range(self.number_column_2):
                Matrix.matr_2[l].append(int(input(f'Ввод элемента {l + 1} строки и {c + 1} столбца: ')))

    def __str__(self):
        print('Первая матрица: ')
        for i in range(self.number_line):
            print(Matrix.matr_1[i])
        print('Вторая матрица: ')
        for i in range(self.number_line_2):
            print(Matrix.matr_2[i])

    def __add__(self):
        self.sum_matr = []
        for i in range(self.number_line):
            Matrix.sum_matr.append([])
            for j in range(self.number_column):
                k = Matrix.matr_1[i][j] + Matrix.matr_2[i][j]
                Matrix.sum_matr[i].append(k)
        print('Сумарная матрица')
        for i in range(self.number_line):
            print(Matrix.sum_matr[i])


#передаем параметры соответствующие количеству строк и столбцов матрицы
mat = Matrix(2, 2)
mat.__str__()
mat.__add__()
