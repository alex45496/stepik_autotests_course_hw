from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_basket_is_empty(self):
        full_message = 'Your basket is empty. Continue shopping'
        message_basket_is_empty = self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_EMPTY).text
        assert full_message == message_basket_is_empty, f"expected '{message_basket_is_empty}' not equal'{full_message}'"

    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE), \
            "Title basket is presented, but should not be"
