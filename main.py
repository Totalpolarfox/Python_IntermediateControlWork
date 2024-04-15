# функция создания файла
def create_file_csv(file: str = 'file name'):
    with open(file, 'w', encoding='utf-8') as f:
        f.write('ID;Заголовок;Заметка;Дата_создания\n')
    print(f'\u001b[32mФайл {file} создан\u001b[0m')

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


if __name__ == '__main__':
    main()
