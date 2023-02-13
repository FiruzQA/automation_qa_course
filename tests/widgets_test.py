import time

from Pages.widgets_page import AccordianPage, AutoCompletePage, DataPickerPage, SliderPage, ProgressBarPage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0
            assert second_title == 'Where does it come from?' and second_content > 0
            assert third_title == 'Why do we use it?' and third_content > 0

    class TestAutoComplete:

        def test_fill_multi_autocomplete(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            colours = auto_complete_page.check_fill_multi_autocomplete()
            colours_result = auto_complete_page.check_colour_in_multi()
            print(colours)
            print(colours_result)
            assert colours == colours_result

        def test_remove_value_from_multi(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            auto_complete_page.check_fill_multi_autocomplete()
            count_value_before, count_value_after = auto_complete_page.remove_value_from_multi()
            assert count_value_before != count_value_after

        def test_fill_single_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            colour = auto_complete_page.fill_input_single()
            colour_result = auto_complete_page.check_colout_in_single()
            assert colour == colour_result

    class TestDataPickerPage:
        def test_change_date(self, driver):
            date_picker_page = DataPickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_data_after = date_picker_page.select_date()
            assert value_date_before != value_data_after, 'the date has not been changed'

        def test_change_date_and_time(self, driver):
            date_picker_page = DataPickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_data_after = date_picker_page.select_date_and_time()
            print(value_date_before)
            print(value_data_after)
            assert value_date_before != value_data_after, 'the date and time has not been changed'

class TestSliderPage:
    def test_slider(self, driver):
        slider = SliderPage(driver, 'https://demoqa.com/slider')
        slider.open()
        before, after = slider.change_slider_value()
        assert before != after, 'the slider value has not been changed'


class TestProgressBarPage:
    def test_progress_bar(self, driver):
        progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
        progress_bar.open()
        value_before, value_after = progress_bar.change_progress_bar_value()
        assert value_before != value_after
