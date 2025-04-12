import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from metaclasses.meta_locators import MetaLocator


class BasePage(metaclass=MetaLocator):
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 15, 1)

    def open(self):
        with allure.step(f"Открытие страницы: {self._PAGE_URL}"):
            self.driver.get(self._PAGE_URL)

    def element(self, locator):
        with allure.step(f"Поиск элемента по локатору {locator}"):
            return self.driver.find_element(*locator)

    def click_element(self, locator):
        with allure.step(f"Клик по локатору {locator}"):
            self.driver.find_element(*locator).click()

    def enter_text(self, locator, text):
        with allure.step(f"Ввод переданного текста: {text} в локатор {locator}"):
            self.element(locator).send_keys(text)
