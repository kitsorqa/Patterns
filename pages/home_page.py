import time

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    _PAGE_URL = 'https://demo.opensource-socialnetwork.org/home'
    _POST_TEXT = ("xpath", "//textarea[@name='post']")
    _CREATE_POST = ("xpath", "//input[@value='Post']")
    _LAST_POST = ("xpath", "//div[contains(@class, 'ossn-wall-item')]")

    def create_post(self, text):
        self.enter_text(self._POST_TEXT, text)
        self.click_element(self._CREATE_POST)

    def is_post_published(self):
        return self.element(self._LAST_POST).is_displayed()