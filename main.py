from os import system, name


def clear():  
    if name == 'nt':  
        _ = system('cls')  
    else:  
        _ = system('clear')


def read_data(file):
    try:
        with open(file, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print('Файл контактов не найден.\nДля начала работы - введите данные.')
        return []


def show_data(contacts, message='Для возврата в меню нажмите ENTER'):
        for i in range(len(contacts)):
            print(f'{i + 1}\t1{contacts[i].replace('\n', '')}')
        return input(message)


def write_data(file):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as file:
        file.write(f'{phone_number}\t{last_name} {first_name} {patronymic}\n')


def search_data(file):
    contacts = read_data(file)
    search_str = input('Введите фрагмент ФИО для поиска: ')
    founded = []
    for item in contacts:
        if search_str.lower() in item.split('\t')[1].lower():
            founded.append(item)
    return(founded)


def copy_data(contacts):
    select = int(show_data(contacts, 'Введите номер строки: '))
    try:
        with open('copy.txt', 'a', encoding='utf-8') as file:
            file.write(f'{contacts[select - 1]}\n')
    except FileNotFoundError:
        with open('copy.txt', 'w', encoding='utf-8') as file:
            file.write(f'{contacts[select - 1]}\n')


def main():
    file_name = 'contatсs.txt'
    check = True
    while check:
        clear()
        print('1 - Показать все контакты\n'
              '2 - Добавить контакт\n'
              '3 - Найти контакт\n'
              '4 - Копирование в другой файл\n\n'
              '0 - ВЫХОД\n')
        select = input("Выберите действие: ")
        if select == '0':
            check = False
        elif select == '1':
            clear()
            show_data(read_data(file_name))
        elif select == '2':
            clear()
            write_data(file_name)
        elif select == '3':
            clear()
            show_data(search_data(file_name))
        elif select == '4':
            clear()
            copy_data(read_data(file_name))


if __name__ == '__main__':
    main()