from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoAlertPresentException

class BasketPage(BasePage):
    def get_basket_message(self):
        basket_message=self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        return basket_message.text

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT), \
        "Success message is presented, but should not be"
    
    def should_be_message_about_no_product_in_basket(self):
        basket_message=self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        str = "Your basket is empty"
        assert str in basket_message, "Product in the basket, but should not be"
