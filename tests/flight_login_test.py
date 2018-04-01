import pytest
from selenium import webdriver
from pages import flight_login_page
import os

class TestFlightLogin():

    @pytest.fixture
    def login(self, driver):
        return flight_login_page.FlightLoginPage(driver)

    def test_valid_credentials(self, login): 
        login.login_with("mercury", "mercury")
        assert login.success_msg_exist()




