class OfficeAppliances:
    counter_prints = 1
    counter_scanners = 1
    counter_machine = 1

    def __init__(self, name, price, count):

        self.name = name
        self.price = price
        self.count = count
        self.office_appliance = [{'Название (модель)': name, 'Цена': price, 'Количество': count}]

    def add(self):
        name_in = input('Введите название оборудования (модель): ')
        price_in = int(input('Введите цену: '))
        count_in = int(input('Введите количество: '))
        dict_appliance = {'Название (модель)': name_in, 'Цена': price_in, 'Количество': count_in}
        self.office_appliance.append(dict_appliance)

    def add_new_appliance(self):
        while True:
            choice = input(
                'Если Вы хотите сделать запись по принтерам нажмите "1", по сканерам "2", по ксероксам "3": ')
            if choice == '1':
                try:
                    OfficeAppliances.add(self)
                    OfficeAppliances.counter_prints += 1
                except:
                    print('Ошибка ввода данных')
            elif choice == '2':
                try:
                    OfficeAppliances.add(self)
                    OfficeAppliances.counter_scanners += 1
                except:
                    print('Ошибка ввода данных')
            elif choice == '3':
                try:
                    OfficeAppliances.add(self)
                    OfficeAppliances.counter_machine += 1
                except:
                    print('Ошибка ввода данных')
            else:
                continue

            exit = input('Для выхода введите "exit", для продолжения любой символ: ')
            if exit == 'exit':
                print(f'Общий список оргтехники {self.office_appliance}')
                break
            else:
                continue


class Printer(OfficeAppliances):
    def info_count_printer(self):
        return f'Количество принтеров на складе: {OfficeAppliances.counter_prints}'


class Scanner(OfficeAppliances):
    def info_count_scanner(self):
        return f'Количество принтеров на складе: {OfficeAppliances.counter_scanners}'


class CopyMachine(OfficeAppliances):
    def info_count_cm(self):
        return f'Количество принтеров на складе: {OfficeAppliances.counter_machine}'


priner = OfficeAppliances('принтер', 12500, 3)
priner.add_new_appliance()
count_prints = Printer('принтер', 12500, 3)
print(count_prints.info_count_printer())

