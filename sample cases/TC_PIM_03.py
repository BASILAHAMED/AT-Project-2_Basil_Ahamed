"""
Test case ID: TC_PIM_03 <--------

Test objective:
Creation of New Employee under PIM

Precondition:
Launch URL and Login as “Admin”.

Orange HRM 3.0 site is launched on a compatible browser

Steps:
1. Go to Admin page and Click on PIM option.
2. Validate the below MENU options (on Side Pane) are displaying on PIM page
3. Click (+Add) button on PIM.
4. Toggle the “Create Login Details on the Add Employee and Fill all the
mandatory fields.
5. Select Enabled — Radio Button.
6. Click Save button.

Expected Result:
The user should be able to see the page moved to “Employee List” once user is created. """


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestNewEmployee:
    def tc_pim_03(self):
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
        xpath_of_pim_button = '//li[@class="oxd-main-menu-item-wrapper"][2]//a'
        click_pim_button = driver.find_element(By.XPATH, xpath_of_pim_button)
        click_pim_button.click()
        # time.sleep(5)

        # STEP 2 - click (+add) button on pim
        xpath_of_add = '//div[@class="orangehrm-header-container"]//button'
        add_button = driver.find_element(By.XPATH, xpath_of_add)
        add_button.click()
        # time.sleep(5)

        # STEP 3 - toggle the create login details on the add employee
        xpath_of_toggle = '//div[@class="oxd-switch-wrapper"]//span'
        wait1 = WebDriverWait(driver, 5)
        toggle_button = wait1.until(EC.visibility_of_element_located((By.XPATH, xpath_of_toggle)))
        toggle_button.click()

        # STEP 4 - fill the mandatory fields
        xpath_of_first_name = '//input[@name="firstName"]'
        first_name = driver.find_element(By.XPATH, xpath_of_first_name)
        first_name.send_keys('ajay')

        xpath_of_last_name = '//input[@name="lastName"]'
        last_name = driver.find_element(By.XPATH, xpath_of_last_name)
        last_name.send_keys('k')

        xpath_of_user_name = '//div[@class="orangehrm-employee-container"]//div[3]/div/div[1]/div/div[2]/input'
        user_name = driver.find_element(By.XPATH, xpath_of_user_name)
        user_name.send_keys('ajay1245')

        # STEP 5 - select enabled — radio button
        xpath_of_status_radio_button = '//div[@class="--status-grouped-field"]//div[1]//div[2]//span'
        status_radio_button = driver.find_element(By.XPATH, xpath_of_status_radio_button)
        status_radio_button.click()

        xpath_of_password = '//div[@class="oxd-grid-item oxd-grid-item--gutters user-password-cell"]//div[1]//div[2]//input'
        password = driver.find_element(By.XPATH, xpath_of_password)
        password.send_keys('Basil@1234')

        xpath_of_confirm_password = '//div[@class="oxd-form-row user-password-row"]//div//div[2]//div//div[2]//input'
        # xpath_of_confirm_password = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
        confirm_password = driver.find_element(By.XPATH, xpath_of_confirm_password)
        confirm_password.send_keys('Basil@1234')

        # STEP 6 - click save button
        xpath_of_save_button = '//button[@type="submit"]'
        save_button = driver.find_element(By.XPATH, xpath_of_save_button)
        save_button.click()
        # time.sleep(5)

        # validate page moved to employee list
        wait1 = WebDriverWait(driver, 5)
        employee_list = wait1.until(EC.text_to_be_present_in_element((By.XPATH, '//li[@class="oxd-topbar-body-nav-tab --visited"]//a'), "Employee List"))
        employee_text = driver.find_element(By.XPATH, '//li[@class="oxd-topbar-body-nav-tab --visited"]//a').text

        assert employee_text == "Employee List"
        print("SUCCESS # PAGE MOVED TO EMPLOYEE LIST")

        # close driver instance
        driver.close()


TN = TestNewEmployee()
TN.tc_pim_03()

