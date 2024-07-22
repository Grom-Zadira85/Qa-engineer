from .base_page import BasePage
from .locators import LoginPageLocators
from .urls import LoginPageLink

""" страница не нужна при выполнении проверки на присутствие элементов  - Форма Логин и Регистрация, если  я выношу  
assert  и click() send ()  в файл с тестом.  поэтому и большинство строк  закомментировал.
Если тестировать поля ввода этих форм (логин, регистрация) , то страница будет нужна для  указания строки 
пример:
login_email_address_field = self.browser.find_element(*LoginPageLocators.LOGIN_IN_EMAIL_ADDRESS)
        а  строку  login_email_address_field.click() выносим в тест,  также и assert .
        
тест не видит  self.is_element_present(*LoginPageLocators.LOGIN_FORM)  через переменную, которую пишу в assert
переменная создавалась  в  функциях def should_be_login_form(self): и def should_be_register_form(self): 
 """




class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        # сделал 2 assert-а (на этой странице и в тесте), согласно степик assert, click, send пишется здесь
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url == LoginPageLink.login_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        return self

        # login_email_address_field = self.browser.find_element(*LoginPageLocators.LOGIN_IN_EMAIL_ADDRESS)
        # login_email_address_field.click()
        # login_email_address_field.send ("email_address@gmail.com")

        # login_password = self.browser.find_element(*LoginPageLocators.LOGIN_IN_PASSWORD)
        # login_password.click()
        # login_password.send("1234")
        # button_log_in = self.browser.find_element(*LoginPageLocators.BUTTON_LOG_IN)
        # button_log_in.click()

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        return self
