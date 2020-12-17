from functools import reduce

even_list = [el for el in range(100, 1001) if el % 2 == 0]
answer = reduce(lambda x, y: x * y, even_list)
print(f'Произведение всех четных элементов в диапозоне от 100 до 1000 {answer}')
