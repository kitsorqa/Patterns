from base.base_test import BaseTest
import allure


@allure.epic("Users")
@allure.feature("Trial Accounts")
@allure.story("New accounts")
class TestRegistrationPage(BaseTest):
    def test_successful_registration(self):
        self.setup_method()
        self.registration_page.open()
        self.registration_page.type_first_name("boba")
        self.registration_page.type_last_name("biba")
        self.registration_page.type_email_name("biba@boba.it")
        self.registration_page.type_re_email_name("biba@boba.it")
        self.registration_page.type_username("boba")
        self.registration_page.type_password("qwerty12345")
        self.registration_page.open_birthday_modal()
        self.registration_page.choose_birth_year('2000')
        self.registration_page.choose_birth_month('May')
        self.registration_page.choose_birth_day(15)
        self.registration_page.choose_male_gender()
        self.registration_page.agree_terms()
        self.registration_page.click_create_account_button()
