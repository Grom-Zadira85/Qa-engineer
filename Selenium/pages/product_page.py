from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def in_the_product_page(self):
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_success_massage()
        self.name_product_in_alert_equals_catalog_product_name()
        self.price_product_in_alert_equals_add_basket_product_price()

        self.guest_cant_see_success_message_after_adding_product_to_basket()
        self.guest_cant_see_success_message()
        self.message_disappeared_after_adding_product_to_basket()

    def add_product_to_basket(self):
        product_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        product_link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_success_massage(self):
        success = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        print(success)
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).is_displayed()

    def name_product_in_alert_equals_catalog_product_name(self):
        name_product_in_alert = self.browser.find_element(*ProductPageLocators.ALERT_NAME_PRODUCT_IN_MESSAGE).text
        print(name_product_in_alert)
        name_product_in_catalog = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_ADD_TO_BASKET).text
        print(name_product_in_catalog)
        assert name_product_in_catalog == name_product_in_alert, " названия продуктов не совпадают"

    def price_product_in_alert_equals_add_basket_product_price(self):
        alert_price_product_in_message = self.browser.find_element(
            *ProductPageLocators.ALERT_PRICE_PRODUCT_IN_MESSAGE).text
        print(alert_price_product_in_message)
        price_product_add_to_basket = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_ADD_TO_BASKET).text
        print(price_product_add_to_basket)
        assert alert_price_product_in_message == price_product_add_to_basket

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        # should_not_be_success_message
        success = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        print(success)
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        # метод, который проверяет, что элемент не появляется на странице в течение заданного времени
        # упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.

        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message present, but should not be"

    def guest_cant_see_success_message(self):
        # should_not_be_success_message
        # self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)

        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message present, but should not be"
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

    def message_disappeared_after_adding_product_to_basket(self):  # сообщения об успехе должно исчезнуть
        # success = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        # print(success)
        # Проверяем, что нет сообщения об успехе с помощью is_disappeared
        # is_not_element_present: упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый
        # is_disappeared: будет ждать до тех пор, пока элемент не исчезнет.
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), " Message is present, but must disappeared"

    def go_to_login_page_from_product_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
