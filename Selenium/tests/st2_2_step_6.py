"""-----------Задание на execute_script   .scrollIntoView
1)Открыть страницу https://SunInJuly.github.io/execute_script.html.
2)Считать значение для переменной x.
3)Посчитать математическую функцию от x.
4)Проскроллить страницу вниз.
5)Ввести ответ в текстовое поле.
6)Выбрать checkbox "I'm the robot".
7)Переключить radiobutton "Robots rule!".
8)Нажать на кнопку "Submit". """

import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_calc():
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    print(x)
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
    radio_button = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')

    # "Делаем скролл"
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
    radio_button.click()

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    time.sleep(3)
    browser.quit()
