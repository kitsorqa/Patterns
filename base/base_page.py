from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 15, 1)

    def open(self):
        self.driver.get(self._PAGE_URL)

    def element(self, locator):
        return self.driver.find_element(*locator)

    def element_by_text(self, search_text):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, search_text)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def enter_text(self, locator, text):
        self.element(locator).send_keys(text)
