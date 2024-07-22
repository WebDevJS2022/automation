from selenium.common import ElementClickInterceptedException

from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):
        try:
            self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException")

        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title
