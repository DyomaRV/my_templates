import os


def py_search(input_path: str, data_for_search: str) -> None:
    """
    Функция осуществляет поиск по всем файлам в папке input_path
    текст data_for_search
    """
    for i_file in os.listdir(input_path):
        i_file = '{}/{}'.format(input_path, i_file)
        if not os.path.isfile(i_file):
            if i_file.find('git') != -1 or i_file.find('idea') != -1: # исключение папок с названиями из поиска
                pass
            else:
                py_search(i_file, data_for_search)
        else:
            if os.path.isfile(i_file) and i_file.endswith('.py'):       # поиск только по файлам .py
                with open(i_file, 'r') as file:
                    for line in file:
                        if line.find(data_for_search) != -1:
                            print(os.path.abspath(i_file))              # вывод пути к файлу
                            print('line = ', line, data)                # вывод строки
            elif os.path.isfile(i_file) and not i_file.endswith('.py'):
                pass


path = os.path.abspath('main.py')[:53]             # определение пути к файлу в директории поиска, обрезал имя файла
data = 'class'

py_search(input_path=path, data_for_search=data)