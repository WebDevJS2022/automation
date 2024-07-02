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
