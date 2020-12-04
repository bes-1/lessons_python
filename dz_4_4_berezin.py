begin_list = [1, 5, 5, 6, 15, 4, 4, 4, 23, 12, 12, 3, 4]
answer_list = [el for el in begin_list if begin_list.count(el) < 2]

print(answer_list)
