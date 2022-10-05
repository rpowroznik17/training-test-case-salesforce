from selenium.webdriver.common.by import By


class LoginPage:

    # URL
    URL = "https://login.salesforce.com"

    # Selectors
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "Login")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def get_title(self):
        return self.browser.title

    def fill_credentials(self, username, password):
        username_field = self.browser.find_element(*self.USERNAME)
        username_field.send_keys(username)

        password_field = self.browser.find_element(*self.PASSWORD)
        password_field.send_keys(password)

    def log_in(self):
        login_btn = self.browser.find_element(*self.LOGIN_BTN)
        login_btn.click()

