from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def calc(x, y):
  return str(int(x)+int(y))

link = 'https://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    val_1 = browser.find_element(By.ID, 'num1')
    val_1_checked = val_1.text
    val_2 = browser.find_element(By.ID, 'num2')
    val_2_checked = val_2.text
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(calc(val_1_checked, val_2_checked))
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()