import pytest
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser, load_config
from pages.stepik_login_page import LoginPage

class TestDiffLang:
    @staticmethod
    @pytest.fixture(scope='function')
    def setup(browser, load_config):
        # Открываем страницу
        browser.get(f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        browser.implicitly_wait(10)

    def test_login_page(self, setup):
        print(f'Говно работает!')

