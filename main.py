from utils import *
from tkinter import filedialog
import tkinter as tk

def select_directory():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory(title="Выберите директорию для подсчета файлов")


def super_main():
    directory = select_directory()
    if not directory:
        print("Директория не выбрана.")
        return

    scanner = DirectoryScanner(directory)
    try:
        print(f"Количество файлов в '{directory}': {scanner.count_files()}")
    except ValueError as e:
        print(f"Ошибка: {e}")
        return

    csv_file = 'data.csv'
    try:
        workers = WorkerCollection.from_csv(csv_file)
    except Exception as e:
        print(f"Ошибка при чтении файла '{csv_file}': {e}")
        return

    print("\nИсходные данные:")
    for w in workers:
        print(w)

    sorted_by_name = WorkerCollection.sort_by_string(workers, 'ФИО')
    print("\nОтсортировано по ФИО:")
    for w in sorted_by_name:
        print(w)

    sorted_by_exp = WorkerCollection.sort_by_numeric(workers, 'трудовой стаж')
    print("\nОтсортировано по трудовому стажу:")
    for w in sorted_by_exp:
        print(w)

    try:
        threshold = int(input("\nВведите порог трудового стажа: "))
    except ValueError:
        print("Неверный ввод. Ожидалось целое число.")
        return

    print(f"\nРаботники с трудовым стажем больше {threshold} (генератор):")
    for w in workers.filter_by_experience_gen(threshold):
        print(w)

    print("\nДобавление нового работника:")

    new_num = input("Введите №: ")
    new_fio = input("Введите ФИО: ")
    new_pos = input("Введите должность: ")

    try:
        new_exp = int(input("Введите трудовой стаж: "))
    except ValueError:
        print("Неверное значение трудового стажа. Ожидалось целое число.")
        return

    new_rec = Record(new_num, new_fio, new_pos, new_exp)
    workers.add(new_rec)
    print("Новый работник успешно добавлен.")

    try:
        workers.save_to_csv(csv_file)
        print(f"Обновленные данные сохранены в '{csv_file}'")
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")


if __name__ == '__main__':
    super_main()
