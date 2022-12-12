from pages.common import CommonPage
from locators import CONTENT, CONTINUE_BTN, RIGHT_COLUMN, ACCOUNT_BLOCK, REGISTER_TITLE, FIRSTNAME, \
    LASTNAME, EMAIL, PHONE, PASSWORD, CONFIRM_PASSWORD, NEWS_LETTER_YES, NEWS_LETTER_NO, PRIVACY_POLICY_CHB, \
    CONGRATULATIONS, NEW_CONTINUE_BTN

CREATED_TXT = 'Your Account Has Been Created!'


class UserRegistrationPage(CommonPage):

    def __init__(self, app):
        super().__init__(app)

    def check_user_registration_page_elements(self):
        for elem in CONTENT, CONTINUE_BTN, RIGHT_COLUMN, ACCOUNT_BLOCK:
            self.assert_element(elem)
        assert self.get_elem_text(REGISTER_TITLE) == 'Register Account'

    @property
    def content(self):
        return self.driver.find_element(*CONTENT)

    @property
    def newsletter_yes(self):
        return self.driver.find_element(*NEWS_LETTER_YES)

    @property
    def newsletter_no(self):
        return self.driver.find_element(*NEWS_LETTER_NO)

    def check_get_newsletter(self, get_letter=True):
        self.newsletter_yes.click() if get_letter else self.newsletter_no.click()

    @property
    def privacy_policy(self):
        return self.driver.find_element(*PRIVACY_POLICY_CHB)

    def change_privacy(self, privacy=True):
        if (not self.privacy_policy.is_selected() and privacy) or \
                (self.privacy_policy.is_selected() and not privacy):
            self.privacy_policy.click()

    @property
    def continue_btn(self):
        return self.driver.find_element(*CONTINUE_BTN)

    def save_user(self):
        self.continue_btn.click()

    @property
    def congratulations(self):
        return self.content.find_element(*CONGRATULATIONS)

    def add_user_info_to_form_and_save(self, user):
        self.fill_input(FIRSTNAME, user.get('firstname', 'some_first_name'))
        self.fill_input(LASTNAME, user.get('lastname', 'some_last_name'))
        self.fill_input(EMAIL, user.get('email', 'some_email@mail.ru'))
        self.fill_input(PHONE, user.get('phone', '123456789'))
        self.fill_input(PASSWORD, user.get('password', '!@#QWE123qwe'))
        self.fill_input(CONFIRM_PASSWORD, user.get('password', '!@#QWE123qwe'))
        self.check_get_newsletter(user.get('get_letter', True))
        self.change_privacy(user.get('privacy', True))
        self.click_btn(CONTINUE_BTN)

    def check_user_is_created(self):
        self.assert_element(CONGRATULATIONS)
        assert self.congratulations.text == CREATED_TXT
        self.assert_element(NEW_CONTINUE_BTN)
