from pages.common import CommonPage
from locators import CATALOG_MENU_ITEM, PRODUCTS_MENU_ITEM


class AdminMainPage(CommonPage):

    def __init__(self, app):
        super().__init__(app)

    def open_admin_products_page(self):
        self.click(CATALOG_MENU_ITEM)
        self.click(PRODUCTS_MENU_ITEM)
