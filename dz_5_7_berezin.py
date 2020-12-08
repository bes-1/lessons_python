import json

list_all = []
dict_firm_profit = {}
dict_firm_less = {}
dict_middle_profit = {"middle_profit": []}
dict_profit_less = {"less_profit": []}
with open("dz_5_7.txt") as f_firm:
    sum_profit = 0
    count_profit_plus = 0
    i = 0
    for line in f_firm:
        list_line = line.split(' ')
        profit = int(list_line[2]) - int(list_line[3])
        if profit > 0:
            sum_profit += profit
            count_profit_plus += 1
            dict_firm_profit[list_line[0]] = profit
        else:
            dict_firm_less[list_line[0]] = profit
    middle_profit = sum_profit / count_profit_plus
    list_all.append(dict_firm_profit)
    list_all.append(dict_middle_profit)
    list_all.append(dict_firm_less)
    dict_middle_profit["middle_profit"] = middle_profit
print(list_all)

with open("dz_5_7.json", "w") as f_json:
    json.dump(list_all, f_json)
