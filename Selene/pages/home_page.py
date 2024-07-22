from selene import be
from selene.support.shared.jquery_style import s

from Selene.pages.base_page import BasePage
from Selene.pages.locators import ProductLocators as PL


class HomePage(BasePage):

    def add_to_cart_from_main_page(self):
        s(PL.ARGUS_All_WEATHER_TANK_SIZE).click()
        s(PL.ARGUS_All_WEATHER_TANK_COLOR).click()
        s(PL.ARGUS_All_WEATHER_TANK_ADD_TO_CARD).click()

    def go_to_mini_cart(self):
        s(PL.MINI_BASKET_WINDOW).should(be.clickable).click()

    def go_to_checkout_cart(self):
        s(PL.VIEW_AND_EDIT_CART_LINK).click()

    def find_counter_number(self):
        return s(PL.MINICART_COUNTER)

    def is_counter_number_visible(self):
        return self.find_counter_number().should(be.visible)
