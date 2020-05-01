from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    def should_be_message_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT), "Massege about product is not presented"
        
    def product_in_message_product_should_be_equal_product_in_basket(self,product_name):
        basket_name=self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT).text
        assert product_name == basket_name, "Other product in the basket:"+ basket_name+" ;" + product_name+ "!= " + basket_name

    def price_in_message_should_be_equal_price_in_basket(self,product_price):
        basket_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text
        assert product_price == basket_price,"Other price of product in the basket:" +basket_price+" ; "+ product_price+ "!= "+basket_price
        

    def should_be_message_price_of_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE), "Massege about price is not presented"
        