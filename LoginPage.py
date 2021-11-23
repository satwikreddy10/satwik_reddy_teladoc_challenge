# Gathering locators for the elements in the page
# Using page object model
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.user_name = (By.ID, "ap_email")
        self.continue_button = (By.ID, "continue")
        self.password = (By.ID, "ap_password")
        self.signin = (By.ID, "signInSubmit")

    def enter_username(self, value):
        self.driver.find_element(*self.user_name).send_keys(value)

    def click_continue_button(self):
        self.driver.find_element(*self.continue_button).click()

    def enter_password(self, value):
        self.driver.find_element(*self.password).send_keys(value)

    def click_signin_button(self):
        self.driver.find_element(*self.signin).click()