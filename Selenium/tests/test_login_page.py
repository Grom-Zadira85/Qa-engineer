from ..pages.locators import LoginPageLocators
from ..pages.login_page import LoginPage

login_url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


def test_should_be_login_page(browser):
    page = LoginPage(browser, login_url)  # передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу

    assert "login" in login_url, " слово login не является подстрокой в login_url"
    assert page.is_element_present(*LoginPageLocators.LOGIN_FORM), "form  login not present"
    assert page.is_element_present(*LoginPageLocators.REGISTER_FORM), "form register not present"




