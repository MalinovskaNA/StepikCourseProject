import pytest
import time

def test_guest_should_see_basket_btn(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #time.sleep(30)
    assert browser.find_element_by_id("add_to_basket_form"), "Should be a butten"
