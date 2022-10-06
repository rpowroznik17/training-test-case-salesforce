from pages.template_page import TemplatePage
from selenium.webdriver.common.by import By


class AccountPage(TemplatePage):

    # Selectors
    EDIT_BTN = (By.XPATH, "//button[@name='Edit']")

    def __init__(self, browser):
        super().__init__(browser)

    def click_edit_button(self):
        edit_btn = self.browser.find_element(*self.EDIT_BTN)
        edit_btn.click()