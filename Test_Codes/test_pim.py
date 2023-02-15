from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data import pim_data
import pytest


class TestPIM:
    url = pim_data.LoginData.url
    
    # Launching driver for running the Python Tests
    @pytest.fixture
    def launch_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # login to orangeHRM webpage
        self.driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_username).send_keys(pim_data.LoginData.username)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_password).send_keys(pim_data.LoginData.password)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_login).click()
        yield
        self.driver.close()
    
    def test_pim1(self, launch_driver):
        # click Admin button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_admin_button).click()

        # STEP 2 - validate the search (text box) is displaying on admin homepage
        search_textbox = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_search_textbox)
        assert search_textbox.is_displayed()
        print("SUCCESS # SEARCH TEXTBOX IS DISPLAYED")

        # STEP 3 - click on search box and validating menu items displayed or not
        # click search box
        search_textbox.click()

        # creating empty list to keep the menu items to be searched
        menu_items = []
        menu = self.driver.find_elements(by=By.XPATH, value=pim_data.ElementLocators.xpath_menu_items)

        # using 'for loop' to append all menu items into list
        for item_name in menu:
            menu_items.append(item_name.text)

        # using WebDriverWait to wait until the searched element will be present on webpage
        wait1 = WebDriverWait(self.driver, 5)

        # sending item one by one in lowercase to the search box for validation
        for item in menu_items:
            search_textbox.send_keys(item.lower())

            # wait until searched element appears
            search_result = wait1.until(EC.presence_of_element_located((By.XPATH, pim_data.ElementLocators.xpath_menu_items)))
            search_result_text = search_result.text
            assert search_result_text.lower() == item.lower()

            # clear search textbox
            search_textbox.send_keys(Keys.CONTROL, "a")
            search_textbox.send_keys(Keys.BACK_SPACE)
        print("SUCCESS # ALL MENU ITEMS ARE DISPLAYED WITH LOWER CASE SEARCH")

        # sending item one by one in upper case to the search box for validation
        for item in menu_items:
            search_textbox.send_keys(item.upper())

            # wait until searched element appears
            search_result = wait1.until(EC.presence_of_element_located((By.XPATH, pim_data.ElementLocators.xpath_menu_items)))
            search_result_text = search_result.text
            assert search_result_text.upper() == item.upper()

            # clear search textbox
            search_textbox.send_keys(Keys.CONTROL, "a")
            search_textbox.send_keys(Keys.BACK_SPACE)
        print("SUCCESS # ALL MENU ITEMS ARE DISPLAYED WITH UPPER CASE SEARCH")

    def test_pim2(self, launch_driver):
        # STEP 1 - click Admin button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_admin_button).click()

        # STEP 2 - click users under user management in header
        # click user management
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_user_management).click()

        # click user menu
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_user_menu).click()

        # validate user role and status dropdown
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_user_role_dropdown).click()

        # check admin and ess are displayed or not
        # using WebDriverWait to wait until the dropdown elements are present
        wait1 = WebDriverWait(self.driver, 5)
        admin_value = wait1.until(EC.presence_of_element_located(
            (By.XPATH, pim_data.ElementLocators.xpath_of_admin_value)))
        ess_value = wait1.until(EC.presence_of_element_located(
            (By.XPATH, pim_data.ElementLocators.xpath_of_ess_value)))

        assert admin_value.is_displayed() and ess_value.is_displayed()
        print("SUCCESS # ADMIN AND ESS VALUES PRESENT")

        # check enabled and disabled are displayed or not
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_status_dropdown).click()

        # using WebDriverWait to wait until the dropdown elements are present
        wait1 = WebDriverWait(self.driver, 5)
        enabled_dropdown = wait1.until(EC.presence_of_element_located(
            (By.XPATH, '')))
        disabled_dropdown = wait1.until(EC.presence_of_element_located(
            (By.XPATH, pim_data.ElementLocators.xpath_of_disabled_dropdown)))

        assert enabled_dropdown.is_displayed() and disabled_dropdown.is_displayed()
        print("SUCCESS # ENABLED AND DISABLED STATUS PRESENT")
