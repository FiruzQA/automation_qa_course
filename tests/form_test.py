import time

import allure

from Pages.form_page import FormPage

@allure.suite("Form")
class TestForm:
    @allure.feature("Form Page")
    class TestFormPage:
        @allure.title("check form page")
        def test_form(self, driver):
            form_page = FormPage(driver, "https://demoqa.com/automation-practice-form")
            form_page.open()
            p = form_page.fill_form_fields()
            result = form_page.form_result()
            print(p.firstname, p.lastname, p.email)
            print(result[0], result[1])
            assert [p.firstname + " " + p.lastname, p.email] == [result[0], result[1]], "The form has not been filled"

