from pages.common import CommonPage
from locators import ADD_TO_CART_BTN, QUANTITY_INPUT, PRODUCT_IMGS, ACTIVE_TAB


class ProductCardPage(CommonPage):

    def check_product_page_elements(self):
        for elem in ADD_TO_CART_BTN, QUANTITY_INPUT, PRODUCT_IMGS:
            self.assert_element(elem)
        assert self.get_elem_text(ACTIVE_TAB) == 'Description'
