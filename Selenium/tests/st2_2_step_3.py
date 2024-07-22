"""Задание: работа с выпадающим списком

======================шаги===========================

1)Открыть страницу https://suninjuly.github.io/selects1.html
2)Посчитать сумму заданных чисел
3)Выбрать в выпадающем списке значение равное расчитанной сумме
4)Нажать кнопку "Submit"
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"


def calc(x, y):
    return x + y


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, 'num1').text
    x = int(x)
    print(x)
    y = browser.find_element(By.ID, 'num2').text
    y = int(y)
    print(y)
    summ = (x + y)
    print(summ)
    summ = str(summ)
    browser.find_element(By.ID, "dropdown").click()
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(summ)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
finally:
    time.sleep(9)
    browser.quit()

