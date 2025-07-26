from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE_ADD_PRODUCT = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1) .alertinner')
    SUCCESS_MESSAGE_INFO_PRICE_PRODUCT = (By.CSS_SELECTOR, '#messages .alert-info p:nth-child(1)')
