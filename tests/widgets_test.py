import time

from Pages.widgets_page import AccordianPage, AutoCompletePage


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
