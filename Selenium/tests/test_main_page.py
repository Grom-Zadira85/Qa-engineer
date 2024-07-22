import time

from ..pages.main_page import MainPage
from ..pages.login_page import LoginPage
from ..pages.urls import MainPageLink, ProductLink


def test_guest_can_go_to_login_page_from_main_page(browser):
    page = MainPage(browser, MainPageLink.Main_link)
    page.open()
    time.sleep(2)
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    time.sleep(2)


def test_guest_should_see_login_link_in_main_page(browser):
    page = MainPage(browser, MainPageLink.Main_link)
    page.open()
    time.sleep(2)
    page.should_be_login_link_in_main_page()
    time.sleep(2)


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = MainPage(browser, ProductLink.Shellcoders_handbook_link)
    page.open()
    time.sleep(2)
    page.go_to_login_page_from_product_page()
    time.sleep(2)


def test_guest_should_see_login_link_in_product_page(browser):
    page = MainPage(browser, ProductLink.Shellcoders_handbook_link)
    page.open()
    time.sleep(2)
    page.should_be_login_link_in_product_page()
    time.sleep(2)
