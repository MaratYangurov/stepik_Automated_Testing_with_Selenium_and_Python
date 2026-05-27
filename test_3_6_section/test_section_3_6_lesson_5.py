import pytest
import math
import time

from pymsgbox import password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser, load_config
from pages.stepik_login_page import LoginPage

class TestParametrize:
    @staticmethod
    def calc_answer():
        # Вычисление актуального ответа
        return str(math.log(int(time.time())))

    @pytest.mark.parametrize(
        'link',
        [
            '236895',
            '236896',
            '236897',
            '236898',
            '236899',
            '236903',
            '236904',
            '236905',
        ]
    )
    def test_parametrize_section_3_6_lesson_5(self, browser, load_config, link):
        # Открываем страницу
        browser.get(f'https://stepik.org/lesson/{link}/step/1')
        browser.implicitly_wait(10)
        # Авторизация
        login_page = LoginPage(browser)
        login_page.login(email=load_config['login_stepik'], password=load_config['password_stepik'])

        # Поле ответа
        textarea = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea.ember-text-area.string-quiz__textarea')))
        textarea.clear()
        # Ввод актуального ответа
        textarea.send_keys(self.calc_answer())
        #browser.implicitly_wait(5)

        # Пытаемся нажать кнопку 'Отправить'
        #submit_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        if browser.find_elements(By.CSS_SELECTOR, 'button.again-btn'):
            again_button = browser.find_element(By.CSS_SELECTOR, 'button.again-btn')
            again_button.click()
            submit_button = browser.find_element(By.CSS_SELECTOR, 'button.submit-submission')
            submit_button.click()
        elif browser.find_element(By.CSS_SELECTOR,'button.submit-submission'):
            submit_button = browser.find_element(By.CSS_SELECTOR,'button.submit-submission')
            submit_button.click()
        #browser.implicitly_wait(3)

        # Получение feedback
        feedback_text= WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.smart-hints')))
        # Проверка результата
        assert feedback_text.text == 'Correct!', f'Expected "Correct!", but got "{feedback_text.text}"'

