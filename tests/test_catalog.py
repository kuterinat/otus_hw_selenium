
def test_catalog_page_elements(browser):
    catalog_page = browser.open_catalog_page()
    catalog_page.check_common_elements()
    catalog_page.check_catalog_page_elements()


