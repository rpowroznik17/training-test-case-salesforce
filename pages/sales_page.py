from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class SalesPage:
    # Selectors
    ACCOUNTS = (By.XPATH, "//one-app-nav-bar-item-root[@data-id='Account']")

    def __init__(self, browser):
        self.browser = browser

    def navigate_to_accounts(self):
        accounts = self.browser.find_element(*self.ACCOUNTS)
        accounts.click()
