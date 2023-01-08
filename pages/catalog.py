from pages.common import CommonPage
from selenium.webdriver.common.by import By
from locators import SORT_TYPE, SHOW_LIMIT, LIST_VIEW_BTN, GRID_VIEW_BTN, LIST_PRODUCTS, GRID_PRODUCTS, \
    BREADCRUMB, CATEGORY_TITLE, LEFT_PANEL


class CatalogPage(CommonPage):

    def currency_elem(self, elem):
        elem_locator = (By.CSS_SELECTOR, f"#form-currency button[name='{elem}']")
        return self.element(elem_locator)

    def choose_sort_elem(self, elem):
        self.currency_elem(elem).click()

    def switch_sort(self, elem):
        self.click(SORT_TYPE)
        self.choose_sort_elem(elem)

    def check_catalog_page_elements(self):
        for elem in BREADCRUMB, CATEGORY_TITLE, LEFT_PANEL, SORT_TYPE, SHOW_LIMIT, LIST_VIEW_BTN, \
                    GRID_VIEW_BTN, GRID_PRODUCTS:
            self.assert_element(elem)
