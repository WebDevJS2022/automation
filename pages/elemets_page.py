from selenium.webdriver import Keys

from conftest import driver
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self, driver):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('Anna')
        self.element_is_visible(self.locators.EMAIL).send_keys('anna@gmail.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('London-Paris')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('Paris-London')
        self.element_is_visible(self.locators.SUBMIT).send_keys(Keys.ENTER)

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address
