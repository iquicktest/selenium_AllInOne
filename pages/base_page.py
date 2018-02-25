class BasePage():

    def __init__(self, driver):
            self.driver = driver

    def _goto(self, url): 
        self.driver.get(url)

    def _find(self, locator):
        return self.driver.find_element(*locator)

    def _click(self, locator): 
        self._find(locator).click()

    def _input(self, locator, input_text): 
        self._find(locator).send_keys(input_text)

    def _is_displayed(self, locator):
        return self._find(locator).is_displayed()
