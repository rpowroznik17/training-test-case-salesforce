from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.sales_page import SalesPage


def test_login(browser, test_data):
    # Pages
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    sales_page = SalesPage(browser)

    # Given Salesforce Login page is opened
    login_page.load()

    assert "Login" in login_page.get_title()

    # When user enters username and password
    login_page.fill_credentials(test_data["username"], test_data["password"])

    # And clicks Log In button
    login_page.log_in()

    # Then setup home page is opened
    WebDriverWait(home_page.get_driver(), 10).until(EC.title_contains("Home"))
    assert "Home" in home_page.get_title()

    home_page.navigate_to_sales()

    sales_page.navigate_to_accounts()