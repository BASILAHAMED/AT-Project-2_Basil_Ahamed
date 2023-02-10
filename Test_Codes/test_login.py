from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import login_data
import pytest


class TestLogin:
    url = "https://opensource-demo.orangehrmlive.com"
    
    # Launching driver for running the Python Tests
    @pytest.fixture
    def launch_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        yield
        self.driver.close()
    
    def test_login(self, launch_driver):
        self.driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_username).send_keys(login_data.LoginData.username)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_password).send_keys(login_data.LoginData.password)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_login).click()
        dashboard = self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_dashboard).text
        assert dashboard == 'Dashboard'
        print("SUCCESS # LOGGED IN WITH USERNAME {username} and PASSWORD {password}".format(username=login_data.LoginData.username, password=login_data.LoginData.password))

    def test_invalid_login(self, launch_driver):
        self.driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_username).send_keys(login_data.LoginData.username)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_password).send_keys(login_data.LoginData.invalid_password)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_login).click()
        invalid = self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_invalid_login).text
        assert invalid == 'Invalid credentials'
        print("SUCCESS # INVALID LOGIN WITH USERNAME {username} and PASSWORD {password}".format(username=login_data.LoginData.username, password=login_data.LoginData.invalid_password))


