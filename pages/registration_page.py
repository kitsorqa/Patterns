from base.base_page import BasePage


class RegistrationPage(BasePage):
    _PAGE_URL = 'https://demo.opensource-socialnetwork.org/'
    _FIRST_NAME = ("xpath", "//input[@name='firstname']")
    _LAST_NAME = ("xpath", "//input[@name='lastname']")
    _EMAIL_NAME = ("xpath", "//input[@name='email']")
    _RE_EMAIL_NAME = ("xpath", "//input[@name='email_re']")
    _USERNAME = ("xpath", '//input[@name="username"]')
    _PASSWORD = ("xpath", '//input[@name="password"]')
    _BIRTHDAY = ("xpath", '//input[@name="birthdate"]')
    _DATEPICKER_YEAR = ("xpath", '//select[@class="ui-datepicker-year"]')
    _DATEPICKER_MONTH = ("xpath", '//select[@class="ui-datepicker-month"]')
    _MALE_GENDER = ("xpath", '//input[@value="male"]')
    _FEMALE_GENDER = ("xpath", '//input[@value="female"]')
    _TERMS_AND_CONDITION = ("xpath", '//input[@name="gdpr_agree"]')
    _CREATE_ACCOUNT = ("xpath", ' //input[@id="ossn-submit-button"]')
    _SUCCESSFUL_REGISTRATION = ("xpath", "//div[contains(text(), 'Your account has been registered!')]")

    def type_first_name(self, _FIRST_NAME):
        self.driver.find_element(*self._FIRST_NAME).send_keys(_FIRST_NAME)

    def type_last_name(self, _LAST_NAME):
        self.driver.find_element(*self._LAST_NAME).send_keys(_LAST_NAME)

    def type_email_name(self, email):
        self.driver.find_element(*self._EMAIL_NAME).send_keys(email)

    def type_re_email_name(self, re_email):
        self.driver.find_element(*self._RE_EMAIL_NAME).send_keys(re_email)

    def type_username(self, _USERNAME):
        self.driver.find_element(*self._USERNAME).send_keys(_USERNAME)

    def type_password(self, _PASSWORD):
        self.driver.find_element(*self._PASSWORD).send_keys(_PASSWORD)

    def choose_male_gender(self):
        self.driver.find_element(*self._MALE_GENDER).click()

    def choose_female_gender(self):
        self.driver.find_element(*self._FEMALE_GENDER).click()

    def agree_terms(self):
        self.driver.find_element(*self._TERMS_AND_CONDITION).click()

    def click_create_account_button(self):
        self.driver.find_element(*self._CREATE_ACCOUNT).click()

    def open_birthday_modal(self):
        self.driver.find_element(*self._BIRTHDAY).click()
        self.driver.find_element(*self._BIRTHDAY).send_keys("04/08/2010")

    def choose_birth_year(self, year):
        self.driver.find_element(*self._DATEPICKER_YEAR).send_keys(year)

    def choose_birth_month(self, month):
        self.driver.find_element(*self._DATEPICKER_MONTH).send_keys(month)

    def choose_birth_day(self, day):
        self.driver.find_element(*("xpath", f'//a[@data-date="{day}"]')).send_keys(day)
        self.driver.find_element(*("xpath", f'//a[@data-date="{day}"]')).click()

    def check_text_of_successful_registration(self):
        self.driver.find_element(*self._SUCCESSFUL_REGISTRATION).is_displayed()