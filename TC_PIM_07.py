""" Test case ID: TC_PIM_7 <---------
Test objective:
Updating Employee Emergency Contact Details page post User Creation.

Precondition:
Launch URL and Login as “Admin”.

Orange HRM 3.0 site is launched on a compatible browser.
Once done with TC-12(Above Contacts Details creation)

Steps:
1. Go to Emergency Contact Details and Click (Add+).
2. Fill out all fields in Emergency Contact Details page.
3. Click Save and validate filled details are present under Assigned Emergency
Contacts.

Expected Result:
The user should be able to see all the filled details present in Emergency Contact Details
page."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class EmployeeEmergency:
    def tc_pim_07(self):
        # launching chrome driver
        driver = webdriver.Chrome()

        # loading orange_hrm webpage
        orange_hrm_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(orange_hrm_url)

        # maximize browser window
        # driver.maximize_window()
        time.sleep(5)

        # input username
        xpath_of_username = '//input[@name="username"]'
        input_username = driver.find_element(By.XPATH, xpath_of_username)
        input_username.send_keys("Admin")

        # input password
        xpath_of_password = '//input[@type="password"]'
        input_password = driver.find_element(By.XPATH, xpath_of_password)
        input_password.send_keys("admin123")

        # click login button
        xpath_of_login_button = '//button[@type="submit"]'
        click_login_button = driver.find_element(By.XPATH, xpath_of_login_button)
        click_login_button.click()
        time.sleep(5)

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
        input_state= driver.find_element(By.XPATH, xpath_of_state)
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

        # close driver instance
        driver.close()


TC = EmployeeEmergency()
TC.tc_pim_07()
