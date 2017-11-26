import sys
import os
from os import urandom


# Главная функция
def main_function():
    if len(sys.argv) != 4:
        print("Введено недостаточное количество аргументов, попробуйте снова")
        help_type_command()
        return
    try:
        number_of_rewriting_cycles = int(sys.argv[2])
    except ValueError:
        print("Недопустимое значение количества циклов перезаписи")
        help_type_command()
        return
    except TypeError:
        print("Недопустимое значение количества циклов перезаписи")
        help_type_command()
        return
    if number_of_rewriting_cycles == 0:
        print("Количество циклов перезаписи равно нулю, перезапись не осуществится")
        help_type_command()
        return
    if sys.argv[3] != "zero" and sys.argv[3] != "random_sequence":
        print("Недопустимое значение типа перезаписи")
        help_type_command()
        return
    if os.path.exists(sys.argv[1]) is True:
        if os.path.isfile(sys.argv[1]) is True:
            rewriting_file(sys.argv[1], number_of_rewriting_cycles)
            print("Перезапись " + sys.argv[1] + " завершена")
            return
        if os.path.isdir(sys.argv[1]) is True:
            rewriting_directory(sys.argv[1], number_of_rewriting_cycles)
            print("Перезапись " + sys.argv[1] + " завершена")
            return
    else:
        print("Такого файла не существует. Проверьте правильность указанного пути")
        help_type_command()
        return


# Перезапись файла
def rewriting_file(path_to_file, number_of_rewriting_cycles):
    size_of_file = os.path.getsize(path_to_file)
    try:
        file = open(path_to_file, "wb")
    except IOError:
        print("Не удалось открыть файл")
        return False
    if sys.argv[3] == "zero":
        rewriting_bytes = bytearray(size_of_file)
        for i in range(size_of_file):
            rewriting_bytes[i] = 0
        for i in range(number_of_rewriting_cycles):
            file.write(rewriting_bytes)
            file.flush()
        file.close()
        return
    if sys.argv[3] == "random_sequence":
        for i in range(number_of_rewriting_cycles):
            rewriting_bytes = bytearray(urandom(size_of_file))
            file.write(rewriting_bytes)
            file.flush()
        file.close()
        return


# Перезапись директории
def rewriting_directory(path_to_directory, number_of_rewriting_cycles):
    list_of_entries = os.listdir(path_to_directory)
    if len(list_of_entries) == 0:
        return
    list_of_paths = []
    for i in range(len(list_of_entries)):
        list_of_paths.append(path_to_directory + "/" + list_of_entries[i])
    for i in range(len(list_of_paths)):
        if os.path.isfile(list_of_paths[i]) is True:
            rewriting_file(list_of_paths[i], number_of_rewriting_cycles)
            continue
        if os.path.isdir(list_of_paths[i]) is True:
            rewriting_directory(list_of_paths[i], number_of_rewriting_cycles)
            continue


# Справка
def help_type_command():
    print("Для корректной работы программы необходимо при запуске указать 3 аргумента:\n"
          "1 - Путь к файлу или каталогу, который нужно удалить (Например: D:/Фотографии/2000)\n"
          "2 - Количество циклов перезаписи (Число в десятеричной системе счисления)\n"
          "3 - Тип перезаписи. Может быть zero (перезапись нулями) или random_sequence (перезапись случайнми числами)")


# Точка входа
main_function()
