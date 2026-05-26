import pytest
import math
import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestParametrize:
    @staticmethod
    def calc_answer():
        # Вычисление актуального ответа
        return str(math.log(int(time.time())))

    @staticmethod
    def login_stepik(browser, load_config):
        wait = WebDriverWait(browser, 20)
        # Если пользователь уже авторизован
        if browser.find_elements(By.CSS_SELECTOR, '.navbar__profile-img'):
            return
        # Кнопка "Войти"
        login_button = wait.until(EC.element_to_be_clickable((By.ID, 'ember503')))
        login_button.click()
        # Поле логина
        #username_input = wait.until(EC.visibility_of_element_located((By.ID, 'id_login_email')))
        username_input = browser.find_element(By.ID, 'id_login_email')
        # Поле пароля
        password_input = browser.find_element(By.ID, 'id_login_password')
        # Ввод данных
        username_input.send_keys(load_config['login_stepik'])
        password_input.send_keys(load_config['password_stepik'])
        # Кнопка входа
        submit_login = browser.find_element(
            By.CSS_SELECTOR,
            '.sign-form__btn'
        )
        submit_login.click()
        # Ждём закрытия модального окна
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.modal--opened')))

    @pytest.mark.parametrize(
        'link',
        [
            'https://stepik.org/lesson/236895/step/1',
            'https://stepik.org/lesson/236896/step/1',
            'https://stepik.org/lesson/236897/step/1',
            'https://stepik.org/lesson/236898/step/1',
            'https://stepik.org/lesson/236899/step/1',
            'https://stepik.org/lesson/236903/step/1',
            'https://stepik.org/lesson/236904/step/1',
            'https://stepik.org/lesson/236905/step/1',
        ]
    )
    def test_parametrize_section_3_6_lesson_5(self, browser, load_config, link):
        wait = WebDriverWait(browser, 20)
        # Открываем страницу
        browser.get(link)
        # Авторизация
        self.login_stepik(browser, load_config)
        # Поле ответа
        textarea = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea')))
        textarea.clear()
        # Ввод актуального ответа
        textarea.send_keys(self.calc_answer())
        # Пытаемся нажать кнопку 'Отправить' несколько раз
        # for i in range(2):
        #     try:
        #         submit_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        #         submit_button.click()
        #         break
        #
        submit_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        submit_button.click()
        # Получение feedback
        feedback_text= WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.smart-hints'))).text
        # Проверка результата
        assert feedback_text == 'Correct!', \
            f'Expected "Correct!", but got "{feedback_text}"'