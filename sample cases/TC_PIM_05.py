"""
Test case ID: TC_PIM_ 5 <--------
Test objective:
Updating Employee Personal Details page post User Creation.

Precondition:
Launch URL and Login as “Admin”.

Orange HRM 3.0 site is launched on a compatible browser.

Once done with TC-09(Above user creation)

Steps:
1. Go to Employee List page (Post User Creation in PIM Module)
2. Fill out all fields in Personal Details page.
3. Click Save and validate filled details are present.

Expected Result:
The user should be able to see all the filled details present in Personal Details page. """

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class EmployeePersonal:
    def tc_pim_05(self):
        # launching chrome driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)

        # loading orange_hrm webpage
        orange_hrm_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(orange_hrm_url)

        # maximize browser window
        # driver.maximize_window()
        # time.sleep(5)

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
        # time.sleep(5)

        # STEP 1 - click PIM button
        xpath_of_pim_button = '//div[2]/ul/li[2]/a'
        click_pim_button = driver.find_element(By.XPATH, xpath_of_pim_button)
        click_pim_button.click()
        # time.sleep(5)

        # STEP 2 - search employee name
        xpath_of_search_employee = '(//input[@placeholder="Type for hints..."])[1]'
        click_search_employee_button = driver.find_element(By.XPATH, xpath_of_search_employee)
        click_search_employee_button.send_keys('ajay')

        # STEP 6 - click search/save button
        xpath_of_save_button = '//button[@type="submit"]'
        save_button = driver.find_element(By.XPATH, xpath_of_save_button)
        save_button.click()
        # time.sleep(5)

        # STEP 7 - click employee edit button
        wait = WebDriverWait(driver, 10)
        xpath_of_employee_list = '(//button[@class="oxd-icon-button oxd-table-cell-action-space"])[2]'
        xpath_of_record_found = '//span[normalize-space()="(1) Record Found"]'
        record_found = wait.until(EC.presence_of_element_located((By.XPATH, xpath_of_record_found)))
        edit_button = driver.find_element(By.XPATH, xpath_of_employee_list)
        edit_button.click()

        # # STEP 2 - click (+add) button on pim
        # xpath_of_add = '//div[2]/div[1]/button'
        # add_button = driver.find_element(By.XPATH, xpath_of_add)
        # add_button.click()
        # # time.sleep(6)
        #
        # # STEP 3 - toggle the create login details on the add employee
        # xpath_of_toggle = '//form/div[1]/div[2]/div[2]/div/label/span'
        # toggle_button = driver.find_element(By.XPATH, xpath_of_toggle)
        # toggle_button.click()
        #
        # # STEP 4 - fill the mandatory fields
        # xpath_of_first_name = '//form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'
        # first_name = driver.find_element(By.XPATH, xpath_of_first_name)
        # first_name.send_keys('atman')
        #
        # xpath_of_last_name = '//form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'
        # last_name = driver.find_element(By.XPATH, xpath_of_last_name)
        # last_name.send_keys('k')
        #
        # xpath_of_user_name = '//form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
        # user_name = driver.find_element(By.XPATH, xpath_of_user_name)
        # user_name.send_keys('shamk89123')
        #
        # # STEP 5 - select enabled — radio button
        # xpath_of_status_radio_button = '//form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
        # status_radio_button = driver.find_element(By.XPATH, xpath_of_status_radio_button)
        # status_radio_button.click()
        #
        # xpath_of_password = '//form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
        # password = driver.find_element(By.XPATH, xpath_of_password)
        # password.send_keys('Basil@1234')
        #
        # xpath_of_confirm_password = '//form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
        # confirm_password = driver.find_element(By.XPATH, xpath_of_confirm_password)
        # confirm_password.send_keys('Basil@1234')
        #
        # # STEP 6 - click save button
        # xpath_of_save_button = '//form/div[2]/button[2]'
        # save_button = driver.find_element(By.XPATH, xpath_of_save_button)
        # save_button.click()
        # time.sleep(10)

        # filling the employee information (Personal details)
        xpath_of_employee_other_id = '(//input[@class="oxd-input oxd-input--active"])[4]'
        input_employee_other_id = wait.until(EC.presence_of_element_located((By.XPATH, xpath_of_employee_other_id)))
        # input_employee_other_id = driver.find_element(By.XPATH, xpath_of_employee_other_id)
        employee_other_id = "27486312"
        input_employee_other_id.send_keys(employee_other_id)

        xpath_of_employee_driver_license_number = '(//input[@class="oxd-input oxd-input--active"])[5]'
        input_employee_driver_license_number = driver.find_element(By.XPATH, xpath_of_employee_driver_license_number)
        employee_driver_license_number = "110579"
        input_employee_driver_license_number.send_keys(employee_driver_license_number)

        xpath_of_employee_license_expiry_date = '(//input[@class="oxd-input oxd-input--active"])[6]'
        input_employee_license_expiry_date = driver.find_element(By.XPATH, xpath_of_employee_license_expiry_date)
        license_expiry_date = "2032-12-10"
        input_employee_license_expiry_date.send_keys(license_expiry_date)

        xpath_of_employee_nationality = '(//div[@class="oxd-select-text--after"]//i)[1]'
        input_employee_nationality = driver.find_element(By.XPATH, xpath_of_employee_nationality)
        input_employee_nationality.click()
        # time.sleep(5)
        xpath_of_indian_nationality = '(//div[@class="oxd-select-text-input"])[1]'
        input_indian_nationality = driver.find_element(By.XPATH, xpath_of_indian_nationality)
        input_indian_nationality.click()

        xpath_of_employee_marital_status = '(//div[@class="oxd-select-text--after"]//i)[2]'
        input_employee_marital_status = driver.find_element(By.XPATH, xpath_of_employee_marital_status)
        input_employee_marital_status.click()
        xpath_of_single_marital_status = '//div[contains(text(),"Single")]'
        single_status = wait.until(EC.text_to_be_present_in_element((By.XPATH, xpath_of_single_marital_status), text_="Single"))
        # input_single_marital_status = driver.find_element(By.XPATH, xpath_of_single_marital_status)
        # input_single_marital_status.click()
        single_status.click()

        xpath_of_employee_dob = '(//input[@class="oxd-input oxd-input--active"])[9]'
        input_employee_dob = driver.find_element(By.XPATH, xpath_of_employee_dob)
        employee_dob = "1992-01-05"
        input_employee_dob.send_keys(employee_dob)

        xpath_of_employee_gender = '(//span[@class="oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input"])[1]'
        input_employee_gender = driver.find_element(By.XPATH, xpath_of_employee_gender)
        input_employee_gender.click()

        # click save button
        xpath_of_save_button = '(//button[@type="submit"])[1]'
        click_save_button = driver.find_element(By.XPATH, xpath_of_save_button)
        click_save_button.click()
        # time.sleep(6)

        # validate filled details are present
        emp_id = input_employee_other_id.get_attribute('value')
        assert emp_id == employee_other_id

        emp_license_no = input_employee_driver_license_number.get_attribute('value')
        assert emp_license_no == employee_driver_license_number

        emp_license_expiry_date = input_employee_license_expiry_date.get_attribute('value')
        assert emp_license_expiry_date == license_expiry_date

        xpath_of_ind_nationality = '//form[@class="oxd-form"]/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
        emp_nation = driver.find_element(By.XPATH, xpath_of_indian_nationality)
        indian_nationality = emp_nation.text
        assert indian_nationality == "Indian"

        xpath_of_emp_marital_status = '//form[@class="oxd-form"]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]'
        emp_marital_status = driver.find_element(By.XPATH, xpath_of_single_marital_status)
        marital_status = emp_marital_status.text
        assert marital_status == "Single"

        emp_dob = input_employee_dob.get_attribute("value")
        assert emp_dob == employee_dob

        xpath_of_emp_gender = '//form[@class="oxd-form"]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
        input_emp_gender = driver.find_element(By.XPATH, xpath_of_employee_gender)
        assert input_emp_gender.is_enabled()
        print("SUCCESS # FILLED DETAILS ARE PRESENT")

        # close driver instance
        driver.quit()


TN = EmployeePersonal()
TN.tc_pim_05()
