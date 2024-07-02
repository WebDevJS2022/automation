import time

from conftest import driver
from pages.elemets_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            driver.execute_script("window.scrollTo(0, 700)")  # СКРОЛЛИНГ
            text_box_page.fill_all_fields(self)
            time.sleep(2)
