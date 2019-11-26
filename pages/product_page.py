from .base_page import BasePage
from .locators import ProductPageLocators
from collections import namedtuple


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def _product_alerts(self):
        alerts = self.browser.find_elements(*ProductPageLocators.ALERTS_LOCATOR)
        product = namedtuple('product', 'name, price')
        return product(alerts[0].text, alerts[2].text)

    def _product_name_and_price(self):
        product_locator = self.browser.find_element(*ProductPageLocators.PRODUCT_LOCATOR)
        product_text = product_locator.text.split('\n')
        product = namedtuple('product', 'name, price')
        return product(product_text[0], product_text[1])

    def should_message_product_in_basket_equal_to_the_product_name(self):
        assert self._product_name_and_price().name in self._product_alerts().name,\
            f'name of product "{self._product_name_and_price().name}" are not equal to the product name in alert'

    def should_message_price_of_product_in_basket_equal_to_product_price(self):
        assert self._product_name_and_price().price in self._product_alerts().price,\
            f'product price "{self._product_name_and_price().price}" are not equal to the product price in alert'
