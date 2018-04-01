import pytest
import os
from selenium import webdriver
from tests import config

def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action="store",
                     default="http://newtours.demoaut.com",
                     help="base URL for the application under test")
    parser.addoption("--browser",
                     action="store",
                     default="firefox",
                     help="the browser name that you want to test")

@pytest.fixture
def driver(request):
    config.base_url = request.config.getoption("--baseurl")
    config.browser = request.config.getoption("--browser").lower()
    if config.browser == 'firefox':
        _geckodriver = os.path.join(os.getcwd(), 'drivers', 'geckodriver') 
        driver_ = webdriver.Firefox(executable_path=_geckodriver)
    elif config.browser == 'chrome':
        _chromedriver = os.path.join(os.getcwd(), 'drivers', 'chromedriver') 
        driver_ = webdriver.Chrome(executable_path=_chromedriver)

    def quit(): 
        driver_.quit()

    request.addfinalizer(quit) 
    return driver_
