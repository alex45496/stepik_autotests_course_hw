from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from faker import Faker
import pytest


PRODUCT_BASE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
REGISTER_PAGE = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'


@pytest.mark.need_review
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{PRODUCT_BASE_LINK}/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_add_product()
    page.should_be_message_price_product()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_BASE_LINK)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_BASE_LINK)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_BASE_LINK)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_BASE_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_BASE_LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_message_basket_is_empty()
    basket_page.should_be_basket_empty()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # open page registration
        login_page = LoginPage(browser, REGISTER_PAGE)
        login_page.open()
        login_page.should_be_login_page()
        # generate email and password
        fake = Faker()
        user_email = fake.email()
        user_password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
        login_page.register_new_user(email=user_email, password=user_password)
        # check authorized user
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, PRODUCT_BASE_LINK)
        page.open()
        page.add_product_to_basket()
        page.should_be_message_add_product()
        page.should_be_message_price_product()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, PRODUCT_BASE_LINK)
        page.open()
        page.should_not_be_success_message()
