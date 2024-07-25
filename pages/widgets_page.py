import random
import time

from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        global section_content
        accordian = {'first':
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_CONTENT_FIRST},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_CONTENT_SECOND},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_CONTENT_THIRD},
                     }

        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        try:
            section_title.click()
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException")
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            print("TimeoutException")
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(1, 11))
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.element_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.element_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    # def check_remove_all_button(self):
    #     self.element_is_visible(self.locators.MULTIPLE_REMOVE_ALL_BUTTON).click()
    #     try:
    #         return self.elements_are_visible(self.locators.MULTI_VALUE)
    #     except TimeoutException:
    #         return

    def check_color_in_multi(self):
        color_list = self.elements_are_visible(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        try:
            input_date.click()
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException")
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        try:
            input_date.click()
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException")
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after

    def set_date_by_text(self, element, value):
        select = Select(self.element_is_visible(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        try:
            item_list = self.elements_are_visible(elements)
            for item in item_list:
                if item.text == value:
                    item.click()
                    break
        except TimeoutException:
            print("TimeoutException")


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        progress_bar_button = self.element_is_clickable(self.locators.PROGRESS_BAR_BUTTON)
        try:
            progress_bar_button.click()
        except (TimeoutException, ElementClickInterceptedException):
            print("TimeoutException, ElementClickInterceptedException")
        time.sleep(random.randint(2, 5))
        try:
            progress_bar_button.click()
        except (TimeoutException, ElementClickInterceptedException):
            print("TimeoutException, ElementClickInterceptedException")
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, name_tab):
        tabs = {'what':
                    {'title': self.locators.TABS_WHAT,
                     'content': self.locators.TABS_WHAT_CONTENT},
                'origin':
                    {'title': self.locators.TABS_ORIGIN,
                     'content': self.locators.TABS_ORIGIN_CONTENT},
                'use':
                    {'title': self.locators.TABS_USE,
                     'content': self.locators.TABS_USE_CONTENT},
                'more':
                    {'title': self.locators.TABS_MORE,
                     'content': self.locators.TABS_MORE_CONTENT},
                }

        button = self.element_is_visible(tabs[name_tab]['title'])
        try:
            button.click()
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException")
        what_content = self.element_is_visible(tabs[name_tab]['content']).text
        return button.text, len(what_content)


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def get_text_from_tool_tips(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.action_move_to_element(element)
        self.element_is_visible(wait_elem)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
        text = tool_tip_text.text
        return text

    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tool_tips(self.locators.BUTTON, self.locators.TOOL_TIP_BUTTON)
        tool_tip_text_field = self.get_text_from_tool_tips(self.locators.FIELD, self.locators.TOOL_TIP_FIELD)
        tool_tip_text_contrary = self.get_text_from_tool_tips(self.locators.CONTRARY_LINK,
                                                              self.locators.TOOL_TIP_CONTRARY)
        tool_tip_text_section = self.get_text_from_tool_tips(self.locators.SECTION_LINK,
                                                             self.locators.TOOL_TIP_SECTION)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section
