import allure

from base.base_page import BasePage


class LoginPage(BasePage):
    _PAGE_URL = "https://demo.opensource-socialnetwork.org/login"
    _USERNAME_FIELD = ("xpath", "//input[@name='username']")
    _PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    _LOGIN_BUTTON = ("xpath", "//input[@value='Login']")
    _RESET_PASSWORD = ("xpath", "//a[text()='Reset Password ']")

    def enter_login(self, login):
        with allure.step(f"Ввод логина: {login}"):
            self.driver.find_element(*self._USERNAME_FIELD).clear()
            self.enter_text(self._USERNAME_FIELD, login)

    def enter_password(self, password):
        with allure.step(f"Ввод пароля: {password}"):
            self.driver.find_element(*self._PASSWORD_FIELD).clear()
            self.enter_text(self._PASSWORD_FIELD, password)

    @allure.step("Клик на кнопку логина")
    def click_login_button(self):
        self.click_element(self._LOGIN_BUTTON)
