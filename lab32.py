import os
import csv
import shutil

# Путь к исходной папке с изображениями
source_dataset_folder = 'C:/Users/pnikb/OneDrive/Desktop/YEAR3/PD/LAB2/dataset'

# Путь к папке, в которую вы хотите скопировать датасет
destination_folder = 'C:/Users/pnikb/OneDrive/Desktop/YEAR3/PD/LAB3/dataset_copy'

# Создать или открыть файл-аннотации для записи
with open('dataset_copy_annotation.csv', 'w', newline='', encoding='utf-8') as annotation_file:
    csv_writer = csv.writer(annotation_file)

    # Записать заголовки столбцов
    csv_writer.writerow(['Абсолютный путь', 'Относительный путь', 'Метка класса'])

    # Перебрать все файлы в исходной папке
    for class_label in os.listdir(source_dataset_folder):
        class_folder = os.path.join(source_dataset_folder, class_label)

        if not os.path.isdir(class_folder):
            continue

        for index, image_file in enumerate(os.listdir(class_folder)):
            # Полный путь к исходному файлу
            source_file = os.path.join(class_folder, image_file)

            # Полный путь к файлу назначения
            destination_class_folder = os.path.join(destination_folder, f'{class_label}_copy')
            os.makedirs(destination_class_folder, exist_ok=True)
            destination_file = os.path.join(destination_class_folder, f'{class_label}_{index:04d}.jpg')

            # Копирование файла и переименование
            shutil.copy(source_file, destination_file)

            # Записать данные в файл-аннотации
            csv_writer.writerow([destination_file, os.path.relpath(destination_file, start=destination_folder), class_label])

print("Датасет скопирован и аннотация создана.")
