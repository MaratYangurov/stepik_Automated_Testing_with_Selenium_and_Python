import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import json


@pytest.fixture(scope='function')
def browser():
    # Фикстура для браузера
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    browser.quit()


@pytest.fixture(scope='function')
def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open('config.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        return config