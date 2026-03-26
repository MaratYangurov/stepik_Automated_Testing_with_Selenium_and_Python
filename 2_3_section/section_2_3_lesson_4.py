from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()

try:
    # Открыть страницу
    browser.get(link)
    # Нажать на кнопку
    button1 = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')  # Не нужно, так как определили выше
    button1.click()
    # Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    # Получаем значение x
    val = browser.find_element(By.XPATH, '//div[@class="form-group"]//span[@id="input_value"]')
    val_checked = val.text
    # Вводим ответ
    answer_field = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    answer_field.send_keys(calc(val_checked))
    # Нажать на кнопку
    button2 = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')  # Не нужно, так как определили выше
    button2.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()