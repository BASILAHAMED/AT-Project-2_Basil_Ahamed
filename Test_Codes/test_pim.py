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

    def test_pim4(self, launch_driver):  # test from pim4 again
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
        # xpath_of_save_button = '//form/div[2]/button[2]' ..
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_save_button1).click()

        # STEP 7 - validate filled details are present
        emp_id = input_employee_other_id.get_attribute('value')
        assert emp_id == pim_data.PersonalDetails.employee_other_id

        emp_license_no = input_employee_driver_license_number.get_attribute('value')
        assert emp_license_no == pim_data.PersonalDetails.license_number

        emp_license_expiry_date = input_employee_license_expiry_date.get_attribute('value')
        assert emp_license_expiry_date == pim_data.PersonalDetails.license_expiry_date

        # xpath_of_ind_nationality = '//form[@class="oxd-form"]/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
        emp_nation = self.driver.find_element(By.XPATH, pim_data.ElementLocators.xpath_of_indian_nationality)
        indian_nationality = emp_nation.text
        assert indian_nationality == "Indian"

        # xpath_of_emp_marital_status = '//form[@class="oxd-form"]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]'
        emp_marital_status = self.driver.find_element(By.XPATH, pim_data.ElementLocators.xpath_of_single_marital_status)
        marital_status = emp_marital_status.text
        assert marital_status == "Single"

        emp_dob = employee_dob.get_attribute("value")
        assert emp_dob == employee_dob

        # xpath_of_emp_gender = '//form[@class="oxd-form"]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
        input_emp_gender = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_employee_gender)
        assert input_emp_gender.is_enabled()
        print("SUCCESS # FILLED PERSONAL DETAILS ARE PRESENT")

    def test_pim6(self, launch_driver):
        # STEP 1 - click PIM button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_pim_button).click()

        # STEP 2 - click (+add) button on pim
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_add_button).click()

        # STEP 3 - toggle the create login details on the add employee
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_toggle).click()

        # STEP 4 - fill the mandatory fields
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_first_name).send_keys(pim_data.PersonalDetails.first_name)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_last_name).send_keys('k')
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_user_name).send_keys(pim_data.PersonalDetails.user_name)

        # STEP 5 - select enabled — radio button
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_status_radio_button).click()
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_password).send_keys(pim_data.PersonalDetails.password)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_confirm_password).send_keys(pim_data.PersonalDetails.confirm_password)

        # STEP 6 - click save button
        # xpath_of_save_button = '//form/div[2]/button[2]' ..
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_save_button).click()

        # filling the employee information (Personal details)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_employee_other_id).send_keys(pim_data.PersonalDetails.employee_other_id)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_employee_driver_license_number).send_keys(pim_data.PersonalDetails.license_number)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_employee_license_expiry_date).send_keys(pim_data.PersonalDetails.license_expiry_date)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_employee_nationality).click()

        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_indian_nationality).click()
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_employee_marital_status).click()
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_single_marital_status).click()
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_employee_dob).send_keys(pim_data.PersonalDetails.employee_dob)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_employee_gender).click()

        # click save button
        # xpath_of_save_button = '//form/div[5]/button' ..
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_save_button).click()

        # Go to Contact Details
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_contact_details).click()

        # Fill out all fields
        input_street1 = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_street1)
        input_street1.send_keys(pim_data.PersonalDetails.street1)

        input_street2 = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_street2)
        input_street2.send_keys(pim_data.PersonalDetails.street2)

        input_city = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_city)
        input_city.send_keys(pim_data.PersonalDetails.employee_city)

        input_state = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_state)
        input_state.send_keys(pim_data.PersonalDetails.employee_state)

        input_zipcode = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_zipcode)
        input_zipcode.send_keys(pim_data.PersonalDetails.employee_zipcode)

        # xpath_of_employee_nationality = '//form/div[1]/div/div[6]/div/div[2]/div/div/div[2]/i' ..
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_employee_nationality).click()
        # xpath_of_indian_nationality = '//form/div[1]/div/div[6]/div/div[2]/div/div[2]/div[100]' ..
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_indian_nationality).click()

        # click save details button
        # xpath_of_save_details = '//form/div[4]/button' ..
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_of_save_details).click()

        # validate filled details are present
        emp_street1 = input_street1.get_attribute('value')
        assert emp_street1 == pim_data.PersonalDetails.street1

        emp_street2 = input_street2.get_attribute('value')
        assert emp_street2 == pim_data.PersonalDetails.street2

        emp_city = input_city.get_attribute('value')
        assert emp_city == pim_data.PersonalDetails.employee_city

        emp_state = input_state.get_attribute('value')
        assert emp_state == pim_data.PersonalDetails.employee_state

        emp_zipcode = input_zipcode.get_attribute('value')
        assert emp_zipcode == pim_data.PersonalDetails.employee_zipcode

        xpath_of_ind_nationality = "//form/div[1]/div/div[6]/div/div[2]/div/div/div[1]"
        emp_nation = self.driver.find_element(By.XPATH, xpath_of_ind_nationality)
        indian_nationality = emp_nation.text
        assert indian_nationality == "Indian"
        print("SUCCESS # FILLED CONTACT DETAILS ARE PRESENT")

    def test_pim7(self, launch_driver):
        # STEP 1 - click PIM button
        xpath_of_pim_button = '//div[2]/ul/li[2]/a'
        click_pim_button = driver.find_element(By.XPATH, xpath_of_pim_button)
        click_pim_button.click()
        time.sleep(5)

        # STEP 2 - click (+add) button on pim
        xpath_of_add = '//div[2]/div[1]/button'
        add_button = driver.find_element(By.XPATH, xpath_of_add)
        add_button.click()
        time.sleep(6)

        # STEP 3 - toggle the create login details on the add employee
        xpath_of_toggle = '//form/div[1]/div[2]/div[2]/div/label/span'
        toggle_button = driver.find_element(By.XPATH, xpath_of_toggle)
        toggle_button.click()

        # STEP 4 - fill the mandatory fields
        xpath_of_first_name = '//form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'
        first_name = driver.find_element(By.XPATH, xpath_of_first_name)
        first_name.send_keys('abinesh')

        xpath_of_last_name = '//form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'
        last_name = driver.find_element(By.XPATH, xpath_of_last_name)
        last_name.send_keys('k')

        xpath_of_user_name = '//form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
        user_name = driver.find_element(By.XPATH, xpath_of_user_name)
        user_name.send_keys('shamk89123')

        # STEP 5 - select enabled — radio button
        xpath_of_status_radio_button = '//form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
        status_radio_button = driver.find_element(By.XPATH, xpath_of_status_radio_button)
        status_radio_button.click()

        xpath_of_password = '//form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
        password = driver.find_element(By.XPATH, xpath_of_password)
        password.send_keys('Basil@1234')

        xpath_of_confirm_password = '//form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
        confirm_password = driver.find_element(By.XPATH, xpath_of_confirm_password)
        confirm_password.send_keys('Basil@1234')

        # STEP 6 - click save button
        xpath_of_save_button = '//form/div[2]/button[2]'
        save_button = driver.find_element(By.XPATH, xpath_of_save_button)
        save_button.click()
        time.sleep(8)

        # filling the employee information (Personal details)
        xpath_of_employee_other_id = '//form/div[2]/div[1]/div[2]/div/div[2]/input'
        input_employee_other_id = driver.find_element(By.XPATH, xpath_of_employee_other_id)
        employee_other_id = "27486312"
        input_employee_other_id.send_keys(employee_other_id)

        xpath_of_employee_driver_license_number = '//form/div[2]/div[2]/div[1]/div/div[2]/input'
        input_employee_driver_license_number = driver.find_element(By.XPATH, xpath_of_employee_driver_license_number)
        employee_driver_license_number = "110579"
        input_employee_driver_license_number.send_keys(employee_driver_license_number)

        xpath_of_employee_license_expiry_date = '//form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
        input_employee_license_expiry_date = driver.find_element(By.XPATH, xpath_of_employee_license_expiry_date)
        license_expiry_date = "2032-12-10"
        input_employee_license_expiry_date.send_keys(license_expiry_date)

        xpath_of_employee_nationality = '//form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i'
        input_employee_nationality = driver.find_element(By.XPATH, xpath_of_employee_nationality)
        input_employee_nationality.click()
        xpath_of_indian_nationality = '//form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[94]/span'
        input_indian_nationality = driver.find_element(By.XPATH, xpath_of_indian_nationality)
        input_indian_nationality.click()

        xpath_of_employee_marital_status = '//form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i'
        input_employee_marital_status = driver.find_element(By.XPATH, xpath_of_employee_marital_status)
        input_employee_marital_status.click()
        xpath_of_single_marital_status = '//form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]'
        input_single_marital_status = driver.find_element(By.XPATH, xpath_of_single_marital_status)
        input_single_marital_status.click()

        xpath_of_employee_dob = '//form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
        input_employee_dob = driver.find_element(By.XPATH, xpath_of_employee_dob)
        employee_dob = "1992-01-05"
        input_employee_dob.send_keys(employee_dob)

        xpath_of_employee_gender = '//form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
        input_employee_gender = driver.find_element(By.XPATH, xpath_of_employee_gender)
        input_employee_gender.click()

        # click save button
        xpath_of_save_button = '//form/div[5]/button'
        click_save_button = driver.find_element(By.XPATH, xpath_of_save_button)
        click_save_button.click()
        time.sleep(10)

        # Go to Contact Details
        xpath_of_contact_details = "//div[2]/div[2]/a"
        click_contact_details = driver.find_element(By.XPATH, xpath_of_contact_details)
        click_contact_details.click()
        time.sleep(5)

        # Fill out all fields
        xpath_of_street1 = '//form/div[1]/div/div[1]/div/div[2]/input'
        input_street1 = driver.find_element(By.XPATH, xpath_of_street1)
        street1 = "Greams Road"
        input_street1.send_keys(street1)

        xpath_of_street2 = '//form/div[1]/div/div[2]/div/div[2]/input'
        input_street2 = driver.find_element(By.XPATH, xpath_of_street2)
        street2 = "Main Street"
        input_street2.send_keys(street2)

        xpath_of_city = '//form/div[1]/div/div[3]/div/div[2]/input'
        input_city = driver.find_element(By.XPATH, xpath_of_city)
        employee_city = "Chennai"
        input_city.send_keys(employee_city)

        xpath_of_state = '//form/div[1]/div/div[4]/div/div[2]/input'
        input_state = driver.find_element(By.XPATH, xpath_of_state)
        employee_state = "Tamilnadu"
        input_state.send_keys(employee_state)

        xpath_of_zipcode = '//form/div[1]/div/div[5]/div/div[2]/input'
        input_zipcode = driver.find_element(By.XPATH, xpath_of_zipcode)
        employee_zipcode = "601208"
        input_zipcode.send_keys(employee_zipcode)

        xpath_of_employee_nationality = '//form/div[1]/div/div[6]/div/div[2]/div/div/div[2]/i'
        input_employee_nationality = driver.find_element(By.XPATH, xpath_of_employee_nationality)
        input_employee_nationality.click()
        xpath_of_indian_nationality = '//form/div[1]/div/div[6]/div/div[2]/div/div[2]/div[100]'
        input_indian_nationality = driver.find_element(By.XPATH, xpath_of_indian_nationality)
        input_indian_nationality.click()

        # click save details button
        xpath_of_save_details = '//form/div[4]/button'
        save_details = driver.find_element(By.XPATH, xpath_of_save_details)
        save_details.click()

        # STEP 1 - Go to Emergency Contact Details
        xpath_of_emergency_contact_details = '//div[3]/a'
        emergency_details = driver.find_element(By.XPATH, xpath_of_emergency_contact_details)
        emergency_details.click()

        # Click (Add+)
        xpath_of_add_details = '//div/div[2]/div[1]/div/button'
        add_details = driver.find_element(By.XPATH, xpath_of_add_details)
        add_details.click()

        # Fill out all fields in Emergency Contact Details
        xpath_of_name = '//form/div[1]/div/div[1]/div/div[2]/input'
        input_name = driver.find_element(By.XPATH, xpath_of_name)
        name = "Anson"
        input_name.send_keys(name)

        xpath_of_relationship = '//form/div[1]/div/div[2]/div/div[2]/input'
        input_relationship = driver.find_element(By.XPATH, xpath_of_relationship)
        relationship = "Friend"
        input_relationship.send_keys(relationship)

        xpath_of_home_telephone = '//form/div[2]/div/div[1]/div/div[2]/input'
        input_home_telephone = driver.find_element(By.XPATH, xpath_of_home_telephone)
        home_telephone = "26868975"
        input_home_telephone.send_keys(home_telephone)

        xpath_of_mobile = '//form/div[2]/div/div[2]/div/div[2]/input'
        input_mobile = driver.find_element(By.XPATH, xpath_of_mobile)
        mobile = "987652600"
        input_mobile.send_keys(mobile)

        xpath_of_work_telephone = '//form/div[2]/div/div[3]/div/div[2]/input'
        input_work_telephone = driver.find_element(By.XPATH, xpath_of_work_telephone)
        work_telephone = "26869876"
        input_work_telephone.send_keys(work_telephone)

        # click save button
        xpath_of_save_emergency = '//form/div[3]/button[2]'
        save_emergency = driver.find_element(By.XPATH, xpath_of_save_emergency)
        save_emergency.click()

        # validate filled details are present
        xpath_of_emer_name = '//div[3]/div/div[2]/div/div/div[2]/div'
        emer_name = driver.find_element(By.XPATH, xpath_of_emer_name)
        emer_name_text = emer_name.text
        if emer_name_text == name:
            print("Emergency Name is present")

        xpath_of_relationship = '//div[3]/div/div[2]/div/div/div[3]/div'
        emer_relationship = driver.find_element(By.XPATH, xpath_of_relationship)
        emer_relationship_text = emer_relationship.text
        if emer_relationship == relationship:
            print("Emergency Relationship is present")

        xpath_of_home_telephone = '//div[3]/div/div[2]/div/div/div[4]/div'
        emer_home_telephone = driver.find_element(By.XPATH, xpath_of_home_telephone)
        emer_home_telephone_text = emer_home_telephone.text
        if emer_home_telephone_text == home_telephone:
            print("Employee Home Telephone is present")

        xpath_of_mobile = '//div[3]/div/div[2]/div/div/div[5]/div'
        emer_mobile = driver.find_element(By.XPATH, xpath_of_mobile)
        emer_mobile_text = emer_name.text
        if emer_mobile_text == mobile:
            print("Employee mobile is present")

        xpath_of_work_telephone = '//div[3]/div/div[2]/div/div/div[6]/div'
        emer_work_telephone = driver.find_element(By.XPATH, xpath_of_work_telephone)
        emer_work_telephone_text = emer_work_telephone.text
        if emer_work_telephone_text == work_telephone:
            print("Employee Work Telephone is present")





