# This file consists of Test Information like username, password, XPATH etc

# Python Class for Username and Password
class LoginData:
    username = "Admin"
    password = "admin123"
    invalid_password = "password"


# Python Class for Selenium Selectors
class ElementLocators:
    xpath_username = '//input[@name="username"]'
    xpath_password = '//input[@type="password"]'
    xpath_login = '//button[@type="submit"]'
    xpath_dashboard = '//div[1]/span/h6'
    xpath_invalid_login = '//div[1]/p'
