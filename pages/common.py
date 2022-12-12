from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *


class CommonPage:

    def __init__(self, app):
        self.driver = app.driver
        self.wait = WebDriverWait(self.driver, 10)

    @property
    def main_top(self):
        return self.driver.find_element(*MAIN_TOP)

    @property
    def product_menu(self):
        return self.driver.find_element(*PRODUCT_MENU)

    @property
    def cart_btn(self):
        return self.driver.find_element(*CART_BTN)

    @property
    def cart_total(self):
        return self.driver.find_element(*CART_TOTAL)

    @property
    def search_input(self):
        return self.driver.find_element(*SEARCH_INPUT)

    @property
    def search_btn(self):
        return self.driver.find_element(*SEARCH_BTN)

    @property
    def currency_selector(self):
        return self.main_top.find_element(*MAIN_TOP_CURRENCY)

    def currency_elem(self, elem):
        return self.driver.find_element(By.CSS_SELECTOR, f"#form-currency button[name='{elem}']")

    def choose_currency_elem(self, elem):
        self.currency_elem(elem).click()

    def get_current_currency(self):
        return self.currency_selector.text

    def switch_currency(self, elem):
        self.currency_selector.click()
        self.choose_currency_elem(elem)

    def get_cart_total_value(self):
        return self.cart_total.text

    def assert_element(self, locator, special_timeout=None):
        if special_timeout:
            wait = WebDriverWait(self.driver, special_timeout)
        else:
            wait = self.wait

        try:
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Элемент не найден: {locator}")

    def get_elem_text(self, locator):
        return self.driver.find_element(*locator).text

    def type(self, locator, value):
        field = self.driver.find_element(*locator)
        current_value_in_field = field.get_attribute("value")
        if current_value_in_field != value:
            field.click()
            if current_value_in_field != '':
                field.clear()
            field.send_keys(value)
        return self

    def is_displayed(self, locator, context=None):
        if not context:
            context = self.driver
        try:
            return context.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

    def check_common_elements(self):
        for elem in MAIN_TOP, MAIN_TOP_CURRENCY, PRODUCT_MENU, SEARCH_INPUT, \
                    SEARCH_BTN, CART_BTN, CART_TOTAL, FOOTER, CONTENT:
            self.assert_element(elem)

    def fill_input(self, locator, text):
        return self.driver.find_element(*locator).send_keys(text)

    def click_btn(self, locator):
        return self.driver.find_element(*locator).click()
