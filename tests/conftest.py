import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


DEFAULT_BROWSER_ADDRESS = "selenoid.autotests.cloud"


def pytest_addoption(parser):
    parser.addoption(
        "--browser_address"
    )

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope="function")
def browser_driver(request):
    browser_address = request.config.getoption('--browser_address')
    browser_address = browser_address if browser_address is not None else DEFAULT_BROWSER_ADDRESS
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    options = Options()

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "126.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.page_load_strategy = "eager"
    options.capabilities.update(capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{browser_address}/wd/hub",
        options=options
    )

    browser.config.driver = driver

    yield
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    browser.quit()
