import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn_add_basket = self.browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
        btn_add_basket.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_message_add_product(self):
        product_name = self.get_product_name()
        full_message = f'{product_name} has been added to your basket.'
        message_success_add_product = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_ADD_PRODUCT).text
        assert full_message == message_success_add_product,\
            f"expected '{product_name}' to be substring of '{message_success_add_product}'"

    def should_be_message_price_product(self):
        product_price = self.get_product_price()
        full_message = f'Your basket total is now {product_price}'
        message_info_price_product = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_INFO_PRICE_PRODUCT).text
        assert full_message == message_info_price_product,\
            f"expected '{product_price}' to be substring of '{message_info_price_product}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ADD_PRODUCT), \
            "Success message is presented, but should not be"

    def should_be_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_ADD_PRODUCT), \
            "Success message is presented, but should not be"
