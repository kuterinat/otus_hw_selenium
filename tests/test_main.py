from locators import *


def test_main_page_elements(browser):
    main_page = browser.open_main_page()
    main_page.check_common_elements()
    main_page.check_main_page_elements()


def test_main_cart_total(browser):
    main_page = browser.open_main_page()

    main_page.assert_element(CART_BTN)
    main_page.assert_element(CART_TOTAL)
    cur_sign = main_page.get_current_currency()[0]
    assert main_page.get_cart_total_value() == f"0 item(s) - {cur_sign}0.00"


def test_main_change_currency(browser):
    main_page = browser.open_main_page()

    main_page.assert_element(MAIN_TOP_CURRENCY)
    assert main_page.get_current_currency() == f"{main_page.CURRENCIES['USD']} Currency "
    assert main_page.get_cart_total_value() == f"0 item(s) - {main_page.CURRENCIES['USD']}0.00"
    main_page.switch_currency('GBP')
    assert main_page.get_current_currency() == f"{main_page.CURRENCIES['GBP']} Currency "
    assert main_page.get_cart_total_value() == f"0 item(s) - {main_page.CURRENCIES['GBP']}0.00"
    main_page.switch_currency('EUR')
    assert main_page.get_current_currency() == f"{main_page.CURRENCIES['EUR']} Currency "
    assert main_page.get_cart_total_value() == f"0 item(s) - 0.00{main_page.CURRENCIES['EUR']}"
    main_page.switch_currency('USD')
    assert main_page.get_current_currency() == f"{main_page.CURRENCIES['USD']} Currency "
    assert main_page.get_cart_total_value() == f"0 item(s) - {main_page.CURRENCIES['USD']}0.00"