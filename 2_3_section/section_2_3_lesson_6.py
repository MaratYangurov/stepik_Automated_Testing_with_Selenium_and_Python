from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()

try:
    # Открываем страницу
    browser.get(link)

    # Нажимаем кнопку (открывает новую вкладку)
    browser.find_element(By.TAG_NAME, 'button').click()

    # Переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Получаем значение x
    x = browser.find_element(By.ID, 'input_value').text

    # Вводим ответ
    browser.find_element(By.ID, 'answer').send_keys(calc(x))

    # Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, '.btn').click()

finally:
    time.sleep(10)
    browser.quit()