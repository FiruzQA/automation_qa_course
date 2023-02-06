import time

from Pages.alerts_frame_window_page import BrowserWindowsPage


class TestAlertsFrameWindow:
    class TestBrowserWindows:

        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == 'This is a sample page'

        def test_new_window(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            text_result = new_tab_page.check_opened_window()
            assert text_result == 'This is a sample page'
