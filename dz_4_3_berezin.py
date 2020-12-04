answer_list = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(answer_list)

# если нужно до 240 включительно, то второй параметр range нужно брать 241
