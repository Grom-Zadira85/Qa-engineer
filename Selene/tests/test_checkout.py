import time

import allure
import pytest
from selene import browser, have

from Selene.pages import checkout_cart
from Selene.pages.home_page import HomePage
from Selene.pages.urls import *


@pytest.fixture
def go_to_shopping_cart_page():
    page = HomePage(browser, main_page_link)
    page.open()
    page.add_to_cart_from_main_page()
    page.is_counter_number_visible()
    page.go_to_mini_cart()
    page.go_to_checkout_cart()


@allure.link("https://trello.com/c/lvLslLGD")
@allure.title('ТС_005.001.016| Main page > Cart > View and edit cart > Checking that the size color product-image and '
              'product name are correct in the Cart page')
def test_size_color_and_product_name_are_correct_in_the_checkout_cart_page(go_to_shopping_cart_page):
    checkout_cart.check_product_name_is_correct("Argus All-Weather Tank")
    checkout_cart.check_size_is_correct("M")
    checkout_cart.check_color_is_correct("Gray")


@allure.link("https://trello.com/c/SQ3op4DX")
@allure.title(
    'ТС_005.001.017| Main page > Cart > View and edit cart > Check price and Cart Subtotal present in Cart page')
def test_check_price_qty_and_cart_subtotal_present_in_checkout_cart_page(go_to_shopping_cart_page):
    checkout_cart.check_price_present("$22.00")
    checkout_cart.check_subtotal("$22.00")
    checkout_cart.check_qty()
    time.sleep(2)


@allure.link('https://trello.com/c/1AQzogwV')
@allure.title('ТС_005. 001.018| Main page > Cart > View and edit cart > Checking Estimate Shipping and Tax')
def test_checking_estimate_shipping_and_tax(go_to_shopping_cart_page):
    checkout_cart.check_change_qty("3")
    checkout_cart.update_click()
    checkout_cart.estimate_shipping_drop()
    checkout_cart.select_country_drop()
    checkout_cart.select_country("South Korea")
    # checkout_cart_page.select_country("Canada")
    checkout_cart.select_state_region("Alberta")
    checkout_cart.post_code("79980")
    checkout_cart.flat_rate_should_be_present()
    checkout_cart.fixed_type_of_shipping_selected()
    checkout_cart.shipping_price_is_correct("$15")
    subtotal = checkout_cart.check_subtotal_value_is_present_and_correct("3", "$22.00")
    checkout_cart.check_order_total_has_the_correct_amount(subtotal, "$15")


@allure.link('https://trello.com/c/e2ezawti')
@allure.title('ТС_005.001.019| Main page > Cart > View and edit cart  > Checking the ability to change the quantity '
              'of items and deleting an item on the cart page')
def test_checking_ability_to_change_quantity_items_and_deleting_on_the_cart_page(go_to_shopping_cart_page):
    checkout_cart.check_change_qty("3")
    checkout_cart.update_click()
    checkout_cart.delete_item()
    checkout_cart.item_should_not_present()
    time.sleep(3)


@allure.link('https://trello.com/c/9y9lAlqC')
@allure.title('ТС_005.001.020| Main page > Cart > View and edit cart > Checking clickability “Proceed to Checkout" '
              'button and redirection to checkout-shipping page.')
def test_checking_clickability_proceed_to_checkout_button_and_redirection(go_to_shopping_cart_page):
    checkout_cart.check_change_qty("3")
    checkout_cart.update_click()
    checkout_cart.estimate_shipping_drop()
    checkout_cart.select_country_drop()
    checkout_cart.select_country("South Korea")
    checkout_cart.select_state_region("Alberta")
    checkout_cart.post_code("79980")
    checkout_cart.fixed_type_of_shipping_selected()
    checkout_cart.check_proceed_to_checkout_button_should_be_clickable()
    checkout_cart.redirection_to_checkout_shipping_page()
    browser.should(have.url('https://magento.softwaretestingboard.com/checkout/#shipping'))
