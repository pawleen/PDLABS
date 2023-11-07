import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

# Определение пути к текущему скрипту
current_script_path = os.path.realpath(sys.argv[0])
current_directory = os.path.dirname(current_script_path)

# Определяем функцию create_folder_if_not_exists, которая проверяет, существует ли указанная папка, и создает ее, если она отсутствует.
def create_folder_if_not_exists(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Создаем папку "dataset" в текущей директории (если она не существует) для хранения данных.
dataset_folder = os.path.join(current_directory, "dataset")
create_folder_if_not_exists(dataset_folder)

# Создаем подпапку "rose" внутри папки "dataset" (если она не существует) для хранения изображений класса "rose".
rose_folder = os.path.join(dataset_folder, "rose")
create_folder_if_not_exists(rose_folder)

# Создаем подпапку "tulip" внутри папки "dataset" (если она не существует) для хранения изображений класса "tulip".
tulip_folder = os.path.join(dataset_folder, "tulip")
create_folder_if_not_exists(tulip_folder)

# Определяем функцию download_images для загрузки изображений из интернета.
def download_images(query, folder_name, num_images):
    # Устанавливаем базовый URL для поиска изображений на Yandex Images.
    base_url = "https://yandex.ru/images/search"
    
    # Устанавливаем параметры запроса, включая запрос (query), размер изображений и другие параметры.
    params = {
        "text": query,
        "isize": "eq",
        "iw": "1920",
        "ih": "1080",
    }
    
    # Устанавливаем HTTP-заголовки, включая "User-Agent" для имитации браузера Chrome.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }

    # Инициализируем счетчики страницы и скачанных изображений.
    page = 1
    downloaded_images = 0

    # Начинаем цикл, который продолжается, пока не скачано нужное количество изображений.
    while downloaded_images < num_images:
        try:
            # Пытаемся выполнить GET-запрос для получения страницы результатов поиска.
            response = requests.get(base_url, params=params, headers=headers)
            soup = BeautifulSoup(response.content, "html.parser")

            # Используем BeautifulSoup для анализа HTML-кода страницы.
            links = soup.find_all("a", class_="serp-item__link")
            
            # Находим все ссылки на изображения в HTML-коде.
            for link in links:
                image_url = link.get("href")

                # Перебираем найденные ссылки.
                if image_url:
                    image_url = parse_qs(urlparse(image_url).query).get("img_url", [None])[0]
                    
                    # Извлекаем URL изображения из ссылки.
                    if image_url:
                        response = requests.get(image_url)
                        
                        # Пытаемся загрузить изображение по его URL.
                        if response.status_code == 200:
                            # Генерируем имя файла для сохранения изображения.
                            filename = os.path.join(folder_name, f"{downloaded_images:04d}.jpg")
                            
                            # Записываем содержимое изображения в файл.
                            with open(filename, "wb") as f:
                                f.write(response.content)
                            downloaded_images += 1
                            if downloaded_images >= num_images:
                                break
        except Exception as e:
            # Обрабатываем ошибки при скачивании изображений.
            print(f"Error: {str(e)}")

# Загружаем изображения для класса "rose" в папку "dataset/rose".
download_images("rose", rose_folder, 21)

# Загружаем изображения для класса "tulip" в папку "dataset/tulip".
download_images("tulip", tulip_folder, 20)

# Выводим сообщение о завершении загрузки изображений.
print("Загрузка изображений завершена.")
