list_in = []
while True:
    parametr = input('Если хотите ввести строку нажмите "1", в противном случае любую другую кнопк:')
    if parametr == "1":
        str_in = input('Введите строку: ')
        list_in.append(str_in)
    else:
        break


with open ("dz_5_1.txt", "w") as in_str:
    for line in list_in:
        in_str.write(line + "\n")

in_str.close()
