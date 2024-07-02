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
            time.sleep(1)
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            print(output_name)
            print(output_email)
            print(output_cur_addr)
            print(output_per_addr)
