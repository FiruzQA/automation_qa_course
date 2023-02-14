import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from Pages.base_page import BasePage
from generator.generator import generated_colour, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DataPickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
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
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]

class AutoCompletePage(BasePage):

    locators = AutoCompletePageLocators()

    def check_fill_multi_autocomplete(self):
        colours = random.sample(next(generated_colour()).colour_name, k=random.randint(2, 5))
        for colour in colours:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(colour)
            input_multi.send_keys(Keys.ENTER)
        return colours

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_colour_in_multi(self):
        colour_list = self.elements_are_visible(self.locators.MULTI_VALUE)
        colours = []
        for colour in colour_list:
            colours.append(colour.text)
        return colours

    def fill_input_single(self):
        colour = random.sample(next(generated_colour()).colour_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(colour)
        input_single.send_keys(Keys.ENTER)
        return colour[0]

    def check_colout_in_single(self):
        colour = self.element_is_visible(self.locators.SINGLE_VALUE)
        return colour.text

class DataPickerPage(BasePage):
    locators = DataPickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_data_after = input_date.get_attribute('value')
        return value_date_before, value_data_after

    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
        self.set_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        input_day_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_data_after = input_day_after.get_attribute('value')
        return value_date_before, value_data_after

    def set_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

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
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_clickable(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(2, 5))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
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
        button.click()
        what_content = self.element_is_visible(tabs[name_tab]['content']).text
        return button.text, len(what_content)
