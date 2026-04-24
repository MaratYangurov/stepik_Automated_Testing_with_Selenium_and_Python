import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



link = 'https://stepik.org/lesson/236895/step/1'

def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.CLASS_NAME, 'ember-view navbar__auth navbar__auth_login st-link st-link_style_button')
    button.click()



