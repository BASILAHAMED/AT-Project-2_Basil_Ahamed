# This file consists of test datas like username, password, XPATH etc

# Python Class for Username and Password
class LoginData:
    url = "https://opensource-demo.orangehrmlive.com"
    username = "Admin"
    password = "admin123"


class PersonalDetails:
    # pim 3
    first_name = "Ajith"
    last_name = "Kumar"
    user_name = "ajith78"
    password = "Ajith@1256"
    confirm_password = "Ajith@1256"
    employee_other_id = "27486312"
    license_number = "110579"
    license_expiry_date = "2032-12-10"
    employee_dob = "1992-01-05"
    marital_status = "Single"

    # pim 6
    street1 = "Greams Road"
    street2 = "Main Street"
    employee_city = "Chennai"
    employee_state = "Tamilnadu"
    employee_zipcode = "601208"


# Python Class for Selenium Selectors
class ElementLocators:
    # default login locators
    xpath_username = '//input[@name="username"]'
    xpath_password = '//input[@type="password"]'
    xpath_login = '//button[@type="submit"]'

    # pim 1
    # click Admin button
    xpath_admin_button = '//a[@href="/web/index.php/admin/viewAdminModule"]'
    # click search_textbox button
    xpath_search_textbox = '//input[@placeholder="Search"]'
    # xpath of menu items
    xpath_menu_items = '//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]'

    # pim 2
    # click user management
    xpath_of_user_management = '//li[@class="oxd-topbar-body-nav-tab --parent --visited"]'
    # click user menu
    xpath_of_user_menu = '//a[@role="menuitem"]'
    xpath_of_user_role_dropdown = '//div[@class="oxd-grid-4 orangehrm-full-width-grid"]//div[2]//div//div[2]//div//div//div//i'
    xpath_of_admin_value = '//div[@class="oxd-grid-item oxd-grid-item--gutters"][2]/div/div[2]/div/div[2]/div[2]'
    xpath_of_ess_value = '//div[@class="oxd-grid-item oxd-grid-item--gutters"][2]/div/div[2]/div/div[2]/div[3]'
    xpath_of_status_dropdown = '//div[@class="oxd-grid-4 orangehrm-full-width-grid"]//div[4]//div//div[2]//div//div//div//i'
    xpath_of_enabled_dropdown = '//div[@class="oxd-grid-item oxd-grid-item--gutters"][4]/div/div[2]/div/div[2]/div[2]'
    xpath_of_disabled_dropdown = '//div[@class="oxd-grid-item oxd-grid-item--gutters"][4]/div/div[2]/div/div[2]/div[3]'

    # pim 3
    # click PIM module
    xpath_pim_button = '//li[@class="oxd-main-menu-item-wrapper"][2]//a'
    # click add button
    xpath_add_button = '//div[@class="orangehrm-header-container"]//button'
    xpath_of_toggle = '//div[@class="oxd-switch-wrapper"]//span'
    xpath_of_first_name = '//input[@name="firstName"]'
    xpath_of_last_name = '//input[@name="lastName"]'
    xpath_of_user_name = '//div[@class="orangehrm-employee-container"]//div[3]/div/div[1]/div/div[2]/input'
    xpath_of_status_radio_button = '//div[@class="--status-grouped-field"]//div[1]//div[2]//span'
    xpath_of_password = '//div[@class="oxd-grid-item oxd-grid-item--gutters user-password-cell"]//div[1]//div[2]//input'
    xpath_of_confirm_password = '//div[@class="oxd-form-row user-password-row"]//div//div[2]//div//div[2]//input'
    xpath_of_save_button = '//button[@type="submit"]'
    xpath_of_employee_list = '//li[@class="oxd-topbar-body-nav-tab --visited"]//a'

    # pim 4
    xpath_of_search_employee = '(//input[@placeholder="Type for hints..."])[1]'
    xpath_of_employee_list1 = '(//button[@class="oxd-icon-button oxd-table-cell-action-space"])[2]'
    xpath_of_tab_items = '//div[@role="tab"]//a'

    # pim 5
    xpath_of_record_found = '//span[normalize-space()="(1) Record Found"]'
    xpath_of_employee_other_id = '(//input[@class="oxd-input oxd-input--active"])[4]'
    xpath_of_employee_driver_license_number = '(//input[@class="oxd-input oxd-input--active"])[5]'
    xpath_of_employee_license_expiry_date = '(//input[@class="oxd-input oxd-input--active"])[6]'
    xpath_of_employee_nationality = '(//div[@class="oxd-select-text--after"]//i)[1]'
    xpath_of_indian_nationality = '(//div[@class="oxd-select-text-input"])[1]'
    xpath_of_employee_marital_status = '(//div[@class="oxd-select-text--after"]//i)[2]'
    xpath_of_single_marital_status = '//div[contains(text(),"Single")]'
    xpath_of_employee_dob = '(//input[@class="oxd-input oxd-input--active"])[9]'
    xpath_of_employee_gender = '(//span[@class="oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input"])[1]'
    xpath_of_save_button1 = '(//button[@type="submit"])[1]'

    # pim 6
    xpath_of_contact_details = "//div[2]/a"
    xpath_of_street1 = '//form/div[1]/div/div[1]/div/div[2]/input'
    xpath_of_street2 = '//form/div[1]/div/div[2]/div/div[2]/input'
    xpath_of_city = '//form/div[1]/div/div[3]/div/div[2]/input'
    xpath_of_state = '//form/div[1]/div/div[4]/div/div[2]/input'
    xpath_of_zipcode = '//form/div[1]/div/div[5]/div/div[2]/input'
    xpath_of_save_details = '//form/div[4]/button'

