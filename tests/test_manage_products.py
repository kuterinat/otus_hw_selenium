import json
from config.config import ADMIN
from data import PRODUCT
from pages.admin_main import AdminMainPage
from pages.admin_products import AdminProductsPage


def test_add_new_product(browser):
    with open(PRODUCT, "r") as f:
        product = json.loads(f.read())

    admin_auth_page = browser.open_admin_auth_page()
    admin_auth_page.login(ADMIN["login"], ADMIN["password"])
    AdminMainPage(browser).open_admin_products_page()

    admin_products_page = AdminProductsPage(browser)
    admin_products_page.open_add_product_form()
    admin_products_page.add_product_info_to_form_and_save(product)

    assert admin_products_page.is_product_in_list(product["name"])


def test_remove_product(browser):
    admin_auth_page = browser.open_admin_auth_page()
    admin_auth_page.login(ADMIN["login"], ADMIN["password"])
    AdminMainPage(browser).open_admin_products_page()

    admin_products_page = AdminProductsPage(browser)
    products_before = admin_products_page.get_products_rows()
    admin_products_page.delete_last_product()
    products_after = admin_products_page.get_products_rows()
    assert len(products_after) == len(products_before) - 1
