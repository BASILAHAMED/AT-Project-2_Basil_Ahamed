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
            (By.XPATH, pim_data.ElementLocators.xpath_of_enabled_dropdown)))
        disabled_dropdown = wait1.until(EC.presence_of_element_located(
            (By.XPATH, pim_data.ElementLocators.xpath_of_disabled_dropdown)))

        assert enabled_dropdown.is_displayed() and disabled_dropdown.is_displayed()
        print("SUCCESS # ENABLED AND DISABLED STATUS PRESENT")

    def test_pim3(self, launch_driver):
        # STEP 1 - click PIM button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_pim_button).click()

        # STEP 2 - click (+add) button on pim
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_add_button).click()

        # STEP 3 - toggle the create login details on the add employee
        wait1 = WebDriverWait(self.driver, 5)
        toggle_button = wait1.until(EC.visibility_of_element_located((By.XPATH, pim_data.ElementLocators.xpath_of_toggle)))
        toggle_button.click()

        # STEP 4 - fill the mandatory fields
        # send first name
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_first_name).send_keys(pim_data.PersonalDetails.first_name)

        # send last name
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_last_name).send_keys(pim_data.PersonalDetails.last_name)

        # send username
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_user_name).send_keys(pim_data.PersonalDetails.user_name)

        # STEP 5 - select enabled — radio button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_status_radio_button).click()
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_password).send_keys(pim_data.PersonalDetails.password)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_confirm_password).send_keys(pim_data.PersonalDetails.confirm_password)

        # STEP 6 - click save button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_save_button).click()

        # validate page moved to employee list
        wait1 = WebDriverWait(self.driver, 5)
        employee_list = wait1.until(
            EC.text_to_be_present_in_element((By.XPATH, pim_data.ElementLocators.xpath_of_employee_list), "Employee List"))
        employee_text = self.driver.find_element(By.XPATH, pim_data.ElementLocators.xpath_of_employee_list).text

        assert employee_text == "Employee List"
        print("SUCCESS # PAGE MOVED TO EMPLOYEE LIST")

    def test_pim4(self, launch_driver):
        # STEP 1 - click PIM button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_pim_button).click()

        # STEP 2 - search employee name
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_search_employee).click()

        # STEP 3 - click search/save button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_save_button).click()

        # STEP 4 - click employee edit button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_employee_list1).click()

        # STEP 5 - creating empty list to keep the tab items to be validated
        tab_items = []
        tab = self.driver.find_elements(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_tab_items)

        # using 'for loop' to append all tab items into list
        for tab_name in tab:
            tab_items.append(tab_name.text)

        # create a list of tabs to validate
        search_result_text = ['Personal Details', 'Contact Details', 'Emergency Contacts', 'Dependents', 'Immigration',
                              'Job', 'Salary', 'Tax Exemptions', 'Report-to', 'Qualifications', 'Memberships']

        # STEP 6 - sending item one by one to assert if it is present
        for item in search_result_text:
            assert item in tab_items
        print("SUCCESS # ALL TABS ARE PRESENT")

    def test_pim5(self, launch_driver):
        # STEP 1 - click PIM button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_pim_button).click()

        # STEP 2 - search employee name
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_search_employee).send_keys(pim_data.PersonalDetails.first_name)

        # STEP 3 - click search/save button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_save_button).click()

        # STEP 4 - click employee edit button
        wait = WebDriverWait(self.driver, 10)
        record_found = wait.until(EC.presence_of_element_located((By.XPATH, pim_data.ElementLocators.xpath_of_record_found)))
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_employee_list1).click()

        # STEP 5 - filling the employee information (Personal details)
        input_employee_other_id = wait.until(EC.presence_of_element_located((By.XPATH, pim_data.ElementLocators.xpath_of_employee_other_id)))
        # input_employee_other_id = driver.find_element(By.XPATH, xpath_of_employee_other_id)
        input_employee_other_id.send_keys(pim_data.PersonalDetails.employee_other_id)

        input_employee_driver_license_number = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_employee_driver_license_number)
        input_employee_driver_license_number.send_keys(pim_data.PersonalDetails.license_number)

        input_employee_license_expiry_date = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_employee_license_expiry_date)
        input_employee_license_expiry_date.send_keys(pim_data.PersonalDetails.license_expiry_date)

        # click employee nationality and select Indian
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_employee_nationality).click()
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_indian_nationality).click()

        # select martial status to single
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_employee_marital_status).click()
        single_status = wait.until(
            EC.text_to_be_present_in_element((By.XPATH, pim_data.ElementLocators.xpath_of_single_marital_status),
                                             text_=pim_data.PersonalDetails.marital_status))
        # input_single_marital_status = driver.find_element(By.XPATH, xpath_of_single_marital_status)
        # input_single_marital_status.click()
        single_status.click()

        # select employee dob
        employee_dob = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_employee_dob)
        employee_dob.send_keys(pim_data.PersonalDetails.employee_dob)

        # select employee gender
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_employee_gender).click()

        # STEP 6 - click save button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_save_button1).click()

        # STEP 7 - validate filled details are present
        emp_id = input_employee_other_id.get_attribute('value')
        assert emp_id == pim_data.PersonalDetails.employee_other_id

        emp_license_no = input_employee_driver_license_number.get_attribute('value')
        assert emp_license_no == pim_data.PersonalDetails.license_number

        emp_license_expiry_date = input_employee_license_expiry_date.get_attribute('value')
        assert emp_license_expiry_date == pim_data.PersonalDetails.license_expiry_date

        xpath_of_ind_nationality = '//form[@class="oxd-form"]/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
        emp_nation = self.driver.find_element(By.XPATH, pim_data.ElementLocators.xpath_of_indian_nationality)
        indian_nationality = emp_nation.text
        assert indian_nationality == "Indian"

        xpath_of_emp_marital_status = '//form[@class="oxd-form"]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]'
        emp_marital_status = self.driver.find_element(By.XPATH, pim_data.ElementLocators.xpath_of_single_marital_status)
        marital_status = emp_marital_status.text
        assert marital_status == "Single"

        emp_dob = employee_dob.get_attribute("value")
        assert emp_dob == employee_dob

        xpath_of_emp_gender = '//form[@class="oxd-form"]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
        input_emp_gender = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_employee_gender)
        assert input_emp_gender.is_enabled()
        print("SUCCESS # FILLED DETAILS ARE PRESENT")






