from pages.template_page import TemplatePage
from selenium.webdriver.common.by import By


class SalesPage(TemplatePage):
    # Selectors
    ACCOUNTS = (By.XPATH, "//one-app-nav-bar-item-root[@data-id='Account']")

    def __init__(self, browser):
        super().__init__(browser)

    def navigate_to_accounts(self):
        accounts = self.browser.find_element(*self.ACCOUNTS)
        accounts.click()
