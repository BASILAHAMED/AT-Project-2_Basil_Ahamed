""" Test case ID: TC_PIM_02 <-------
Test objective:
Validation of Page Headers — Drop Down on Admin Page

Precondition:
Launch URL and Login as “Admin”.
Orange HRM 3.0 site is launched on a compatible browser

Steps:
1. Go to Admin page.
2. Validate the below MENU options (on Side Pane) are displaying on Admin page
3. Click users under User Management in header.
4. Validate below fields are available under System Users:

a. User Role —- Drop Down
b. Status - Drop Down.

Expected Result:
The user should be able to see the below values in Drop-Down:
User-Role - Admin, ESS
Status - Enabled, Disabled """

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestDropDown:
    def tc_pim_02(self):
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

        # STEP 1 - click Admin button
        xpath_of_admin_button = '//li[@class="oxd-main-menu-item-wrapper"][1]/a'
        click_admin_button = driver.find_element(By.XPATH, xpath_of_admin_button)
        click_admin_button.click()
        # time.sleep(5)

        # STEP 2 - click users under user management in header

        # click user management
        xpath_of_user_management = '//li[@class="oxd-topbar-body-nav-tab --parent --visited"]'
        user_management = driver.find_element(By.XPATH, xpath_of_user_management)
        user_management.click()
        # time.sleep(5)

        # click user menu
        xpath_of_user_menu = '//a[@role="menuitem"]'
        user_menu = driver.find_element(By.XPATH, xpath_of_user_menu)
        user_menu.click()
        # time.sleep(5)

        # validate user role and status dropdown
        xpath_of_user_role_dropdown = '//div[@class="oxd-grid-4 orangehrm-full-width-grid"]//div[2]//div//div[2]//div//div//div//i'
        user_role_dropdown = driver.find_element(By.XPATH, xpath_of_user_role_dropdown)
        user_role_dropdown.click()
        # time.sleep(5)

        # check admin and ess are displayed or not
        # using WebDriverWait to wait until the dropdown elements are present
        wait1 = WebDriverWait(driver, 5)
        admin_value = wait1.until(EC.presence_of_element_located((By.XPATH, '//div[@class="oxd-grid-item oxd-grid-item--gutters"][2]/div/div[2]/div/div[2]/div[2]')))
        ess_value = wait1.until(EC.presence_of_element_located((By.XPATH, '//div[@class="oxd-grid-item oxd-grid-item--gutters"][2]/div/div[2]/div/div[2]/div[3]')))

        assert admin_value.is_displayed() and ess_value.is_displayed()
        print("SUCCESS # ADMIN AND ESS VALUES PRESENT")

        xpath_of_status_dropdown = '//div[@class="oxd-grid-4 orangehrm-full-width-grid"]//div[4]//div//div[2]//div//div//div//i'
        status_dropdown = driver.find_element(By.XPATH, xpath_of_status_dropdown)
        status_dropdown.click()
        # time.sleep(8)

        # check enabled and disabled are displayed or not
        # using WebDriverWait to wait until the dropdown elements are present
        wait1 = WebDriverWait(driver, 5)
        enabled_dropdown = wait1.until(EC.presence_of_element_located((By.XPATH, '//div[@class="oxd-grid-item oxd-grid-item--gutters"][4]/div/div[2]/div/div[2]/div[2]')))
        disabled_dropdown = wait1.until(EC.presence_of_element_located((By.XPATH, '//div[@class="oxd-grid-item oxd-grid-item--gutters"][4]/div/div[2]/div/div[2]/div[3]')))

        assert enabled_dropdown.is_displayed() and disabled_dropdown.is_displayed()
        print("SUCCESS # ENABLED AND DISABLED STATUS PRESENT")

        # close driver instance
        driver.close()


TD = TestDropDown()
TD.tc_pim_02()
