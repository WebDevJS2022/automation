import time

from conftest import driver
from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage


class TestWidgets:

    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, "First accordian incorrect"
            assert second_title == 'Where does it come from?' and second_content > 0, "Second accordian incorrect"
            assert third_title == 'Why do we use it?' and third_content > 0, "Third accordian incorrect"

    class TestAutoComplete:

        def test_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            colors = auto_complete_page.fill_input_multi()
            colors_result = auto_complete_page.check_color_in_multi()
            assert colors == colors_result, "Colors not added"

        def test_remove_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            # autocomplete_page.check_remove_all_button()
            assert count_value_before != count_value_after, "multi count before and after are equal"

        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result, "single color has not been added"

    class TestDatePickerPage:
        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            time.sleep(2)
            assert value_date_before != value_date_after, "Dates before and after are the same"

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            time.sleep(2)
            assert value_date_before != value_date_after, "Dates and time before and after are the same"

    class TestSliderPage:
        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            before, after = slider.change_slider_value()
            assert before != after, "slider has not changed value"

    class TestProgressBarPage:
        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            before, after = progress_bar.change_progress_bar_value()
            assert before != after, "progress bar has not changed value"

    class TestTabsPage:

        def test_tabs(self, driver):
            tabs = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs.open()
            what_button, what_content = tabs.check_tabs('what')
            origin_button, origin_content = tabs.check_tabs('origin')
            use_button, use_content = tabs.check_tabs('use')
            # more_button, more_content = tabs.check_tabs('more')
            assert what_button == 'What' and what_content != 0, "tab What not pressed or text missing"
            assert origin_button == 'Origin' and origin_content != 0, "tab Origin not pressed or text missing"
            assert use_button == 'Use' and use_content != 0, "tab Use not pressed or text missing"

    class TestToolTips:

        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
            assert button_text == 'You hovered over the Button', "hover missing or incorrect content"
            assert field_text == 'You hovered over the text field', "hover missing or incorrect content"
            assert contrary_text == 'You hovered over the Contrary', "hover missing or incorrect content"
            assert section_text == 'You hovered over the 1.10.32', "hover missing or incorrect content"
