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
    val = browser.find_element(By.XPATH, '//div[@class="form-group"]//span[@id="input_value"]')
    val_checked = val.text
    answer_field = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    answer_field.send_keys(calc(val_checked))
finally:
    time.sleep(10)
    browser.quit()