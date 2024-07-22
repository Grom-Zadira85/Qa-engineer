"""Задание: кликаем по checkboxes и radiobuttons (капча для роботов)

------------------------------ шаги:
1)Открыть страницу https://suninjuly.github.io/math.html.
2)Считать значение для переменной x.
3)Посчитать математическую функцию от x (код для этого приведён ниже).
4)Ввести ответ в текстовое поле.
5)Отметить checkbox "I'm the robot".
6)Выбрать radiobutton "Robots rule!".
7)Нажать на кнопку Submit.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "[type='checkbox']").click()
    browser.find_element(By.CSS_SELECTOR, '[value="robots"]').click()
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(5)
    browser.quit()
