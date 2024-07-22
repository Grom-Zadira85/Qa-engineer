from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_OR_REGISTER_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class ProductPageLocators():
    LOGIN_OR_REGISTER_LINK = (By.ID, "registration_link")  # for test_login_page

    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '[value="Add to basket"]')

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:first-child.alert-success .alertinner strong")
    ALERT_NAME_PRODUCT_IN_MESSAGE = (By.CSS_SELECTOR, "#messages>div:first-child.alert-success .alertinner strong")
    # "#messages > div:nth-child(1) > div > strong"
    NAME_PRODUCT_ADD_TO_BASKET = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main>h1")

    ALERT_PRICE_PRODUCT_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade"
                                                       ".in > div > p:nth-child(1) > strong")
    PRICE_PRODUCT_ADD_TO_BASKET = (
    By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')


class LoginPageLocators():
    LOGIN_OR_REGISTER_LINK = (By.CSS_SELECTOR, "#login_link")

    LOGIN_FORM = (By.ID, "login_form")  # [id="login_form"]
    LOGIN_IN_EMAIL_ADDRESS = (By.CSS_SELECTOR, '[name="login-username"]')
    LOGIN_IN_PASSWORD = (By.CSS_SELECTOR, '[name="login-password"]')
    I_FORGOTTEN_MY_PASSWORD = (By.CSS_SELECTOR, '[href="/en-gb/password-reset/"]')
    BUTTON_LOG_IN = (By.CSS_SELECTOR, '[name="login_submit"]')

    REGISTER_FORM = (By.ID, "register_form")  # [id="register_form"]
    REGISTER_EMAIL_ADDRESS = (By.CSS_SELECTOR, '[name="registration-email"]')
    REGISTER_PASSWORD = (By.CLASS_NAME, "registration-password1")  # [name="registration-password1"]
    REGISTER_CONFIRM_PASSWORD = (By.CLASS_NAME, "registration-password2")  # [name="registration-password2"]
    BUTTON_REGISTER = (By.CLASS_NAME, "registration_submit")  # [name="registration_submit"]
