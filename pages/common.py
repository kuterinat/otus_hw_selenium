from pages.base import BasePage
from locators import *


class CommonPage(BasePage):

    def choose_currency_elem(self, elem):
        self.click((By.CSS_SELECTOR, f"#form-currency button[name='{elem}']"))

    def get_current_currency(self):
        return self.get_elem_text(MAIN_TOP_CURRENCY)

    def switch_currency(self, elem):
        self.click(MAIN_TOP_CURRENCY)
        self.choose_currency_elem(elem)

    def get_cart_total_value(self):
        return self.get_elem_text(CART_TOTAL)

    def check_common_elements(self):
        for elem in MAIN_TOP, MAIN_TOP_CURRENCY, PRODUCT_MENU, SEARCH_INPUT, \
                    SEARCH_BTN, CART_BTN, CART_TOTAL, FOOTER, CONTENT:
            self.assert_element(elem)
