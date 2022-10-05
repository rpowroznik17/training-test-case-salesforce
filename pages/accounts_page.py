from pages.template_page import TemplatePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountsPage(TemplatePage):

    # Selectors
    LIST_VIEW = (By.CSS_SELECTOR, "div[data-aura-class='forceListViewPicker']")
    ALL_ACCOUNTS_VIEW = (By.XPATH, "//span[text()='All Accounts']")
    ACCOUNTS = (By.XPATH, "//a[@data-refid='recordId' and string(@title)]")

    def __init__(self, browser):
        super().__init__(browser)

    def click_list_view(self):
        list_view = self.browser.find_element(*self.LIST_VIEW)
        list_view.click()

    def click_all_accounts_view(self):
        all_accounts_view = self.browser.find_element(*self.ALL_ACCOUNTS_VIEW)
        all_accounts_view.click()

    def select_account(self, index):
        accounts = self.browser.find_elements(*self.ACCOUNTS)
        accounts[index].click()