import csv
import random

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

def main():
    annotation_file = 'dataset_annotation.csv'  #  путь к  файлу аннотации

    class_label = input("Введите метку класса (например, 'rose'): ")
    iterator = ClassInstanceIterator(class_label, annotation_file)
    i=0
    while True:
        
        next_instance = iterator.get_next_instance()
        if next_instance:
            print(f"{i}Следующий экземпляр класса '{class_label}': {next_instance}")
            i+=1
        else:
            print(f"Все экземпляры класса '{class_label}' исчерпаны.")
            break

if __name__ == "__main__":
    main()
