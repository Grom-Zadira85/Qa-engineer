from .base_page import BasePage
from .locators import MainPageLocators, ProductPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_OR_REGISTER_LINK)
        # * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
        # alert = self.browser.switch_to.alert
        # alert.accept()

    def should_be_login_link_in_main_page(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_OR_REGISTER_LINK), "Login link is not presented"

    def go_to_login_page_from_product_page(self):
        login_link = self.browser.find_element(*ProductPageLocators.LOGIN_OR_REGISTER_LINK)
        login_link.click()

    def should_be_login_link_in_product_page(self):
        assert self.is_element_present(*ProductPageLocators.LOGIN_OR_REGISTER_LINK), "Login link is not presented"
