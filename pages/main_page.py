from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from .login_page import LoginPage

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def add_to_basket(self):
        button_basket=self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)  
        button_basket.click()

    def get_product_name(self):
        product_name=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def get_product_price(self):
        product_price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text   
