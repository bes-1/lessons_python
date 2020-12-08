with open("dz_5_5.txt", "w") as f:
    str_nambers = input('Введите числа через пробел: ')
    f.write(str_nambers)

with open("dz_5_5.txt") as f:
    list_numbers = f.read().split(' ')
    sum_list = sum(map(int, list_numbers))
    print(sum_list)








