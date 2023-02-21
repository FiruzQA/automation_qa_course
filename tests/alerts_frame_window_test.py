import time

import allure

from Pages.alerts_frame_window_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage

@allure.suite("Alerts, Frame & Windows")
class TestAlertsFrameWindow:
    @allure.feature("Browser Windows")
    class TestBrowserWindows:

        @allure.title("checking the opening of new tab")
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == 'This is a sample page'

        @allure.title("checking opening of a new window")
        def test_new_window(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            text_result = new_tab_page.check_opened_window()
            assert text_result == 'This is a sample page'

    @allure.feature("Alerts Page")
    class TestAlertPage:

        @allure.title("Checking the opening of an alert")
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button'

        @allure.title("Checking the opening of the alert after 5 seconds")
        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds'

        @allure.title("Checking the opening of the alert with confirm")
        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == 'You selected Ok'

        @allure.title("Checking the opening of the alert with prompt")
        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            print(text)
            print(alert_text)
            assert alert_text == f'You entered {text}', 'or text in alert_text'

    @allure.feature("Frame Page")
    class TestFramesPage:

        @allure.title("Check the page with frames")
        def test_frames(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame_1 = frame_page.check_frame('frame1')
            result_frame_2 = frame_page.check_frame('frame2')
            assert result_frame_1 == ['This is a sample page', '500px', '350px'], 'frame does not exist'
            assert result_frame_2 == ['This is a sample page', '100px', '100px'], 'frame does not exist'

    @allure.feature("Nested Page")
    class TestNestedFrames:

        @allure.title("Check the page with nested frames")
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == 'Parent frame'
            assert child_text == 'Child Iframe'

    @allure.feature("Modal Dialog Page")
    class TestModalDialogs:
        @allure.title("Check the page with modal dialogs")
        def test_modal_dialogs(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_dialog_page.open()
            small, large = modal_dialog_page.check_model_dialogs()
            assert small[1] < large[1]
            assert small[0] == 'Small Modal'
            assert large[0] == 'Large Modal'
