from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    # Открываем страницу
    browser.get(link)
    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    wait = WebDriverWait(browser, 12)
    wait.until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    browser.find_element(By.ID, "book").click()
    # Получаем значение x
    x = browser.find_element(By.ID, 'input_value').text
    # Вводим ответ
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    # Нажимаем Submit
    browser.find_element(By.ID, 'solve').click()
finally:
    time.sleep(10)
    browser.quit()