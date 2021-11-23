# Gathering locators for the elements in the page
# Using page object model
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Amazon():

    def __init__(self, driver):
        self.driver = driver

        self.accounts_link = (By.ID, "nav-link-accountList")
        self.search_box = (By.ID, 'twotabsearchtextbox')
        self.search_button = (By.ID, "nav-search-submit-button")
        self.first_Result = (By.CSS_SELECTOR, "[data-cel-widget='search_result_1'] img")
        self.main_price = (By.XPATH, "//td[text()='Price:']/following-sibling::"
                                         "td/span[contains(@class,'apexPriceToPay')]/span[2]")
        self.subscribe_price = (By.XPATH, "//div[@id='snsAccordionRowMiddle']//span[@id='sns-base-price']")
        self.set_up_now = (By.ID, "rcx-subscribe-submit-button-announce")
        self.proceed_to_checkout = (By.XPATH, "//a[contains(text(),'Proceed to checkout')]")
        self.add_credit_or_debit_button = (By.XPATH, "//span[text()='Add a credit or debit card']")
        self.subscribe_and_save_link = (By.XPATH, "//a[contains(.,'Subscribe & Save Items')]")
        self.shop_subscribe_and_save_store = (By.XPATH, "//a[contains(text(),'Shop the Subscribe & Save store')]")

    def click_accounts_link(self):
        self.driver.find_element(*self.accounts_link).click()

    def move_to_accounts_link(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*self.accounts_link)).perform()

    def is_subscribe_and_save_link_displayed(self):
        return self.driver.find_element(*self.subscribe_and_save_link).is_displayed()

    def click_subscribe_and_save_link(self):
        self.driver.find_element(*self.subscribe_and_save_link).click()

    def is_shop_subscribe_and_save_store_displayed(self):
        return self.driver.find_element(*self.shop_subscribe_and_save_store).is_displayed()

    def enter_search_text(self, value):
        self.driver.find_element(*self.search_box).send_keys(value)

    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()

    def click_first_result(self):
        self.driver.find_element(*self.first_Result).click()

    def get_price_of_product(self):
        return float(self.driver.find_element(*self.main_price).text.strip().split("$")[1])

    def get_subscribe_price(self):
        return float(self.driver.find_element(*self.subscribe_price).text.strip().split("(")[0].strip().split("$")[1])

    def click_set_up_now(self):
        self.driver.find_element(*self.set_up_now).click()

    def click_proceed_to_checkout(self):
        self.driver.find_element(*self.proceed_to_checkout).click()

    def is_payment_page_displayed(self):
        return len(self.driver.find_elements(*self.add_credit_or_debit_button)) > 0

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 50).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(3)


