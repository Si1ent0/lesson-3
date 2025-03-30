import pytest
from selene import browser


# Настройка размера окна браузера
@pytest.fixture()
def browser_size():
    browser.config.window_width = 600
    browser.config.window_height = 600


# Открытие страницы поисковика с настройками
@pytest.fixture()
def open_url(browser_size):
    browser.open('https://ya.ru')

    yield

    browser.quit()
