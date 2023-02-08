from selenium.webdriver.common.by import By
import random


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    TITLE_NEW = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")

class AlertsPageLocators:
    SEE_ALERTS_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    APPEAR_ALERT_AFTER_5_SEC_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    CONFIRM_RESULT = (By.CSS_SELECTOR, f"span[id='confirmResult']")
    PROMPT_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")
    PROMPT_RESULT = (By.CSS_SELECTOR, "span[id='promptResult']")

class FramesPageLocators:

    FIRST_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    SECOND_FRAME = (By.CSS_SELECTOR, "iframe[id='frame2']")
    TITLE_FRAME = (By.CSS_SELECTOR, "h1[id='sampleHeading']")

class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    PARENT_TEXT = (By.CSS_SELECTOR, "body")
    CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    CHILD_TEXT = (By.CSS_SELECTOR, "p")

class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='closeSmallModal']")
    BODY_SMALL_MODAL = (By.CSS_SELECTOR, "div[class='modal-body']")
    TITLE_SMALL_MODAL = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-sm']")

    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='showLargeModal']")
    BODY_LARGE_MODAL = (By.CSS_SELECTOR, "div[class='modal-body'] p")
    TITLE_LARGE_MODAL = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-lg']")
