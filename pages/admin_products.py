from pages.common import CommonPage
from locators import ADD_BTN, DELETE_BTN, PRODUCT_NAME, PRODUCT_TAG, PRODUCT_META_TAG_TITLE, PRODUCT_MODEL,\
    PRODUCT_META_TAG_KEYWORDS, PRODUCT_META_TAG_DESCRIPTION, PRODUCT_PRICE, SAVE_PRODUCT_BTN, \
    PRODUCT_ROW_IN_PRODUCTS_TABLE, CHECKBOX_IN_PRODUCT_ROW, ADD_PANEL_TITLE
from selenium.webdriver.common.by import By


class AdminProductsPage(CommonPage):

    def __init__(self, app):
        super().__init__(app)

    def get_products_rows(self):
        return self.driver.find_elements(*PRODUCT_ROW_IN_PRODUCTS_TABLE)

    def mark_product_checked(self, product_row):
        product_row.find_element(*CHECKBOX_IN_PRODUCT_ROW).click()

    def confirm_product_delete(self):
        self.driver.switch_to.alert.accept()

    def switch_to_tab(self, tab_name):
        tab_locator = (By.CSS_SELECTOR, f'a[href="#tab-{tab_name}"]')
        self.driver.find_element(*tab_locator).click()

    def open_add_product_form(self):
        self.click_btn(ADD_BTN)
        assert self.is_displayed(ADD_PANEL_TITLE)
        assert self.get_elem_text(ADD_PANEL_TITLE) == 'Add Product'

    def add_product_info_to_form_and_save(self, product):
        self.fill_input(PRODUCT_NAME, product.get('name', 'some_product_name'))
        self.fill_input(PRODUCT_META_TAG_TITLE, product.get('meta_tag_title', 'some_tag_title'))
        self.fill_input(PRODUCT_META_TAG_DESCRIPTION, product.get('meta_tag_description', 'some_tag_description'))
        self.fill_input(PRODUCT_META_TAG_KEYWORDS, product.get('meta_tag_keywords', 'some_tag_keywords'))
        self.fill_input(PRODUCT_TAG, product.get('product_tags', 'some_product_tags'))
        self.switch_to_tab('data')
        self.fill_input(PRODUCT_MODEL, product.get('model', 'some_product_model'))
        self.fill_input(PRODUCT_PRICE, product.get('price', '111'))
        self.click_btn(SAVE_PRODUCT_BTN)

    def is_product_in_list(self, product_name):
        product_locator = (By.XPATH, f"//td[.='{product_name}']")
        return self.is_displayed(product_locator)

    def delete_last_product(self):
        self.mark_product_checked(self.get_products_rows()[-1])
        self.click_btn(DELETE_BTN)
        self.confirm_product_delete()
