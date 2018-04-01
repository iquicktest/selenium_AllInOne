from selenium.common.exceptions import NoSuchElementException, TimeoutException 
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests import config

class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def _goto(self, url): 
        self.driver.get(config.base_url + url)

    def _find(self, locator):
        return self.driver.find_element(*locator)

    def _click(self, locator): 
        self._find(locator).click()

    def _input(self, locator, input_text): 
        self._find(locator).send_keys(input_text)

    def _is_displayed(self, locator):
        try:
            self._find(locator).is_displayed() 
        except NoSuchElementException:
            return False 
        return True

    def _wait_until_displayed(self, locator, timeout): 
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                expected_conditions.visibility_of_element_located(*locator))
        except TimeoutException: 
            return False
        return True

