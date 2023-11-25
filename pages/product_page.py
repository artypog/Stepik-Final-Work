from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button is not presented"

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_product_name_after_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name after adding is not presented"

    def get_product_name_after_adding(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_AFTER_ADDING).text

    def should_be_equal_names(self):
        name = self.get_product_name()
        name_after_add = self.get_product_name_after_adding()
        assert name == name_after_add, "Names are not equal"

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_basket_price(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text

    def should_be_equal_prices(self):
        prod_price = self.get_product_price()
        basket_price = self.get_basket_price()
        assert prod_price == basket_price, "Prices are not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear"



