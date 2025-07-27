from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_TITLE = (By.CSS_SELECTOR, ".basket-title")


class LoginPageLocators:
    # main locators
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    # form registration
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_REPEAT_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE_ADD_PRODUCT = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1) .alertinner')
    SUCCESS_MESSAGE_INFO_PRICE_PRODUCT = (By.CSS_SELECTOR, '#messages .alert-info p:nth-child(1)')
