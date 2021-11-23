import unittest

from selenium import webdriver

from Amazon import Amazon
from LoginPage import LoginPage
from data import data_Amazon


class Automation(unittest.TestCase):

    # test case to validate 5% off on eligible subscribe and save items
    def test_subscribe_and_save_price(self):

        self.driver = webdriver.Chrome()
        self.driver.get(data_Amazon.url)
        self.driver.maximize_window()

        amazon = Amazon(self.driver)
        amazon.click_accounts_link()
        login_page = LoginPage(self.driver)
        login_page.enter_username(data_Amazon.username)
        login_page.click_continue_button()
        login_page.enter_password(data_Amazon.password)
        login_page.click_signin_button()
        amazon.enter_search_text(data_Amazon.search_text)
        amazon.click_search_button()
        amazon.wait_for_page_load()
        amazon.click_first_result()
        amazon.wait_for_page_load()
        price = amazon.get_price_of_product()
        subscribe_price = amazon.get_subscribe_price()
        self.assertEqual(round((price/100)*95,2), subscribe_price)
        amazon.click_set_up_now()
        amazon.wait_for_page_load()
        amazon.click_proceed_to_checkout()
        amazon.wait_for_page_load()
        self.assertEqual(True, amazon.is_payment_page_displayed())
        self.driver.quit()

    # test case to validate fields under Subscribe and Save link
    def test_subscribe_and_save_page_navigation(self):

        self.driver = webdriver.Chrome()
        self.driver.get(data_Amazon.url)
        self.driver.maximize_window()

        amazon = Amazon(self.driver)
        amazon.click_accounts_link()
        login_page = LoginPage(self.driver)
        login_page.enter_username(data_Amazon.username)
        login_page.click_continue_button()
        login_page.enter_password(data_Amazon.password)
        login_page.click_signin_button()
        amazon.move_to_accounts_link()
        self.assertEqual(True, amazon.is_subscribe_and_save_link_displayed())
        amazon.click_subscribe_and_save_link()
        amazon.wait_for_page_load()
        self.assertEqual(True, amazon.is_shop_subscribe_and_save_store_displayed())
        self.driver.quit()

