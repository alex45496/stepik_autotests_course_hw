from pages.product_page import ProductPage
import pytest

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{product_base_link}/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_add_product()
    page.should_be_message_price_product()
