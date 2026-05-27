import pytest
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = 'https://stepik.org/lesson/236895/step/1'
class TestLogin:
    def test_guest_should_see_login_link(self, browser, load_config):
        browser.get(link)

        # Нажать кнопку "Войти"
        time.sleep(10)
        login_button = browser.find_element(By.CSS_SELECTOR, '.navbar__auth_login')
        login_button.click()

        # Ждём появления формы логина
        wait = WebDriverWait(browser, 10)
        username_input = wait.until(EC.presence_of_element_located((By.NAME, 'login')))
        password_input = browser.find_element(By.NAME, 'password')
        login = load_config['login_stepik']
        password = load_config['password_stepik']
        username_input.send_keys(login)
        password_input.send_keys(password)

        # Нажимаем кнопку "Войти"
        browser.find_element(By.CLASS_NAME, 'sign-form__btn').click()

        # Ждём, пока попап авторизации исчезнет
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal--opened")))

        # Проверяем, что авторизация успешна
        assert "lesson" in browser.current_url
