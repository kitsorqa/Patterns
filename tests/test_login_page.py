from allure_commons._allure import step

from base.base_test import BaseTest
import allure
import pytest

@allure.epic("Users")
@allure.feature("Trial Accounts")
@allure.story("Test accounts")
class TestLoginPage(BaseTest):

    @allure.title("Авторизация в тестовый аккаунт")
    def test_login_and_post(self):
        self.setup_method()
        self.login_page.open()
        self.login_page.enter_login('administrator')
        self.login_page.enter_password('administrator')
        self.login_page.click_login_button()
        self.home_page.create_post('test')
        self.home_page.is_post_published()
