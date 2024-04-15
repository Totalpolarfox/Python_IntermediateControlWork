import csv
import datetime
import os

# функция создания файла
def create_file_csv(file: str = 'file name'):
    with open(file, 'w', encoding='utf-8') as f:
        f.write('ID;Заголовок;Заметка;Дата_создания\n')
    print(f'\u001b[32mФайл {file} создан\u001b[0m')

# функция вывода данных
def show_data(data: list[str]):
    if not data:
        print('Файл не содержит заметок!')
    else:
        for element in data:
            print(f'ID: {element[0]}  Дата создания: {element[3]}')
            print(f'\tЗаголовок: {element[1]}')
            print(f'\tЗаметка: {element[2]}')

# функция чтения данных из файла
def read_data(file: str = 'file name'):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f, delimiter = ";")
            return list(csv_reader)[1:] # удаляет строку заголовка
    except FileNotFoundError:
        print('\u001b[31mФайл  не найден.\n\u001b[0m')
        return []  

# функция фильтрации данных по дате
def filtering_data(data: list[str]):
    format = '%d.%m.%Y'
    try:
        starting_date = datetime.datetime.strptime(input('Введите начальную дату (dd.mm.yyyy): '), format)
        end_date = datetime.datetime.strptime(input('Введите конечную дату (dd.mm.yyyy): '), format)
        data = filter(lambda x: starting_date<= datetime.datetime.strptime(x[3], format)<=end_date, data)
        print('Найденные заметки: \n')
    except ValueError:
        print('\u001b[31mПри вводе даты был использован другой формат!\u001b[0m')
        print('\u001b[32mПросмотрите все заметки \n\u001b[0m')    
    return data

# функция записи данных в файл
def write_data(data: list[str], file: str = 'file name'):
    with open(file, 'w', encoding='utf-8') as f:
        csv_writer = csv.writer(f, delimiter = ";", lineterminator="\r")
        csv_writer.writerow(['ID', 'Заголовок', 'Заметка', 'Дата_создания'])
        csv_writer.writerows(data)

# функция создания заметки
def creating_note(data: list[str]):
    if not data:
        new_id = 1
    else:
        max_id = max([int(item[0]) for item in data])
        new_id = max_id + 1
    
    heading = input('Введите заголовок заметки: ')
    note = input('Введите текст заметки: ')
    today = datetime.date.today()
    current_date = today.strftime("%d.%m.%Y")
    new_line = [str(new_id), heading, note, current_date]
    data.append(new_line)
    print('Новая заметка успешно лобавлена.')
    return data

# функция редактирования заметки
def edit_note(data: list[str]):
    select_id = int(input('Для редактирования заметки введите её ID: '))
    found = False
    for index, item in enumerate(data):
        if int(item[0]) == select_id:
            found = True
            heading = input('Введите новый заголовок заметки: ')
            note = input('Введите новое содержание заметки: ')
            today = datetime.date.today()
            current_date = today.strftime("%d.%m.%Y")
            data[index] = [str(select_id), heading, note, current_date]
            print('Редактирование заметки прошло успешно.')
            break
    if not found:
        print('\u001b[31mУказанный ID в заметках не найден!\u001b[0m')        
    return data

# функция удаления заметки
def delete_note(data: list[str]):
    select_id = int(input('Для удаления заметки введите её ID: '))
    found = False
    for index, item in enumerate(data):
        if int(item[0]) == select_id:
            del data[index]
            found = True
            print('Удаление заметки прошло успешно.')
            break
    if not found:
        print('\u001b[31mУказанный ID в заметках не найден!\u001b[0m')        
    return data

def main():
    file_name = input('Введите имя файла, в котором будут хранится заметки: ') + '.csv'
    create_file_csv(file_name)
    flag = True
    while flag:
        print()
        print('\u001b[32m 0 \u001b[0m - Выход из программы')
        print('\u001b[32m 1 \u001b[0m - Просмотреть все заметки')
        print('\u001b[32m 2 \u001b[0m - Просмотреть заметки с фильтрацией по дате')
        print('\u001b[32m 3 \u001b[0m - Создать новую заметку')
        print('\u001b[32m 4 \u001b[0m - Редактировать заметку')
        print('\u001b[32m 5 \u001b[0m - Удалить заметку')
        print()
        answer = input('\u001b[4mВыберите необходимое действие:\u001b[0m ')
        if answer == '0':
            os.system('cls')
            print('Выбрано: \u001b[32mВыход из программы \u001b[0m')
            flag = False
        elif answer == '1':
            print('Выбрано: \u001b[32mПросмотреть все заметки \u001b[0m')
            data = read_data(file_name)
            show_data(data)        
        elif answer == '2':
            print('Выбрано: \u001b[32mПросмотреть заметки с фильтрацией по дате \u001b[0m')
            data = read_data(file_name)
            f_data = filtering_data(data)
            show_data(f_data)    
        elif answer == '3':
            print('Выбрано: \u001b[32mСоздать новую заметку \u001b[0m')
            data = read_data(file_name)
            new_note = creating_note(data)
            write_data(new_note, file_name)
        elif answer == '4':
            print('Выбрано: \u001b[32mРедактировать заметку \u001b[0m')
            data = read_data(file_name)
            new_data = edit_note(data)
            write_data(new_data, file_name)
        elif answer == '5':
            print('Выбрано: \u001b[32mУдалить заметку \u001b[0m')
            data = read_data(file_name)
            new_note = delete_note(data)
            write_data(new_note, file_name)

if __name__ == '__main__':
    main()
