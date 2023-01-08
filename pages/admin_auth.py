from pages.common import CommonPage
from locators import OPENCART_IMG, USERNAME_INPUT, PASSWORD_INPUT, LOGIN_BTN, FORGOTTEN_PASSWORD_LINK, \
    USERNAME_LBL, PASSWORD_LBL


class AdminAuthPage(CommonPage):

    def check_admin_auth_page_elements(self):
        for elem in OPENCART_IMG, USERNAME_INPUT, PASSWORD_INPUT, LOGIN_BTN, FORGOTTEN_PASSWORD_LINK:
            self.assert_element(elem)
        assert self.get_elem_text(USERNAME_LBL) == 'Username'
        assert self.get_elem_text(PASSWORD_LBL) == 'Password'

    def login(self, login, password):
        self.fill_input(USERNAME_INPUT, login)
        self.fill_input(PASSWORD_INPUT, password)
        self.click(LOGIN_BTN)
