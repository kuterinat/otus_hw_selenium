from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, app):
        self.driver = app.driver
        self.wait = WebDriverWait(self.driver, 10)

    def element(self, locator):
        return self.driver.find_element(*locator)

    def elements(self, locator):
        return self.driver.find_elements(*locator)

    def assert_element(self, locator, special_timeout=None):
        if special_timeout:
            wait = WebDriverWait(self.driver, special_timeout)
        else:
            wait = self.wait

        try:
            wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Элемент не найден: {locator}")

    def get_elem_text(self, locator):
        return self.driver.find_element(*locator).text

    def fill_input(self, locator, value):
        field = self.driver.find_element(*locator)
        current_value_in_field = field.get_attribute("value")
        if current_value_in_field != value:
            field.click()
            if current_value_in_field != '':
                field.clear()
            field.send_keys(value)

    def is_displayed(self, locator, context=None):
        if not context:
            context = self.driver
        try:
            return context.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
