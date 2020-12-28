class ComplexNumbers:
    def __init__(self, first_part, second_part):
        self.first_part = first_part
        self.second_part = second_part


    def __add__(self, other):
        return f'Cумма = {self.first_part + other.first_part} + ({self.second_part + other.second_part})*i'

    def __mul__(self, other):
        return f'Произведение = {self.first_part * other.first_part - self.second_part * other.second_part} +' \
               f' ({self.second_part * other.first_part + self.first_part * other.second_part})*i'


first_number = ComplexNumbers(-3, 1)
second_number = ComplexNumbers(1, 2)
sum = first_number + second_number
print(sum)
mul = first_number * second_number
print(mul)