# функция создания файла
def create_file_csv(file: str = 'file name'):
    with open(file, 'w', encoding='utf-8') as f:
        f.write('ID;Заголовок;Заметка;Дата_создания\n')
    print(f'\u001b[32mФайл {file} создан\u001b[0m')

# функция вывода данных
def show_data(data: list[str]):
    for element in data:
        print(f'ID: {element[0]}  Дата создания: {element[3]}')
        print(f'\tЗаголовок: {element[1]}')
        print(f'\tЗаметка: {element[2]}')
    # print(data)

# функция чтения данных из файла
def read_data(file: str = 'file name'):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f, delimiter = ";")
            return list(csv_reader)[1:] # удаляет строку заголовка

    except FileNotFoundError:
        print('\u001b[31mФайл  не найден.\n\u001b[0m')
        return []  

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
    

if __name__ == '__main__':
    main()
