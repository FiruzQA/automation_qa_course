import random
import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from Pages.base_page import BasePage
from generator.generator import generated_colour, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DataPickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolsTipsPageLocators, MenuPageLocators


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    @allure.step("accordian")
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

    @allure.step("fill multi autocomplete")
    def check_fill_multi_autocomplete(self):
        colours = random.sample(next(generated_colour()).colour_name, k=random.randint(2, 5))
        for colour in colours:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(colour)
            input_multi.send_keys(Keys.ENTER)
        return colours

    @allure.step("remove value from multi")
    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    @allure.step("colour in multi")
    def check_colour_in_multi(self):
        colour_list = self.elements_are_visible(self.locators.MULTI_VALUE)
        colours = []
        for colour in colour_list:
            colours.append(colour.text)
        return colours

    @allure.step("fill input single")
    def fill_input_single(self):
        colour = random.sample(next(generated_colour()).colour_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(colour)
        input_single.send_keys(Keys.ENTER)
        return colour[0]

    @allure.step("colour in single")
    def check_colout_in_single(self):
        colour = self.element_is_visible(self.locators.SINGLE_VALUE)
        return colour.text

class DataPickerPage(BasePage):
    locators = DataPickerPageLocators()

    @allure.step("select date")
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

    @allure.step("select date and time")
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

    @allure.step("set item from list")
    def set_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

class SliderPage(BasePage):
    locators = SliderPageLocators()

    @allure.step("slider value")
    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    @allure.step("progress bar value")
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

    @allure.step("tabs")
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

class ToolsTipsPage(BasePage):
    locators = ToolsTipsPageLocators()

    @allure.step("get text from tool tips")
    def get_text_from_tool_tips(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.action_move_to_element(element)
        self.element_is_visible(wait_elem)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
        text = tool_tip_text.text
        return text

    @allure.step("tool tips")
    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tool_tips(self.locators.BUTTON, self.locators.TOOL_TIP_BUTTON)
        time.sleep(1)
        tool_tip_text_field = self.get_text_from_tool_tips(self.locators.FIELD, self.locators.TOOL_TIP_FIELD)
        time.sleep(1)
        tool_tip_text_contrary = self.get_text_from_tool_tips(self.locators.CONTRARY_LINK,
                                                              self.locators.TOOL_TIP_CONTRARY_LINK)
        time.sleep(1)
        tool_tip_text_section = self.get_text_from_tool_tips(self.locators.SECTION_LINK,
                                                             self.locators.TOOL_TIP_SECTION_LINK)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section

class MenuPage(BasePage):
    locators = MenuPageLocators()

    @allure.step("menu")
    def check_menu(self):
        menu_item_list = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data
