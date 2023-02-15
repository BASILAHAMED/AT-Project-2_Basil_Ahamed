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
        # click PIM module
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_pim_module).click()

        # search existing employee added earlier ("Ajith Kumar")
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_search).send_keys(
            pim_data.PersonalDetails.employee_search)

        # click search button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_save_button).click()

        # click edit employee button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_edit_button).click()

        # editing the employee information (Personal details)
        send_updated_employee_id = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee1_id)
        send_updated_employee_id.send_keys(Keys.CONTROL, "a")  # <--- Using ctrl+A key combination to delete default values --->
        send_updated_employee_id.send_keys(Keys.DELETE)
        send_updated_employee_id.send_keys(pim_data.PersonalDetails.updated_employee_id)

        send_employee_other_id = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_other_id)
        send_employee_other_id.send_keys(Keys.CONTROL, "a")
        send_employee_other_id.send_keys(Keys.DELETE)
        send_employee_other_id.send_keys(pim_data.PersonalDetails.updated_employee_other_id)

        send_employee_driver_license_number = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_driver_license_number)
        send_employee_driver_license_number.send_keys(Keys.CONTROL, "a")
        send_employee_driver_license_number.send_keys(Keys.DELETE)
        send_employee_driver_license_number.send_keys(pim_data.PersonalDetails.updated_license_number)

        send_employee_license_expiry_date = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_license_expiry_date)
        send_employee_license_expiry_date.send_keys(Keys.CONTROL, "a")
        send_employee_license_expiry_date.send_keys(Keys.DELETE)
        send_employee_license_expiry_date.send_keys(pim_data.PersonalDetails.updated_license_expiry_date)

        # click save button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_save1_button).click()

        # verifying employee details edited or not
        # click employee list button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_list_button).click()

        # search existing employee edited now ("Ajith Kumar")
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_search).send_keys(
            pim_data.PersonalDetails.employee_search)

        # click search button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_save_button).click()

        # assert employee id equals to edited employee id
        fetch = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_edited_id).text
        assert fetch == "9876"
        print("SUCCESS # EMPLOYEE \"{first_name} {last_name}\" DETAILS EDITED".format(
            first_name=pim_data.PersonalDetails.first_name.upper(),
            last_name=pim_data.PersonalDetails.last_name.upper()))

    def test_pim3(self, launch_driver):
        # click PIM module
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_pim_module).click()

        # search existing employee added earlier ("Ajith Kumar")
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_employee_search).send_keys(
            pim_data.PersonalDetails.employee_search)

        # click search button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_save_button).click()

        # click delete employee button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_delete_button).click()

        # click delete confirmation alert
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_delete_alert).click()

        # verify deletion by again searching employee present or not
        # click search button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_save_button).click()

        # print employee deleted status
        # if no records found for that employee, then employee deleted
        no_records = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_confirm_no_records).text
        assert no_records == "No Records Found"
        print("SUCCESS # EMPLOYEE \"{first_name} {last_name}\" DETAILS DELETED".format(
            first_name=pim_data.PersonalDetails.first_name.upper(),
            last_name=pim_data.PersonalDetails.last_name.upper()))
