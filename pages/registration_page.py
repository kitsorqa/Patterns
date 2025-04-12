import allure

from base.base_page import BasePage


class RegistrationPage(BasePage):
    _PAGE_URL = 'https://demo.opensource-socialnetwork.org/'
    _FIRST_NAME = "//input[@name='firstname']"
    _LAST_NAME = "//input[@name='lastname']"
    _EMAIL_NAME = "//input[@name='email']"
    _RE_EMAIL_NAME = "//input[@name='email_re']"
    _USERNAME = '//input[@name="username"]'
    _PASSWORD = '//input[@name="password"]'
    _BIRTHDAY = '//input[@name="birthdate"]'
    _DATEPICKER_YEAR = '//select[@class="ui-datepicker-year"]'
    _DATEPICKER_MONTH = '//select[@class="ui-datepicker-month"]'
    _MALE_GENDER = '//input[@value="male"]'
    _FEMALE_GENDER = '//input[@value="female"]'
    _TERMS_AND_CONDITION = '//input[@name="gdpr_agree"]'
    _CREATE_ACCOUNT = '//input[@id="ossn-submit-button"]'
    _SUCCESSFUL_REGISTRATION = "//div[contains(text(), 'Your account has been registered!')]"

    @allure.step("Ввод фамилии")
    def type_first_name(self, _FIRST_NAME):
        self.driver.find_element(*self._FIRST_NAME).send_keys(_FIRST_NAME)

    @allure.step("Ввод имени")
    def type_last_name(self, _LAST_NAME):
        self.driver.find_element(*self._LAST_NAME).send_keys(_LAST_NAME)

    @allure.step("Ввод эмейла")
    def type_email_name(self, email):
        self.driver.find_element(*self._EMAIL_NAME).send_keys(email)

    @allure.step("Ввод эмейла повторно")
    def type_re_email_name(self, re_email):
        self.driver.find_element(*self._RE_EMAIL_NAME).send_keys(re_email)

    @allure.step("Ввод логина")
    def type_username(self, _USERNAME):
        self.driver.find_element(*self._USERNAME).send_keys(_USERNAME)

    @allure.step("Ввод пароля")
    def type_password(self, _PASSWORD):
        self.driver.find_element(*self._PASSWORD).send_keys(_PASSWORD)

    @allure.step("Выбор мужского пола")
    def choose_male_gender(self):
        self.driver.find_element(*self._MALE_GENDER).click()

    @allure.step("Ввод женского пола")
    def choose_female_gender(self):
        self.driver.find_element(*self._FEMALE_GENDER).click()

    @allure.step("Подтверждение условий соглашения")
    def agree_terms(self):
        self.driver.find_element(*self._TERMS_AND_CONDITION).click()

    @allure.step("Клик по кнопке создания аккаунта")
    def click_create_account_button(self):
        self.driver.find_element(*self._CREATE_ACCOUNT).click()

    @allure.step("Отрытие модалки дня рождения и ввод даты рождения")
    def open_birthday_modal(self):
        self.driver.find_element(*self._BIRTHDAY).click()
        self.driver.find_element(*self._BIRTHDAY).send_keys("04/08/2010")

    @allure.step("Выбор года рождения")
    def choose_birth_year(self, year):
        self.driver.find_element(*self._DATEPICKER_YEAR).send_keys(year)

    @allure.step("Выбор месяца рождения")
    def choose_birth_month(self, month):
        self.driver.find_element(*self._DATEPICKER_MONTH).send_keys(month)

    @allure.step("Выбор дня рождения")
    def choose_birth_day(self, day):
        self.driver.find_element(*("xpath", f'//a[@data-date="{day}"]')).send_keys(day)
        self.driver.find_element(*("xpath", f'//a[@data-date="{day}"]')).click()

    @allure.step("Проверка алерта об успешной регистрации")
    def check_text_of_successful_registration(self):
        self.driver.find_element(*self._SUCCESSFUL_REGISTRATION).is_displayed()
