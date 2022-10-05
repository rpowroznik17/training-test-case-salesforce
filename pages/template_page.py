from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TemplatePage:

    def __init__(self, browser):
        self.browser = browser

    def get_title(self):
        return self.browser.title

    def wait_for_title_to_load(self, title):
        WebDriverWait(self.browser, 10).until(EC.title_contains(title))