from time import sleep


def test_login(browser, test_data, pages):
    pages["login_page"].load()

    assert "Login" in pages["login_page"].get_title(), "Page title should contain 'Login'"

    pages["login_page"].fill_credentials(test_data["username"], test_data["password"])

    pages["login_page"].log_in()

    pages["home_page"].wait_for_title_to_load("Home")

    assert "Home" in pages["home_page"].get_title()

    pages["home_page"].navigate_to_sales()

    pages["sales_page"].navigate_to_accounts()

    pages["accounts_page"].wait_for_title_to_load("Accounts")

    assert "Accounts" in pages["accounts_page"].get_title(), "Page title should contain 'Accounts'"

    pages["accounts_page"].click_list_view()

    pages["accounts_page"].click_all_accounts_view()

    pages["accounts_page"].wait_for_title_to_load("All Accounts")

    assert "All Accounts" in pages["accounts_page"].get_title(), "Page title should contain 'All accounts'"

    pages["accounts_page"].select_account(0)