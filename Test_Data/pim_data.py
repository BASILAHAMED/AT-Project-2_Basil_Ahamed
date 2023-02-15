# This file consists of Test Information like username, password, XPATH etc

# Python Class for Username and Password
class LoginData:
    url = "https://opensource-demo.orangehrmlive.com"
    username = "Admin"
    password = "admin123"


class PersonalDetails:
    # pim1
    first_name = "Ajith"
    last_name = "Kumar"
    employee_id = "0872"
    employee1_id = "0786"
    employee_other_id = "27486312"
    license_number = "110579"
    license_expiry_date = "2032-12-10"
    employee_dob = "1992-01-05"

    # pim2
    employee_search = "Ajith Kumar"
    updated_employee_id = "9876"
    updated_employee_other_id = "355"
    updated_license_number = "0528"
    updated_license_expiry_date = "1995-12-10"


# Python Class for Selenium Selectors
class ElementLocators:
    # default login locators
    xpath_username = '//input[@name="username"]'
    xpath_password = '//input[@type="password"]'
    xpath_login = '//button[@type="submit"]'

    # pim1
    # click PIM module
    xpath_pim_module = '//li[@class="oxd-main-menu-item-wrapper"][2]//a'
    # click Admin button
    xpath_admin_button = '//a[@class="oxd-main-menu-item active"]'
    # click add button
    xpath_add_button = '//div[@class="orangehrm-header-container"]//button'
    # click search_textbox button
    xpath_search_textbox = '//input[@placeholder="Search"]'
    xpath_menu_items = '//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]'

    # fill the personal details
    xpath_employee_firstname = '//input[@name="firstName"]'
    xpath_employee_lastname = '//input[@name="lastName"]'
    # clear default employee id and adding new employee id
    xpath_employee_id = '//div[@class="oxd-grid-2 orangehrm-full-width-grid"]//input[@class="oxd-input oxd-input--active"]'
    # click save button
    xpath_save_button = '//button[@type="submit"]'
    # editing the employee information (Personal details)
    xpath_employee1_id = '//form/div[2]/div[1]/div[1]/div/div[2]/input'
    xpath_employee_other_id = '//div[@class="oxd-form-row"][2]/div[1]/div[2]/div//input'
    xpath_employee_driver_license_number = '//div[@class="oxd-form-row"][2]//div[2]//div[@class="oxd-grid-item oxd-grid-item--gutters"][1]//input'
    xpath_employee_license_expiry_date = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
    xpath_employee_nationality = '//form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i'
    xpath_indian_nationality = '//form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[83]/span'
    xpath_employee_marital_status = '//form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i'
    xpath_single_marital_status = '//form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/span'
    xpath_employee_dob = '//form//div[3]//div[2]//div[1]//div//div[2]//div//div//input[@class="oxd-input oxd-input--active"]'
    xpath_employee_gender = '//form//div[3]//div[2]//div[2]//div//div[2]//div[1]//div[2]//div//label//span'
    xpath_save1_button = '//form/div[5]/button'
    xpath_user_generated = '//h6[@class="oxd-text oxd-text--h6 --strong"]'

    # pim2
    xpath_employee_search = '//div/div[1]/div/div[2]/div/div/input'
    xpath_edit_button = '//div[9]/div/button[2]'
    xpath_list_button = '//li[2]//a[@class="oxd-topbar-body-nav-tab-item"]'
    xpath_edited_id = '//div[3]/div/div[2]/div/div/div[2]/div'

    # pim3
    xpath_delete_button = '//button[@class="oxd-icon-button oxd-table-cell-action-space"][1]'
    xpath_delete_alert = '//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]'
    xpath_confirm_no_records = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span'









