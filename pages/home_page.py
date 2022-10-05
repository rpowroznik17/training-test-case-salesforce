from selenium.webdriver.common.by import By
from time import sleep


class HomePage:

    # Selectors
    APP_LAUNCHER = (By.XPATH, "//div[contains(@class, 'appLauncher')]/button")
    # SALES = (By.XPATH, "//a[@data-label='Sales']")
    SALES = (By.XPATH, "//a//span//p[. = 'Sales']")
    SEARCH = (By.XPATH, "//input[@placeholder='Search apps and items...']")

    def __init__(self, browser):
        self.browser = browser

    def get_title(self):
        return self.browser.title

    def get_driver(self):
        return self.browser

    def navigate_to_sales(self):
        app_launcher = self.browser.find_element(*self.APP_LAUNCHER)
        app_launcher.click()

        search = self.browser.find_element(*self.SEARCH)
        search.send_keys("sales")

        sales = self.browser.find_element(*self.SALES)
        sales.click()
