import pytest
from selenium import webdriver
from utils.attach import add_screenshot, add_html, add_logs


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver

    yield

    add_screenshot(driver)
    add_logs(driver)
    add_html(driver)
    driver.quit()
