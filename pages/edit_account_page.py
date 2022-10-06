from pages.template_page import TemplatePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class EditAccountPage(TemplatePage):

    # Selectors
    RATING_PICKLIST = (By.XPATH, "//button[contains(@aria-label, 'Rating')]")
    RATING_WARM = (By.XPATH, "//span[@title='Warm']")
    # SEARCH_ACCOUNTS = (By.XPATH, "//input[@placeholder='Search Accounts...']")
    # SEARCH_RESULT = ()
    PHONE_INPUT = (By.XPATH, "//input[@name='Phone']")
    SAVE_EDIT_BTN = (By.XPATH, "//button[@name='SaveEdit']")

    def __init__(self, browser):
        super().__init__(browser)

    def expand_rating_picklist(self):
        rating_picklist = self.browser.find_element(*self.RATING_PICKLIST)
        rating_picklist.click()

    def choose_option_warm(self):
        rating_warm = self.browser.find_element(*self.RATING_WARM)
        rating_warm.click()

    def change_phone_number(self, phone_number):
        phone_input = self.browser.find_element(*self.PHONE_INPUT)

        # Clear existing text in input field
        phone_input.send_keys(Keys.CONTROL + "a")
        phone_input.send_keys(Keys.DELETE)

        # Provide new phone number
        phone_input.send_keys(phone_number)

    def save_edit(self):
        save_edit_btn = self.browser.find_element(*self.SAVE_EDIT_BTN)
        save_edit_btn.click()
