from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()

    product_page.solve_quiz_and_get_code()

    product_page.should_message_product_in_basket_equal_to_the_product_name()
    product_page.should_message_price_of_product_in_basket_equal_to_product_price()
