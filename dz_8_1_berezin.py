class Date:
    list_date = ''

    def __init__(self, str_date):
        self.str_date = str_date
        Date.list_date = self.str_date

    @classmethod
    def to_int(cls):
        list_date = cls.list_date.split('-')
        return '.'.join(list_date)

    @staticmethod
    def check_in(date):
        out_list_date = date.split('.')
        int_date = list(map(int, out_list_date))
        if (1 <= int_date[0] <= 31) != True:
            print(f'Вы ввели не существующий день: {int_date[0]}')
        if (1 <= int_date[1] <= 12) != True:
            print(f'Вы ввели не существующий месяц: {int_date[1]}')
        if int_date[2] < 0:
            print(f'Вы ввели отрицательный год: {int_date[2]}')


date_1 = Date('17-11-2020')
print(date_1.to_int())
date_1.check_in(date_1.to_int())
