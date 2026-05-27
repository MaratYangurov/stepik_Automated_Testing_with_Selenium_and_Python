from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
try:
    browser.get(link)

    # Считываем значение x с страницы
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    # Заполняем текстовое поле с вычисленным ответом
    answer_field = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    answer_field.send_keys(calc(x))
    # Код, который заполняет обязательные поля
    checkbox1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    checkbox1.click()
    radiobutton1 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    radiobutton1.click()
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()