import pytest
from selenium import webdriver
from pages import flight_login_page
import os

class TestFlightLogin():

    @pytest.fixture
    def login(self, request):
        _gecko_driver = os.path.join(os.getcwd(), 'drivers', 'geckodriver') 
        driver_ = webdriver.Firefox(executable_path=_gecko_driver)

        def quit(): 
            driver_.quit()

        request.addfinalizer(quit) 
        return flight_login_page.FlightLoginPage(driver_)

    def test_valid_credentials(self, login): 
        login.login_with("mercury", "mercury")
        assert login.success_msg_exist()




