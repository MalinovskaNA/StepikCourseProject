from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_url")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")  
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main >.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main >h1")

    MESSAGE_PRICE = (By.CSS_SELECTOR, ".alert.alert-info >.alertinner strong")
    MESSAGE_PRODUCT = (By.CSS_SELECTOR, ".alert.alert-success >.alertinner >strong")