from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def _product_alerts(self):
        alerts = self.browser.find_elements(*ProductPageLocators.ALERTS_LOCATOR)
        product_name_message = alerts[0].text
        product_price_message = alerts[2].text
        return product_name_message, product_price_message

    def _product_name_and_price(self):
        product_locator = self.browser.find_element(*ProductPageLocators.PRODUCT_LOCATOR)
        product_text = product_locator.text.split('\n')
        product_name, product_price = product_text[0], product_text[1]
        return product_name, product_price

    def should_message_product_in_basket_equal_to_the_product_name(self):
        print(self._product_alerts()[0])
        print(self._product_name_and_price()[0])
        assert self._product_name_and_price()[0] in self._product_alerts()[0],\
            f'name of product "{self._product_name_and_price()[0]}" are not equal to the product name in alert'

    def should_message_price_of_product_in_basket_equal_to_product_price(self):
        assert self._product_name_and_price()[1] in self._product_alerts()[1],\
            f'product price "{self._product_name_and_price()[0]}" are not equal to the product price in alert'
