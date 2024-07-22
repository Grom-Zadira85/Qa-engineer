import pytest
import allure

from ..pages.auth_page import LoginPage

base_url = 'https://victoretc.github.io/selenium_waits/'


@pytest.fixture()
def login_page(browser):
    page = LoginPage(browser, base_url)
    return page


@allure.title("Autorization")
def test_auth_positive(login_page):
    login_page.open()

    main_header = login_page.check_main_header()
    # создана  переменная   main_header чтоб  текст из self.is_visible((By.XPATH, "/html/body/h1")).text файла auth-page
    # был получен  и вставлен в assert

    login_page.start_button().click()

    login_page.login_field() \
        .password_field() \
        .agree_button() \
        .registration_button()

    assert main_header == "Практика с ожиданиями в Selenium", "заголовок не соответствует требованию"
    assert login_page.loader().is_displayed()
    assert login_page.success_message().text == 'Вы успешно зарегистрированы!'
