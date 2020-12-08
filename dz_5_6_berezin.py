
dict_disciplines = {}
i = 0
with open("dz_5_6.txt", encoding='utf-8') as f:
    for line in f.readlines():
        list_disc = line.split(' ')
        nums = [int(el) for el in list_disc if el.isdigit()]
        sum_hours = sum(nums)
        dict_disciplines[list_disc[0]] = sum_hours
        i += 1
print(dict_disciplines)
