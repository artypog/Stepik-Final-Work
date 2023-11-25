from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOPPING), \
            "Continue shopping link not presented"

    def should_not_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.CONTINUE_SHOPPING), \
            "Continue shopping link is presented, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "'Your basket is empty' message not presented"

    def should_not_be_empty_basket_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "'Your basket is empty' message is presented, but should not be"






