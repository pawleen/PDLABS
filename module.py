def read_text_file(file_path):
    """
    Читает текстовый файл и возвращает его содержимое.

    :param file_path: Путь к текстовому файлу.
    :return: Содержимое файла в виде строки.
    """
    with open(file_path, 'r') as file:
        return file.read()

def write_text_file(file_path, content):
    """
    Записывает текстовое содержимое в файл.

    :param file_path: Путь к текстовому файлу.
    :param content: Строка, которую нужно записать в файл.
    """
    with open(file_path, 'w') as file:
        file.write(content)

def count_words(text):
    """
    Подсчитывает количество слов в тексте.

    :param text: Текст, в котором нужно подсчитать слова.
    :return: Количество слов в тексте.
    """
    words = text.split()
    return len(words)

file_content = read_text_file("example.txt")
print("Содержимое файла:")
print(file_content)

# Запись в файл
new_content = "Это новое содержимое файла."
write_text_file("example.txt", new_content)
print("Новое содержимое файла записано.")

# Подсчет слов в тексте
word_count = count_words(new_content)
print(f"Количество слов в тексте: {word_count}")