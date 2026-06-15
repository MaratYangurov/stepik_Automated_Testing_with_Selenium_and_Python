import pytest
from selenium.webdriver.common.by import By


class TestDiffLang:
    @staticmethod
    @pytest.fixture(scope='function')
    def setup(browser, load_config):
        # Открываем страницу
        browser.get(f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        browser.implicitly_wait(10)

    def test_login_page(self, setup, browser):
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')

        assert button.is_displayed(), "Кнопка добавления в корзину не найдена на странице"

