import os
import csv

# Определить классы и папки, соответствующие каждому классу
classes = {
    'rose': 'rose',
    'tulip': 'tulip'
}
dataset_folder = 'C:/Users/pnikb/OneDrive/Desktop/YEAR3/PD/LAB2/dataset'
# Здесь создайте переменную annotation_path с путем к файлу аннотации
annotation_path = './annotation.csv'

# Затем определите функцию create_annotation
def create_annotation(dataset_folder, annotation_path, classes):
    with open(annotation_path, 'w', newline='', encoding='utf-8') as annotation_file:
        csv_writer = csv.writer(annotation_file)

        # Запишите заголовки столбцов
        csv_writer.writerow(['Абсолютный путь', 'Относительный путь', 'Метка класса'])

        # Переберите все классы и изображения в каждом классе
        for class_label, class_folder in classes.items():
            class_path = os.path.join(dataset_folder, class_folder)

            # Проверьте существование папки
            if not os.path.exists(class_path):
                continue

            image_files = os.listdir(class_path)

            for image_file in image_files:
                # Получите абсолютный путь к файлу
                absolute_path = os.path.join(class_path, image_file)

                # Получите относительный путь относительно вашего проекта
                relative_path = os.path.relpath(absolute_path, start='C:/Users/pnikb/OneDrive/Desktop/YEAR3/PD/LAB3')

                # Запишите данные в файл аннотации
                csv_writer.writerow([absolute_path, relative_path, class_label])

# Здесь вызовите функцию create_annotation
create_annotation(dataset_folder, annotation_path, classes)

print("Файл-аннотация создан в директории LAB3.")
