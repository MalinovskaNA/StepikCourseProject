﻿from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in str(self.browser.current_url),  "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self,email, password):
        email_user=self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_user.send_keys(email)
        password1=self.browser.find_element(*LoginPageLocators.REGISTRATION_PAS1)
        password1.send_keys(password)
        password2=self.browser.find_element(*LoginPageLocators.REGISTRATION_PAS2)
        password2.send_keys(password)
        btn_submit=self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        btn_submit.click()

        
