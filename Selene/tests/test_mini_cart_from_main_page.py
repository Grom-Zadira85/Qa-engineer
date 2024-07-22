import allure
from selene import browser

from Selene.pages import mini_cart
from Selene.pages.home_page import HomePage
from Selene.pages.urls import *


def go_to_mini_cart():
    page = HomePage(browser, main_page_link)
    page.open()
    page.add_to_cart_from_main_page()
    page.is_counter_number_visible()
    page.go_to_mini_cart()


@allure.link('https://trello.com/c/WVaLK93g')
@allure.title('ТС_005.001.011 | Main page > Cart > View and edit cart > Check color and clickability of "View and '
              'edit cart" link in the mini-cart')
def test_color_and_clickability_of_view_and_edit_cart_link_in_the_mini_cart():
    go_to_mini_cart()
    # mini_cart = BasketPage(browser, main_page_link)
    mini_cart.check_color_of_view_and_edit_cart_link_in_the_mini_cart()
    mini_cart.check_clickability_of_view_and_edit_cart_link_in_the_mini_cart()


@allure.link('https://trello.com/c/w8Of4GYe')
@allure.title('ТС_005.001.012 | Main page > Cart > View and edit cart  > Сhecking the redirection to the cart page')
def test_checking_the_link_opens_the_cart_page():
    go_to_mini_cart()
    mini_cart.checking_the_link_opens_checkout_cart_page()


@allure.link("https://trello.com/c/v4hVrwzq")
@allure.title('ТС_005.001.013| Main page > Cart > View and edit cart > Checking that the size color and product name '
              'are correct')
def test_size_color_and_product_name_are_correct():
    go_to_mini_cart()
    mini_cart.checking_the_size_color_and_product_name_are_correct("M", "Gray", "Argus All-Weather Tank")


@allure.link("https://trello.com/c/p6iExP1c")
@allure.title('ТС_005.001.014 | Main page > Cart > View and edit cart > Checking present price item and Cart Subtotal '
              ' in the mini cart ')
def test_checking_present_price_item_and_cart_subtotal_in_the_mini_cart():
    go_to_mini_cart()
    mini_cart.checking_present_price_item_and_cart_subtotal_in_the_mini_cart("$22.00", "$22.00")


@allure.link("https://trello.com/c/uCZZgQks")
@allure.title('ТС_005.001.015| Main page > Cart > View and edit cart > Check the ability to change the quantity of an '
              'item and changes price in Cart Subtotal from mini cart')
def test_change_quantity_of_an_item_and_changes_price_in_cart_subtotal_mini_cart():
    go_to_mini_cart()
    mini_cart.should_be_success_message("You added Argus All-Weather Tank to your shopping cart.")
    mini_cart.change_qty("7")
    mini_cart.should_be_quantity_change("7")
    mini_cart.should_be_change_subtotal("$22.00", "$154.00")
