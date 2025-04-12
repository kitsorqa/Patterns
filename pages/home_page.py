import allure

from base.base_page import BasePage


class HomePage(BasePage):
    _PAGE_URL = 'https://demo.opensource-socialnetwork.org/home'
    _POST_TEXT = ("xpath", "//textarea[@name='post']")
    _CREATE_POST = ("xpath", "//input[@value='Post']")
    _LAST_POST = ("xpath", "//div[contains(@class, 'ossn-wall-item')]")

    def create_post(self, text):
        with allure.step(f"Ввод {text} и создание тестового поста"):
            self.enter_text(self._POST_TEXT, text)
            self.click_element(self._CREATE_POST)

    @allure.step("Проверка, что пост отображается на странице")
    def is_post_published(self):
        return self.element(self._LAST_POST).is_displayed()