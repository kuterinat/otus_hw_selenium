from pages.catalog import CatalogPage
from pages.admin_auth import AdminAuthPage
from pages.main import MainPage
from pages.product_card import ProductCardPage
from pages.user_registration import UserRegistrationPage


class App:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.implicitly_wait(3)
        self.base_url = base_url

        self.main_page = None
        self.catalog_page = None
        self.product_card_page = None
        self.admin_login_page = None
        self.user_registration_page = None

    def open_main_page(self):
        self.driver.get(self.base_url)
        if self.main_page is None:
            self.main_page = MainPage(self)
        return self.main_page

    def open_catalog_page(self, category_id=20):
        self.driver.get(self.base_url + f"/index.php?route=product/category&path={category_id}")
        if self.catalog_page is None:
            self.catalog_page = CatalogPage(self)
            self.catalog_page.category_id = category_id
        return self.catalog_page

    def open_product_card_page(self, product_id=43):
        self.driver.get(self.base_url + f"/index.php?route=product/product&product_id={product_id}")
        if self.product_card_page is None:
            self.product_card_page = ProductCardPage(self)
            self.product_card_page.product_id = product_id
        return self.product_card_page

    def open_admin_auth_page(self):
        self.driver.get(self.base_url + "/admin/")
        if self.admin_login_page is None:
            self.admin_login_page = AdminAuthPage(self)
        return self.admin_login_page

    def open_user_registration_page(self):
        self.driver.get(self.base_url + "/index.php?route=account/register")
        if not self.user_registration_page:
            self.user_registration_page = UserRegistrationPage(self)
        return self.user_registration_page
