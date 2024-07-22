
# Необходимо написать автотесты для сайта saucedemo: Ссылка на сайт: https://www.saucedemo.com/
# Функционал, который необходимо покрыть автотестами:
#
# Авторизация:
# Авторизация используя корректные данные (standard_user, secret_sauce)

import time

from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import Select

from Automatization_testing.data.data_auth_url import *
from Automatization_testing.pages.locators import *


# создаем функцию для авторизации
def logins(browser):
    browser.implicitly_wait(8)
    browser.get(MAIN_PAGE)
    browser.find_element(*F_USER_NAME).send_keys(LOGIN)
    browser.find_element(*F_PASSWORD).send_keys(PASSWORD)
    browser.find_element(*F_BUTTON).click()


# Авторизация используя корректные данные
def test_auth_positive(browser):
    logins(browser)
    time.sleep(5)
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'Url не соответствует ожидаемому'
    browser.quit()


# Авторизация используя некорректные данные (user, user)
def test_auth_negative(browser):
    browser.get(MAIN_PAGE)
    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Username']")
    input1.send_keys("user")
    input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Password']")
    input2.send_keys("user")
    button = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
    button.click()
    time.sleep(5)
    # проверяем, что мы не перешли на доугую страницу- не попали на сайт магазина
    assert browser.current_url == "https://www.saucedemo.com/", 'Url не соответствует ожидаемому'
    browser.quit()


# Корзина
# Добавление товара в корзину через каталог
def test_add_card_from_catalog(browser):
    logins(browser)
    browser.find_element(*ADD_TO_CARD).click()
    time.sleep(2)
    browser.get(BASKET_LINK)
    assert browser.find_element(By.XPATH, '//*[text()="Sauce Labs Bike Light"]'), 'нет товара'
    time.sleep(2)


# Удаление товара из корзины через корзину
def test_remove_card_from_basket(browser):
    logins(browser)
    browser.find_element(*ADD_TO_CARD).click()
    browser.get(BASKET_LINK)
    browser.find_element(*REMOVE_CARD).click()
    check_remove_card = browser.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert len(check_remove_card) == 0, 'товар остался в козpине'
    browser.quit()


# Добавление товара в корзину из карточки товара
def test_add_card_from_card(browser):
    logins(browser)
    browser.find_element(By.XPATH, '//*[text()="Sauce Labs Bike Light"]').click()
    browser.find_element(By.ID, 'add-to-cart').click()
    time.sleep(2)
    # переходим в корзину и проверяем наличие товара
    browser.get(BASKET_LINK)
    assert browser.find_element(By.XPATH, '//*[text()="Sauce Labs Bike Light"]'), 'нет товара'
    browser.quit()


# Удаление товара из корзины через карточку товара
def test_remove_card_from_card(browser):
    logins(browser)
    browser.find_element(By.XPATH, '//*[text()="Sauce Labs Bike Light"]').click()
    browser.find_element(By.ID, 'add-to-cart').click()
    # делаем повторный клик для удаления товара
    browser.find_element(By.ID, 'remove').click()
    #  проверяем наличие товара, кнопка изменила свой код и вместо id = remove cтала id = add-to-card
    assert browser.find_element(By.ID, 'add-to-cart'), 'товар остался в корзине '
    browser.quit()


# Карточка товара
# Успешный переход к карточке товара после клика на картинку товара
def test_click_picture_card(browser):
    logins(browser)
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, '[src="/static/media/bike-light-1200x1500.37c843b0.jpg"]').click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=0', 'Url не соответствует ожидаемому'
    browser.quit()


# Успешный переход к карточке товара после клика на название товара
def test_click_name_card(browser):
    logins(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[text()="Sauce Labs Bike Light"]').click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=0', 'Url не соответствует ожидаемому'
    browser.quit()


# Оформление заказа
# Оформление заказа используя корректные данные
def test_placing_an_order(browser):
    logins(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[text()="Sauce Labs Bike Light"]').click()
    time.sleep(2)
    browser.find_element(By.ID, 'add-to-cart').click()
    # переходим в корзину
    browser.get(BASKET_LINK)
    browser.find_element(By.CSS_SELECTOR, '[id="checkout"]').click()

    input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]')
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]')
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Zip/Postal Code"]')
    input3.send_keys("0147")

    # заполнили поля ввода заказа
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, '[class="btn btn_action btn_medium cart_button"]').click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/checkout-complete.html', 'Url не соответствует ожидаемому'
    browser.quit()


# Фильтр
# Проверка работоспособности фильтра (A to Z)
def test_filter_a_to_z(browser):
    logins(browser)
    select = Select(browser.find_element(By.CSS_SELECTOR, '[class="product_sort_container"]'))
    # browser.find_element(By.CSS_SELECTOR, "option:nth-child(4)").click()
    select.select_by_index(1)

    select = Select(browser.find_element(By.CSS_SELECTOR, '[class="product_sort_container"]'))
    select.select_by_index(0)
    #  поиск по value . значения в дроп боксе начинаются с 0 , то есть значеие 1 это второй вариант в списке
    # select.select_by_value("1")

    lst = browser.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    names = []
    for x in lst:
        names.append(x.text)
        print(x.text)
    assert names == sorted(names), 'сортировка не работает'
    browser.quit()


# Проверка работоспособности фильтра (Z to A)
# создал  на верху функцию logins чтоб  сократить код
def test_filter_z_to_a(browser):
    logins(browser)
    select = Select(browser.find_element(By.CSS_SELECTOR, '[class="product_sort_container"]'))
    select.select_by_index(1)
    # проверяем  сортироку  карточек по заданному значению
    lst = browser.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    names = []
    for x in lst:
        lst = lst + [x]
        names.append(x.text)
        print(x.text)
    assert names == names, 'сортировка не работает'
    browser.quit()


# Проверка работоспособности фильтра (low to high)
def test_low_to_high(browser):
    logins(browser)

    select = Select(browser.find_element(By.CSS_SELECTOR, '[class="product_sort_container"]'))
    select.select_by_index(2)
    time.sleep(2)
    lst = browser.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
    number = []
    for x in lst:
        number.append(
            float(x.text[1:]))  # начинаем с индекса 1 потому что под индексом 0 находится знак доллара-это цена
        print(x.text)
    assert number == sorted(number), 'сортировка не работает'
    browser.quit()

# Проверка работоспособности фильтра (high to low)
def test_high_to_low(browser):
    logins(browser)
    select = Select(browser.find_element(By.CSS_SELECTOR, '[class="product_sort_container"]'))
    select.select_by_index(3)
    time.sleep(2)

    lst = browser.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
    number = []
    for x in lst:
        number.append(float(x.text[-1:]))
        print(x.text)
    assert number == sorted(number), 'сортировка не работает'
    browser.quit()


# Бургер меню
# Выход из системы
def test_logout(browser):
    logins(browser)
    time.sleep(2)
    browser.find_element(By.ID, 'react-burger-menu-btn').click()
    browser.find_element(By.ID, 'logout_sidebar_link').click()
    assert browser.current_url == 'https://www.saucedemo.com/', 'Url не соответствует ожидаемому'
    browser.quit()


# Проверка работоспособности кнопки "About" в меню
def test_about(browser):
    logins(browser)
    browser.find_element(By.ID, 'react-burger-menu-btn').click()
    browser.find_element(By.ID, 'about_sidebar_link').click()
    assert browser.current_url == 'https://saucelabs.com/', 'Url не соответствует ожидаемому'
    browser.quit()


# Проверка работоспособности кнопки "Reset App State"
def test_reset_app_state(browser):
    logins(browser)
    browser.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    time.sleep(2)

    browser.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(2)
    browser.find_element(By.ID, 'reset_sidebar_link').click()
    time.sleep(2)
    # проверяем удалит ли сброс  состояния cтраницы товары в корзине
    try:
        browser.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert False, "Товар не удален из корзины"
    except NoSuchElementException:
        assert True
