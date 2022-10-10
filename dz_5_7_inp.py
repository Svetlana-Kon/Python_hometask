def mod():
    mod = input('Выберите режим: 1 - экспорт, 2 - импорт: ')
    return mod

def inp_data():
    last_name = input('Введите фамилию контакта: ')
    first_name = input('Введите имя контакта: ')
    mob_number = input('Введите номер телефона: ')
    another_number = input('Хотите добавить еще один номер? д/н ')
    next_number = ''
    if another_number == 'д':
        next_number = next_number + input('Введите номер телефона: ')
        another_number = input('Хотите добавить еще один номер? д/н  ')
    str_person = (f'{last_name} {first_name}, {mob_number}, {next_number}')
    # str_person = input('Введите данные для импорта: ')
    return str_person 

def exp_data():
    second_name = input('Введите фамилию контактного лица: ')
    return second_name
