import json
from data import USER


def test_user_registration_elements(browser):
    user_registration_page = browser.open_user_registration_page()
    user_registration_page.check_common_elements()
    user_registration_page.check_user_registration_page_elements()


def test_new_user_registration(browser):
    with open(USER, "r") as f:
        user = json.loads(f.read())
    user_registration_page = browser.open_user_registration_page()
    user_registration_page.add_user_info_to_form_and_save(user)
    user_registration_page.check_user_is_created()
