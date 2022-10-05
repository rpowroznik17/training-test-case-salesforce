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
        # WebDriverWait(self.browser, 10).until(EC.visibility_of_all_elements_located(self.ACCOUNTS))
        # self.browser.execute_script("document.querySelector('a[href='/lightning/o/Account/home'] > span').click()")
        # accounts = self.browser.find_element(*self.ACCOUNTS)
        # accounts.click()
        sleep(7)
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(self.ACCOUNTS)).click()
