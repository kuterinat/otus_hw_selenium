from pages.common import CommonPage
from locators import MAIN_SLIDER, MAIN_CAROUSEL, PRODUCTS


class MainPage(CommonPage):

    CURRENCIES = {'USD': '$', 'GBP': '£', 'EUR': '€'}

    def __init__(self, app):
        super().__init__(app)

    def check_main_page_elements(self):
        for elem in MAIN_SLIDER, MAIN_CAROUSEL, PRODUCTS:
            self.assert_element(elem)
