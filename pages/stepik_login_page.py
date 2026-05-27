from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.navbar__auth_login')
    LOGIN_INPUT = (By.ID, 'id_login_email')
    PASSWORD_INPUT = (By.ID, 'id_login_password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '.sign-form__btn')

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 20)

    def login(self, email, password):
        # Если пользователь уже авторизован
        if self.browser.find_elements(By.CSS_SELECTOR, '.navbar__profile-img'):
            return
        # Кнопка "Войти"
        login_button = self.wait.until(EC.element_to_be_clickable((self.LOGIN_BUTTON)))
        login_button.click()
        # Поле логина
        username_input = self.browser.find_element(*self.LOGIN_INPUT)
        # Поле пароля
        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        # Ввод данных
        username_input.send_keys(email)
        password_input.send_keys(password)
        # Кнопка входа
        submit_login = self.browser.find_element(*self.SUBMIT_BUTTON)
        submit_login.click()

        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.modal--opened')))
