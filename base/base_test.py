from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage


class BaseTest:
    def setup_method(self):
        self.registration_page = RegistrationPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)