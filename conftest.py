import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome',  help='Specify browser, it is chrome by default')
    parser.addoption('--headless', action='store_true', help='Specify headless mode, it is false by default')
    parser.addoption("--driver_folder", default=os.path.expanduser("~/otus/otus_hw_selenium/drivers"),
                     help="Specify driver folder, it is '~/otus/otus_hw_selenium/drivers' by default")
    parser.addoption("--url", action="store", default="http://192.168.1.126:8081",
                     help="Specify opencard url, it is 'http://192.168.1.126:8081' by default")


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture
def browser(request):
    browsers = {'firefox': {'webdriver': webdriver.Firefox, 'driver': 'geckodriver', 'options': FirefoxOptions(),
                            'service': FirefoxService},
                'chrome': {'webdriver': webdriver.Chrome, 'driver': 'chromedriver', 'options': ChromeOptions(),
                           'service': ChromeService},
                'edge': {'webdriver': webdriver.Edge, 'driver': 'msedgedriver', 'options': EdgeOptions(),
                         'service': EdgeService},
                'yandex': {'webdriver': webdriver.Chrome, 'driver': 'yandexdriver', 'options': ChromeOptions(),
                           'service': ChromeService}
                }

    _browser = request.config.getoption('--browser').lower()
    driver_folder = request.config.getoption("--driver_folder")
    headless = request.config.getoption("--headless")
    if _browser == 'ff':
        _browser = 'firefox'
    elif _browser not in browsers:
        raise Exception(f"Browser '{_browser}' is not supported")
    browser_data = browsers[_browser]

    options = browser_data['options']
    options.headless = headless
    service = browser_data['service']
    driver = browser_data['webdriver'](service=service(f"{driver_folder}{os.sep}{browser_data['driver']}"),
                                       options=options)
    driver.maximize_window()

    yield driver

    driver.close()


@pytest.fixture
def app(browser, base_url, request):
    add_url = request.param if hasattr(request, 'param') else ''
    browser.get(base_url+add_url)
    return browser
