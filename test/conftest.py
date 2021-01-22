from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"

    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:/Drivers/New folder/chromedriver_win32 (2)/chromedriver.exe")
    elif browser_name == "firfox":
        print("firfox")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
