def int_func(word):
    return word.title()


def int_func_more(words):
    return list(map(int_func, words))


list_words = input('Введите слова через пробел: ').split()
print(' '.join(int_func_more(list_words)))
