import allure
from selene import be, have, command, query
from selene.support.shared.jquery_style import s

from Selene.pages.locators import ProductLocators as PL, ShoppingCart as SC


@allure.link("https://trello.com/c/lvLslLGD")
def check_product_name_is_correct(item_name):
    s(PL.NAME_ARGUS_ALL_WEATHER_TANK_CHECKOUT_CART).should(have.text(item_name))


def check_size_is_correct(size):
    s(PL.SIZE_M_ARGUS_ALL_WEATHER_TANK_CHECKOUT_CART).should(have.text(size))


def check_color_is_correct(color):
    s(PL.COLOR_GRAY_ARGUS_CHECKOUT_CART).should(have.text(color))


@allure.link("https://trello.com/c/SQ3op4DX")
def check_price_present(item_price):
    s(PL.PRICE_ITEM_CHECKOUT_CART).should(be.present).should(have.text(item_price))


def check_qty():
    s(PL.QTY_FIELD_CHECKOUT_CART).should(be.present)


def check_change_qty(qty):
    s('[data-role="cart-item-qty"]').set(qty)


def update_click():
    s('[class="action update"]').click()


def delete_item():
    s('[class="action action-delete"]').click()


def item_should_not_present():
    s(PL.NAME_ARGUS_ALL_WEATHER_TANK_CHECKOUT_CART).should(be.not_.present)


def check_subtotal(subtotal):
    s(PL.CART_SUBTOTAL_CHECKOUT_CART).should(be.present).should(have.text(subtotal))


def estimate_shipping_drop():
    s(SC.ESTIMATE_SHIPPING).click()


def select_country_drop():
    s(SC.COUNTRY_SELECT_DROP)


def select_country(country):
    s(f'//*[contains(text(), "{country}")]').click()

    # 2-й способ
    # country = s(f'//option[@data-title="{country}"]').perform(command.js.scroll_into_view).click()
    # country.click()


# def select_state_region(region):
# для штатов из дроп-даун
# state = s(f'//option[@data-title="{region}"]').perform(command.js.scroll_into_view)
# state.click()
# Для input field, без дроп-даун
# s('//*[@name="region"]').type(region)


def select_state_region(region):
    # # Проверяем наличие элемента списка штатов для выбора
    # state_dropdown = s('//select[@name="state"]')

    try:
        # Если элемент списка штатов существует, выбираем штат из дропдауна
        state = s(f'option[data-title="{region}"]').with_(timeout=4).perform(command.js.scroll_into_view)
        state.click()
    except Exception:
        # Если элемент списка штатов отсутствует, вводим регион в поле ввода
        input_region = s('input[name="region"]')
        input_region.type(region)


def post_code(code):
    s('//*[@name="postcode"]').type(code)


def flat_rate_should_be_present():
    s(SC.FLAT_RATE).should(be.present)


def fixed_type_of_shipping_selected():
    s('// *[text() = "Fixed"]').click()


def check_subtotal_value_is_present_and_correct(qty, price):
    s(f'[class="control qty"] [value="{qty}"]').should(have.attribute("value").value("3"))
    s(PL.PRICE_ITEM_CHECKOUT_CART).should(have.text(price))

    # shadow_root = s('[data-role="cart-item-qty"][id="editing-view-port"]').should(have.text(qty)).get(query.text)
    # print(shadow_root)

    subtotal = s(SC.SUBTOTAL_VAlUE).should(have.text(f'${int(qty) * float(price[1:])}')).get(query.text)
    print(subtotal)
    return subtotal


def shipping_price_is_correct(fixed):
    s('[data-th="Shipping"]').should(have.text(fixed))


def check_order_total_has_the_correct_amount(subtotal, shipping_flatRate_fixed):
    order_total = s(SC.ORDER_TOTAL_VALUE).should(
        have.text(f'${float(subtotal[1:]) + float(shipping_flatRate_fixed[1:])}')).get(query.text)
    print(order_total)


def check_proceed_to_checkout_button_should_be_clickable():
    s(SC.PROCESEED_TO_CHECKOUT_BUTTON).should(be.visible).should(be.clickable)


def redirection_to_checkout_shipping_page():
    s(SC.PROCESEED_TO_CHECKOUT_BUTTON).click()
