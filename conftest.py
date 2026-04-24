import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

@pytest.fixture(scope="function")
def browser():
    # Фикстура для браузера
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()