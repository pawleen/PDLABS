import unittest
from module import read_text_file, write_text_file, count_words

class TestFileOperations(unittest.TestCase):
    def test_read_text_file(self):
        # Проверяем, что функция правильно читает файл
        file_content = read_text_file("test_file.txt")
        expected_content = "This is a test file."
        self.assertEqual(file_content, expected_content)

    def test_write_text_file(self):
        # Проверяем, что функция правильно записывает содержимое в файл
        content_to_write = "This is new content."
        write_text_file("test_write.txt", content_to_write)
        with open("test_write.txt", "r") as file:
            written_content = file.read()
        self.assertEqual(written_content, content_to_write)

    def test_count_words(self):
        # Проверяем, что функция правильно подсчитывает количество слов
        text = "This is a sample text with multiple words."
        word_count = count_words(text)
        self.assertEqual(word_count, 7)

if __name__ == '__main__':
    unittest.main()
