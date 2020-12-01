def info_man(name, surname, year_of_birth, city, email, phone_number):
    list_info = []
    list_info.append(name)
    list_info.append(surname)
    list_info.append(year_of_birth)
    list_info.append(city)
    list_info.append(email)
    list_info.append(phone_number)
    return list_info


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year_of_birth = input('Введите год рождения: ')
city = input('Введите город: ')
email = input('Введите email: ')
phone_number = input('Введите номер телефона: ')
list_info_man = info_man(name=name, surname=surname, year_of_birth=year_of_birth, city=city, email=email,
                         phone_number=phone_number)
str_info_man = ' '.join(list_info_man)
print(str_info_man)

