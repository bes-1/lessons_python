structure_product = []
number = int(input('Какое количество товаров Вы хоттите записать? '))
list_value_name = []
list_value_price = []
list_value_quantity = []
list_value_unit = []
for goods_index in range(number):
    info_goods = []
    name = input('Введите название товара: ')
    list_value_name.append(name)
    price = int(input('Введите цену товара: '))
    list_value_price.append(price)
    quantity = int(input('Введите количество товара: '))
    list_value_quantity.append(quantity)
    unit = input('Введите единицу измерения товара: ')
    list_value_unit.append(unit)
    goods = {'Название': name, 'Цена': price, 'Количество': quantity, 'Единица измерения': unit}
    info_goods.append(goods_index + 1)
    info_goods.append(goods)
    info_goods_tuple = tuple(info_goods)
    structure_product.append(info_goods_tuple)

print(structure_product)

analytics_name = {'название': list_value_name, 'цена': list_value_price,
                  'количество': list_value_quantity, 'единица измерения': list_value_unit}

analytics_request = input(
    'О какой характеристике товаров хотите узнать:"Название", "Цена", "Количество", "Единица измерения" ').lower()
for key in analytics_name:
    if analytics_request == key:
        print(f'{key}: {analytics_name[key]}')
        break
    elif analytics_request != key:
        continue
else:
    print('Такой характеристики нет')

all_analytics = int(input(
    'Хотите ли просмотреть всю аналитику для всех товаров? Если да, то введите 1, в противном случае введите 0: '))
if all_analytics == 1:
    print('Вся аналитика о всех товаров:')
    for key, value in analytics_name.items():
        print(key, ':', value, sep='')
else:
    print('Программа завершила свою работу')
