
"""===========================Задание: переход на новую вкладку=========================================================
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку
 и решить в ней задачу.

Шаги:
1)Открыть страницу http://suninjuly.github.io/redirect_accept.html
2)Нажать на кнопку
3)Переключиться на новую вкладку
4)Пройти капчу для робота и получить число-ответ"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/redirect_accept.html"
link2 = "https://suninjuly.github.io/redirect_page.html?"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_new_window():
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    # "Перешли в новое окно после нажатия плавающей кнопки и переключаем браузер в новую вкладку"
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    time.sleep(4)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    time.sleep(4)
    browser.quit()
