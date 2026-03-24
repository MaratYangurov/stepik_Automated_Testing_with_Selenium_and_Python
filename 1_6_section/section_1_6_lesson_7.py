from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/huge_form.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys('Мой ответ')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла