import time
from pages.base_page import BasePage
from conftest import driver


def test(driver):
    page = BasePage(driver, 'https://www.google.co.uz/?hl=ru')
    page.open()
    time.sleep(3)