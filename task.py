from os.path import exists
from csv import DictReader, DictWriter

file_name = 'phone.csv'


def get_info():
    first_name = 'Aleksandr'
    last_name = 'Smith'
    phone_number = '99264445566'
    return [first_name, last_name, phone_number]


def create_file(file_name):
    # with - Менеджер контекста
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        # Объект типа reader
        f_reader = DictReader(data)
        # Список из словарей
        return list(f_reader)


def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)


def main():
    while True:
        command = input('Введите команду ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует. Создайте его.')
                continue
            print(*read_file(file_name))


# Домашнее задание
file_copy_name = 'phone_copy.csv'


def copy_data(file_name):
    copy_row = int(input(
        f'Введите номер строки (от 1 до 5),\nкоторую нужно скопировать из файла {file_name} в файл {file_copy_name}: '))
    obj = read_file(file_name)[copy_row - 1]
    lst = []
    for item in obj:
        lst.append(obj[item])
    create_file(file_copy_name)
    write_file(file_copy_name, lst)
    print(f'\nФайл {file_copy_name} создан, строка {copy_row} скопирована')


copy_data(file_name)
# main()
