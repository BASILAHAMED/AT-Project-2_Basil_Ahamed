"""
Test case ID: TC_PIM 9 <---------

Test objective:
Updating Employee Job Details page.

Precondition:
Launch URL and Login as “Admin”.

Orange HRM 3.0 site is launched on a compatible browser.

Once done with TC-14

Steps:
1. Go to Job Details.
2. Fill out details under job details.
3. Toggle — Include Employment Contact Details Button.
4. Fill out all fields in Contract Details.
5. Click Save and validate filled details are present under Job Details.

Expected Result:
The user should be able to see all the filled details present in Job Details page.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class EmployeeJobDetails:
    def tc_pim_09(self):
        # launching chrome driver
        driver = webdriver.Chrome()

        # loading orange_hrm webpage
        orange_hrm_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(orange_hrm_url)

        # maximize browser window
        driver.maximize_window()
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

        # STEP 1 - Go to Job Details
        xpath_of_job_details = '//div[6]/a'
        job_details = driver.find_element(By.XPATH, xpath_of_job_details)
        job_details.click()
        time.sleep(6)

        # Fill out all fields in Job Details
        xpath_of_joined_date = '//div/div[2]/div/div/input'
        input_joined_date = driver.find_element(By.XPATH, xpath_of_joined_date)
        date = "03-02-1992"
        input_joined_date.send_keys(date)

        xpath_of_job_title = '//div[2]/div/div[2]/div/div/div[2]/i'
        input_job_title = driver.find_element(By.XPATH, xpath_of_job_title)
        input_job_title.click()
        xpath_of_ceo_job = '//div[2]/div/div[2]/div[3]'
        input_ceo_job = driver.find_element(By.XPATH, xpath_of_ceo_job)
        input_ceo_job.click()

        xpath_of_job_category = '//div[4]/div/div[2]/div/div/div[2]/i'
        input_job_category= driver.find_element(By.XPATH, xpath_of_job_category)
        input_job_category.click()
        xpath_of_official = '//div/div[2]/div/div[2]/div[5]'
        input_official = driver.find_element(By.XPATH, xpath_of_official)
        input_official.click()

        xpath_of_sub_unit = '//div[5]/div/div[2]/div/div/div[2]/i'
        input_sub_unit = driver.find_element(By.XPATH, xpath_of_sub_unit)
        input_sub_unit.click()
        xpath_of_engg = '//div[2]/div/div[2]/div[3]'
        input_engg = driver.find_element(By.XPATH, xpath_of_engg)
        input_engg.click()

        xpath_of_job_location = '//div[6]/div/div[2]/div/div/div[2]/i'
        input_job_location = driver.find_element(By.XPATH, xpath_of_job_location)
        input_job_location.click()
        xpath_of_sales_office = '//div[2]/div/div[2]/div[4]'
        input_sales_office = driver.find_element(By.XPATH, xpath_of_sales_office)
        input_sales_office.click()

        xpath_of_employment_status = '//div[7]/div/div[2]/div/div/div[2]/i'
        input_employment_status = driver.find_element(By.XPATH, xpath_of_employment_status)
        input_employment_status.click()
        xpath_of_ft_permanent = '//div[2]/div/div[2]/div[4]'
        input_ft_permanent = driver.find_element(By.XPATH, xpath_of_ft_permanent)
        input_ft_permanent.click()

        # Click Toggle — Include Employment Contact Details Button
        xpath_of_include_contract = '//form/div[2]/div/label/span'
        include_contract = driver.find_element(By.XPATH, xpath_of_include_contract)
        include_contract.click()

        xpath_of_dob = '//div[3]/div/div[1]/div/div[2]/div/div/input'
        input_dob = driver.find_element(By.XPATH, xpath_of_dob)
        dob = "02-03-2021"
        input_dob.send_keys(dob)

        xpath_of_dob = '//div[3]/div/div[2]/div/div[2]/div/div/input'
        input_dob = driver.find_element(By.XPATH, xpath_of_dob)
        dob = "02-08-2022"
        input_dob.send_keys(dob)

        xpath_of_contract_details = '//form/div[4]/div/div/div/div/div[2]/div/div[1]'
        upload_contract_file = driver.find_element(By.XPATH, xpath_of_contract_details)
        upload_contract_file.send_keys("D:\\screen.jpg")

        # click save button
        xpath_of_save_job = '//form/div[5]/button'
        save_job = driver.find_element(By.XPATH, xpath_of_save_job)
        save_job.click()
        time.sleep(5)
        
        # close driver instance
        driver.close()


TC = EmployeeJobDetails()
TC.tc_pim_09()
