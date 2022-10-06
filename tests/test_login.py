from time import sleep


def test_login(browser, test_data, pages):
    pages["login_page"].load()
    assert "Login" in pages["login_page"].validate_title("Login"), "Page title should contain 'Login'"

    pages["login_page"].fill_credentials(test_data["username"], test_data["password"])
    pages["login_page"].log_in()
    assert "Home" in pages["home_page"].validate_title("Home"), "Page title should contain 'Home'"

    pages["home_page"].navigate_to_sales()
    pages["sales_page"].navigate_to_accounts()
    assert "Accounts" in pages["accounts_page"].validate_title("Accounts"), "Page title should contain 'Accounts'"

    pages["accounts_page"].click_list_view()
    pages["accounts_page"].click_all_accounts_view()
    assert "All Accounts" in pages["accounts_page"].validate_title("All Accounts"), "Page title should contain 'All accounts'"

    pages["accounts_page"].select_account(0)
    pages["account_page"].click_edit_button()
    assert "Edit" in pages["account_page"].validate_title("Edit"), "Page title should contain 'Edit'"

    pages["edit_account_page"].expand_rating_picklist()
    pages["edit_account_page"].choose_option_warm()
    pages["edit_account_page"].change_phone_number("(244) 345-7002")
    pages["edit_account_page"].save_edit()
