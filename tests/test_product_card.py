
def test_product_card_elements(browser):
    product_card_page = browser.open_product_card_page()
    product_card_page.check_common_elements()
    product_card_page.check_product_page_elements()
