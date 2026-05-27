import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbs(unittest.TestCase):
    def setUp(self):
        """Этот метод выполняется перед каждым тестом"""
        self.browser = webdriver.Chrome()

    def tearDown(self):
        """Этот метод выполняется после каждого теста"""
        self.browser.quit()

    def test_registration1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        self.browser.get(link)

        # Заполняем обязательные поля
        input1 = self.browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
        input1.send_keys('Ivan')

        input2 = self.browser.find_element(By.XPATH,
                                           '//div[@class="first_block"]//input[@class="form-control second"]')
        input2.send_keys('Petrov')

        input3 = self.browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
        input3.send_keys('gmail.com')

        # Отправляем форму
        button = self.browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        # Проверяем, что регистрация прошла успешно
        time.sleep(1)  # Ждем загрузки страницы
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text

        # Используем assertEqual для проверки результата
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!')

    def test_registration2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        self.browser.get(link)

        # Заполняем обязательные поля
        input1 = self.browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
        input1.send_keys('Ivan')

        input2 = self.browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control second"]')
        input2.send_keys('Petrov')

        input3 = self.browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
        input3.send_keys('gmail.com')

        # Отправляем форму
        button = self.browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        # Проверяем, что регистрация прошла успешно
        time.sleep(1)  # Ждем загрузки страницы
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text

        # Используем assertEqual для проверки результата
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!')



if __name__ == "__main__":
    unittest.main()
