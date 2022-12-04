import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

MAIN_URL = ''
CATALOG_URL = "/index.php?route=product/category&path=20"
PRODUCT_URL = "/index.php?route=product/product&product_id=40"
ADMIN_LOGIN_URL = "/admin/"
USER_REGISTRATION_URL = "/index.php?route=account/register"
# common elements
MAIN_TOP = (By.CSS_SELECTOR, "#top")
MAIN_TOP_CURRENCY = (By.CSS_SELECTOR, "#form-currency button[data-toggle='dropdown']")
SEARCH_INPUT = (By.CSS_SELECTOR, "#search input")
SEARCH_BTN = (By.CSS_SELECTOR, "#search button")
PRODUCT_MENU = (By.CSS_SELECTOR, "#menu")
CART_BTN = (By.CSS_SELECTOR, "#cart")
CART_TOTAL = (By.CSS_SELECTOR, "#cart-total")
FOOTER = (By.CSS_SELECTOR, "footer")
CONTENT = (By.CSS_SELECTOR, "div#content")
# main page
MAIN_SLIDER = (By.CSS_SELECTOR, "#slideshow0")
MAIN_CAROUSEL = (By.CSS_SELECTOR, "#carousel0")
PRODUCTS = (By.CSS_SELECTOR, "div.product-thumb")
# catalog page
BREADCRUMB = (By.CSS_SELECTOR, "ul.breadcrumb")
CATEGORY_TITLE = (By.CSS_SELECTOR, "#content h2")
LEFT_PANEL = (By.CSS_SELECTOR, "#column-left")
SORT_TYPE = (By.CSS_SELECTOR, "#input-sort")
SHOW_LIMIT = (By.CSS_SELECTOR, "#input-limit")
LIST_VIEW_BTN = (By.CSS_SELECTOR, "#list-view")
GRID_VIEW_BTN = (By.CSS_SELECTOR, "#grid-view")
LIST_PRODUCTS = (By.CSS_SELECTOR, "div.product-list")
GRID_PRODUCTS = (By.CSS_SELECTOR, "div.product-grid")
# product card page
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button#button-cart")
QUANTITY_INPUT = (By.CSS_SELECTOR, "input#input-quantity")
PRODUCT_IMGS = (By.CSS_SELECTOR, "ul.thumbnails img")
ACTIVE_TAB = (By.CSS_SELECTOR, "ul.nav-tabs li.active")
# admin login page
OPENCART_IMG = (By.CSS_SELECTOR, "img[alt='OpenCart']")
USERNAME_INPUT = (By.CSS_SELECTOR, "input#input-username")
PASSWORD_INPUT = (By.CSS_SELECTOR, "input#input-password")
USERNAME_LBL = (By.CSS_SELECTOR, "label[for='input-username']")
PASSWORD_LBL = (By.CSS_SELECTOR, "label[for='input-password']")
LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
FORGOTTEN_PASSWORD_LINK = (By.CSS_SELECTOR, "span.help-block a")
# user registration page
PRIVACY_POLICY_CHB = (By.CSS_SELECTOR, "input[name='agree']")
CONTINUE_BTN = (By.CSS_SELECTOR, "input[type='submit']")
RIGHT_COLUMN = (By.CSS_SELECTOR, "aside#column-right")
REGISTER_TITLE = (By.CSS_SELECTOR, "#content h1")
ACCOUNT_BLOCK = (By.CSS_SELECTOR, "fieldset#account")


def assert_element(app, locator, timeout=1):
    try:
        return WebDriverWait(app, timeout).until(EC.visibility_of_element_located(locator))
    except TimeoutException:
        raise AssertionError(f"Элемент не найден: {locator}")


def get_elem_text(app, locator, timeout=1):
    return assert_element(app, locator, timeout).text


@pytest.mark.parametrize("app", [MAIN_URL, CATALOG_URL, PRODUCT_URL, USER_REGISTRATION_URL], indirect=['app'])
def test_check_common_elements(app):
    for elem in MAIN_TOP, MAIN_TOP_CURRENCY, PRODUCT_MENU, SEARCH_INPUT, \
                SEARCH_BTN, CART_BTN, CART_TOTAL, FOOTER, CONTENT:
        assert_element(app, elem)


def test_check_main_page_elements(app):
    for elem in MAIN_SLIDER, MAIN_CAROUSEL, PRODUCTS:
        assert_element(app, elem)


@pytest.mark.parametrize("app", [CATALOG_URL], indirect=['app'])
def test_check_catalog_page_elements(app):
    for elem in BREADCRUMB, CATEGORY_TITLE, LEFT_PANEL, SORT_TYPE, SHOW_LIMIT, LIST_VIEW_BTN, \
                GRID_VIEW_BTN, GRID_PRODUCTS:
        assert_element(app, elem)


@pytest.mark.parametrize("app", [PRODUCT_URL], indirect=['app'])
def test_check_product_page_elements(app):
    for elem in ADD_TO_CART_BTN, QUANTITY_INPUT, PRODUCT_IMGS:
        assert_element(app, elem)
    assert get_elem_text(app, ACTIVE_TAB) == 'Description'


@pytest.mark.parametrize("app", [ADMIN_LOGIN_URL], indirect=['app'])
def test_check_admin_login_page_elements(app):
    for elem in OPENCART_IMG, USERNAME_INPUT, PASSWORD_INPUT, LOGIN_BTN, FORGOTTEN_PASSWORD_LINK:
        assert_element(app, elem)
    assert get_elem_text(app, USERNAME_LBL) == 'Username'
    assert get_elem_text(app, PASSWORD_LBL) == 'Password'


@pytest.mark.parametrize("app", [USER_REGISTRATION_URL], indirect=['app'])
def test_check_user_registration_page_elements(app):
    for elem in CONTENT, CONTINUE_BTN, RIGHT_COLUMN, ACCOUNT_BLOCK:
        assert_element(app, elem)
    assert get_elem_text(app, REGISTER_TITLE) == 'Register Account'
