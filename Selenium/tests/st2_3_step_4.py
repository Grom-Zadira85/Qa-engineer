"""                        Alerts
             Задание: принимаем alert

Шаги:
1)Открыть страницу http://suninjuly.github.io/alert_accept.html
2)Нажать на кнопку
3)Принять confirm
4)На новой странице решить капчу для роботов, чтобы получить число с ответом
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "https://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_confirm():
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(3)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(3)
    # "переходим на другую вкладку"
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    print(x)
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    time.sleep(3)
    browser.quit()
