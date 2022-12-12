from pages.common import CommonPage
from locators import SORT_TYPE, SHOW_LIMIT, LIST_VIEW_BTN, GRID_VIEW_BTN, LIST_PRODUCTS, GRID_PRODUCTS, \
    BREADCRUMB, CATEGORY_TITLE, LEFT_PANEL


class CatalogPage(CommonPage):

    def __init__(self, app):
        super().__init__(app)

    @property
    def sort_by_selector(self):
        return self.driver.find_element(*SORT_TYPE)

    @property
    def get_current_sort_by(self):
        return self.sort_by_selector.text

    def choose_sort_elem(self, elem):
        self.currency_elem(elem).click()

    def switch_sort(self, elem):
        self.sort_by_selector.click()
        self.choose_sort_elem(elem)

    @property
    def show_limit_selector(self):
        return self.driver.find_element(*SHOW_LIMIT)

    def choose_list_view(self):
        self.driver.find_element(*LIST_VIEW_BTN).click()

    def choose_grid_view(self):
        self.driver.find_element(*GRID_VIEW_BTN).click()

    @property
    def get_list_products(self):
        return self.driver.find_elements(*LIST_PRODUCTS)

    @property
    def get_grid_products(self):
        return self.driver.find_elements(*GRID_PRODUCTS)

    def check_catalog_page_elements(self):
        for elem in BREADCRUMB, CATEGORY_TITLE, LEFT_PANEL, SORT_TYPE, SHOW_LIMIT, LIST_VIEW_BTN, \
                    GRID_VIEW_BTN, GRID_PRODUCTS:
            self.assert_element(elem)
