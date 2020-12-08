with open("dz_5_2.txt", "r") as f:
    count_str = 0
    dict_count_word = {}
    for line in f:
        list_str = line.split(' ')
        count_word = len(list_str)
        count_str += 1
        dict_count_word[f'Количество слов в {count_str} строке'] = count_word
print(f'Количество строк в файле: {count_str} \nИнформация о количестве слов в строках: {dict_count_word}')


