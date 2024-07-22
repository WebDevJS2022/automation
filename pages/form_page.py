import os
import time

from selenium.common import TimeoutException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        # self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.firstname)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.lastname)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        try:
            self.element_is_visible(self.locators.GENDER).click()
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException")
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
        self.element_is_visible(self.locators.SUBJECT).send_keys('Maths')
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.zoom_page()
        try:
            self.element_is_visible(self.locators.HOBBIES).click()
        except TimeoutException:
            print("TimeoutException")
        self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        try:
            self.element_is_visible(self.locators.SELECT_STATE).click()
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException")

        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        try:
            self.element_is_visible(self.locators.SELECT_CITY).click()
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException")
        try:
            self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        except ElementNotInteractableException:
            print("ElementNotInteractableException")
        try:
            self.element_is_visible(self.locators.SUBMIT).click()
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException")
        return person

    def form_result(self):
        result_list = self.element_are_present(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data
