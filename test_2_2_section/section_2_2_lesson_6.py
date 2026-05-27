from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://SunInJuly.github.io/execute_script.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    # Получаем значение x
    val = browser.find_element(By.XPATH, '//div[@class="form-group"]//span[@id="input_value"]')
    val_checked = val.text
    # Вводим ответ
    answer_field = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    answer_field.send_keys(calc(val_checked))
    # Скроллим к кнопке (лучший способ)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    browser.execute_script("arguments[0].scrollIntoView(true);", button)
    # Выбрать checkbox
    checkbox1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    checkbox1.click()
    # Переключить radiobutton
    radiobutton1 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    radiobutton1.click()
    # Нажать на кнопку
    #button = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]') # Не нужно, так как определили выше
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()