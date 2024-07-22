"==============================2.4 Настройка ожиданий  =========================================="

"""-----------------------------Задание: ждем нужный текст на странице--------------------------

Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. 
Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

Шаги:
1)Открыть страницу http://suninjuly.github.io/explicit_wait2.html
2)Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
3)Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
4)Чтобы определить момент, когда цена аренды уменьшится до $100,
используйте метод text_to_be_present_in_element из библиотеки expected_conditions."""

import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_price():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/explicit_wait2.html")
        # Ожидание, пока цена уменьшится до $100
        price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
        print(price)
        # Нажатие на кнопку "Book"
        button = browser.find_element(By.ID, "book")
        button.click()

        x_element = browser.find_element(By.ID, 'input_value')
        x = x_element.text
        print(x)
        y = calc(x)
        browser.find_element(By.ID, "answer").send_keys(y)
        browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    finally:
        time.sleep(5)  # Для наглядности оставляем браузер открытым на 5 секунд
        browser.quit()
