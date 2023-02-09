"""
Test case ID: TC_PIM_4 <----------
Test objective:
Validation of Employee Personal Details page post User Creation.

Precondition:
Launch URL and Login as “Admin".

Orange HRM 3.0 site is launched on a compatible browser.
Once done with TC-09(Above user creation)

Steps:
1. Go to Employee List page (Post User Creation in PIM Module)

2. Validate below tabs are present in PIM page:

a. Personal Details
b. Contact Details
c. Emergency Contacts
d. Dependents
e. Immigration
f. Job
g. Salary
h. Tax Exemptions
i. Report-to
j. Qualifications
k. Memberships

Expected Result:
The user should be able to see all the tabs present in Employee List page."""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestNewEmployee:
    def tc_pim_04(self):
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
        time.sleep(5)

        # STEP 3 - toggle the create login details on the add employee
        xpath_of_toggle = '//form/div[1]/div[2]/div[2]/div/label/span'
        toggle_button = driver.find_element(By.XPATH, xpath_of_toggle)
        toggle_button.click()

        # STEP 4 - fill the mandatory fields
        xpath_of_first_name = '//form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'
        first_name = driver.find_element(By.XPATH, xpath_of_first_name)
        first_name.send_keys('ajay')

        xpath_of_last_name = '//form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'
        last_name = driver.find_element(By.XPATH, xpath_of_last_name)
        last_name.send_keys('k')

        xpath_of_user_name = '//form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
        user_name = driver.find_element(By.XPATH, xpath_of_user_name)
        user_name.send_keys('shamk8912')

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
        time.sleep(5)

        # validate page moved to employee list
        wait1 = WebDriverWait(driver, 5)
        employee_list = wait1.until(EC.presence_of_element_located((By.XPATH, '//li[@class="oxd-topbar-body-nav-tab --visited"]/a[@class]')))
        employee_text = employee_list.text

        if employee_text == "Employee List":
            print("The page moved to “Employee List")
        time.sleep(8)

        # TC_PIM_04
        # creating empty list to keep the tab items to be validated
        tab_items = []
        xpath_of_tab_items = '//div[@role="tab"]//a'
        tab = driver.find_elements(By.XPATH, xpath_of_tab_items)

        # using 'for loop' to append all tab items into list
        for tab_name in tab:
            tab_items.append(tab_name.text)
        print(tab_items)
        time.sleep(5)

        # create a list of tabs to validate
        search_result_text = ['Personal Details', 'Contact Details', 'Emergency Contacts', 'Dependents', 'Immigration', 'Job',
                              'Salary', 'Tax Exemptions', 'Report-to', 'Qualifications', 'Memberships']

        # sending item one by one to validate if it is present
        for item in search_result_text:
            assert item in tab_items
        print("all the tabs are present in Employee List page")

        # close driver instance
        driver.close()


TN = TestNewEmployee()
TN.tc_pim_04()

