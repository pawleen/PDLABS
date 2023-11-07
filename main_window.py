import os
import csv
import random
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import cv2
from lab31 import create_annotation 
# Импортируйте свои функции и объекты из других файлов

class ClassInstanceIterator:
    def __init__(self, class_label, annotation_file):
        self.class_label = class_label
        self.instances = self._load_instances(annotation_file)
        self.index = 0

    def _load_instances(self, annotation_file):
        instances = []

        with open(annotation_file, 'r', encoding='utf-8') as annotation_file:
            csv_reader = csv.reader(annotation_file)
            next(csv_reader)  # Пропустить заголовки

            for row in csv_reader:
                _, _, label = row
                if label == self.class_label:
                    instances.append(row[0])  # Путь к экземпляру

        random.shuffle(instances)  # Перемешать экземпляры

        return instances

    def get_next_instance(self):
        if self.index < len(self.instances):
            next_instance = self.instances[self.index]
            self.index += 1
            return next_instance
        else:
            return None

class DatasetAnnotationApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Инициализация вашего GUI
        self.init_ui()

    def init_ui(self):
        # Создайте и настройте элементы вашего GUI (кнопки, поля ввода и др.)
        self.setWindowTitle("Dataset Annotation App")
        self.setGeometry(100, 100, 400, 200)

        self.folder_button = QtWidgets.QPushButton("Выбрать папку с исходным датасетом", self)
        self.folder_button.clicked.connect(self.select_dataset_folder)

        self.annotation_button = QtWidgets.QPushButton("Выбрать файл аннотации", self)
        self.annotation_button.clicked.connect(self.select_annotation_file)

        self.next_rose_button = QtWidgets.QPushButton("Следующая роза", self)
        self.next_rose_button.clicked.connect(self.get_next_rose)

        self.next_tulip_button = QtWidgets.QPushButton("Следующий тюльпан", self)
        self.next_tulip_button.clicked.connect(self.get_next_tulip)

        self.image_label = QtWidgets.QLabel(self)

        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.folder_button)
        layout.addWidget(self.annotation_button)
        layout.addWidget(self.next_rose_button)
        layout.addWidget(self.next_tulip_button)
        layout.addWidget(self.image_label)
        self.setLayout(layout)

        self.dataset_folder = None
        self.annotation_file = None
        self.rose_iterator = None
        self.tulip_iterator = None

    def select_dataset_folder(self):
        
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку с исходным датасетом')

        if folder_path:
            self.dataset_folder = folder_path

    def select_annotation_file(self):
        annotation_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл аннотации', filter='CSV Files (*.csv)')

        if annotation_path:
            self.annotation_file = annotation_path



    def get_next_rose(self):
        if self.dataset_folder and self.annotation_file:
            if not self.rose_iterator:
                self.rose_iterator = ClassInstanceIterator('rose', self.annotation_file)

            next_instance = self.rose_iterator.get_next_instance()
            if next_instance:
                self.show_image(next_instance)
            else:
                QtWidgets.QMessageBox.information(self, "Информация", "Экземпляры роз закончились")

    def get_next_tulip(self):
        if self.dataset_folder and self.annotation_file:
            if not self.tulip_iterator:
                self.tulip_iterator = ClassInstanceIterator('tulip', self.annotation_file)

            next_instance = self.tulip_iterator.get_next_instance()
            if next_instance:
                self.show_image(next_instance)
            else:
                QtWidgets.QMessageBox.information(self, "Информация", "Экземпляры тюльпанов закончились")


    def show_image(self, image_path):
        image = cv2.imread(image_path)

        if image is not None and not image.size == 0:
            width, height = 640, 480
            image = cv2.resize(image, (width, height))

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = QtGui.QImage(image.data, width, height, image.strides[0], QtGui.QImage.Format_RGB888)

            pixmap = QtGui.QPixmap.fromImage(image)
            self.image_label.setPixmap(pixmap)
            self.image_label.setAlignment(QtCore.Qt.AlignCenter)



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = DatasetAnnotationApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
