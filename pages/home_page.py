from pages.template_page import TemplatePage
from selenium.webdriver.common.by import By


class HomePage(TemplatePage):

    # Selectors
    APP_LAUNCHER = (By.XPATH, "//div[contains(@class, 'appLauncher')]/button")
    SALES = (By.XPATH, "//a//span//p[. = 'Sales']")
    SEARCH = (By.XPATH, "//input[@placeholder='Search apps and items...']")

    def __init__(self, browser):
        super().__init__(browser)

    def navigate_to_sales(self):
        app_launcher = self.browser.find_element(*self.APP_LAUNCHER)
        app_launcher.click()

        search = self.browser.find_element(*self.SEARCH)
        search.send_keys("sales")

        sales = self.browser.find_element(*self.SALES)
        sales.click()
