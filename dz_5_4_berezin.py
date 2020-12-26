dict_f = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
list_for_rus = []
i = 0
with open("dz_5_4_en.txt") as f_en:
    for line in f_en:
        list_str = line.split(' ', 1)
        list_for_rus.append(dict_f[list_str[0]] + ' ' + list_str[1])

with open("dz_5_4_ru.txt", "w") as f_ru:
    f_ru.writelines(list_for_rus)

