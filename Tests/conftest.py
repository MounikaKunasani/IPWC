import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser")
    if browser == "chrome":
        driver = webdriver.Chrome("/Users/mounikakunasani/Downloads/Selenium Python/chromedriver")
        website = "https://rahulshettyacademy.com/angularpractice/"
        driver.get(website)
        driver.implicitly_wait(5)
        driver.maximize_window()
        request.cls.driver = driver
        yield
        driver.close()
    else:
        return print("Intended driver is not specified")