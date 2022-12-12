
def test_admin_auth_page_elements(browser):
    admin_auth_page = browser.open_admin_auth_page()
    admin_auth_page.check_admin_auth_page_elements()
