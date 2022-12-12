import pytest
from functions import *
from locators import *


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
