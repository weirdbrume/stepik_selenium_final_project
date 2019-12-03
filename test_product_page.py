import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('offer_number', ['0', '1', '2', '3', '4',
                                          '5', '6', pytest.param('7', marks=pytest.mark.xfail), '8', '9'])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()

    product_page.solve_quiz_and_get_code()

    product_page.should_message_product_in_basket_equal_to_the_product_name()
    product_page.should_message_price_of_product_in_basket_equal_to_product_price()
