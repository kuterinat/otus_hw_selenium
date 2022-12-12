from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

MAIN_URL = ''
CATALOG_URL = "/index.php?route=product/category&path=20"
PRODUCT_URL = "/index.php?route=product/product&product_id=40"
ADMIN_LOGIN_URL = "/admin/"
USER_REGISTRATION_URL = "/index.php?route=account/register"


def assert_element(app, locator, timeout=1):
    try:
        return WebDriverWait(app, timeout).until(EC.visibility_of_element_located(locator))
    except TimeoutException:
        raise AssertionError(f"Элемент не найден: {locator}")


def get_elem_text(app, locator, timeout=1):
    return assert_element(app, locator, timeout).text
