import pytest
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser, load_config
from pages.stepik_login_page import LoginPage

class TestParametrize:
    @staticmethod
    def setup(cls):
        pass

    def test_login_page(self, setup):
        pass

