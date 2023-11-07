import os
import csv
import random
import shutil

# Путь к исходной папке с изображениями
source_dataset_folder = 'C:/Users/pnikb/OneDrive/Desktop/YEAR3/PD/LAB2/dataset'

# Путь к папке, в которую вы хотите скопировать датасет
destination_folder = 'C:/Users/pnikb/OneDrive/Desktop/YEAR3/PD/LAB3/random_dataset'

# Создать папку назначения (если она не существует)
os.makedirs(destination_folder, exist_ok=True)

# Создать или открыть файл-аннотации для записи
with open('random_dataset_annotation.csv', 'w', newline='', encoding='utf-8') as annotation_file:
    csv_writer = csv.writer(annotation_file)

    # Записать заголовки столбцов
    csv_writer.writerow(['Абсолютный путь', 'Относительный путь', 'Метка класса'])

    for class_label in os.listdir(source_dataset_folder):
        class_folder = os.path.join(source_dataset_folder, class_label)

        if not os.path.isdir(class_folder):
            continue

        for image_file in os.listdir(class_folder):
            # Генерировать случайный номер от 0 до 10000
            random_number = random.randint(0, 10000)

            # Полный путь к исходному файлу
            source_file = os.path.join(class_folder, image_file)

            # Полный путь к файлу назначения
            destination_file = os.path.join(destination_folder, f'{random_number:04d}.jpg')

            # Копирование файла
            shutil.copy(source_file, destination_file)

            # Записать данные в файл-аннотации
            csv_writer.writerow([destination_file, os.path.relpath(destination_file, start=destination_folder), class_label])

print("Случайный датасет создан и аннотация создана.")
