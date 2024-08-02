import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

# Автоматическая установка chromedriver
chromedriver_autoinstaller.install()

# Опции для работы с Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Отключение графического интерфейса
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Создание объекта Service
service = Service()

# Создание экземпляра браузера
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Открытие страницы
    driver.get("https://www.divan.ru/category/divany-i-kresla")

    # Подождите немного, чтобы страница загрузилась
    time.sleep(5)

    # Открытие CSV файла для записи
    with open('sofa_prices.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Название', 'Цена']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Найти все элементы с товарами
        items = driver.find_elements_by_css_selector(".product-item")

        for item in items:
            try:
                # Получить название
                name = item.find_element_by_css_selector(".product-item__title").text
            except:
                name = "Нет названия"

            try:
                # Получить цену
                price = item.find_element_by_css_selector(".product-item__price").text
            except:
                price = "Нет цены"

            # Записать данные в CSV файл
            writer.writerow({'Название': name, 'Цена': price})
            print(f"Название: {name} | Цена: {price}")

finally:
    # Закрытие браузера
    driver.quit()
