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
    parser.addoption("--run_by",
                     action="store",
                     default="saucelabs",
                     help="run by saucelabs or local")
    parser.addoption("--browser_version",
                     action="store",
                     default="dev",
                     help="browser version that you want to test")
    parser.addoption("--platform",
                     action="store",
                     default="macOS 10.13",
                     help="Operation system that you want to test")

@pytest.fixture
def driver(request):
    config.base_url = request.config.getoption("--baseurl")
    config.browser = request.config.getoption("--browser").lower()
    config.run_by = request.config.getoption("--run_by").lower()
    config.browser_version = request.config.getoption("--browser_version").lower()
    config.platform = request.config.getoption("--platform").lower()
    if config.run_by == 'saucelabs':
        _desired_caps = {}
        _desired_caps['browserName'] = config.browser
        _desired_caps['version'] = config.browser_version
        _desired_caps['platform'] = config.platform
        _desired_caps["name"] = request.cls.__name__ + "." + request.function.__name__
        _credentials = os.environ["SAUCE_USERNAME"] + ":" + os.environ["SAUCE_ACCESS_KEY"]
        _url = "http://" + _credentials + "@ondemand.saucelabs.com:80/wd/hub"
        driver_ = webdriver.Remote(_url, _desired_caps)
    elif config.run_by == 'localhost':
        if config.browser == 'firefox':
            _geckodriver = os.path.join(os.getcwd(), 'drivers', 'geckodriver') 
            driver_ = webdriver.Firefox(executable_path=_geckodriver)
        elif config.browser == 'chrome':
            _chromedriver = os.path.join(os.getcwd(), 'drivers', 'chromedriver') 
            driver_ = webdriver.Chrome(executable_path=_chromedriver)

    def quit(): 
        try:
            if config.run_by == "saucelabs":
                if request.node.result_call.failed:
                    driver_.execute_script("sauce:job-result=failed")
                    print("http://saucelabs.com/beta/tests/" + driver_.session_id)
                elif request.node.result_call.passed:
                    driver_.execute_script("sauce:job-result=passed")
        finally:
            driver_.quit()

    request.addfinalizer(quit) 
    return driver_


@pytest.hookimpl(tryfirst=True, hookwrapper=True) 
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    setattr(item, "result_" + result.when, result)






