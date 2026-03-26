from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    # Заполняем текстовые поля
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('Ivan')
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('Petrov')
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('gmail.com')
    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    # получаем путь к file_example.txt
    file_path = os.path.join(current_dir, file_name)
    # отправляем файл
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    # Нажать кнопку
    button = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')  # Не нужно, так как определили выше
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()