"""Test case ID: TC_PIM_01 <-------

Test objective:
Search — (text Box) Validation on Admin Page

Precondition:
Launch URL and Login as “Admin”.
Orange HRM 3.0 site is launched on a compatible browser

Steps:
1. Go to Admin page.
2. Validate the below MENU options (on Side Pane) are displaying on Admin page
3. Validate the Search (Text Box) is displaying on Admin Homepage.
4. Click on Search Box and search with below text in (Both Lower and Upper Case):

a) Admin
b) PIM
c) Leave
d) Time
e) Recruitment
f) My Info
g) Performance
h) Dashboard
i) Directory
j) Maintenance
k) Buzz

Expected Result:
The user should be able to search the above-mentioned Admin Page Menu and these
individual menu name should be displayed under search text box """

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestSearchBox:
    def tc_pim_01(self):
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
        time.sleep(8)

        # STEP 1 - click Admin button
        xpath_of_admin_button = '//li[1]/a[@class="oxd-main-menu-item"]'
        click_admin_button = driver.find_element(By.XPATH, xpath_of_admin_button)
        click_admin_button.click()
        time.sleep(5)

        # STEP 2 - validate the search (text box) is displaying on admin homepage
        xpath_of_search_textbox = '//input[@placeholder="Search"]'
        search_textbox = driver.find_element(By.XPATH, xpath_of_search_textbox)
        if search_textbox.is_displayed():
            print("* Search Textbox is displayed on Admin Homepage")
        else:
            print("* Search Textbox is not displayed on Admin Homepage")

        # STEP 3 - click on search box and validating menu items displayed or not
        # click search box
        search_textbox.click()
        time.sleep(5)

        # creating empty list to keep the menu items to be searched
        menu_items = []
        xpath_of_menu_items = '//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]'
        menu = driver.find_elements(By.XPATH, xpath_of_menu_items)

        # using 'for loop' to append all menu items into list
        for item_name in menu:
            menu_items.append(item_name.text)

        # using WebDriverWait to wait until the searched element will be present on webpage
        wait1 = WebDriverWait(driver, 5)

        # sending item one by one in lowercase to the search box for validation
        for item in menu_items:
            search_textbox.send_keys(item)
            time.sleep(3)

            search_result = wait1.until(EC.presence_of_element_located((By.XPATH, '//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]')))
            search_result_text = search_result.text
            assert search_result_text.lower() == item.lower()

            search_textbox.send_keys(Keys.CONTROL, "a")
            search_textbox.send_keys(Keys.BACK_SPACE)

        print(f"* Searched in lower case and all menu items are displayed under search text box")

        # sending item one by one in upper case to the search box for validation
        for item in menu_items:
            search_textbox.send_keys(item)
            time.sleep(3)

            search_result = wait1.until(EC.presence_of_element_located((By.XPATH, '//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]')))
            search_result_text = search_result.text
            assert search_result_text.upper() == item.upper()

            search_textbox.send_keys(Keys.CONTROL, "a")
            search_textbox.send_keys(Keys.BACK_SPACE)

        print(f"* Searched in upper case and all menu items are displayed under search text box")

        # close driver instance
        driver.close()


TL = TestSearchBox()
TL.tc_pim_01()
