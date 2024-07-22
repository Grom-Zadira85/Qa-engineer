import time

import pytest

from ..pages.product_page import ProductPage
from ..pages.urls import ProductLink, LoginPageLink, MainPageLink


def test_go_to_product_page(browser):
    page = ProductPage(browser, ProductLink.Coders_at_Work)
    page.open()
    # assert page.browser.current_url == ProductLink.The_shellcoders_handbook,  "не сработает"
    # параметризация языка (english or russian) из conftest меняет URL


# Expected :'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
# Actual   :'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",

                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_success_massage()
    page.name_product_in_alert_equals_catalog_product_name()
    page.price_product_in_alert_equals_add_basket_product_price()
    time.sleep(1)
    browser.quit()


@pytest.mark.xfail
# "Негативное тестирование"
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductLink.The_shellcoders_handbook)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.guest_cant_see_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductLink.The_shellcoders_handbook)
    page.open()
    page.guest_cant_see_success_message()


@pytest.mark.xfail
# "Негативное тестирование"
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductLink.The_shellcoders_handbook)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.message_disappeared_after_adding_product_to_basket()


@pytest.mark.login_guest_from_main
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, MainPageLink.Main_link)
        page.open()
        page.go_to_login_page_from_product_page()
        assert browser.current_url == LoginPageLink.login_url, " not login page"

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, MainPageLink.Main_link)
        page.open()
        page.should_be_login_link()


@pytest.mark.login_guest_from_product
class TestLoginFromProductPage():

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, ProductLink.The_City_and_the_Stars)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, ProductLink.The_City_and_the_Stars)
        page.open()
        page.go_to_login_page_from_product_page()
        assert browser.current_url == LoginPageLink.login_url, " not login page"
