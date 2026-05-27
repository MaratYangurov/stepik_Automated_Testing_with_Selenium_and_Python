from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
try:
    browser.get(link)

    # Считываем значение x со страницы
    chest_radio = browser.find_element(By.ID, "treasure")
    chest_checked = chest_radio.get_attribute("valuex")
    # Заполняем текстовое поле с вычисленным ответом
    answer_field = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    answer_field.send_keys(calc(chest_checked))

    # Код, который заполняет обязательные поля
    checkbox1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    checkbox1.click()
    radiobutton1 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    radiobutton1.click()
    button = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()