enter_str = input('Введите строку из нескольких слов через пробел: ')
list_str = enter_str.split()
enter = '\n'
for i in range(len(list_str)):
    if len(list_str[i]) > 10:
        print(f"Значение {i + 1} слова больше 10 символов, первые 10 символов = {list_str[i][:10]}")
    else:
        print(f"Значение {i + 1} слова = {list_str[i]}")
